from poller import config
from poller.dataclass_config import Config, RabbitConfig, TgConfig 
import typing
import yaml

def poller_config(config_path: str) -> Config:
    with open(config_path, "r", encoding="utf-8") as f:
            raw_config = yaml.safe_load(f)
    return  Config(
        rabbit=RabbitConfig(
            queue_name=raw_config["rabbitmq"]["queue_name"],
            exchange_name=raw_config["rabbitmq"]["exchange_name"],
            rabbit_url=raw_config["rabbitmq"]["rabbit_url"],
        ),
        tg=TgConfig(
            token=raw_config["bot"]["token"],
            api_path=raw_config["bot"]["api_path"]
        )
    )       
