# nafsmon
# preSetup.py - setup for db and other stuff
# Copyright Vilhelm Prytz 2018

import logging

# imports
from database import dbConnection

def setupServerListConfDb(config):
    connection, cursor, connectionStatus = dbConnection(config.serverListConfPath)

    if connectionStatus == False:
        logging.critical("Exit due to SQL connection failure")
        exit(1)
