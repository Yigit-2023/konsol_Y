#Yazan Yiğit çıtak

import sistem
import random
import data
import degiskenler as veri
import os
from sys import exit
import GUI as gui


def yigit():#Buranın ilk fonksiyonu
    print("Program: >Beni geliştiren yazılımcı :D")

def yardim():
    print(f"{veri.prgm}Komutlar:\n{veri.komutlar}")

def komut_lock():
    while True:
        komut_main_input = input(f"{veri.sen}{veri.komut}")
        try:
            data.data_yaz(komut_main_input)
        except:
            pass

        if komut_main_input == "geri git" or komut_main_input == "çık":
            break
        elif komut_main_input == "kapat" or komut_main_input == "kapan":
            exit()

        elif komut_main_input == "":
            pass


        elif komut_main_input == "geçmiş":
            #gecmis_data = open("DATA/DataText.yc","r")
            #data_oku = gecmis_data.read()
            #print(f"{veri.prgm}Geçmişiniz:\n\n",data_oku)
            #gecmis_data.close()
            try:
                data.data_oku()
            except:
                print(f"{veri.prgm}{veri.hata}Başka bir konumda bulunduğunuz için geçmişi kaydeten dosyayı açamıyoruz :(")

        elif komut_main_input == "yardım":
            print(f"{veri.prgm}Komutlar:\n{veri.komutlar_lock}")

        elif komut_main_input == "sil" or komut_main_input == "clear":
            sistem.clear()

        elif komut_main_input == "rastgele":
            rastgele()

        elif komut_main_input == "konum" or komut_main_input == "kon":
            konum()

        elif komut_main_input[0:8] == "ışınlan ":
            isinlan(komut_main_input,8)

        elif komut_main_input == "listele" or komut_main_input == "lis":
            listele()

        elif komut_main_input[0:5] == "klos ":
            klasor_olustur(komut_main_input,5)

        elif komut_main_input[0:6] == "klos+ ":
            coklu_klasor_olustur(komut_main_input,6)

        elif komut_main_input[0:6] == "klsil ":
            klasor_sil(komut_main_input,6)

        elif komut_main_input[0:7] == "klsil+ ":
            coklu_klasor_sil(komut_main_input,7)

        elif komut_main_input[0:4] == "gir ":
            ileri(komut_main_input,4)

        elif komut_main_input == "neofetch" or komut_main_input == "işletim sistemi":
            neofetch()

        elif komut_main_input == "ls":
            list_y()

        elif komut_main_input[0:4] == "sil ":
            dosya_sil(komut_main_input,4)

        elif komut_main_input == "geri":
            geri()

        elif komut_main_input[0:12] == "git kopyala ":
            git(komut_main_input,12)

        elif komut_main_input[0:8] == "klsil++ ":
            klasor_sil_pp(komut_main_input,8)


        elif komut_main_input == "sistem kapat":
            sistem_kapat()

        elif komut_main_input == "sistem yeniden başlat":
            sistem_yeniden_baslat()

        elif komut_main_input[0:13] == "git kopyala+ ":
            gitp(komut_main_input,13)

        elif komut_main_input[0:4] == "kur ":
            apt_install(komut_main_input,4)

        elif komut_main_input[0:7] == "kaldır ":
            apt_remove(komut_main_input,7)

        elif komut_main_input == "sistem güncelle":
            update()

        elif komut_main_input[0:10] == "güncelle: ":
            paket_update(komut_main_input,10)

        elif komut_main_input == "temizle":
            sistem.clear()

        elif komut_main_input[0:12] == "linux komut=":
            linux(komut_main_input,12)

        elif komut_main_input == "gui-apt":
            try:
                gui.apt()
            except:
                print(f"{veri.prgm}{veri.hata}GUI devre dışı")


        else:
            print(f"{veri.prgm}Geçersiz komut")



