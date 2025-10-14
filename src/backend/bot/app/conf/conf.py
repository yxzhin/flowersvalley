import os

from ....utils import ConfigLoader

ConfigLoader.import_env()


class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    BOT_SECRET = os.getenv("BOT_SECRET")
