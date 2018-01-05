# nafsmon
# versionCheck - check for new versions
# Copyright Vilhelm Prytz 2018

from version import version
import logging
import requests

def checkUpdate():
    log("Checking if a new version is available..")
    r = requests.get("https://raw.githubusercontent.com/MrKaKisen/nafsmon/master/version.txt")

    # check if we got a good code, requests has builtin codes which are OK
    if (r.status_code == requests.codes.ok):
        if (r.text.split("\n")[0] == version):
            log("DEBUG", "You're running the latest version, " + version + "!")
        else:
            log("WARN", "NOTICE: There is a new version available! New version: " + r.text.split("\n")[0])
    else:
        log("CRITICAL", "Couldn't receive latest version (on GitHub). Quitting.")
        exit(1)
