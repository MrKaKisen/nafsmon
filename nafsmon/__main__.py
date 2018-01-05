# nafsmon
# __main__ - main startup file
# Copyright Vilhelm Prytz 2017

# imports
from version import version
from versionCheck import checkUpdate
from fileParser import *
from database import setupTimeScheduleDb
import os

# logging
import sys
import logging

def main():
    # logger setup
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # format for logger
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    # add stdout to logger
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # add file handler to logger
    fh = logging.FileHandler(logPath)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    # welcome
    logging.info("Welcome to nafsmon version " + version + "!")

    # check for new versions
    checkUpdate()

    # get configurations
    config = getConfig()

    # check if time schedule is here
    if not os.path.isfile(config.timeSchedulePath):
        logging.info("Time schedule file was not found. performing first time setup.")
        setupTimeScheduleDb(config)

    # run the daemon
    runDaemon(config)

if __name__ == "__main__":
    main()
