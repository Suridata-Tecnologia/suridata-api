from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def setup_server() -> FastAPI:
    config = {
        'title': 'Suridata API.v1',
        'redoc_url': '/docs',
        'docs_url': '/docss'
    }
    app = FastAPI(root_path='/api/v1', **config)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )

    return app