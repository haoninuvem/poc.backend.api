from typing import List
from dto import CandleDto
from fastapi import APIRouter, BackgroundTasks, Depends, status
from infra.container import Container
from repository import AlpacaRepository
from dependency_injector.wiring import inject, Provide
from service import CandleService


router = APIRouter()

@router.get("/symbols/")
@inject
async def root(repo: AlpacaRepository = Depends(Provide[Container.alpaca_repository])):
    symbols = repo.get_all_symbols()
    return {"symbols": symbols}


@router.get("/candles/{symbol}/{start_date}/{end_date}")
@inject
# async def root(symbol: str, start_date: str, end_date: str):
async def root(symbol: str, start_date: str, end_date: str, service: CandleService = Depends(Provide[Container.candle_service])) -> List[CandleDto]:
    # service = AlpacaRepository()
    candles = service.get_candles(symbol, start_date, end_date)
    return candles
