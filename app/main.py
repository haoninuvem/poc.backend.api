from fastapi import FastAPI, Depends
from infra.container import Container
from app.routers import alpaca_router


def create_app() -> FastAPI:
    container = Container()

    app = FastAPI()
    app.container = container

    app.include_router(alpaca_router.router)

    return app

app = create_app()


@app.get("/")
async def root():
    return {"message": "Hello World"}


