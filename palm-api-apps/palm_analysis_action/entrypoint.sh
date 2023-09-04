#!/bin/sh

file_path=$1
api_key=$2

sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-pip
# pip install -r $GITHUB_PATH/requirements.txt
#
# touch analysis.txt
# result=$(python3 $GITHUB_PATH/main.py $1 $2)
#
# touch result.txt
# echo "$result" >> result.txt
# cat result.txt

# exit $?

