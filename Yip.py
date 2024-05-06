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
	while True:
		minecraft_x = input(f"{veri.prgm}Kurulacak Paketler: Minecraft,Java| Kurulum başlasın mı? [e,h]")
		if minecraft_x == "e" or minecraft_x == "E":
			system("sudo mkdir opt/Yip/minecraft")
			system("sudo git clone https://github.com/Yip-2023/Legacy_Launcher.git /opt/Yip/minecraft")
			system("sudo apt update")
			system("sudo apt install default-jre")
			system("sudo apt update")
			system("sudo apt install default-jdk")
			print(veri.yip_install)
			break
		elif minecraft_x == "h" or minecraft_x == "H":
			print(f"{veri.prgm}Kurulum iptal edildi")
			break
		else:
			pass

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
	print(veri.yip_install)

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
	print(veri.yip_install)

def Simple_Text_Editor_start():
	system("python3 /opt/Yip/Simple_Text_Editor/Simple_Text_Editor.py")

def Simple_Text_Editor_kaldir():
	system("sudo rm -r /opt/Yip/Simple_Text_Editor/")
	print(f"{veri.prgm}Kaldırıldı")
#----------[Simple Text Editor


#----------[Yıldız Engelleri
def Yildiz_Engelleri():
	system("sudo mkdir opt/Yip/yildiz-engelleri")
	system("sudo git clone https://github.com/Yip-2023/oyun1.git /opt/Yip/yıldız-engelleri")
	system("sudo unzip /opt/Yip/yıldız-engelleri/oyun1.zip -d /opt/Yip/yıldız-engelleri/oyun1/")
	print(veri.yip_install)

def Yildiz_Engelleri_start():
	system("/opt/Yip/yıldız-engelleri/oyun1/Yıldız-Engelleri/oyun1")

def Yildiz_Engelleri_kaldir():
	system("sudo rm -r /opt/Yip/yıldız-engelleri")
	print(f"{veri.prgm}Kaldırıldı")

#----------[Yıldız Engelleri

#----------[Sublime text editor
#							Geliştirilme aşamasında
def sublime_text_editor():
	system("sudo mkdir /opt/Yip/sublime-text-editor")
	system("sudo git clone https://github.com/Yip-2023/sublime_text.git /opt/Yip/sublime-text-editor/")
	system("sudo dpkg -r /opt/Yip/sublime-text-editorsublime-text_build-3211_amd64.deb")

def sublime_text_editor_start():
	system("sudo sublime")#Bu paket hatalı


#----------[Sublime text editor

def yip_kaldir(paket_adi):
	if paket_adi == "minecraft":
		minecraft_kaldir()
	elif paket_adi == "not-defteri":
		not_defteri_kaldir()
	elif paket_adi == "simple-text-editor":
		Simple_Text_Editor_kaldir()
	elif paket_adi == "yıldız-engelleri":
		Yildiz_Engelleri_kaldir()

	else:
		print(f"{veri.prgm}{paket_adi} İsimli paket bulunamadı")

def yip_kur(paket_adi):
	if paket_adi == "minecraft":
		minecraft()
	elif paket_adi == "not-defteri":
		not_defteri()
	elif paket_adi == "simple-text-editor":
		Simple_Text_Editor()
	elif paket_adi == "yıldız-engelleri":
		Yildiz_Engelleri()
	elif paket_adi == "sublime-text-editor":
		sublime_text_editor()

	else:
		print(f"{veri.prgm}{paket_adi} İsimli paket bulunamadı")

def yip_baslat(paket_adi):
	if paket_adi == "minecraft":
		minecraft_start()
	elif paket_adi == "not-defteri":
		not_defteri_start()
	elif paket_adi == "simple-text-editor":
		Simple_Text_Editor_start()
	elif paket_adi == "yıldız-engelleri":
		Yildiz_Engelleri_start()

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
