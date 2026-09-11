//+------------------------------------------------------------------+
//|                                                   PhoenixAI.mq5  |
//|                       PROJECT PHOENIX AI                          |
//|                       Native MT5 Autonomous Trading Engine       |
//+------------------------------------------------------------------+
#property copyright "PROJECT PHOENIX AI"
#property version   "3.21"
#property strict

#include <Trade/Trade.mqh>

//====================================================================
// INPUT
//====================================================================
input group "=== PHOENIX GENERAL ==="
input string          InpSymbol              = "";
input ENUM_TIMEFRAMES InpTimeframe           = PERIOD_CURRENT;
input ulong           InpMagicNumber         = 260813;
input int             InpTimerSeconds        = 10;
input bool            InpEnableTrading       = false;
input bool            InpTradeOnlyNewBar     = true;
input int             InpMaxPositions        = 1;
input int             InpDeviationPoints     = 20;

input group "=== PHOENIX RISK ==="
input double InpRiskPercent       = 1.0;
input double InpRiskReward        = 2.0;
input double InpATRMultiplier     = 1.0;
input double InpMaxMarginPercent  = 50.0;
input int    InpStopSafetyPoints  = 5;

input group "=== PHOENIX DECISION ENGINE ==="
input int  InpMinimumScore       = 60;
input int  InpMinimumConfidence  = 55;
input bool InpAllowStrongSignals = true;

input group "=== PHOENIX MULTI TIMEFRAME ==="
input bool            InpUseHigherTFConfirmation = true;
input ENUM_TIMEFRAMES InpHigherTimeframe         = PERIOD_H1;
input int             InpHigherTFWeight           = 10;

input group "=== PHOENIX POSITION MANAGEMENT ==="
input bool   InpUseBreakEven      = true;
input double InpBreakEvenRR       = 1.0;
input bool   InpUseTrailingStop   = true;
input double InpTrailingATRMult   = 1.0;

input group "=== PHOENIX INDICATORS ==="
input int InpEMA20       = 20;
input int InpEMA50       = 50;
input int InpRSIPeriod   = 14;
input int InpATRPeriod   = 14;
input int InpADXPeriod   = 14;
input int InpMACDFast    = 12;
input int InpMACDSlow    = 26;
input int InpMACDSignal  = 9;

//====================================================================
// GLOBALS
//====================================================================
CTrade trade;

string           PhoenixSymbol     = "";
ENUM_TIMEFRAMES  PhoenixTimeframe  = PERIOD_CURRENT;
ENUM_TIMEFRAMES  PhoenixHigherTF   = PERIOD_H1;

datetime LastBarTime  = 0;
datetime LastTradeBar = 0;

int HandleEMA20 = INVALID_HANDLE;
int HandleEMA50 = INVALID_HANDLE;
int HandleRSI   = INVALID_HANDLE;
int HandleATR   = INVALID_HANDLE;
int HandleADX   = INVALID_HANDLE;
int HandleMACD  = INVALID_HANDLE;

int HandleHTFEMA20 = INVALID_HANDLE;
int HandleHTFEMA50 = INVALID_HANDLE;

//====================================================================
// DECISION STRUCTURE
//====================================================================
struct PhoenixDecision
{
   string action;
   int    score;
   int    confidence;
   int    bullish_score;
   int    bearish_score;
   bool   conflict;
   bool   higher_tf_bull;
   bool   higher_tf_bear;
   string reason;
};

//====================================================================
// LOGGING
//====================================================================
void PhoenixLog(string message)
{
   Print("[PHOENIX] ", message);
}

//====================================================================
// SYMBOL
//====================================================================
string GetPhoenixSymbol()
{
   if(InpSymbol == "")
      return _Symbol;

   return InpSymbol;
}

//====================================================================
// VOLUME DIGITS
//====================================================================
int VolumeDigits()
{
   double step =
      SymbolInfoDouble(
         PhoenixSymbol,
         SYMBOL_VOLUME_STEP
      );

   if(step >= 1.0)   return 0;
   if(step >= 0.1)   return 1;
   if(step >= 0.01)  return 2;
   if(step >= 0.001) return 3;

   return 4;
}

//====================================================================
// NORMALIZE VOLUME DOWN
//====================================================================
double NormalizeVolumeDown(double volume)
{
   double min_volume =
      SymbolInfoDouble(
         PhoenixSymbol,
         SYMBOL_VOLUME_MIN
      );

   double max_volume =
      SymbolInfoDouble(
         PhoenixSymbol,
         SYMBOL_VOLUME_MAX
      );

   double step =
      SymbolInfoDouble(
         PhoenixSymbol,
         SYMBOL_VOLUME_STEP
      );

   if(step <= 0.0 || max_volume <= 0.0)
      return 0.0;

   volume = MathMin(volume, max_volume);

   double normalized =
      MathFloor(
         (volume / step) + 1e-9
      ) * step;

   if(normalized < min_volume)
      return 0.0;

   return NormalizeDouble(
      normalized,
      VolumeDigits()
   );
}

