import configparser
import logging

config = configparser.RawConfigParser()
config.read("./Configurations/config.ini")

class ReadConfig:

    @staticmethod
    def get_url():
        url =  config.get("common data","baseURL")
        return url
    
    @staticmethod
    def get_user():
        return config.get("common data","useremail")
    
    @staticmethod
    def get_pwd():
        return config.get("common data","password")
    
class LogInfo:

    @staticmethod
    def loginfo():
        
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

        logging.basicConfig(filename="./Logs/automation.log",
                                     format = '%(asctime)s: %(filename)s: %(levelname)s: %(message)s',
                                     datefmt='%d/%m/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
