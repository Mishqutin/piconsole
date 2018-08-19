class mainClass:
    def cmdExec(line):

        if len(line.split())<1: line="xd"

        cmd = line.split()[0]
        args = line.split()[1:]

        if cmd in mainClass.cmds:
            mainClass.cmds[cmd](args)
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
        print(mainClass.helpText.replace("\n", "<br>"))
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