//====================================================================
// COUNT PHOENIX POSITIONS
//====================================================================
int CountPhoenixPositions()
{
   int count = 0;

   for(int i = PositionsTotal() - 1;
       i >= 0;
       i--)
   {
      ulong ticket =
         PositionGetTicket(i);

      if(ticket == 0)
         continue;

      if(!PositionSelectByTicket(ticket))
         continue;

      string symbol =
         PositionGetString(
            POSITION_SYMBOL
         );

      long magic =
         PositionGetInteger(
            POSITION_MAGIC
         );

      if(
         symbol == PhoenixSymbol &&
         (ulong)magic == InpMagicNumber
      )
      {
         count++;
      }
   }

   return count;
}

//====================================================================
// NEW BAR
//====================================================================
bool IsNewBar()
{
   datetime current_bar =
      iTime(
         PhoenixSymbol,
         PhoenixTimeframe,
         0
      );

   if(current_bar <= 0)
      return false;

   if(current_bar != LastBarTime)
   {
      LastBarTime = current_bar;
      return true;
   }

   return false;
}

//====================================================================
// GET INDICATOR VALUE
//====================================================================
bool GetBufferValue(
   int handle,
   int buffer,
   int shift,
   double &value
)
{
   if(handle == INVALID_HANDLE)
      return false;

   double data[];
   ArraySetAsSeries(data, true);

   int copied =
      CopyBuffer(
         handle,
         buffer,
         shift,
         1,
         data
      );

   if(copied != 1)
      return false;

   value = data[0];

   if(value == EMPTY_VALUE)
      return false;

   return true;
}

//====================================================================
// INITIALIZE INDICATORS
//====================================================================
bool InitializeIndicators()
{
   HandleEMA20 =
      iMA(
         PhoenixSymbol,
         PhoenixTimeframe,
         InpEMA20,
         0,
         MODE_EMA,
         PRICE_CLOSE
      );

   HandleEMA50 =
      iMA(
         PhoenixSymbol,
         PhoenixTimeframe,
         InpEMA50,
         0,
         MODE_EMA,
         PRICE_CLOSE
      );

   HandleRSI =
      iRSI(
         PhoenixSymbol,
         PhoenixTimeframe,
         InpRSIPeriod,
         PRICE_CLOSE
      );

   HandleATR =
      iATR(
         PhoenixSymbol,
         PhoenixTimeframe,
         InpATRPeriod
      );

   HandleADX =
      iADX(
         PhoenixSymbol,
         PhoenixTimeframe,
         InpADXPeriod
      );

   HandleMACD =
      iMACD(
         PhoenixSymbol,
         PhoenixTimeframe,
         InpMACDFast,
         InpMACDSlow,
         InpMACDSignal,
         PRICE_CLOSE
      );

   if(HandleEMA20 == INVALID_HANDLE) return false;
   if(HandleEMA50 == INVALID_HANDLE) return false;
   if(HandleRSI   == INVALID_HANDLE) return false;
   if(HandleATR   == INVALID_HANDLE) return false;
   if(HandleADX   == INVALID_HANDLE) return false;
   if(HandleMACD  == INVALID_HANDLE) return false;

   if(InpUseHigherTFConfirmation)
   {
      HandleHTFEMA20 =
         iMA(
            PhoenixSymbol,
            PhoenixHigherTF,
            InpEMA20,
            0,
            MODE_EMA,
            PRICE_CLOSE
         );

      HandleHTFEMA50 =
         iMA(
            PhoenixSymbol,
            PhoenixHigherTF,
            InpEMA50,
            0,
            MODE_EMA,
            PRICE_CLOSE
         );

      if(HandleHTFEMA20 == INVALID_HANDLE)
         return false;

      if(HandleHTFEMA50 == INVALID_HANDLE)
         return false;
   }

   return true;
}

//====================================================================
// RELEASE INDICATORS
//====================================================================
void ReleaseIndicators()
{
   if(HandleEMA20 != INVALID_HANDLE)
      IndicatorRelease(HandleEMA20);

   if(HandleEMA50 != INVALID_HANDLE)
      IndicatorRelease(HandleEMA50);

   if(HandleRSI != INVALID_HANDLE)
      IndicatorRelease(HandleRSI);

   if(HandleATR != INVALID_HANDLE)
      IndicatorRelease(HandleATR);

   if(HandleADX != INVALID_HANDLE)
      IndicatorRelease(HandleADX);

   if(HandleMACD != INVALID_HANDLE)
      IndicatorRelease(HandleMACD);

   if(HandleHTFEMA20 != INVALID_HANDLE)
      IndicatorRelease(HandleHTFEMA20);

   if(HandleHTFEMA50 != INVALID_HANDLE)
      IndicatorRelease(HandleHTFEMA50);

   HandleEMA20    = INVALID_HANDLE;
   HandleEMA50    = INVALID_HANDLE;
   HandleRSI      = INVALID_HANDLE;
   HandleATR      = INVALID_HANDLE;
   HandleADX      = INVALID_HANDLE;
   HandleMACD     = INVALID_HANDLE;
   HandleHTFEMA20 = INVALID_HANDLE;
   HandleHTFEMA50 = INVALID_HANDLE;
}