def rastgele():
    random_input_sayi1 = input(f"{veri.prgm}Şu sayıdan: ")
    random_input_sayi2 = input(f"{veri.prgm}Şu sayıya kadar: ")
    try:
        def random_sonuc():
            return random.randint(int(random_input_sayi1),int(random_input_sayi2))

        for _ in range(1):
            print(f"{veri.prgm}",random_sonuc())
    except:
        print(f"{veri.prgm}{veri.hata}Hattalı girdi!")




def konum():
    print(veri.prgm,os.getcwd())


def isinlan(konum,bsl):
    try:
        os.chdir(konum[bsl:])
        print(f"{veri.prgm}Konum değiştirirdi")
    except:
        print(f"{veri.prgm}Girdiğiniz konum bulunamadı")

def listele():
    print(veri.prgm," ",os.listdir())

def klasor_olustur(klasor_isim,bsl):
    os.mkdir(klasor_isim[bsl:])
    print(f"{veri.prgm}{klasor_isim[bsl:]} isimli klasör oluştururdu :D")

def coklu_klasor_olustur(klasor_isim,bsl):
    os.makedirs(klasor_isim[bsl:])
    print(f"{veri.prgm}{klasor_isim[bsl:]} dizisi oluştururdu :D")

def klasor_sil(klasor_isim,bsl):
    try:
        os.rmdir(klasor_isim[bsl:])
        print(f"{veri.prgm}{klasor_isim[bsl:]} isimli klasör silindi")
    except:
        print(f"{veri.prgm}Böyle bir klasör bulunamadı :/ veya bu bir dizi olabilir")

def coklu_klasor_sil(klasor_isim,bsl):
    try:
        os.removedirs(klasor_isim[bsl:])
        print(f"{veri.prgm}{klasor_isim[bsl:]} dizisi silindi")
    except:
        print(f"{veri.prgm}Böyle bir dizi bulunamadı :/")

def ileri(sonraki_klasor,bsl):
    try:
        simdiki_konum = os.getcwd()
        ileri_konum = simdiki_konum + "/" + sonraki_klasor[bsl:]
        os.chdir(ileri_konum)
        print(f"{veri.prgm}{sonraki_klasor[bsl:]} Klasörünün içindesin")
    except:
        print(f"{veri.prgm}Böyle bir klasör bulunamadı")

def neofetch():
    os.system("neofetch")

def list_y():
    os.system("ls")

def dosya_sil(dosya_isim,bsl):
    try:
        os.remove(dosya_isim[bsl:])
        print(f"{veri.prgm}{dosya_isim[bsl:]} isimli dosya silindi")
    except:
        print(f"{veri.prgm}{dosya_isim[bsl:]} isimli dosya bulunamadı")

def geri():
    current_directory = os.getcwd()
    parent_directory = os.path.dirname(current_directory)
    os.chdir(parent_directory)
    print(f"{veri.prgm}Geri gittiniz :D")

def git(paket_adi,bsl):
    os.system(f"git clone {paket_adi[bsl:]}")
    print("\ngit deposu içe aktarıldı :D")

def klasor_sil_pp(klasor_isim,bsl):
    os.system(f"cd {klasor_isim[bsl]}")
    os.system(f"rm -rf {klasor_isim[bsl:]}")


def sistem_kapat():
    os.system("sudo shutdown now")

def sistem_yeniden_baslat():
    os.system("sudo reboot")

def gitp(paket_adi,bsl):
    os.system(f"git clone https://github.com/{paket_adi[bsl:]}")

def apt_install(apt_paket_adı,bsl):
    os.system(f"sudo apt install {apt_paket_adı[bsl:]}")

def apt_remove(apt_paket_adı,bsl):
    os.system(f"sudo apt purge {apt_paket_adı[bsl:]}")

def update():
    os.system("sudo apt update")

def paket_update(paket_adi,bsl):
    os.system(f"sudo apt upgrade {paket_adi[bsl:]}")

def linux(komut,bsl):
    os.system(komut[bsl:])

















































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