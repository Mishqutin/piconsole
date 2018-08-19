#!/usr/bin/env python3
import sys

ClientIP = sys.argv[1]


CWD = "/var/www/html/piconsole"

f = open(CWD + "/README.md")
x = f.read()
f.close()

print(x.replace("\n", "<br>"))

someText = """\
Po pomoc wpisz: help
<br>
"""

print(someText.replace("\n", "<br>"))
