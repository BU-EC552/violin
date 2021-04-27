#!/bin/bash

env_setup () {
    # install requirements
    if [ "$dev_env" == "windows" ]
    then
        pip install -r ../requirements.txt
    else
        pip3 install -r ../requirements.txt
    fi
}
# Ask user for development environment
echo "Please follow the prompts for setting up VIOLIN"
echo "To help you set up your enviroment,"
echo "Please enter which environment you're developing on (windows, mac, linux, unix): "
read dev_env
env_setup

#PS3='Please enter your choice: '
#options=("Define Logic" "Create my own truth table" "Quit")
#select opt in "${options[@]}"
#do
#    case $opt in
#        "Option 1")
#            echo "you chose choice 1"
#            ;;
#        "Option 2")
#            echo "you chose choice 2"
#            ;;
#        "Option 3")
#            echo "you chose choice $REPLY which is $opt"
#            ;;
#        "Quit")
#            break
#            ;;
#        *) echo "invalid option $REPLY";;
#    esac
#done
#echo "To help you set up your enviroment,"