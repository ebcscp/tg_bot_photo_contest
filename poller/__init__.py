with open(config_path, "r", encoding="utf-8") as f:
        raw_config = yaml.safe_load(f)
token = os.getenv("BOT_TOKEN")
    config = PollerConfig(
        worker_client_config=WorkerClientConfig(
            rabbit_url=os.getenv("RABBITMQ_URL"),
            queue_name="bot_poller"
        ),
        logger_config=BotLoggerConfig(
            rabbit_url=os.getenv("RABBITMQ_URL"),
            mongo_url=os.getenv("MONGO_URL"),
            name="bot_logger",
        )
    )

def create_config(config_path: str) -> Config:
    with open(config_path, "r", encoding="utf-8") as f:
        raw_config = yaml.safe_load(f)

    return Config(
        rabbit=RabbitConfig(
            queue_name=raw_config["rabbitmq"]["queue_name"],
            exchange_name=raw_config["rabbitmq"]["exchange_name"],
            rabbit_url=raw_config["rabbitmq"]["rabbit_url"],
        ),
        tg=TgConfig(
            token=raw_config["bot"]["token"]
        )
    )