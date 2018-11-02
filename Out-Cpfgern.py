#ScriptingBy: OutLast/Nocivo

from random import randint
from time import *
from os import *

sleep( 1 )
system("clear")

def gerar():
	n1 = randint(100,999)
	n2 = randint(110,990)
	n3 = randint(120,980)
	n4 = randint(10,99)
	return (f"{n1}.{n2}.{n3}-{n4}")
              
print("\033[1;33m  ____        __  ____")
print(" / ___|_ __  / _|/ ___| ___ _ __ _ __")
print("| |   | '_ \| |_| |  _ / _ \ '__| '_ \ ")
print("| |___| |_) |  _| |_| |  __/ |  | | | | ")
print(" \____| .__/|_|  \____|\___|_|  |_| |_| ")
print("______|_|\033[1;36mByKoded: \033[1;33m[\033[1;35m\033[1;31mOutLast\033[1;33m/\033[1;34mNocivo\033[1;33m/\033[1;32mFox\033[1;33m]\n")
print("\033[1;7;35mByTeam:\033[0m \033[1;32mArea 51")
print("\033[1;7;35mByTeam:\033[0m \033[1;32mMalwareTec")
quant = int(input("\n\033[1;7;36mDESEJA GERAR QUANTOS [CPFs] ?:\033[0m\033[0;31m "))
print("")

for a in range(0,quant):
	print("\033[1;35mCPF \033[1;33mGERADO:\033[0m\033[1;31m --\033[1;36m>> \033[1;7;37m{}\033[0m".format(gerar()))
print("\n\033[1;7;34m[CPFs] GERADOS COM SUCESSO !\033[0m")
menu = str(input("\n\033[1;33mDeseja Voltar pro Menu ?\033[1;32m[\033[1;34m1\033[1;37ms\033[1;32m/\033[1;34m2\033[1;37mn\033[1;32m]\033[1;33m: \033[0;31m"))

if menu == "1":
	print("\033[1;36mVoltando pro Menu")
	sleep( 2 )
	system("ls;python Out-Cpfgern.py")

if menu == "2":
	print("\033[1;36mDeixando Script")
	sleep( 2 )
	system("clear")

else:
	print("\033[1;33mDIGITE A OPCAO CORRETA !\033[0m")
