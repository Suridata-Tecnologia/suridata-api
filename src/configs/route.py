import importlib
from pathlib import Path
from fastapi import FastAPI


def setup_routes(app: FastAPI) -> FastAPI:
    routes_path = 'src/routes'

    for file in Path(routes_path).glob('*.py'):
        module_path = file.as_posix().replace('/', '.').strip('.py')

        router_module = importlib.import_module(module_path, 'router')
        app.include_router(router_module.router)
