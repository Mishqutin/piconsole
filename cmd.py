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


def logout():
    print("<h1>GRAMY DUBSTEPY OKRADAMY SKLEPY!!</h1>")
    print("Rozpierdalamy witryny skurwysyny<>")
    print("<h3>Chce bys sie kurwa zesral ze smiechu jak pojebany klaun!</h3>")
    print("<h2>MASZ PSZEJEBANE_________JAK BALWAN NA SACHARZE!</h2>")
    print("<h2>You're about to log off, have a nice day!<h2>")
    print('<meta http-equiv="refresh" content="0; url=http://78.28.45.60/piconsole/login/logout.php" />')





def saveConfig(config):
    f = open(CWD + "/cmdConfig", "w")
    f.write(str(config))
    f.close()

def cfgVarGet(name):
    return config["vars"][name]

def cfgVarSet(name, value):
    global config
    config["vars"][name] = value






ClientIP = sys.argv[1]

if not ClientIP in config["users"]:
    print("You seem new here! Lemme config your account...<br>")
    config["users"][ClientIP] = {"IP": ClientIP, "execClass": "home", "name": "unnamed", "cscConfig":{"host": "localhost", "port": 33302, "entryCode": "CHWDP_JP100"}}
    saveConfig(config)
    print("Hello! :)<br><br>")





def classExists(string):
    return os.path.isfile(CWD + "/data/cmdClasses/" + string + ".py")



# Load selected class from file

f = open(CWD + "/data/cmdClasses/" + config["users"][ClientIP]["execClass"]+".py", 'r')
code = f.read()
f.close()

exec(code, globals())














# Command execution



line = ' '.join(sys.argv[2:])

if line[0:2]=="?#":
    if classExists(line[2:]):
        config["users"][ClientIP]["execClass"] = line[2:]
        print("Updated execution class")
    else:
        print("No such class!")
elif line=="?stats":
    print("IP: {}<br>Username: {}<br>Class: {}".format(ClientIP, config["users"][ClientIP]["name"], config["users"][ClientIP]["execClass"]))
elif line=="?class":
    print(os.listdir(CWD + "/data/cmdClasses"))
elif line=="?logout":
    logout()
else:
    mainClass.cmdExec(line)

saveConfig(config)
