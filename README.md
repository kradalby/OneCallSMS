# OneCallSMS

This is a simple python package which lets you send SMS from a script and application written in python.

You will need to be a customer of OneCall to use this.

It is written for Python 3.4, but i cannot think of any reasons why it should not work with other versions.

## Features

* Send SMS

### Not yet implemented

* Good error handling
* Messages longer than 480 characters
* Multiple recipients
* Password not in plaintext

## Installation
To install just simply pip install:
    
    pip install git+git://github.com/kradalby/OneCallSMS.git

## Usage

    from onecall.onecall import OneCallSession, SMS

    oc = OneCallSession('phoneNumber', 'password')
    oc.login()

    sms = SMS('toPhoneNumber', 'Message', oc)
    sms.send()

# sms.py command

## Usage

    usage: sms.py [-h] [--number NUMBER] --tonumber TONUMBER --message MESSAGE

    Send SMS from commandline

    optional arguments:
      -h, --help            show this help message and exit
      --number NUMBER, -n NUMBER
                            OneCall phonenumber that you will send from
      --tonumber TONUMBER, -t TONUMBER
                            Phonenumber of the recipient
      --message MESSAGE, -m MESSAGE
                            The message you would like to send


## Configuration file
The sms.py script will look for a config file in your home dir named .onecallsms.json

It is written in JSON and might look like this:
    
    {
        "number": "",
        "password": ""
    }
