# nafsmon
# versionCheck - check for new versions
# Copyright Vilhelm Prytz 2018

from version import version
import logging
import requests

def checkUpdate():
    logging.info("Checking if a new version is available..")
    r = requests.get("https://raw.githubusercontent.com/MrKaKisen/nafsmon/master/version.txt")

    # check if we got a good code, requests has builtin codes which are OK
    if (r.status_code == requests.codes.ok):
        if (r.text.split("\n")[0] == version):
            logging.info("You're running the latest version, " + version + "!")
        else:
            logging.info("NOTICE: There is a new version available! New version: " + r.text.split("\n")[0])
            performUpgrade()
    else:
        log("CRITICAL", "Couldn't receive latest version (on GitHub). Quitting.")
        exit(1)

# perform the auto upgrade
def performUpgrade():
    
