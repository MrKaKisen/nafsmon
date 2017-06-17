# nafsmon
# __main__ - main startup file
# Copyright Vilhelm Prytz 2017

# imports
from getConfig import setupConfig
from daemonLog import setupLog
from version import version
from versionCheck import checkUpdate

# get config
config = setupConfig()

# setup the logger
setupLog(config)
from daemonLog import log

log("DEBUG", "Welceom to nafsmon version " + version + "!")

# check for new versions
checkUpdate()
