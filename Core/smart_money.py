"""
========================================
PROJECT PHOENIX AI
Smart Money
Versione 13.0
========================================
"""

from Logs.logger import Logger

from Core.smart_money_structure import SmartMoneyStructure
from Core.smart_money_fvg import SmartMoneyFVG
from Core.smart_money_orderblocks import SmartMoneyOrderBlocks
from Core.smart_money_liquidity import SmartMoneyLiquidity


class SmartMoney:

    def __init__(self):

        Logger.success(
            "Smart Money V13 inizializzato."
        )

        self.structure = SmartMoneyStructure()
        self.fvg = SmartMoneyFVG()
        self.orderblocks = SmartMoneyOrderBlocks()
        self.liquidity = SmartMoneyLiquidity()

    def detect_bos(
        self,
        data,
        lookback=20
    ):

        return self.structure.detect_bos(
            data,
            lookback
        )

    def detect_choch(
        self,
        data
    ):

        return self.structure.detect_choch(
            data
        )

    def detect_fvg(
        self,
        data
    ):

        return self.fvg.detect(
            data
        )

    def detect_order_block(
        self,
        data
    ):

        return self.orderblocks.detect(
            data
        )

    def detect_liquidity(
        self,
        data
    ):

        return self.liquidity.detect(
            data
        )