//====================================================================
// HIGHER TIMEFRAME CONFIRMATION
//====================================================================
bool GetHigherTFConfirmation(
   bool &bullish,
   bool &bearish
)
{
   bullish = false;
   bearish = false;

   if(!InpUseHigherTFConfirmation)
      return true;

   double htf_ema20 = 0.0;
   double htf_ema50 = 0.0;

   if(!GetBufferValue(
      HandleHTFEMA20,
      0,
      1,
      htf_ema20
   ))
      return false;

   if(!GetBufferValue(
      HandleHTFEMA50,
      0,
      1,
      htf_ema50
   ))
      return false;

   if(htf_ema20 > htf_ema50)
      bullish = true;
   else if(htf_ema20 < htf_ema50)
      bearish = true;

   return true;
}

//====================================================================
// DECISION ENGINE
//====================================================================
bool CalculateDecision(
   PhoenixDecision &decision,
   double &atr
)
{
   decision.action         = "HOLD";
   decision.score          = 0;
   decision.confidence     = 0;
   decision.bullish_score  = 0;
   decision.bearish_score  = 0;
   decision.conflict       = false;
   decision.higher_tf_bull = false;
   decision.higher_tf_bear = false;
   decision.reason         = "";

   double ema20;
   double ema50;
   double rsi;
   double adx;
   double plusDI;
   double minusDI;
   double macdMain;
   double macdSignal;

   if(!GetBufferValue(
      HandleEMA20, 0, 1, ema20
   ))
      return false;

   if(!GetBufferValue(
      HandleEMA50, 0, 1, ema50
   ))
      return false;

   if(!GetBufferValue(
      HandleRSI, 0, 1, rsi
   ))
      return false;

   if(!GetBufferValue(
      HandleATR, 0, 1, atr
   ))
      return false;

   if(!GetBufferValue(
      HandleADX, 0, 1, adx
   ))
      return false;

   if(!GetBufferValue(
      HandleADX, 1, 1, plusDI
   ))
      return false;

   if(!GetBufferValue(
      HandleADX, 2, 1, minusDI
   ))
      return false;

   if(!GetBufferValue(
      HandleMACD, 0, 1, macdMain
   ))
      return false;

   if(!GetBufferValue(
      HandleMACD, 1, 1, macdSignal
   ))
      return false;

   if(!GetHigherTFConfirmation(
      decision.higher_tf_bull,
      decision.higher_tf_bear
   ))
      return false;

   int bull = 0;
   int bear = 0;

   string reasons = "";

   // TREND
   if(ema20 > ema50)
   {
      bull += 25;
      reasons += "Trend rialzista; ";
   }
   else if(ema20 < ema50)
   {
      bear += 25;
      reasons += "Trend ribassista; ";
   }

   // MACD
   if(macdMain > macdSignal)
   {
      bull += 20;
      reasons += "MACD BUY; ";
   }
   else if(macdMain < macdSignal)
   {
      bear += 20;
      reasons += "MACD SELL; ";
   }

   // ADX + DI
   if(adx >= 20.0)
   {
      if(plusDI > minusDI)
      {
         bull += 20;
         reasons += "Trend forte rialzista; ";
      }
      else if(minusDI > plusDI)
      {
         bear += 20;
         reasons += "Trend forte ribassista; ";
      }
   }

   // RSI
   if(rsi >= 50.0 && rsi < 70.0)
      bull += 15;
   else if(rsi > 30.0 && rsi < 50.0)
      bear += 15;

   if(rsi >= 70.0)
      bear += 10;

   if(rsi <= 30.0)
      bull += 10;

   // ADX STRENGTH
   if(adx >= 25.0)
   {
      if(plusDI > minusDI)
         bull += 10;
      else if(minusDI > plusDI)
         bear += 10;
   }

   // HIGHER TIMEFRAME CONFIRMATION
   if(InpUseHigherTFConfirmation)
   {
      if(decision.higher_tf_bull)
      {
         bull += MathMax(
            0,
            InpHigherTFWeight
         );

         reasons +=
            "Conferma HTF rialzista; ";
      }
      else if(decision.higher_tf_bear)
      {
         bear += MathMax(
            0,
            InpHigherTFWeight
         );

         reasons +=
            "Conferma HTF ribassista; ";
      }
      else
      {
         reasons +=
            "HTF neutro; ";
      }
   }

   decision.bullish_score = bull;
   decision.bearish_score = bear;

   int total = bull + bear;

   if(total <= 0)
   {
      decision.reason =
         "Dati insufficienti.";

      return true;
   }

   decision.score =
      MathMin(
         100,
         MathMax(
            bull,
            bear
         )
      );

   int difference =
      MathAbs(
         bull - bear
      );

   decision.conflict =
      (
         bull > 0 &&
         bear > 0 &&
         difference < 25
      );

   decision.confidence =
      (int)MathMin(
         100.0,
         50.0 +
         ((double)difference * 1.5)
      );

   if(decision.conflict)
      decision.confidence = 49;

   // HARD HTF FILTER:
   // se il timeframe superiore e' chiaramente opposto,
   // Phoenix non entra nella direzione contraria.
   bool htf_blocks_buy =
      InpUseHigherTFConfirmation &&
      decision.higher_tf_bear;

   bool htf_blocks_sell =
      InpUseHigherTFConfirmation &&
      decision.higher_tf_bull;

   if(
      bull > bear &&
      bull >= InpMinimumScore &&
      decision.confidence >= InpMinimumConfidence &&
      !decision.conflict &&
      !htf_blocks_buy
   )
   {
      decision.action = "BUY";
   }
   else if(
      bear > bull &&
      bear >= InpMinimumScore &&
      decision.confidence >= InpMinimumConfidence &&
      !decision.conflict &&
      !htf_blocks_sell
   )
   {
      decision.action = "SELL";
   }
   else
   {
      decision.action = "HOLD";
   }

   if(htf_blocks_buy)
      reasons +=
         "BUY bloccato dal timeframe superiore; ";

   if(htf_blocks_sell)
      reasons +=
         "SELL bloccato dal timeframe superiore; ";

   if(
      InpAllowStrongSignals &&
      decision.action == "BUY" &&
      bull >= 80
   )
   {
      reasons +=
         "Segnale BUY forte; ";
   }

   if(
      InpAllowStrongSignals &&
      decision.action == "SELL" &&
      bear >= 80
   )
   {
      reasons +=
         "Segnale SELL forte; ";
   }

   decision.reason = reasons;

   return true;
}

