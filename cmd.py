#!/usr/bin/env python3
import sys, random, os

invalidCmd = ["Jestes ********", "********* cie", "Noo i ****", "**** wie", "**********", "*********** Ci obore", "Przepraszam, lecz podajac mi takowe oto argumenty rozumiem, iz nie boisz sie, ze wilize ci piety lub wyrzecam ci wlosy lonowe widelcem do ostryg.."]


cmds = {}

def cmdHelp(args):
    print("Tutaj pomocy nie znajdziesz.")
cmds["help"] = cmdHelp

def cmdEcho(args):
    if len(args)<1:
        print("Uzycie: echo tekst")
    else:
        print(' '.join(args))
cmds["echo"] = cmdEcho

def cmdCat(args):
    if len(args)<1:
        print("Uzycie: cat plik")
    else:
        if args[0]!="README.md":
            print("Lol nie masz praw")
        else:
            f = open("/var/www/html/piconsole/" + args[0], "r")
            x = f.read()
            f.close()
            print(x.replace("\n", "<br>"))
cmds["cat"] = cmdCat




line = ' '.join(sys.argv[1:])

if len(line.split())<1: line="xd"

cmd = line.split()[0]
args = line.split()[1:]

if cmd in cmds:
    cmds[cmd](args)
else:
    print(random.choice(invalidCmd))
