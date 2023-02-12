import typing
from dataclasses import dataclass

import yaml

if typing.TYPE_CHECKING:
    from app.app import Application


# @dataclass
# class SessionConfig:
#     key: str


# @dataclass
# class AdminConfig:
#     email: str
#     password: str


@dataclass
class BotConfig:
    token: str
    api_path: int


@dataclass
class Config:
    # admin: AdminConfig
    # session: SessionConfig = None
    bot: BotConfig = None


def setup_config(app: "Application", config_path: str):
    # TODO: добавить BotConfig и SessionConfig по данным из config.yml
    with open(config_path, "r") as f:
        raw_config = yaml.safe_load(f)

    app.config = Config(
        # admin=AdminConfig(
        #     email=raw_config["admin"]["email"],
        #     password=raw_config["admin"]["password"],
        # ),

        # session=SessionConfig(
        #     key=raw_config["session"]["key"],
        # ),

        bot=BotConfig(
            token=raw_config["bot"]["token"],
            api_path=raw_config["bot"]["api_path"],
        ),
    )