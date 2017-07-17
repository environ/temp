#!/bin/sh

ps auxw | grep temp.py | grep -v grep > /dev/null

if [ $? != 0 ]
then
       sudo python -u ~/temp/temp.py &
fi
