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


class MT5ExecutionEngine:

    def __init__(
        self,
        symbol,
        magic=260813
    ):

        self.symbol = symbol
        self.magic = magic

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
            self.symbol
        )

    # =====================================
    # TICK
    # =====================================

    def tick(self):

        return mt5.symbol_info_tick(
            self.symbol
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
                self.symbol,

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
