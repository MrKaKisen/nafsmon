# nafsmon
# fileParser - parses different files such as the config
# Copyright Vilhelm Prytz 2018

import logging

# imports
from database import dbConnection
from configDir import configDir
import ConfigParser

# obj for the main config (makes it easier to throw the config around)
class Config(object):
    # init the object (aka parsing the config)
    def __init__(self, configDir):
        parser = ConfigParser.ConfigParser()
        parser.read(configFile)

        try:
            self.timeSchedulePath = parser.get("nafsmon", "timeSchedulePath")
        except Exception:
            logging.exception("Could not read the configuration.")
            logging.critical("Could not read the configuration. Please check your configuration.")
            quit(1)

# parse the main config
def getConfig():
    config = Config(configDir)

    return config

# parse the timeSchedule
def parseTimeSchedule():
