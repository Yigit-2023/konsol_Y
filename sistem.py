#Yazan Yiğit çıtak

import data
import degiskenler as veri
from os import name
from sys import exit
from os import system
import commands as komut
#import os

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
	print(f"""\n 		
	Hoş gedldiniz. konsol Y sÜrüm {veri.sürüm}
	Büyük harf girdisi geçersizdir :D
	""")

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

def data_cek():
	data_cek_input = input(f"{veri.prgm}Önce yiğit olduğunu kanıtla\n{veri.sif}")
	data.data_yaz(data_cek_input)


	if data_cek_input == "8888":
		gecmis_data = open("DATA/DataText.yc","r")
		data_oku = gecmis_data.read()
		print(f"\n{data_oku}")
		gecmis_data.close()
		print(f"\n{veri.prgm}Merhaba yiğt :) işte talep ettiğin datalar")

	else:
		print(f"{veri.prgm}Sen yiğit değilsin")


























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