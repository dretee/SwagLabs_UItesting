import logging


class logen:

    @staticmethod
    def logging_info():
        logging.basicConfig(filename=".\\Logs\\automation.log",
                            format="%(asctime)s: %(levelname)s: %(message)s", datefmt="%d/%m/%Y %I:%M:%S %p")

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        return logger
