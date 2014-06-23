#!/usr/bin/env python3

import argparse
import getpass
import json
import os
from onecall.onecall import OneCallSession, SMS

if __name__ == "__main__":

    configFile = "%s/.onecallsms.json" % os.getenv("HOME")
    config = ""

    parser = argparse.ArgumentParser(description='Send SMS from commandline')

    if os.path.isfile(configFile):
        config = json.loads(open(configFile, 'r').read())
        parser.add_argument('--number', '-n', dest='number', 
                            help='OneCall phonenumber that you will send from')
    else:
        print("You should use a config file, read docs")
        parser.add_argument('--number', '-n', dest='number', required=True, 
                            help='OneCall phonenumber that you will send from')

    parser.add_argument('--tonumber', '-t', dest='tonumber', required=True,
                        nargs='+', help='Phonenumber of the recipient')
    parser.add_argument('--message', '-m', dest='message', required=True,
                        help='The message you would like to send')

    args = parser.parse_args()
    
    if config == "":
        number = args.number
        password = getpass.getpass()
    else: 
        number = config["number"]
        password = config["password"]

    oc = OneCallSession(number, password)
    oc.login()

    sms = SMS(args.tonumber, args.message, oc)
    sms.send()
