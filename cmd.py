#!/usr/bin/env python3
import sys, random, os

invalidCmdWtf = ["Jestes ********", "********* cie", "Noo i ****", "**** wie", "**********", "*********** Ci obore", "Przepraszam, lecz podajac mi takowe oto argumenty rozumiem, iz nie boisz sie, ze wilize ci piety lub wyrzecam ci wlosy lonowe widelcem do ostryg.."]
invalidCmd = ["Twoja komenda jest inwalida"]

CWD = "/var/www/html/piconsole"

f = open(CWD + "/cmdConfig", 'r')
config = eval(f.read())
f.close()


class basicCmds:
    def cmdExec(line):
        line = ' '.join(sys.argv[1:])

        if len(line.split())<1: line="xd"

        cmd = line.split()[0]
        args = line.split()[1:]

        if cmd in cmds:
            cmds[cmd](args)
        else:
            print(random.choice(invalidCmd))


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

class testCmds:
    def cmdExec(line):
        print(line)


# Command execution
execClass = eval(config["execClass"])

line = ' '.join(sys.argv[1:])
if line[0:1]=="#?":
    config["execClass"] = line[2:]
    f = open(CWD + "/cmdConfig", "w")
    f.write(str(config))
    f.close()
    print("Updated execution class")
else:
    execClass.cmdExec(line)
