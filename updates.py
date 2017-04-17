#!/usr/bin/env python3

import feedparser
import subprocess

data = feedparser.parse('https://www.archlinux.org/feeds/news/')

updatesList = subprocess.Popen("pacaur -Qu | cut -d ' ' -f 1 | tr '\n' ' '",
        stdout=subprocess.PIPE,
        shell=True).stdout.read().split()

exclamation = ""
downArrow = ""
checkMark = ""

for update in updatesList:
    for post in data.entries[0:2]:
        if update in post:
            print("<span color='#FF0000'>%s</span>" % exclamation)
            quit()

if len(updatesList) > 0:
    print("<span color='#FFF600'>%s</span>" % downArrow)
else:
    print("<span color='#00FF00'>%s</span>" % checkMark)
