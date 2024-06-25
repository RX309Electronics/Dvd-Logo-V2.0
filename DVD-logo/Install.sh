#!/bin/sh
clear
cat << "EOF"
****************
* ____ __  ___ *
*|__ //  \/ _ \*
* |_ \ () \_, /*
*|___/\__/ /_/ *
*  | __| |___  *
*  | _|| / -_) *
*  |___|_\___| *
****************
EOF
echo "Thank you for downloading this project from my github!"
sleep 1
echo "This automated installer will now install everything that is required to be able to use/run my projects i made!"
sleep 0.5
echo "Please note, you might be asked to put in your password. This is because the installer needs to install some packages with root access (basicaly meaning the installer has permission to copy over and install the files needed and it also auto updates your system packages so everything is up to date) This wont harm your pc in any way i promise! This is just Linux being extra secure over what gets installed, but everything i use is opensource or virus free (also because i dont want to infect myself with malware)"
echo 
echo
echo "Please note that it might take some time before everything is updated and installed"
sleep 3
clear
echo "Updating system packages..."
sudo apt update && sudo apt upgrade -y
sleep 1
clear
echo "Done!"
sleep 1
echo 
echo "Installing packages..."
sudo apt install python3 python3-pip
sleep 1
clear
echo "Installing python libraries and modules..."
pip install -r requirements.txt --break-system-packages
sleep 1
clear
echo "Done and dusted!"
echo "Everything should be installed and ready to go."
echo "Now simply execute in the terminal of the project folder 'python3 Main.py' and the project should run. Have fun!"
sleep 2
exit
