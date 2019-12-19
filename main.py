#!/usr/bin/env python3

import requests
import json
import re
import applescript
import time
import os
import subprocess
import atexit

caffeinate = subprocess.Popen('caffeinate')

def exit_handler():
    caffeinate.terminate()
    caffeinate.kill()

atexit.register(exit_handler)

while True:
    url = "https://www.redbus.in/next-date/130/134/Pune/Vijayawada/20%20Dec%202019/EN"
    seatThreshold = 12
    operatorName = 'nh safari'
    # Set the headers like we are a browser.
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}
    responseJson = requests.get(url, headers=headers).json()
    for row in responseJson['srpRow']:
        if operatorName in row['operator'].lower():
            seats = list(map(int, re.findall('\d+', row['seats'])))
            if min(seats) <= seatThreshold:
                applescript.run("set volume output volume 100")
                while True:
                    applescript.run('say "Book Tickets."')
                    time.sleep(0.2)
    time.sleep(10)
