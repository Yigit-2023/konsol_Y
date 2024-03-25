
#Yazan Yiğit çıtak

import chat
import sistem
import game
import commands as komut
import data
import degiskenler as veri
import GUI as gui
import Yip
from sys import exit

#sistem.konum()
sistem.yip()
sistem.kontrol()
#sistem.logo_bas()
sistem.title()
sistem.komut_kilitle()

while True:

	try:
		sistem.komut_kilitle()
	except FileNotFoundError:
		print(f"{veri.prgm}{veri.hata}Program sistem klasörü dışında çalıştırılamaz :(")
		break

	main_input = input(veri.sen)
	try:
		data.data_yaz(main_input)
	except:
		pass


	if main_input == "çık" or main_input == "kapat" or main_input == "kapan":
		#for i_kapanma in range(10000):
		#	print(f"Kapatılıyor {i_kapanma}")
		break

	elif main_input == "":
		pass

#---------------------------------------------------------------------------------------------[Chat




	elif main_input == "chat bot":
		chat.chat_bot()





	elif main_input == "kaynak kodları" or main_input == "kaynak kodlarını ver" or main_input == "kaynak kodlarını verirmisi":
		print(veri.prgm,veri.Kaynak_kod)
	elif main_input == "kaynak kodu" or main_input == "kaynak kodunu ver" or main_input == "kaynak kodunu verirmisi":
		print(veri.prgm,veri.Kaynak_kod)
	elif main_input == "kaynak kod":
		print(veri.prgm,veri.Kaynak_kod)

	elif main_input == "logo":
		print(veri.logo)





	

#---------------------------------------------------------------------------------------------[Chat



#---------------------------------------------------------------------------------------------[Komut
	elif main_input == "km-rastgele":
		komut.rastgele()

	elif main_input == "km-geçmiş":
		try:
			data.data_oku()
		except:
			print(f"{veri.prgm}{veri.hata}Başka bir konumda bulunduğunuz için geçmişi kaydeten dosyayı açamıyoruz :(")

	elif main_input == "km-yardım" or main_input == "km-help":
		print(veri.help_1)

	elif main_input == "km-konum" or main_input == "km-kon":
		komut.konum()

	elif main_input[0:11] == "km-ışınlan ":
		komut.isinlan(main_input,11)

	elif main_input == "km-listele" or main_input == "km-lis":
		komut.listele()

	elif main_input[0:8] == "km-klos ":
		komut.klasor_olustur(main_input,8)

	elif main_input[0:9] == "km-klos+ ":
		komut.coklu_klasor_olustur(main_input,9)

	elif main_input[0:9] == "km-klsil ":
		komut.klasor_sil(main_input,9)

	elif main_input[0:10] == "km-klsil+ ":
		komut.coklu_klasor_sil(main_input,10)	

	elif main_input[0:7] == "km-gir ":
		komut.ileri(main_input,7)

	elif main_input == "km-neofetch" or main_input == "km-işletim sistemi":
		komut.neofetch()

	elif main_input == "km-ls":
		komut.list_y()

	elif main_input == "km-geri":
		komut.geri()

	elif main_input[0:15] == "km-git kopyala ":
		komut.git(main_input,15)

	elif main_input[0:11] == "km-klsil++ ":
		komut.klasor_sil_pp(main_input,11)

	elif main_input[0:7] == "km-sil ":
		komut.dosya_sil(main_input,7)

	elif main_input == "km-sistem kapat":
		komut.sistem_kapat()

	elif main_input == "km-sistem yeniden baslat":
		komut.sistem_yeniden_baslat()

	elif main_input[0:16] == "km-git kopyala+ ":
		komut.gitp(main_input,16)

	elif main_input[0:7] == "km-kur ":
		komut.apt_install(main_input,7)

	elif main_input[0:10] == "km-kaldır ":
		komut.apt_remove(main_input,10)

	elif main_input == "km-sistem güncelle":
		komut.update()

	elif main_input[0:12] == "km-güncelle ":
		komut.paket_update(main_input,12)

	elif main_input[0:15] == "km-linux komut=":
		komut.linux(main_input,15)

	elif main_input == "km-gui-apt":
		try:
			gui.apt()
		except:
			print(f"{veri.prgm}{veri.hata}GUI devre dışı")

	elif main_input[0:17] == "km-komut kilitle=":
		komut.baslangic_kilidi(main_input[17:])

	elif main_input == "km-yip-kur":
		Yip.git_kur()

	elif main_input == "km-yip temizle":
		Yip.clear()

	elif main_input == "km-yip paketler":
		Yip.paketler()

	elif main_input[0:14:] == "km-yip kaldır ":
		Yip.yip_kaldir(main_input[14:])

	elif main_input[0:11] == "km-yip kur ":
		Yip.yip_kur(komut_main_input[11:])

	elif main_input[0:10] == "km-başlat ":
		Yip.yip_baslat(main_input[10:])

	elif main_input == "km-geçmiş temizle":
		komut.history_clear()



#---------------------------------------------------------------------------------------------[Komut



#---------------------------------------------------------------------------------------------[Sistem

	elif main_input == "sil" or main_input == "clear":
		sistem.clear()

	elif main_input == "komut":
		komut.komut_lock()

	elif main_input == "sürüm":
		print(veri.prgm,veri.sürüm)



	



#---------------------------------------------------------------------------------------------[Sistem



#---------------------------------------------------------------------------------------------[Süpriz

	elif main_input == "zar" or main_input == "Zar":
		try:
			game.zar()
		except:
			print(f"{veri.prgm}{veri.hata}GUI devre dışı")


	elif main_input == "benim için oyun açarmısın" or main_input == "yılan oyunu" or main_input == "oyun1":
		try:
			game.oyun1()
		except:
			#print(f"{veri.prgm}{veri.hata}GUI devre dışı")
			pass

	elif main_input == "bir pencere oluştur" or main_input == "pencere oluştur" or main_input == "benim için bir pencere oluştur":
		try:
			game.pencere()
		except:
			print(f"{veri.prgm}{veri.hata}GUI devre dışı")
	elif main_input == "pencere aç" or main_input == "pencere aç ve şunu yaz":
		try:
			game.pencere()
		except:
			print(f"{veri.prgm}{veri.hata}GUI devre dışı")


#---------------------------------------------------------------------------------------------[Süpriz



	else:
		print(f"{veri.prgm}Dediğinizi anlamadım, daha anlaşılır bir şekilde yazarmısınız O_O ?")
















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