#!/bin/bash
# nafsmon
# Installation script
# Copyright Vilhelm Prytz 2018

# check if user is root or not
if [[ $EUID -ne 0 ]]; then
  echo "This script must be run with root privileges (sudo)." 1>&2
  exit 1
fi

DL_URL="https://github.com/MrKaKisen/nafsmon/archive"
INSTALL_DIR="/etc/nafsmon/bin"

echo "############################################################################"
echo "* nafsmon installation script revision"
echo "* ONLY install nafsmon on clean OS installations"
echo "* please note that this script will NOT upgrade a current installation"
echo "* copyright Vilhelm Prytz 2018"
echo "############################################################################"
echo -n "* Which version would you like to install? (type latest for latest version): "
read USER_VERSION
echo -n "* Continue installation? (y/n): "
read CONFIRM

if [ "$CONFIRM" == "y" ]; then
  echo "* Proceeding..."
else
  echo "* Exiting installer..."
  exit 0
fi

# working dir
CURRENT_DIR=pwd
mkdir /tmp/nafsmon-installation && cd /tmp/nafsmon-installation

# detect which OS

# install pip
echo "* Instaling pip.."
if [ "$OS" == "CentOS" ]; then
  curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
  python get-pip.py
elif [ "$OS" == "Debian" ] || [ "$OS" == "Ubuntu" ]; then
  apt-get update -y
  apt-get install python-pip -y
else
  echo "* Invalid operating system ($OS)."
  exit 1
fi

# install requirements
echo "* Installing required packages.."
curl -o requirements.txt https://raw.githubusercontent.com/MrKaKisen/nafsmon/master/scripts/requirements.txt

pip install -r requirements.txt

# get latest version
echo "* Fetching latest version.."
LATEST_VERSION=$(curl https://raw.githubusercontent.com/MrKaKisen/nafsmon/master/version.txt)
echo "* Latest version is: $LATEST_VERSION"

# delete working dir
cd $CURRENT_DIR
rm -rf /tmp/nafsmon-installation

echo "############################################################################"
echo "* Installation complete."
