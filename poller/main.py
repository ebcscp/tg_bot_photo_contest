import os

from poller import poller_config
from poller.poller.poller import run_poller

if __name__ == "__main__":
    run_poller(
        poller_config(
            config_path=os.path.join(
                os.path.dirname(os.path.realpath(__file__)), "config.yml"
            )
        )
    )