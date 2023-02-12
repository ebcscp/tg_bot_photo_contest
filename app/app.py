from aiohttp.web import Application
from app.logger import setup_logging
from app.config import setup_config

app = Application()


def setup_app(config_path: str):
    setup_config(app, config_path)
    setup_logging(app)
    return app