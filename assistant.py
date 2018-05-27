#!/usr/bin/env python
#
# assistant.py
# Custom Google Home based on the Google Assistant SDK for Python.
# Use this script as is or modify it to suit your requirements.
#
# Date:      27/05/2018
# Author:    Jonathan Lundstrom
# Website:   http://jonathanlundstrom.me
# Email:     contact@jonathanlundstrom.me

import time
import json
import struct
import serial
import os.path
import argparse
import RPi.GPIO as GPIO

import google.oauth2.credentials
from google.assistant.library import Assistant
from google.assistant.library.event import EventType
from google.assistant.library.file_helpers import existing_file

# Serial setup:
ring = serial.Serial('/dev/ttyUSB0', 115200, timeout=1);
time.sleep(2)
ring.write(b'0')

# GPIO setup:
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(25, GPIO.OUT)

def process_event(event):
    if event.type == EventType.ON_START_FINISHED:
        print()
        ring.write(b'1')

    if event.type == EventType.ON_CONVERSATION_TURN_STARTED:
        print()
        ring.write(b'2')
        GPIO.output(25,True)

    print(event)

    if event.type == EventType.ON_NO_RESPONSE:
        print()

    if event.type == EventType.ON_RESPONDING_STARTED:
        print()
        ring.write(b'3')

    if event.type == EventType.ON_RESPONDING_FINISHED:
        print()

    if (event.type == EventType.ON_CONVERSATION_TURN_FINISHED and event.args and not event.args['with_follow_on_turn']):
        print()
        ring.write(b'4')
        GPIO.output(25,False)

def initialize():

    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--credentials', type=existing_file, metavar='OAUTH2_CREDENTIALS_FILE', default=os.path.join(os.path.expanduser('/home/pi/.config'), 'google-assistant', 'credentials.json'), help='Path to store and read OAuth2 credentials')
    args = parser.parse_args()
    with open(args.credentials, 'r') as f:
        credentials = google.oauth2.credentials.Credentials(token=None, **json.load(f))

    with Assistant(credentials) as assistant:
        for event in assistant.start():
            process_event(event)


if __name__ == '__main__':
    initialize()
