#!/usr/bin/env python

from ast import List
import fastapi
from lib.factories.a_factory import AFactory
from lib.factories.factory_provider import FactoryProvider
from lib.repository.persist_fs import PersistFS


def run_main(argv):
    """run main new_section"""
    factory: AFactory = FactoryProvider(PersistFS).provide()
    return factory.get_processor(argv).process()


def demo():
    """Just a demo"""
    import uvicorn
    import os

    os.environ["CONFIG_FILE"] = "./map.yaml"
    app = fastapi.FastAPI()

    @app.get("/")
    async def usage():
        """Usage"""
        return {"usage": "/docs"}

    @app.get("/app")
    async def run_app(arg="app help"):
        """run_app"""
        argsv = arg.split(" ")
        return run_main(argsv)

    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    demo()