//====================================================================
// POSITION SIZE
//====================================================================
double CalculatePositionSize(
   ENUM_ORDER_TYPE order_type,
   double entry,
   double stop_loss
)
{
   double balance =
      AccountInfoDouble(
         ACCOUNT_BALANCE
      );

   if(balance <= 0.0)
      return 0.0;

   double risk_amount =
      balance *
      (InpRiskPercent / 100.0);

   if(risk_amount <= 0.0)
      return 0.0;

   double profit_for_one_lot = 0.0;

   if(!OrderCalcProfit(
      order_type,
      PhoenixSymbol,
      1.0,
      entry,
      stop_loss,
      profit_for_one_lot
   ))
   {
      PhoenixLog(
         "RISK | OrderCalcProfit fallito."
      );

      return 0.0;
   }

   double risk_per_lot =
      MathAbs(
         profit_for_one_lot
      );

   if(risk_per_lot <= 0.0)
      return 0.0;

   double raw_volume =
      risk_amount /
      risk_per_lot;

   double volume =
      NormalizeVolumeDown(
         raw_volume
      );

   PhoenixLog(
      StringFormat(
         "RISK | Balance=%.2f | Risk=%.2f | Risk/Lot=%.2f | Lots=%.2f",
         balance,
         risk_amount,
         risk_per_lot,
         volume
      )
   );

   return volume;
}

//====================================================================
// MINIMUM STOP DISTANCE
//====================================================================
double MinimumStopDistance()
{
   long stops_level =
      SymbolInfoInteger(
         PhoenixSymbol,
         SYMBOL_TRADE_STOPS_LEVEL
      );

   long freeze_level =
      SymbolInfoInteger(
         PhoenixSymbol,
         SYMBOL_TRADE_FREEZE_LEVEL
      );

   double point =
      SymbolInfoDouble(
         PhoenixSymbol,
         SYMBOL_POINT
      );

   long effective_level =
      (long)MathMax(
         stops_level,
         freeze_level
      );

   double minimum =
      (double)effective_level *
      point;

   double safety =
      (double)MathMax(
         0,
         InpStopSafetyPoints
      ) * point;

   return minimum + safety;
}

//====================================================================
// VALIDATE STOPS
//====================================================================
bool ValidateStops(
   ENUM_ORDER_TYPE order_type,
   double entry,
   double stop_loss,
   double take_profit
)
{
   double minimum_distance =
      MinimumStopDistance();

   if(order_type == ORDER_TYPE_BUY)
   {
      if(stop_loss >= entry)
         return false;

      if(take_profit <= entry)
         return false;

      if(
         (entry - stop_loss) <
         minimum_distance
      )
         return false;

      if(
         (take_profit - entry) <
         minimum_distance
      )
         return false;
   }
   else if(order_type == ORDER_TYPE_SELL)
   {
      if(stop_loss <= entry)
         return false;

      if(take_profit >= entry)
         return false;

      if(
         (stop_loss - entry) <
         minimum_distance
      )
         return false;

      if(
         (entry - take_profit) <
         minimum_distance
      )
         return false;
   }
   else
   {
      return false;
   }

   return true;
}

//====================================================================
// MARGIN GATE
//====================================================================
bool MarginGate(
   ENUM_ORDER_TYPE order_type,
   double volume,
   double price
)
{
   double required_margin = 0.0;

   if(!OrderCalcMargin(
      order_type,
      PhoenixSymbol,
      volume,
      price,
      required_margin
   ))
   {
      PhoenixLog(
         "RISK GATE | OrderCalcMargin fallito."
      );

      return false;
   }

   double equity =
      AccountInfoDouble(
         ACCOUNT_EQUITY
      );

   double margin_free =
      AccountInfoDouble(
         ACCOUNT_MARGIN_FREE
      );

   if(
      equity <= 0.0 ||
      margin_free <= 0.0
   )
      return false;

   double max_margin =
      equity *
      (InpMaxMarginPercent / 100.0);

   if(required_margin > max_margin)
   {
      PhoenixLog(
         StringFormat(
            "RISK GATE BLOCCATO | Margin=%.2f | Max=%.2f",
            required_margin,
            max_margin
         )
      );

      return false;
   }

   if(required_margin > margin_free)
   {
      PhoenixLog(
         StringFormat(
            "RISK GATE BLOCCATO | FreeMargin=%.2f | Required=%.2f",
            margin_free,
            required_margin
         )
      );

      return false;
   }

   return true;
}

