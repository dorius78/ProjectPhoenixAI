"""
========================================
PROJECT PHOENIX AI
MT5 Execution Bridge
Versione 4.0
========================================

Responsabilità:

- Connessione MT5
- Lettura simbolo
- Conversione unità -> lotti
- Normalizzazione volume
- Preparazione ordine
- order_check()
- Risk Gate MT5
- DRY RUN
- Esecuzione reale controllata

IMPORTANTE:

Il Core calcola la size astratta.

Il Bridge converte la size nelle
unità operative reali di MT5.
========================================
"""

import math

import MetaTrader5 as mt5

from Config.mt5_credentials import SYMBOL_MAP


class MT5ExecutionEngine:

    def _resolve_mt5_symbol(self, symbol):
        import MetaTrader5 as mt5

        raw = str(symbol).strip()

        candidates = [
            raw,
            raw.replace("-", ""),
            raw.replace("_", ""),
            raw.replace(".", ""),
        ]

        normalized = (
            raw
            .replace("-", "")
            .replace("_", "")
            .replace(".", "")
            .upper()
        )

        symbols = mt5.symbols_get()

        if symbols:

            for info in symbols:

                name = str(info.name)

                compact = (
                    name
                    .replace("-", "")
                    .replace("_", "")
                    .replace(".", "")
                    .upper()
                )

                if compact == normalized:

                    if not info.visible:

                        mt5.symbol_select(
                            name,
                            True
                        )

                    tick = mt5.symbol_info_tick(
                        name
                    )

                    if tick is not None:

                        return name

        for candidate in candidates:

            info = mt5.symbol_info(
                candidate
            )

            if info is None:
                continue

            if not info.visible:

                mt5.symbol_select(
                    candidate,
                    True
                )

            tick = mt5.symbol_info_tick(
                candidate
            )

            if tick is not None:

                return candidate

        return None


    def __init__(
        self,
        symbol,
        magic=260813
    ):

        self.symbol = symbol
        self.magic = magic

        # =================================
        # PHOENIX -> MT5 AUTONOMOUS MT5 INIT
        # =================================
        #
        # Il bridge NON deve dipendere da una
        # connessione MT5 lasciata aperta da un
        # componente precedente.
        #
        # PaperDecisionBridge puo' terminare la
        # propria sessione MT5 prima dell'esecuzione.
        # Il bridge di execution deve quindi essere
        # autonomo e riallacciare MT5.
        # =================================

        if not mt5.initialize():
            raise RuntimeError(
                f"MT5 initialize fallito: {mt5.last_error()}"
            )

        # =================================
        # PHOENIX -> MT5 SYMBOL RESOLUTION
        # =================================

        # PHOENIX -> MT5 BROKER SYMBOL
        # Risoluzione dinamica del simbolo broker.

        resolved_symbol = self._resolve_mt5_symbol(
            symbol
        )

        if resolved_symbol is None:
            raise RuntimeError(
                "Simbolo MT5 non disponibile: "
                + str(symbol)
            )

        self.mt5_symbol = resolved_symbol

        # =================================
        # RISK GATE
        # =================================

        # Massimo margine utilizzabile
        # rispetto all'equity disponibile.
        self.max_margin_usage = 0.50

        # Margin level minimo consentito.
        self.min_margin_level = 200.0

        # Numero massimo di posizioni
        # contemporanee gestite da Phoenix.
        self.max_open_positions = 1

    # =====================================
    # CONNECTION
    # =====================================

    def connect(self):

        return bool(
            mt5.initialize()
        )

    def disconnect(self):

        mt5.shutdown()

    # =====================================
    # ACCOUNT
    # =====================================

    def account_info(self):

        return mt5.account_info()

    # =====================================
    # SYMBOL
    # =====================================

    def symbol_info(self):

        return mt5.symbol_info(
            self.mt5_symbol
        )

    # =====================================
    # TICK
    # =====================================

    def tick(self):

        return mt5.symbol_info_tick(
            self.mt5_symbol
        )

    # =====================================
    # CONTRACT SIZE
    # =====================================

    def get_contract_size(self):

        info = self.symbol_info()

        if info is None:
            return 0.0

        contract_size = float(
            info.trade_contract_size
        )

        if contract_size <= 0:
            return 0.0

        return contract_size

    # =====================================
    # CORE -> MT5
    # =====================================

    def core_units_to_lots(
        self,
        units
    ):

        units = float(units)

        if units <= 0:
            return 0.0

        contract_size = (
            self.get_contract_size()
        )

        if contract_size <= 0:
            return 0.0

        return (
            units /
            contract_size
        )

    # =====================================
    # NORMALIZE VOLUME
    # =====================================

    def normalize_volume(
        self,
        volume
    ):

        info = self.symbol_info()

        if info is None:
            return 0.0

        volume = float(volume)

        volume_min = float(
            info.volume_min
        )

        volume_max = float(
            info.volume_max
        )

        volume_step = float(
            info.volume_step
        )

        if volume_step <= 0:
            volume_step = 0.01

        # ---------------------------------
        # ROUND DOWN
        # ---------------------------------

        units = math.floor(
            volume /
            volume_step
            + 1e-12
        )

        normalized = (
            units *
            volume_step
        )

        # ---------------------------------
        # DECIMALS
        # ---------------------------------

        step_text = (
            f"{volume_step:.10f}"
            .rstrip("0")
        )

        decimals = 0

        if "." in step_text:

            decimals = len(
                step_text.split(".")[1]
            )

        normalized = round(
            normalized,
            decimals
        )

        # ---------------------------------
        # LIMITS
        # ---------------------------------

        if normalized < volume_min:
            return 0.0

        if normalized > volume_max:

            normalized = volume_max

            units = math.floor(
                normalized /
                volume_step
                + 1e-12
            )

            normalized = round(
                units *
                volume_step,
                decimals
            )

        return normalized

    # =====================================
    # FILLING MODE
    # =====================================

    def get_filling_mode(self):

        info = self.symbol_info()

        if info is None:

            return mt5.ORDER_FILLING_FOK

        mode = int(
            info.filling_mode
        )

        if mode & 1:

            return mt5.ORDER_FILLING_FOK

        if mode & 2:

            return mt5.ORDER_FILLING_IOC

        return mt5.ORDER_FILLING_RETURN

    # =====================================
    # PREPARE VOLUME
    # =====================================

    def prepare_volume(
        self,
        trade
    ):

        if not trade:
            return 0.0

        size = float(
            trade.get(
                "size",
                0
            )
        )

        if size <= 0:
            return 0.0

        size_unit = str(
            trade.get(
                "size_unit",
                "lots"
            )
        ).lower().strip()

        # ---------------------------------
        # CORE UNITS
        # ---------------------------------

        if size_unit == "units":

            lots = (
                self.core_units_to_lots(
                    size
                )
            )

        # ---------------------------------
        # GIÀ IN LOTTI
        # ---------------------------------

        else:

            lots = size

        return self.normalize_volume(
            lots
        )

    # =====================================
    # VALIDATE TRADE
    # =====================================

    def validate_trade(
        self,
        trade
    ):

        if not trade:

            return False, "Trade vuoto"

        if trade.get(
            "side"
        ) not in (
            "BUY",
            "SELL"
        ):

            return False, (
                "Direzione non valida"
            )

        required = (
            "symbol",
            "entry",
            "stop_loss",
            "take_profit",
            "size",
        )

        for field in required:

            if field not in trade:

                return False, (
                    f"Campo mancante: {field}"
                )

        info = self.symbol_info()

        if info is None:

            return False, (
                f"Simbolo non disponibile: "
                f"{self.symbol}"
            )

        volume = self.prepare_volume(
            trade
        )

        if volume <= 0:

            return False, (
                "Volume MT5 non valido."
            )

        # ---------------------------------
        # TICK
        # ---------------------------------

        tick = self.tick()

        if tick is None:

            return False, (
                "Tick MT5 non disponibile"
            )

        if (
            float(tick.bid) <= 0
            or
            float(tick.ask) <= 0
        ):

            return False, (
                "Prezzo MT5 non valido"
            )

        # ---------------------------------
        # PREZZI
        # ---------------------------------

        entry = float(
            trade["entry"]
        )

        stop_loss = float(
            trade["stop_loss"]
        )

        take_profit = float(
            trade["take_profit"]
        )

        if entry <= 0:
            return False, "Entry non valida"

        if stop_loss <= 0:
            return False, "Stop Loss non valido"

        if take_profit <= 0:
            return False, "Take Profit non valido"

        # ---------------------------------
        # DIREZIONE SL
        # ---------------------------------

        side = trade["side"]

        if side == "BUY":

            if stop_loss >= entry:

                return False, (
                    "BUY: Stop Loss "
                    "non valido"
                )

            if take_profit <= entry:

                return False, (
                    "BUY: Take Profit "
                    "non valido"
                )

        else:

            if stop_loss <= entry:

                return False, (
                    "SELL: Stop Loss "
                    "non valido"
                )

            if take_profit >= entry:

                return False, (
                    "SELL: Take Profit "
                    "non valido"
                )

        return True, (
            "Trade validato"
        )

    # =====================================
    # PREPARE ORDER
    # =====================================

    def prepare_order(
        self,
        trade
    ):

        valid, message = (
            self.validate_trade(
                trade
            )
        )

        if not valid:

            return {

                "valid": False,

                "message": message,

                "order": None,

            }

        side = trade["side"]

        order_type = (

            mt5.ORDER_TYPE_BUY

            if side == "BUY"

            else

            mt5.ORDER_TYPE_SELL

        )

        tick = self.tick()

        price = (

            float(tick.ask)

            if side == "BUY"

            else

            float(tick.bid)

        )

        volume = (
            self.prepare_volume(
                trade
            )
        )

        order = {

            "action":
                mt5.TRADE_ACTION_DEAL,

            "symbol":
                self.mt5_symbol,

            "volume":
                volume,

            "type":
                order_type,

            "price":
                price,

            "sl":
                float(
                    trade["stop_loss"]
                ),

            "tp":
                float(
                    trade["take_profit"]
                ),

            "deviation":
                20,

            "magic":
                self.magic,

            "comment":
                "PROJECT PHOENIX AI",

            "type_time":
                mt5.ORDER_TIME_GTC,

            "type_filling":
                self.get_filling_mode(),

        }

        return {

            "valid": True,

            "message":
                "Ordine preparato",

            "order":
                order,

        }

    # =====================================
    # POSIZIONI PHOENIX
    # =====================================

    def get_open_positions(self):

        positions = mt5.positions_get()

        if positions is None:

            return []

        return list(
            positions
        )

    # =====================================
    # CONTA POSIZIONI PHOENIX
    # =====================================

    def get_phoenix_positions(self):

        positions = (
            self.get_open_positions()
        )

        phoenix = []

        for position in positions:

            if (
                int(
                    getattr(
                        position,
                        "magic",
                        0
                    )
                )
                == self.magic
            ):

                phoenix.append(
                    position
                )

        return phoenix

    # =====================================
    # RISK GATE
    # =====================================

    def risk_gate(
        self,
        order,
        check
    ):

        # =================================
        # ACCOUNT
        # =================================

        account = (
            self.account_info()
        )

        if account is None:

            return {

                "allowed": False,

                "reason":
                    "Account MT5 non disponibile",

            }

        balance = float(
            getattr(
                account,
                "balance",
                0
            )
        )

        equity = float(
            getattr(
                account,
                "equity",
                0
            )
        )

        margin = float(
            getattr(
                account,
                "margin",
                0
            )
        )

        margin_free = float(
            getattr(
                account,
                "margin_free",
                0
            )
        )

        margin_level = float(
            getattr(
                account,
                "margin_level",
                0
            )
        )

        # =================================
        # ACCOUNT VALIDITY
        # =================================

        if equity <= 0:

            return {

                "allowed": False,

                "reason":
                    "Equity MT5 non valida",

            }

        # =================================
        # ORDER CHECK RESULT
        # =================================

        check_margin = float(
            getattr(
                check,
                "margin",
                0
            )
        )

        check_margin_free = float(
            getattr(
                check,
                "margin_free",
                0
            )
        )

        check_margin_level = float(
            getattr(
                check,
                "margin_level",
                0
            )
        )

        check_retcode = int(
            getattr(
                check,
                "retcode",
                -1
            )
        )

        # =================================
        # RETCODE
        # =================================

        if check_retcode != 0:

            return {

                "allowed": False,

                "reason":
                    (
                        "MT5 order_check "
                        f"retcode={check_retcode}"
                    ),

            }

        # =================================
        # MARGIN
        # =================================

        if check_margin <= 0:

            return {

                "allowed": False,

                "reason":
                    "Margine ordine non valido",

            }

        # =================================
        # MARGIN FREE
        # =================================

        if check_margin_free <= 0:

            return {

                "allowed": False,

                "reason":
                    "Margine libero insufficiente",

            }

        # =================================
        # MAX MARGIN USAGE
        # =================================

        max_allowed_margin = (
            equity *
            self.max_margin_usage
        )

        if check_margin > max_allowed_margin:

            return {

                "allowed": False,

                "reason":
                    (
                        "Margine richiesto "
                        f"({check_margin:.2f}) "
                        "supera il limite "
                        f"({max_allowed_margin:.2f})"
                    ),

            }

        # =================================
        # MARGIN LEVEL
        # =================================

        if (
            check_margin_level > 0
            and
            check_margin_level
            < self.min_margin_level
        ):

            return {

                "allowed": False,

                "reason":
                    (
                        "Margin level insufficiente: "
                        f"{check_margin_level:.2f}%"
                    ),

            }

        # =================================
        # POSIZIONI PHOENIX
        # =================================

        phoenix_positions = (
            self.get_phoenix_positions()
        )

        if (
            len(phoenix_positions)
            >= self.max_open_positions
        ):

            return {

                "allowed": False,

                "reason":
                    (
                        "Numero massimo "
                        "di posizioni Phoenix "
                        "raggiunto."
                    ),

            }

        # =================================
        # RESULT
        # =================================

        return {

            "allowed": True,

            "reason":
                "Risk Gate superato",

            "balance":
                balance,

            "equity":
                equity,

            "current_margin":
                margin,

            "current_margin_free":
                margin_free,

            "order_margin":
                check_margin,

            "order_margin_free":
                check_margin_free,

            "margin_level":
                check_margin_level,

            "max_allowed_margin":
                max_allowed_margin,

            "phoenix_positions":
                len(
                    phoenix_positions
                ),

        }

    # =====================================
    # ORDER CHECK
    # =====================================

    def check_order(
        self,
        trade
    ):

        prepared = (
            self.prepare_order(
                trade
            )
        )

        if not prepared["valid"]:

            return prepared

        check = mt5.order_check(
            prepared["order"]
        )

        if check is None:

            return {

                "valid": False,

                "message":
                    (
                        "order_check fallito: "
                        f"{mt5.last_error()}"
                    ),

                "order":
                    prepared["order"],

                "check":
                    None,

                "risk_gate":
                    None,

            }

        # =================================
        # RISK GATE
        # =================================

        gate = self.risk_gate(

            prepared["order"],

            check

        )

        if not gate["allowed"]:

            return {

                "valid": False,

                "message":
                    (
                        "RISK GATE BLOCCATO: "
                        f"{gate['reason']}"
                    ),

                "order":
                    prepared["order"],

                "check":
                    check,

                "risk_gate":
                    gate,

            }

        return {

            "valid": True,

            "message":
                "MT5 order_check + Risk Gate OK",

            "order":
                prepared["order"],

            "check":
                check,

            "risk_gate":
                gate,

        }

    # =====================================
    # EXECUTE
    # =====================================

    def execute(
        self,
        trade,
        dry_run=True
    ):

        checked = (
            self.check_order(
                trade
            )
        )

        if not checked["valid"]:

            return {

                **checked,

                "executed":
                    False,

                "dry_run":
                    dry_run,

            }

        # =================================
        # DRY RUN
        # =================================

        if dry_run:

            return {

                "executed":
                    False,

                "dry_run":
                    True,

                "message":
                    (
                        "DRY RUN: "
                        "nessun ordine inviato"
                    ),

                "order":
                    checked["order"],

                "check":
                    checked["check"],

                "risk_gate":
                    checked["risk_gate"],

            }

        # =================================
        # REAL EXECUTION
        # =================================

        result = mt5.order_send(
            checked["order"]
        )

        if result is None:

            return {

                "executed":
                    False,

                "dry_run":
                    False,

                "message":
                    (
                        "order_send fallito: "
                        f"{mt5.last_error()}"
                    ),

                "result":
                    None,

            }

        return {

            "executed":
                result.retcode
                == mt5.TRADE_RETCODE_DONE,

            "dry_run":
                False,

            "message":
                "Ordine inviato a MT5",

            "retcode":
                result.retcode,

            "result":
                result,

            "risk_gate":
                checked["risk_gate"],

        }


    def modify_position(
        self,
        ticket,
        stop_loss=None,
        take_profit=None,
        dry_run=True
    ):
        """
        Modifica protettiva di una posizione MT5.

        Safety:
        - dry_run=True non invia nulla.
        - viene richiesto esplicitamente il ticket.
        - non apre nuove posizioni.
        - utilizza TRADE_ACTION_SLTP.
        """

        try:

            import MetaTrader5 as mt5

            ticket = int(ticket)

            positions = mt5.positions_get(
                ticket=ticket
            )

            if not positions:

                return {
                    "success": False,
                    "executed": False,
                    "dry_run": dry_run,
                    "message": "Posizione non trovata",
                    "retcode": None,
                    "deal": None,
                    "order": None,
                    "ticket": ticket,
                    "price": None,
                    "result": None,
                }

            position = positions[0]

            # ---------------------------------------------
            # MAGIC VALIDATION
            # ---------------------------------------------

            if int(
                getattr(
                    position,
                    "magic",
                    0
                )
            ) != int(
                getattr(
                    self,
                    "magic",
                    260813
                )
            ):

                return {
                    "success": False,
                    "executed": False,
                    "dry_run": dry_run,
                    "message": "Magic number non corrispondente",
                    "retcode": None,
                    "deal": None,
                    "order": None,
                    "ticket": ticket,
                    "price": None,
                    "result": None,
                }

            symbol = str(
                position.symbol
            )

            current_sl = float(
                position.sl
            )

            current_tp = float(
                position.tp
            )

            if stop_loss is None:
                stop_loss = current_sl

            if take_profit is None:
                take_profit = current_tp

            stop_loss = float(
                stop_loss
            )

            take_profit = float(
                take_profit
            )

            request = {
                "action":
                    mt5.TRADE_ACTION_SLTP,

                "symbol":
                    symbol,

                "position":
                    ticket,

                "sl":
                    stop_loss,

                "tp":
                    take_profit,

                "magic":
                    int(
                        getattr(
                            self,
                            "magic",
                            260813
                        )
                    ),

                "comment":
                    "PROJECT PHOENIX AI",

            }

            # ---------------------------------------------
            # DRY RUN
            # ---------------------------------------------

            if dry_run:

                return {
                    "success": True,
                    "executed": False,
                    "dry_run": True,
                    "message":
                        "DRY RUN: nessuna modifica inviata",
                    "retcode": None,
                    "deal": None,
                    "order": None,
                    "ticket": ticket,
                    "price": None,
                    "request": request,
                    "result": None,
                }

            # ---------------------------------------------
            # REAL MT5 MODIFY
            # ---------------------------------------------

            result = mt5.order_send(
                request
            )

            if result is None:

                return {
                    "success": False,
                    "executed": False,
                    "dry_run": False,
                    "message":
                        (
                            "Modifica fallita: "
                            f"{mt5.last_error()}"
                        ),
                    "retcode": None,
                    "deal": None,
                    "order": None,
                    "ticket": ticket,
                    "price": None,
                    "request": request,
                    "result": None,
                }

            success = (
                result.retcode
                in (
                    mt5.TRADE_RETCODE_DONE,
                    mt5.TRADE_RETCODE_DONE_PARTIAL,
                )
            )

            return {
                "success":
                    success,

                "executed":
                    success,

                "dry_run":
                    False,

                "message":
                    (
                        "Posizione modificata"
                        if success
                        else
                        "Modifica posizione rifiutata"
                    ),

                "retcode":
                    result.retcode,

                "deal":
                    getattr(
                        result,
                        "deal",
                        None
                    ),

                "order":
                    getattr(
                        result,
                        "order",
                        None
                    ),

                "ticket":
                    ticket,

                "price":
                    getattr(
                        result,
                        "price",
                        None
                    ),

                "request":
                    request,

                "result":
                    result,
            }

        except Exception as e:

            return {
                "success": False,
                "executed": False,
                "dry_run": dry_run,
                "message":
                    f"Errore modify_position: {e}",
                "retcode": None,
                "deal": None,
                "order": None,
                "ticket": ticket,
                "price": None,
                "result": None,
            }


    def close_position(
        self,
        ticket,
        dry_run=True
    ):
        """
        Chiusura controllata di una posizione MT5.

        Safety:
        - dry_run=True non invia nulla.
        - chiude esclusivamente il ticket specificato.
        - verifica il magic Phoenix.
        - non crea un nuovo ciclo autonomo.
        """

        try:

            import MetaTrader5 as mt5

            ticket = int(ticket)

            positions = mt5.positions_get(
                ticket=ticket
            )

            if not positions:

                return {
                    "success": False,
                    "executed": False,
                    "dry_run": dry_run,
                    "message": "Posizione non trovata",
                    "retcode": None,
                    "deal": None,
                    "order": None,
                    "ticket": ticket,
                    "price": None,
                    "result": None,
                }

            position = positions[0]

            # ---------------------------------------------
            # MAGIC VALIDATION
            # ---------------------------------------------

            if int(
                getattr(
                    position,
                    "magic",
                    0
                )
            ) != int(
                getattr(
                    self,
                    "magic",
                    260813
                )
            ):

                return {
                    "success": False,
                    "executed": False,
                    "dry_run": dry_run,
                    "message": "Magic number non corrispondente",
                    "retcode": None,
                    "deal": None,
                    "order": None,
                    "ticket": ticket,
                    "price": None,
                    "result": None,
                }

            symbol = str(
                position.symbol
            )

            volume = float(
                position.volume
            )

            position_type = int(
                position.type
            )

            tick = mt5.symbol_info_tick(
                symbol
            )

            if tick is None:

                return {
                    "success": False,
                    "executed": False,
                    "dry_run": dry_run,
                    "message": "Tick MT5 non disponibile",
                    "retcode": None,
                    "deal": None,
                    "order": None,
                    "ticket": ticket,
                    "price": None,
                    "result": None,
                }

            # MT5:
            # POSITION_TYPE_BUY  = 0
            # POSITION_TYPE_SELL = 1

            if position_type == mt5.POSITION_TYPE_BUY:

                order_type = (
                    mt5.ORDER_TYPE_SELL
                )

                price = float(
                    tick.bid
                )

            elif position_type == mt5.POSITION_TYPE_SELL:

                order_type = (
                    mt5.ORDER_TYPE_BUY
                )

                price = float(
                    tick.ask
                )

            else:

                return {
                    "success": False,
                    "executed": False,
                    "dry_run": dry_run,
                    "message":
                        "Tipo posizione non valido",
                    "retcode": None,
                    "deal": None,
                    "order": None,
                    "ticket": ticket,
                    "price": None,
                    "result": None,
                }

            filling = None

            try:

                filling = self.get_filling_mode(
                    symbol
                )

            except Exception:

                filling = None

            if filling is None:

                filling = (
                    mt5.ORDER_FILLING_IOC
                )

            request = {
                "action":
                    mt5.TRADE_ACTION_DEAL,

                "symbol":
                    symbol,

                "volume":
                    volume,

                "type":
                    order_type,

                "position":
                    ticket,

                "price":
                    price,

                "deviation":
                    20,

                "magic":
                    int(
                        getattr(
                            self,
                            "magic",
                            260813
                        )
                    ),

                "comment":
                    "PROJECT PHOENIX AI CLOSE",

                "type_time":
                    mt5.ORDER_TIME_GTC,

                "type_filling":
                    filling,
            }

            # ---------------------------------------------
            # DRY RUN
            # ---------------------------------------------

            if dry_run:

                return {
                    "success": True,
                    "executed": False,
                    "dry_run": True,
                    "message":
                        "DRY RUN: nessuna chiusura inviata",
                    "retcode": None,
                    "deal": None,
                    "order": None,
                    "ticket": ticket,
                    "price": price,
                    "request": request,
                    "result": None,
                }

            # ---------------------------------------------
            # REAL MT5 CLOSE
            # ---------------------------------------------

            result = mt5.order_send(
                request
            )

            if result is None:

                return {
                    "success": False,
                    "executed": False,
                    "dry_run": False,
                    "message":
                        (
                            "Chiusura fallita: "
                            f"{mt5.last_error()}"
                        ),
                    "retcode": None,
                    "deal": None,
                    "order": None,
                    "ticket": ticket,
                    "price": price,
                    "request": request,
                    "result": None,
                }

            success = (
                result.retcode
                in (
                    mt5.TRADE_RETCODE_DONE,
                    mt5.TRADE_RETCODE_DONE_PARTIAL,
                )
            )

            return {
                "success":
                    success,

                "executed":
                    success,

                "dry_run":
                    False,

                "message":
                    (
                        "Posizione chiusa"
                        if success
                        else
                        "Chiusura posizione rifiutata"
                    ),

                "retcode":
                    result.retcode,

                "deal":
                    getattr(
                        result,
                        "deal",
                        None
                    ),

                "order":
                    getattr(
                        result,
                        "order",
                        None
                    ),

                "ticket":
                    ticket,

                "price":
                    getattr(
                        result,
                        "price",
                        price
                    ),

                "request":
                    request,

                "result":
                    result,
            }

        except Exception as e:

            return {
                "success": False,
                "executed": False,
                "dry_run": dry_run,
                "message":
                    f"Errore close_position: {e}",
                "retcode": None,
                "deal": None,
                "order": None,
                "ticket": ticket,
                "price": None,
                "result": None,
            }
