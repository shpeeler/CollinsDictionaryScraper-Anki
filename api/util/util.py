import os
import datetime
import json

class Util(object):
       
    @staticmethod
    def get_base_directory():
        """
        returns the modules base directory
        """

        directory = os.path.dirname(os.path.abspath(__file__))
        results = directory.split('\\')
        tail = results[-1].lower()

        while tail != 'collinsdictionaryscraper':
            directory = os.path.dirname(os.path.abspath(directory))
            results = directory.split('\\')
            tail = results[-1].lower()

        return directory

    @staticmethod
    def write(message):
        """
        writes exception-messages in the log.txt file located in the modules base directory
        """

        baseDir = Util.get_base_directory()
        logFile = baseDir + '/log.txt'

        with open(logFile, "a") as log:
            log.write(str('{0} | {1}\n').format(datetime.datetime.now(), message))  

    @staticmethod
    def read_config():
        """ 
        reads the config file located in the resources directory
        """

        content = None

        baseDir = Util.get_base_directory()
        configDir = baseDir + '/resources/config.json'

        try:
            with open(configDir) as json_file:
                content = json.load(json_file)

        except IOError:
            Util.write('Config nicht gefunden unter dem Dateipfad {configDir}\n')

        return content

    @staticmethod
    def get_icon_path():
        baseDir = Util.get_base_directory() 
        return baseDir + '/resources/icon.png' 