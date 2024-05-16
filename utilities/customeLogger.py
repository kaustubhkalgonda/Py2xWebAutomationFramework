import logging, os

class LogGen:

    @staticmethod
    def loggen():
        logger = logging.getLogger()
        fileHandler = logging.FileHandler(
            os.getcwd()+"/Logs/" + "automation.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger
