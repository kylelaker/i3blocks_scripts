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
            print("")
            quit()

if len(updatesList) > 0:
    print("")
else:
    print("")
