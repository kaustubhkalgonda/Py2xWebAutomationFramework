import configparser,os

config = configparser.RawConfigParser()
config.read(os.getcwd()+"/Configurations/config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        return config.get('common info','baseURL')

    @staticmethod
    def getUsername():
        return config.get('common info', 'username')

    @staticmethod
    def getPassword():
        return config.get('common info', 'password')
