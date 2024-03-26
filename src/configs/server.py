from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def setup_server() -> FastAPI:
    app = FastAPI(root_path='/api/v1')

    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )

    return app