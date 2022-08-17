from typing import List

from dto.candle_dto import CandleDto
from repository.alpaca_repository import AlpacaRepository


class CandleService():

    def __init__(self, repo: AlpacaRepository):
        self.repo = repo

    def get_candles(self, symbol: str, start_date: str, end_date: str) -> List[CandleDto]:
        # repo = AlpacaRepository()
        candles = self.repo.get_candles(symbol, start_date, end_date)
        candles_dto = list(map(lambda x: self.__convert_to_dto(candle = x)  ,candles._raw))
        return candles_dto        


    def __convert_to_dto(self, candle) -> CandleDto:
        
        candle_dto = CandleDto()
        candle_dto.open = candle['o']
        candle_dto.high = candle['h']
        candle_dto.low = candle['l']
        candle_dto.close = candle['c']
        candle_dto.volume = candle['v']
        candle_dto.timestamp = candle['t']

        return candle_dto
    
