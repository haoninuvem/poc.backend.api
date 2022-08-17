from dependency_injector import containers, providers
from repository.alpaca_repository import AlpacaRepository
from service.candle_service import CandleService


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(packages=['app.routers'])

    alpaca_repository = providers.Factory(
        AlpacaRepository
    )

    candle_service = providers.Factory(
        CandleService,
        repo=alpaca_repository
    )
