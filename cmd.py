#!/usr/bin/env python3
import sys, random

invalidCmd = ["Jestes ********", "********* cie", "Noo i ****", "**** wie", "**********", "*********** Ci obore", "Przepraszam, lecz podajac mi takowe oto argumenty rozumiem, iz nie boisz sie, ze wilize ci piety lub wyrzecam ci wlosy lonowe widelcem do ostryg.."]


cmds = {}

def cmdHelp(args):
    print("Tutaj pomocy nie znajdziesz.\n Sprobuj: lol")
cmds["help"] = cmdHelp

def cmdLol(args):
    if len(args)<1:
        print("Uzycie: lol tekst")
    else:
        print("Chaslo nieprawilne: "+' '.join(args))
cmds["lol"] = cmdLol






line = ' '.join(sys.argv[1:])

if len(line.split())<1: line="chuj"

cmd = line.split()[0]
args = line.split()[1:]

if cmd in cmds:
    cmds[cmd](args)
else:
    print(random.choice(invalidCmd))


