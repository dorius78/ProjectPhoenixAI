from Logs.logger import Logger


class StrategyValidator:
    def __init__(self):
        Logger.success("Strategy Validator V1 inizializzato.")

    def validate(self, result, criteria):
        if not isinstance(result, dict):
            return {
                "valid": False,
                "decision": "INVALID",
                "reasons": ["Risultato backtest non valido."]
            }

        if not isinstance(criteria, dict):
            criteria = {}

        reasons = []

        checks = [
            ("min_net_profit", "net_profit", ">="),
            ("min_win_rate", "win_rate", ">="),
            ("min_profit_factor", "profit_factor", ">="),
            ("max_drawdown", "max_drawdown", "<="),
            ("min_trades", "total_trades", ">="),
        ]

        for criterion, metric, operator in checks:
            if criterion not in criteria:
                continue

            try:
                expected = float(criteria[criterion])
                actual = float(result.get(metric, 0))
            except (TypeError, ValueError):
                reasons.append(f"Valore non valido per {metric}.")
                continue

            if operator == ">=" and actual < expected:
                reasons.append(
                    f"{metric} insufficiente: {actual} < {expected}"
                )

            elif operator == "<=" and actual > expected:
                reasons.append(
                    f"{metric} troppo alto: {actual} > {expected}"
                )

        valid = len(reasons) == 0

        return {
            "valid": valid,
            "decision": "VALID" if valid else "INVALID",
            "reasons": reasons
        }
