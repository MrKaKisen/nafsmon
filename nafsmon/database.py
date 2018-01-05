# nafsmon
# database.py - database (sql) connections
# Copyright Vilhelm Prytz 2018

import logging

# imports
import sqlite3

def dbConnection(sqlfile):
    try:
        connection = sqlite3.connect(sqlfile)
    except Exception:
        logging.exception("Could not establish SQL connection!")
        logging.error("SQL connection failure - is the specified file present?")

        # return null connection and cursor, but false boolean (so we know conn. failed)
        return None, None, False

    cursor = connection.cursor()
    return connection, cursor, True

def setupTimeScheduleDb(config):
