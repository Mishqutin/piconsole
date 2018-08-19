#!/usr/bin/env python3
import sys, random, os, socket, time, html
from inspect import isclass

invalidCmdWtf = ["Jestes ********", "********* cie", "Noo i ****", "**** wie", "**********", "*********** Ci obore", "Przepraszam, lecz podajac mi takowe oto argumenty rozumiem, iz nie boisz sie, ze wilize ci piety lub wyrzecam ci wlosy lonowe widelcem do ostryg.."]
invalidCmd = ["Twoja komenda jest inwalida"]

CWD = "/var/www/html/piconsole"

f = open(CWD + "/cmdConfig", 'r')
config = eval(f.read())
f.close()


# Text formatting functions:
def txtToHtml(string):
    x = html.escape(string).replace("\n", "<br>")
    return x







def saveConfig(config):
    f = open(CWD + "/cmdConfig", "w")
    f.write(str(config))
    f.close()






ClientIP = sys.argv[1]

if not ClientIP in config["users"]:
    print("You seem new here! Lemme config your account...<br>")
    config["users"][ClientIP] = {"IP": ClientIP, "execClass": "basicCmds", "name": "unnamed", "cscConfig":{"host": "localhost", "port": 33301, "entryCode": "CHWDP_JP100"}}
    saveConfig(config)
    print("Hello! :)<br><br>")





def classExists(string):
    pass
    #os.path.exist()




f = open(CWD + "/data/cmdClasses/" + config["users"][ClientIP]["execClass"], 'r')
code = f.read()
f.close()

exec(code, globals())














# Command execution



line = ' '.join(sys.argv[2:])

if line[0:2]=="?#":
    if classExists(line[2:]):
        config["users"][ClientIP]["execClass"] = line[2:]
        saveConfig(config)
        print("Updated execution class")
    else:
        print("No such class!")
elif line=="?stats":
    print("IP: {}<br>Username: {}<br>Class: {}".format(ClientIP, config["users"][ClientIP]["name"], config["users"][ClientIP]["execClass"]))
else:
    execClass.cmdExec(line)
