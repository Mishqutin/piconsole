import sys

ClientIP = sys.argv[1]


CWD = "/var/www/html/piconsole"

f = open(CWD + "/README.md")
x = f.read()
f.close()

print(x.replace("\n", "<br>"))

someText = """\
Jak nie wiesz co robic to wpisz 'help'
Polecam rowniez 'motd'
<br>
"""

print(someText.replace("\n", "<br>"))
