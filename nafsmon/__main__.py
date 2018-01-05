# nafsmon
# __main__ - main startup file
# Copyright Vilhelm Prytz 2017

# imports
from version import version
from versionCheck import checkUpdate

def main():
    logging.info("Welceom to nafsmon version " + version + "!")

    # check for new versions
    checkUpdate()

if __name__ == "__main__":
    main()