//====================================================================
// FILLING MODE
//====================================================================
ENUM_ORDER_TYPE_FILLING GetFillingMode()
{
   long flags =
      SymbolInfoInteger(
         PhoenixSymbol,
         SYMBOL_FILLING_MODE
      );

   if(
      (flags & SYMBOL_FILLING_FOK) ==
      SYMBOL_FILLING_FOK
   )
      return ORDER_FILLING_FOK;

   if(
      (flags & SYMBOL_FILLING_IOC) ==
      SYMBOL_FILLING_IOC
   )
      return ORDER_FILLING_IOC;

   return ORDER_FILLING_IOC;
}

//====================================================================
// ORDER CHECK
//====================================================================
bool CheckOrder(
   ENUM_ORDER_TYPE order_type,
   double volume,
   double price,
   double stop_loss,
   double take_profit
)
{
   MqlTradeRequest request;
   MqlTradeCheckResult check;

   ZeroMemory(request);
   ZeroMemory(check);

   request.action       = TRADE_ACTION_DEAL;
   request.symbol       = PhoenixSymbol;
   request.volume       = volume;
   request.type         = order_type;
   request.price        = price;
   request.sl           = stop_loss;
   request.tp           = take_profit;
   request.deviation    = InpDeviationPoints;
   request.magic        = InpMagicNumber;
   request.comment      = "PROJECT PHOENIX AI";
   request.type_time    = ORDER_TIME_GTC;
   request.type_filling = GetFillingMode();

   ResetLastError();

   if(!OrderCheck(
      request,
      check
   ))
   {
      PhoenixLog(
         StringFormat(
            "ORDER CHECK FALLITO | LastError=%d",
            GetLastError()
         )
      );

      return false;
   }

   if(
      check.retcode !=
      TRADE_RETCODE_DONE
   )
   {
      PhoenixLog(
         StringFormat(
            "ORDER CHECK RIFIUTATO | Retcode=%u | %s",
            check.retcode,
            check.comment
         )
      );

      return false;
   }

   PhoenixLog(
      StringFormat(
         "ORDER CHECK OK | Margin=%.2f | Free=%.2f",
         check.margin,
         check.margin_free
      )
   );

   return true;
}

//====================================================================
// EXECUTE TRADE
//====================================================================
bool ExecutePhoenixTrade(
   string action,
   double atr
)
{
   if(!InpEnableTrading)
   {
      PhoenixLog(
         "DRY RUN | trading disattivato. Nessun ordine verra' inviato."
      );

      return false;
   }

   if(
      CountPhoenixPositions() >=
      InpMaxPositions
   )
   {
      PhoenixLog(
         "RISK GATE | Numero massimo di posizioni raggiunto."
      );

      return false;
   }

   MqlTick tick;

   if(!SymbolInfoTick(
      PhoenixSymbol,
      tick
   ))
   {
      PhoenixLog(
         "EXECUTION | Tick MT5 non disponibile."
      );

      return false;
   }

   ENUM_ORDER_TYPE order_type;
   double entry;

   if(action == "BUY")
   {
      order_type = ORDER_TYPE_BUY;
      entry = tick.ask;
   }
   else if(action == "SELL")
   {
      order_type = ORDER_TYPE_SELL;
      entry = tick.bid;
   }
   else
   {
      return false;
   }

   double stop_distance =
      atr * InpATRMultiplier;

   if(stop_distance <= 0.0)
   {
      PhoenixLog(
         "EXECUTION | ATR non valido."
      );

      return false;
   }

   double minimum_distance =
      MinimumStopDistance();

   if(stop_distance < minimum_distance)
      stop_distance = minimum_distance;

   int digits =
      (int)SymbolInfoInteger(
         PhoenixSymbol,
         SYMBOL_DIGITS
      );

   double execution_buffer =
      (double)MathMax(
         InpStopSafetyPoints,
         1
      ) *
      SymbolInfoDouble(
         PhoenixSymbol,
         SYMBOL_POINT
      );

   stop_distance +=
      execution_buffer;

   double stop_loss;
   double take_profit;

   if(action == "BUY")
   {
      stop_loss =
         entry - stop_distance;

      take_profit =
         entry +
         (stop_distance * InpRiskReward);
   }
   else
   {
      stop_loss =
         entry + stop_distance;

      take_profit =
         entry -
         (stop_distance * InpRiskReward);
   }

   entry =
      NormalizeDouble(
         entry,
         digits
      );

   stop_loss =
      NormalizeDouble(
         stop_loss,
         digits
      );

   take_profit =
      NormalizeDouble(
         take_profit,
         digits
      );

   if(!ValidateStops(
      order_type,
      entry,
      stop_loss,
      take_profit
   ))
   {
      PhoenixLog(
         "RISK GATE | Stop Loss / Take Profit non validi."
      );

      return false;
   }

   double volume =
      CalculatePositionSize(
         order_type,
         entry,
         stop_loss
      );

   if(volume <= 0.0)
   {
      PhoenixLog(
         "RISK GATE | Volume calcolato sotto il minimo."
      );

      return false;
   }

   if(!MarginGate(
      order_type,
      volume,
      entry
   ))
      return false;

   if(!CheckOrder(
      order_type,
      volume,
      entry,
      stop_loss,
      take_profit
   ))
   {
      PhoenixLog(
         "RISK GATE | MT5 OrderCheck bloccato."
      );

      return false;
   }

   trade.SetExpertMagicNumber(
      InpMagicNumber
   );

   trade.SetDeviationInPoints(
      InpDeviationPoints
   );

   trade.SetTypeFillingBySymbol(
      PhoenixSymbol
   );

   PhoenixLog(
      StringFormat(
         "ORDER READY | %s | Lots=%.2f | Entry=%.*f | SL=%.*f | TP=%.*f",
         action,
         volume,
         digits,
         entry,
         digits,
         stop_loss,
         digits,
         take_profit
      )
   );

   bool result = false;

   if(action == "BUY")
   {
      result =
         trade.Buy(
            volume,
            PhoenixSymbol,
            0.0,
            stop_loss,
            take_profit,
            "PROJECT PHOENIX AI"
         );
   }
   else
   {
      result =
         trade.Sell(
            volume,
            PhoenixSymbol,
            0.0,
            stop_loss,
            take_profit,
            "PROJECT PHOENIX AI"
         );
   }

   uint retcode =
      trade.ResultRetcode();

   if(
      !result ||
      (
         retcode != TRADE_RETCODE_DONE &&
         retcode != TRADE_RETCODE_PLACED
      )
   )
   {
      PhoenixLog(
         StringFormat(
            "ORDINE RIFIUTATO | Retcode=%u | %s",
            retcode,
            trade.ResultRetcodeDescription()
         )
      );

      return false;
   }

   PhoenixLog(
      StringFormat(
         "ORDINE ESEGUITO | %s | Volume=%.2f | Entry=%.*f | SL=%.*f | TP=%.*f | Order=%I64u | Deal=%I64u",
         action,
         volume,
         digits,
         entry,
         digits,
         stop_loss,
         digits,
         take_profit,
         trade.ResultOrder(),
         trade.ResultDeal()
      )
   );

   LastTradeBar =
      iTime(
         PhoenixSymbol,
         PhoenixTimeframe,
         0
      );

   return true;
}

