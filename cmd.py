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
    x = string.replace("\n", "<br>").replace(" ", "&nbsp;") #.replace("<", "&lt;").replace(">", "&gt;")
    return x







def saveConfig(config):
    f = open(CWD + "/cmdConfig", "w")
    f.write(str(config))
    f.close()






ClientIP = sys.argv[1]

if not ClientIP in config["users"]:
    print("You seem new here! Lemme config your account...<br>")
    config["users"][ClientIP] = {"IP": ClientIP, "execClass": "basicCmds", "name": "unnamed"}
    saveConfig(config)
    print("Hello! :)<br><br>")





def classExists(string):
    try:
        if isclass(eval(string)):
            return True
    except:
        return False
    return False


class basicCmds:
    def cmdExec(line):

        if len(line.split())<1: line="xd"

        cmd = line.split()[0]
        args = line.split()[1:]

        if cmd in basicCmds.cmds:
            basicCmds.cmds[cmd](args)
        else:
            print(random.choice(invalidCmd))



    helpText = """\
Tu ma byc pomoc ale na razie jest slaba
Wienc tak:
Jestes w prostej konsoli: basicCmds
Mozesz zmieniac konsole przez: ?#nazwa
Jest jeszcze konsola... No nie wiem, projekt jest od roku lub dwoch, a nie ma nazwy.
Wiec wpisz '?#cscCmds' aby przejsc do konsoli, przez ktora mozesz rozgladac sie po systemie plikow.
Wtedy mozesz uzywac ls, cd, cat itp
Komendy sa w /home/pi/Documents/server/shell

Komendy w basicCmds:
help
username nazwa - zmienia twoj username
motd - Najwazniejsza komenda musisz ja uzyc kazdego dnia chociaz raz, bo timeline sie zalamie
"""



    cmds = {}

    def cmdHelp(args):
        print(basicCmds.helpText.replace("\n", "<br>"))
    cmds["help"] = cmdHelp

    def cmdEcho(args):
        if len(args)<1:
            print("Uzycie: echo tekst")
        else:
            print(' '.join(args))
    cmds["echo"] = cmdEcho

    def cmdLol(args):
        print("uzycie komenda &lt;<b>Bold stuff</b>&gt;")
    cmds["lol"] = cmdLol

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

    def cmdUsername(args):
        global config
        if len(args)<1:
            print("Your username is: "+config["users"][ClientIP]["name"])
        else:
            config["users"][ClientIP]["name"] = args[0]
            saveConfig(config)
    cmds["username"] = cmdUsername

    def cmdMotd(args):
        print("Message of the day:<br><br>->&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;~-- [ SQUATTING LOW, MOVING FAST ] --~<br><br>")
    cmds["motd"] = cmdMotd





class cscCmds:
    def cmdExec(line):
        cscCmds.client(line)

    config = {"name": config["users"][ClientIP]["name"], "entryCode": "CHWDP_JP100"}
    IP = ("localhost", 33301)

    def client(x):
        #if x[0]=="/":
            #reconnect(x[1:].split())
            #return 0

        # Connect to host
        try:
            s = socket.socket()
            s.connect(cscCmds.IP)
        except:
            print("Could not connect to server")
            return 1

        s.send(( cscCmds.config["name"]+"@"+cscCmds.config["entryCode"] ).encode())
        reply = (s.recv(16)).decode("ASCII")
        if reply!="ok":
            print("Access denied.")
            s.close()
            return 2


        # Send command as byte string
        s.send(x.encode())

        # Loop will end after disconnection
        while True:
            try:
                # Receive text and save as string
                txt = (s.recv(65536)).decode("ASCII")

                # Receiving empty string means that socket's closed
                if txt=="": break
                # Execute requested script from /scripts
                elif txt[0:3]=="#//":
                    # Script file name
                    cmd = txt.split()[0][3:]
                    # Additional arguments
                    args = txt.split()[1:]

                    # Script existence check
                    if os.path.isfile("scripts/{}.py".format(cmd)):
                        # Load script
                        f = open("scripts/{}.py".format(cmd), 'r')
                        code = f.read()
                        f.close()

                        # Execute it
                        exec(code, globals())
                    # Invalid script name
                    else:
                        print("Client: Invalid script file")
                # If received simple string then print it out to console
                else:
                    print(txt)
            # If got any error (mainly by socket being closed) break the loop
            except: break

        # Disconnect
        s.close()



class testCmds:
    def cmdExec(line):
        print(line)







# Command execution

execClass = eval(config["users"][ClientIP]["execClass"])

line = ' '.join(sys.argv[2:])

if line[0:2]=="?#":
    if classExists(line[2:]):
        config["users"][ClientIP]["execClass"] = line[2:]
        saveConfig(config)
        print("Updated execution class")
    else:
        print("No such class!")
elif line=="?stats":
    print("IP: {}<br>Class: {}".format(ClientIP, execClass))
else:
    execClass.cmdExec(line)
