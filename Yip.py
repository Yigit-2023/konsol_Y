#Yazan Yiğit çıtak

import degiskenler as veri
from os import system

def clear():
	while True:
		onay = input(f"{veri.prgm}Bütün Yip paketleri kaldıracak. Emin misin[e,h]")
		if onay == "h" or onay == "H":
			break
		elif onay == "e" or onay == "E":
			system("sudo rm -r /opt/Yip")
			system("sudo mkdir /opt/Yip")
			print(f"{veri.prgm}Bütün Yip paketleri silindi")
			break


def kur():
	system("sudo mkdir opt/Yip/konsol_Y")
	system("sudo git clone  https://github.com/Yigit-2023/konsol_Y /opt/Yip/konsol_Y")

def paketler():
	system("ls /opt/Yip")

#----------[Minecraft
def minecraft():
	system("sudo mkdir opt/Yip/minecraft")
	system("sudo git clone https://github.com/Yip-2023/Legacy_Launcher.git /opt/Yip/minecraft")
	system("sudo apt update")
	system("sudo apt install default-jre")
	system("sudo apt update")
	system("sudo apt install default-jdk")

def minecraft_start():
	system("java -jar /opt/Yip/minecraft/LegacyLauncher_legacy.jar")

def minecraft_kaldir():
	system("sudo rm -r /opt/Yip/minecraft")
	print(f"{veri.prgm}Kaldırıldı")
#----------[Minecraft

#----------[Not Defteri
def not_defteri():
	system("sudo mkdir opt/Yip/not_defteri")
	system("sudo git clone https://github.com/emrecanstk/not-defteri.git /opt/Yip/not_defteri")

def not_defteri_start():
	system("python3 /opt/Yip/not_defteri/main.py")

def not_defteri_kaldir():
	system("sudo rm -r /opt/Yip/not_defteri")
	print(f"{veri.prgm}Kaldırıldı")
#----------[Not Defteri

#----------[Simple Text Editor
def Simple_Text_Editor():
	system("sudo mkdir opt/Yip/Simple_Text_Editor")
	system("sudo git clone https://github.com/Yip-2023/Simple_Text_Editor.git /opt/Yip/Simple_Text_Editor")

def Simple_Text_Editor_start():
	system("python3 /opt/Yip/Simple_Text_Editor/Simple_Text_Editor.py")

def Simple_Text_Editor_kaldir():
	system("sudo rm -r /opt/Yip/Simple_Text_Editor/")
	print(f"{veri.prgm}Kaldırıldı")
#----------[Simple Text Editor

def yip_kaldir(paket_adi):
	if paket_adi == "minecraft":
		minecraft_kaldir()
	elif paket_adi == "not-defteri":
		not_defteri_kaldir()
	elif paket_adi == "simple-text-editor":
		Simple_Text_Editor_kaldir()

	else:
		print(f"{veri.prgm}{paket_adi} İsimli paket bulunamadı")

def yip_kur(paket_adi):
	if paket_adi == "minecraft":
		minecraft()
	elif paket_adi == "not-defteri":
		not_defteri()
	elif paket_adi == "simple-text-editor":
		Simple_Text_Editor()

	else:
		print(f"{veri.prgm}{paket_adi} İsimli paket bulunamadı")

def yip_baslat(paket_adi):
	if paket_adi == "minecraft":
		minecraft_start()
	elif paket_adi == "not-defteri":
		not_defteri_start()
	elif paket_adi == "simple-text-editor":
		Simple_Text_Editor_start()

	else:
		print(f"{veri.prgm}{paket_adi} İsimli paket bulunamadı")



def git_kur():
	system("sudo apt install git")







	       	   #/\
              #/  \
             #/    \
            #/      \
           #/        \
          #/          \
         #/ \         /\
        #/   \       /  \
       #/     \     /    \
      #/       \   /      \
     #/         \ /        \
    #/           |          \
   #/            |           \
  #/             |            \
 #/              |             \
#/______________________________\