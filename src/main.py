from src.configs.route import setup_routes
from src.configs.server import setup_server

app = setup_server()
setup_routes(app)