//====================================================================
// POSITION MANAGEMENT
//====================================================================
void ManagePhoenixPositions()
{
   if(
      !InpUseBreakEven &&
      !InpUseTrailingStop
   )
      return;

   double atr = 0.0;

   if(!GetBufferValue(
      HandleATR,
      0,
      1,
      atr
   ))
      return;

   int digits =
      (int)SymbolInfoInteger(
         PhoenixSymbol,
         SYMBOL_DIGITS
      );

   MqlTick tick;

   if(!SymbolInfoTick(
      PhoenixSymbol,
      tick
   ))
      return;

   for(
      int i = PositionsTotal() - 1;
      i >= 0;
      i--
   )
   {
      ulong ticket =
         PositionGetTicket(i);

      if(ticket == 0)
         continue;

      if(!PositionSelectByTicket(ticket))
         continue;

      string symbol =
         PositionGetString(
            POSITION_SYMBOL
         );

      long magic =
         PositionGetInteger(
            POSITION_MAGIC
         );

      if(
         symbol != PhoenixSymbol ||
         (ulong)magic != InpMagicNumber
      )
         continue;

      long type =
         PositionGetInteger(
            POSITION_TYPE
         );

      double open_price =
         PositionGetDouble(
            POSITION_PRICE_OPEN
         );

      double sl =
         PositionGetDouble(
            POSITION_SL
         );

      double tp =
         PositionGetDouble(
            POSITION_TP
         );

      double current =
         (
            type == POSITION_TYPE_BUY
         )
         ? tick.bid
         : tick.ask;

      double risk_distance =
         MathAbs(
            open_price - sl
         );

      if(risk_distance <= 0.0)
         continue;

      double new_sl = sl;

      // BREAK EVEN
      if(InpUseBreakEven)
      {
         double trigger =
            risk_distance *
            InpBreakEvenRR;

         if(
            type == POSITION_TYPE_BUY &&
            current - open_price >= trigger
         )
         {
            if(sl < open_price)
               new_sl = open_price;
         }
         else if(
            type == POSITION_TYPE_SELL &&
            open_price - current >= trigger
         )
         {
            if(
               sl > open_price ||
               sl == 0.0
            )
               new_sl = open_price;
         }
      }

      // TRAILING STOP
      if(InpUseTrailingStop)
      {
         double trail_distance =
            MathMax(
               atr * InpTrailingATRMult,
               MinimumStopDistance()
            );

         if(
            type == POSITION_TYPE_BUY &&
            new_sl >= open_price
         )
         {
            double candidate =
               current - trail_distance;

            if(candidate > new_sl)
               new_sl = candidate;
         }
         else if(
            type == POSITION_TYPE_SELL &&
            new_sl <= open_price
         )
         {
            double candidate =
               current + trail_distance;

            if(
               new_sl == 0.0 ||
               candidate < new_sl
            )
            {
               new_sl = candidate;
            }
         }
      }

      new_sl =
         NormalizeDouble(
            new_sl,
            digits
         );

      if(
         new_sl == sl ||
         new_sl <= 0.0
      )
         continue;

      if(
         type == POSITION_TYPE_BUY &&
         new_sl <= sl
      )
         continue;

      if(
         type == POSITION_TYPE_SELL &&
         sl > 0.0 &&
         new_sl >= sl
      )
         continue;

      double minimum_distance =
         MinimumStopDistance();

      if(
         type == POSITION_TYPE_BUY &&
         (current - new_sl) <
         minimum_distance
      )
         continue;

      if(
         type == POSITION_TYPE_SELL &&
         (new_sl - current) <
         minimum_distance
      )
         continue;

      if(
         trade.PositionModify(
            ticket,
            new_sl,
            tp
         )
      )
      {
         PhoenixLog(
            StringFormat(
               "POSITION MANAGEMENT | Ticket=%I64u | New SL=%.*f",
               ticket,
               digits,
               new_sl
            )
         );
      }
      else
      {
         PhoenixLog(
            StringFormat(
               "POSITION MODIFY RIFIUTATO | Ticket=%I64u | Retcode=%u | %s",
               ticket,
               trade.ResultRetcode(),
               trade.ResultRetcodeDescription()
            )
         );
      }
   }
}

