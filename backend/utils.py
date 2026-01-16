import logging
import logging.config
import yaml
from pathlib import Path

path = Path.cwd() / "backend/logging.yaml"


def config_logger():
    try:
        with open(path) as f:
            config = yaml.safe_load(f)

        logging.config.dictConfig(config)
    except FileNotFoundError:
        print("could not find logging config file")
    except Exception as e:
        print(f"could not config logger {e}")
