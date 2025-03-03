from freqtrade.strategy.interface import IStrategy
import pandas as pd
import numpy as np
from freqtrade.strategy import IntParameter, DecimalParameter
import talib as ta

class MyStrategy(IStrategy):
    # Configurazione della strategia
    timeframe = '5m'
    stoploss = -0.05
    minimal_roi = {"0": 0.1}

    # Aggiunta di parametri per RSI e MACD
    rsi_buy = IntParameter(10, 50, default=30)
    rsi_sell = IntParameter(50, 90, default=70)

    def populate_indicators(self, dataframe: pd.DataFrame, metadata: dict) -> pd.DataFrame:
        dataframe['ema_short'] = ta.EMA(dataframe['close'], timeperiod=9)
        dataframe['ema_long'] = ta.EMA(dataframe['close'], timeperiod=21)
        dataframe['rsi'] = ta.RSI(dataframe, timeperiod=14)
        dataframe['macd'], dataframe['macdsignal'], dataframe['macdhist'] = ta.MACD(dataframe)
        return dataframe

    def populate_buy_trend(self, dataframe: pd.DataFrame, metadata: dict) -> pd.DataFrame:
        dataframe.loc[
            (dataframe['rsi'] < self.rsi_buy.value) & (dataframe['macd'] > dataframe['macdsignal']),
            'buy'] = 1
        return dataframe

    def populate_sell_trend(self, dataframe: pd.DataFrame, metadata: dict) -> pd.DataFrame:
        dataframe.loc[
            (dataframe['rsi'] > self.rsi_sell.value) & (dataframe['macd'] < dataframe['macdsignal']),
            'sell'] = 1
        return dataframe
