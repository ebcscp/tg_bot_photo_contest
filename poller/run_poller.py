import asyncio
from typing import Optional
from poller.poller import Poller

#from rabbit.rmq_worker import WorkerRmq
import os
import yaml

from dataclasses import dataclass

@dataclass
class TokenPoller:
    token:str
    

class BotPoller:
    def __init__(self, config: TokenPoller):
        self.poller: Optional[Poller] = None
        self.config = config

    async def connect(self):
        self.poller = Poller(self.config)
        await self.poller.start()

    async def disconnect(self):
        if self.poller:
            await self.poller.stop()


def get_config():
    config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "configs/config.yml")
    print(config_path)

    with open(config_path, "r", encoding="utf8") as f:
        raw_config = yaml.safe_load(f)

    # return {"queue_name": raw_config["rabbitmq"]["queue_name"],
    #         "rabbit_url": raw_config["rabbitmq"]["rabbit_url"],
    return {"bot_token": raw_config["bot"]["token"]}


def run_poller():
    config = get_config()
    tokenpoler = TokenPoller(
        token=config["bot_token"]
    )
    # rmq_config_worker = WorkerConfig(
    #     queue_name=config["queue_name"],
    #     rabbit_url=config["rabbit_url"],
    #     token=config["bot_token"]
    # )

    bot_poller = BotPoller(tokenpoler)
    loop = asyncio.get_event_loop()
    loop.create_task(bot_poller.connect())
    loop.run_forever()