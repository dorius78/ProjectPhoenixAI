from Logs.logger import Logger


class TradeReport:

    def __init__(self):
        Logger.success(
            "Trade Report V1 inizializzato."
        )

    def print(self, trade):

        if trade is None:
            Logger.warning(
                "Nessun trade generato."
            )
            return

        Logger.section(
            "TRADE MANAGER"
        )

        Logger.info(
            f"Symbol       : {trade.get('symbol', 'N/D')}"
        )

        Logger.info(
            f"Signal       : {trade.get('signal', 'N/D')}"
        )

        Logger.info(
            f"Side         : {trade.get('side', 'N/D')}"
        )

        Logger.info(
            f"Entry        : {trade.get('entry', 'N/D')}"
        )

        Logger.info(
            f"Stop Loss    : {trade.get('stop_loss', 'N/D')}"
        )

        Logger.info(
            f"Take Profit  : {trade.get('take_profit', 'N/D')}"
        )

        Logger.info(
            f"Risk Reward  : {trade.get('risk_reward', 'N/D')}"
        )
