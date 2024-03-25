#Yazan Yiğit çıtak

import data
import degiskenler as veri
from os import name
from sys import exit
from os import system
from os import chdir
import commands as komut

def logo_bas():
	print(veri.logo)


def yip():
	system("sudo mkdir /opt/Yip")
	print("----------------")

def kontrol():
	if name == "posix":
		pass
	elif name == "nt":
		print(f"{veri.prgm}Üzgünüm, bu program sadece linux işletim sisteminde çalışabilir. Windows'ta değil :(")
		exit()
	else:
		print(f"{veri.prgm}Üzgünüm, bu program sadece linux işletim sisteminde çalışabilir :(")
		exit()

def title(): 
	dsyo = open("DATA/komutKilid.yc","r")
	dsyo_aktif = dsyo.read()
	if dsyo_aktif == "aktif":
		print(f"""\n 		
		Hoş gedldiniz. konsol Y sÜrüm {veri.sürüm}
		Büyük harf girdisi geçersizdir :D
		komut listesi için "yardım" komutunu kullanın
		""")
	
	else: 
		print(f"""\n 
		Hoş gedldiniz. konsol Y sÜrüm {veri.sürüm}
		Büyük harf girdisi geçersizdir :D
		komut listesi için "km-yardım" komutunu kullanın
		""")
	dsyo.close()

def komut_kilitle():
    dosya_acildi = open("DATA/komutKilid.yc", "r")
    dosya_aktif = dosya_acildi.read()
    if dosya_aktif == "aktif":
        komut.komut_lock()
    else:
        pass
        #print(dosya_aktif)
    dosya_acildi.close()




def clear():
	for siliniyor in range(10000):
		print("")






def konum():
	system("cd /usr/local/bin")
	chdir("/usr/local/bin")


















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