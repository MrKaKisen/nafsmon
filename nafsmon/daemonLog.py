# nafsmon
# deamonLog - logger functions
# Copyright Vilhelm Prytz 2017

from time import strftime

# log function
def log(level, log):
    from logDir import logDir

    f = open(logDir, "a")
    write = level + ": " + strftime("%a, %d %b %Y %H:%M:%S") + " - " + log + "\n"
    f.write(writes)
    f.close()

    if level == "CRITICAL" or level == "WARN":
        print(write)

# first time setup
def setupLog(config):
    f = open("logDir.py")
    f.write('logDir = "' + config.logDir + '"' + '\n')
    f.close()
