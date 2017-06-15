# nafsmon
# deamonLog - logger functions
# Copyright Vilhelm Prytz 2017

# log function as class
class Log(object):
    from time import strftime

    def __init__(self, configDir):
        self.configDir = configDir

    def log(self, level, log):
        f = open(self.configDir, "a")
        write = level + ": " + strftime("%a, %d %b %Y %H:%M:%S") + " - " + log + "\n"
        f.write(write)
        f.close()

        if level == "CRITICAL" or level == "WARN":
            print(write)

# first time setup
def setupLog(configDir):
    log = Log(configDir)

    return log
