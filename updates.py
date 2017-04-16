#!/usr/bin/env python3

import feedparser
import subprocess

data = feedparser.parse('https://www.archlinux.org/feeds/news/')

updatesProc = subprocess.Popen("pacaur -Qu | cut -d ' ' -f 1 | tr '\n' ' '", stdout=subprocess.PIPE, shell=True)
updates = updatesProc.stdout.read()

updatesList = updates.split()

for update in updatesList:
    for post in data.entries[0:2]:
        if update in post:
            print("<span color='#FF0000'></span>")
            quit()

if len(updatesList) > 0:
    print("<span color='#FFF600'></span>")
else:
    print("<span color='#00FF00'></span>")
