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

    :::python
    from onecallsms import OneCallInstance, SMS

    oc = OneCallInstance('phoneNumber', 'password')
    oc.login()

    sms = SMS('toPhoneNumber', 'essage', oc)
    sms.send()
