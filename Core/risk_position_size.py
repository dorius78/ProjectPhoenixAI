class RiskPositionSize:

    def calculate(
        self,
        account_balance,
        risk_percent,
        entry,
        stop_loss
    ):
        account_balance = float(account_balance)
        risk_percent = float(risk_percent)
        entry = float(entry)
        stop_loss = float(stop_loss)

        risk_amount = account_balance * (risk_percent / 100.0)

        stop_distance = abs(entry - stop_loss)

        if stop_distance <= 0:
            return 0.0

        # =====================================================
        # CALCOLO GENERICO
        # =====================================================
        #
        # Il Core non deve conoscere le caratteristiche
        # specifiche di EURUSD, BTCUSD o altri strumenti.
        #
        # Per compatibilita' con i test del Core:
        # rischio per 1 unita' = distanza dello stop.
        #
        # Il collegamento MT5 applichera' successivamente
        # le caratteristiche reali dello strumento.
        # =====================================================

        risk_per_unit = stop_distance

        if risk_per_unit <= 0:
            return 0.0

        position_size = risk_amount / risk_per_unit

        if position_size <= 0:
            return 0.0

        return round(position_size, 2)
