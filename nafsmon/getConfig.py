# nafsmon
# getConfig - gets the config file
# Copyright Vilhelm Prytz 2017

# we will not import daemonLog as that module hasn't been inited yet
import ConfigParser
import io

class Config(object):

    def __init__(self):
        from configDir import configDir

        with open(configDir) as f:
            rawConfig = f.read()
        config = ConfigParser.RawConfigParser(allow_no_value=True)
        config.readfp(io.BytesIO(rawConfig))

        # add all contents into self vars (this section is cp from nafscraftd)
        for section in config.sections():
            for options in config.options(section):
                if section == "nafsmon":
                    if options == "logging_file":
                        self.logDir = config.get(section, options)
                    elif options == "??":
                        self.?? = config.get(section, options)
                elif section == "??":
                    if options == "??":
                        self.?? = config.get(section, options)
                    elif options == "??":
                        self.?? = config.get(section, options)
