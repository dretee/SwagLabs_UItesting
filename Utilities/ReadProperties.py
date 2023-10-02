import configparser

configs = configparser.RawConfigParser()
configs.read(".\\Configurations\\config.ini")

class Readcongftest:

    @staticmethod
    def Getapplicationurl():
        url = configs.get("common data", "base_url")
        return url

    @staticmethod
    def GetUsername():
        username = configs.get("common data","username")
        return username

    @staticmethod
    def GetPassword():
        password = configs.get("common data","password")
        return password
