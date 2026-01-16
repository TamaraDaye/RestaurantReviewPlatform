import logging
import logging.config
import yaml
from pythonjsonlogger import jsonlogger


logger = logging.getLogger("app")


def main():
    print("from main")
    config_logger()
    logger.info("This is informatics")
    logger.warning("This is a warning")
    logger.debug("Change the highlight of this")


def config_logger():
    with open("logging_config.yaml") as f:
        config = yaml.safe_load(f)

    logging.config.dictConfig(config)


if __name__ == "__main__":
    main()