//====================================================================
// PHOENIX ENGINE
//====================================================================
void RunPhoenixEngine()
{
   ManagePhoenixPositions();

   if(InpTradeOnlyNewBar)
   {
      if(!IsNewBar())
         return;
   }

   if(
      CountPhoenixPositions() >=
      InpMaxPositions
   )
      return;

   PhoenixDecision decision;
   double atr = 0.0;

   if(!CalculateDecision(
      decision,
      atr
   ))
   {
      PhoenixLog(
         "DECISION | Impossibile calcolare gli indicatori."
      );

      return;
   }

   PhoenixLog(
      StringFormat(
         "DECISION | %s | Score=%d | Confidence=%d%% | Bull=%d | Bear=%d | HTF_Bull=%s | HTF_Bear=%s | %s",
         decision.action,
         decision.score,
         decision.confidence,
         decision.bullish_score,
         decision.bearish_score,
         decision.higher_tf_bull ? "YES" : "NO",
         decision.higher_tf_bear ? "YES" : "NO",
         decision.reason
      )
   );

   string htf_trend = "NEUTRAL";
   if(decision.higher_tf_bull)
      htf_trend = "BULLISH";
   else if(decision.higher_tf_bear)
      htf_trend = "BEARISH";

   string mtf_confirmation = "NO";
   if(
      (decision.action == "BUY"  && decision.higher_tf_bull) ||
      (decision.action == "SELL" && decision.higher_tf_bear)
   )
      mtf_confirmation = "YES";

   PhoenixLog(
      StringFormat(
         "MTF CONFIRMATION | MainTF=%s | HigherTF=%s | Decision=%s | HTF=%s | CONFIRMATION=%s",
         EnumToString(PhoenixTimeframe),
         EnumToString(PhoenixHigherTF),
         decision.action,
         htf_trend,
         mtf_confirmation
      )
   );

   if(decision.action == "HOLD")
      return;

   ExecutePhoenixTrade(
      decision.action,
      atr
   );
}

