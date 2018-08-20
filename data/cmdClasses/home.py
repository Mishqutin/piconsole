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
Komendy ogolne:
?#<klasa> - Wybierasz program, ktory uzywasz
?class - Listuje dostepne programy
?stats - Info

Programy:
?#home - Ten program
?#csc  - Zarzadzanie plikami itp.

Komendy w programie home:
help - Ta pomoc
motd - Najwazniejsza komenda, musisz ja uzyc conajmniej raz dziennie, bo inaczej umrzesz!
username <imie> - Zmienia twoja nazwe
lol - Lol xd
"""



    cmds = {}

    def cmdHelp(args):
        print(txtToHtml(mainClass.helpText))
    cmds["help"] = cmdHelp

    def cmdEcho(args):
        if len(args)<1:
            print("Uzycie: echo tekst")
        else:
            print(' '.join(args))
    cmds["echo"] = cmdEcho

    def cmdLol(args):
        lolId = "0"
        cfgVarSet("lolId", 0)
        print('<div id="lol{}"><h1>Haha lol xd</h1></div>'.format(lolId))
        js = """\
<script language="javascript" type="text/javascript">
var col=0;
function changeLolColor()
{
    if(col==0)
    {
        document.getElementById("lol").style.color="#ff0000";
        col=1;
    }
    else
    {
        document.getElementById("lol").style.color="#00ff00";
        col=0;
    }
}
setInterval(changeLolColor,500);
</script>
"""
        print(js)
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
