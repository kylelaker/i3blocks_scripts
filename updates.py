#!/usr/bin/env python3

"""
Script to check availability of updates on ArchLinux. This also checks to see
if there are any recent news entries
"""

import feedparser
import subprocess

def main():
    data = feedparser.parse('https://www.archlinux.org/feeds/news/')

    updatesList = subprocess.Popen(
        "pacaur -Qu | cut -d ' ' -f 1 | tr '\n' ' '",
        stdout=subprocess.PIPE,
        shell=True
    ).stdout.read().split()

    exclamation = " "
    downArrow = " "
    checkMark = " "

    for update in updatesList:
        for post in data.entries[0:2]:
            if update in post:
                print("<span color='#dc322f'>%s</span>" % exclamation)
                quit()

    if len(updatesList) > 0:
        print("<span color='#b58900'>%s</span>" % downArrow)
    else:
        print("<span color='#859900'>%s</span>" % checkMark)

if __name__ == '__main__':
    main()