//====================================================================
// INIT
//====================================================================
int OnInit()
{
   PhoenixSymbol =
      GetPhoenixSymbol();

   PhoenixTimeframe =
      InpTimeframe;

   if(
      PhoenixTimeframe ==
      PERIOD_CURRENT
   )
   {
      PhoenixTimeframe =
         (ENUM_TIMEFRAMES)_Period;
   }

   PhoenixHigherTF =
      InpHigherTimeframe;

   if(
      PhoenixHigherTF ==
      PERIOD_CURRENT
   )
   {
      PhoenixHigherTF =
         PhoenixTimeframe;
   }

   if(PhoenixSymbol == "")
      PhoenixSymbol = _Symbol;

   if(!SymbolSelect(
      PhoenixSymbol,
      true
   ))
   {
      Print(
         "[PHOENIX] Impossibile selezionare il simbolo."
      );

      return INIT_FAILED;
   }

   if(InpTimerSeconds < 1)
   {
      Print(
         "[PHOENIX] Timer non valido."
      );

      return INIT_FAILED;
   }

   if(
      InpRiskPercent <= 0.0 ||
      InpRiskPercent > 100.0
   )
   {
      Print(
         "[PHOENIX] Risk percent non valido."
      );

      return INIT_FAILED;
   }

   if(InpRiskReward <= 0.0)
   {
      Print(
         "[PHOENIX] Risk/Reward non valido."
      );

      return INIT_FAILED;
   }

   if(InpATRMultiplier <= 0.0)
   {
      Print(
         "[PHOENIX] ATR multiplier non valido."
      );

      return INIT_FAILED;
   }

   if(
      InpMaxMarginPercent <= 0.0 ||
      InpMaxMarginPercent > 100.0
   )
   {
      Print(
         "[PHOENIX] Max margin percent non valido."
      );

      return INIT_FAILED;
   }

   if(InpMaxPositions < 1)
   {
      Print(
         "[PHOENIX] Max positions non valido."
      );

      return INIT_FAILED;
   }

   if(
      InpMinimumScore < 1 ||
      InpMinimumScore > 100
   )
   {
      Print(
         "[PHOENIX] Minimum score non valido."
      );

      return INIT_FAILED;
   }

   if(
      InpMinimumConfidence < 1 ||
      InpMinimumConfidence > 100
   )
   {
      Print(
         "[PHOENIX] Minimum confidence non valido."
      );

      return INIT_FAILED;
   }

   if(InpHigherTFWeight < 0)
   {
      Print(
         "[PHOENIX] Higher TF weight non valido."
      );

      return INIT_FAILED;
   }

   if(!InitializeIndicators())
   {
      Print(
         "[PHOENIX] Inizializzazione indicatori fallita."
      );

      ReleaseIndicators();

      return INIT_FAILED;
   }

   trade.SetExpertMagicNumber(
      InpMagicNumber
   );

   trade.SetDeviationInPoints(
      InpDeviationPoints
   );

   trade.SetTypeFillingBySymbol(
      PhoenixSymbol
   );

   EventSetTimer(
      InpTimerSeconds
   );

   PhoenixLog(
      "========================================"
   );

   PhoenixLog(
      "PROJECT PHOENIX AI AVVIATO"
   );

   PhoenixLog(
      "Native MT5 Autonomous Trading Engine"
   );

   PhoenixLog(
      "PHOENIX DECISION ENGINE v3.20"
   );

   PhoenixLog(
      "========================================"
   );

   PhoenixLog(
      "Symbol: " +
      PhoenixSymbol
   );

   PhoenixLog(
      StringFormat(
         "Timeframe: %s",
         EnumToString(
            PhoenixTimeframe
         )
      )
   );

   if(InpUseHigherTFConfirmation)
   {
      PhoenixLog(
         StringFormat(
            "Higher Timeframe: %s | Weight=%d | Confirmation=ON",
            EnumToString(PhoenixHigherTF),
            InpHigherTFWeight
         )
      );
   }
   else
   {
      PhoenixLog(
         "Higher Timeframe Confirmation: OFF"
      );
   }

   PhoenixLog(
      StringFormat(
         "Risk: %.2f%% | RR: 1:%.2f | MaxPositions=%d",
         InpRiskPercent,
         InpRiskReward,
         InpMaxPositions
      )
   );

   PhoenixLog(
      StringFormat(
         "Magic Number: %I64u",
         InpMagicNumber
      )
   );

   if(InpEnableTrading)
      PhoenixLog(
         "TRADING MT5 ATTIVO."
      );
   else
      PhoenixLog(
         "DRY RUN ATTIVO: nessun ordine reale verra' inviato."
      );

   return INIT_SUCCEEDED;
}

//====================================================================
// DEINIT
//====================================================================
void OnDeinit(
   const int reason
)
{
   EventKillTimer();

   ReleaseIndicators();

   PhoenixLog(
      StringFormat(
         "PROJECT PHOENIX AI arrestato. Reason=%d",
         reason
      )
   );
}

//====================================================================
// ON TICK
//====================================================================
void OnTick()
{
   RunPhoenixEngine();
}

//====================================================================
// ON TIMER
//====================================================================
void OnTimer()
{
   int positions =
      CountPhoenixPositions();

   PhoenixLog(
      StringFormat(
         "MONITOR | Posizioni Phoenix=%d | Equity=%.2f | Balance=%.2f | FreeMargin=%.2f",
         positions,
         AccountInfoDouble(ACCOUNT_EQUITY),
         AccountInfoDouble(ACCOUNT_BALANCE),
         AccountInfoDouble(ACCOUNT_MARGIN_FREE)
      )
   );
}

//====================================================================
// ON TRADE TRANSACTION
//====================================================================
//
// MqlTradeTransaction NON contiene il campo "magic".
// Il magic viene recuperato dalla request oppure dalla history.
//====================================================================
void OnTradeTransaction(
   const MqlTradeTransaction& trans,
   const MqlTradeRequest& request,
   const MqlTradeResult& result
)
{
   long magic =
      (long)request.magic;

   if(
      magic == 0 &&
      trans.deal > 0
   )
   {
      if(
         HistoryDealSelect(
            trans.deal
         )
      )
      {
         magic =
            HistoryDealGetInteger(
               trans.deal,
               DEAL_MAGIC
            );
      }
   }

   if(
      magic == 0 &&
      trans.order > 0
   )
   {
      if(
         HistoryOrderSelect(
            trans.order
         )
      )
      {
         magic =
            HistoryOrderGetInteger(
               trans.order,
               ORDER_MAGIC
            );
      }
   }

   if(
      (ulong)magic !=
      InpMagicNumber
   )
      return;

   PhoenixLog(
      StringFormat(
         "TRADE TRANSACTION | Type=%s | Deal=%I64u | Order=%I64u | Retcode=%u | Magic=%I64d",
         EnumToString(trans.type),
         trans.deal,
         trans.order,
         result.retcode,
         magic
      )
   );
}
//+------------------------------------------------------------------+
