
#Yazan Yiğit çıtak

import chat
import sistem
import game
import commands as komut
import data
import degiskenler as veri
import GUI as gui
import Yip

sistem.yip()
sistem.kontrol()
#sistem.logo_bas()
sistem.title()


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

	elif main_input == "merhaba":
		print(f"{veri.prgm}Merhaba :)")

	elif main_input == "nasılsın" or main_input == "nasılsınız" or main_input == "nasıl gidiyor" or main_input == "naptı" or main_input == "naber":
		chat.nasilsin()

	elif main_input == "senin adın ne" or main_input == "adın ne":
		chat.adin_ne()

	elif main_input == "seni kim yaptı" or main_input == "seni kodlayan kim" or main_input == "seni tasarlayan kim" or main_input == "kim yaptı seni":
		chat.kim_yapti()
	elif main_input == "seni yapan kim" or main_input == "kim kodladı seni" or main_input == "seni kim tasarladı" or main_input == "seni yapan kim":
		chat.kim_yapti()

	elif main_input == "selam" or main_input == "selamın aleyküm" or main_input == "selamlar":
		chat.selam()

	elif main_input == "nesin sen" or main_input == "sen nesin " or main_input == "sen kimsin":
		chat.nesin()
	elif main_input == "sen de nesin" or main_input == "sen nesin":
		chat.nesin()

	elif main_input[0:10] == "benim adım":
		chat.tanimla(main_input)

	elif main_input == "sen kaç yaşındasın":
		print(f"{veri.prgm}Ben 8 ocak 2024 yılında geliştirimeye başlandım :)")

	elif main_input == "ben yiğit çıtak":
		print(f"{veri.prgm}Nasıl yardımcı olabilirim, sahip :))")

	elif main_input == "özelliklerin neler" or main_input == "neler yapabilirsin" or main_input == "başka neler yapabilirsin":
		chat.ozellikler()

	elif main_input == "adamsın":
		print(f"{veri.prgm}Ben programım :D")

	elif main_input == "seni çok seviyorum" or main_input == "seni seviyorum" or main_input == "seviyorum seni":
		chat.sevmek()
	elif main_input == "çok şirinsin" or main_input == "sen ne şirin birşeysin" or main_input == "sen çok tatlısın" or main_input == "sen çok şirin birşeysin":
		chat.sevmek()
	elif main_input == "sen çok sevimlisin" or main_input == "sevimlisin" or main_input == "tatlısın" or main_input == "sen çok şirinsin":
		chat.sevmek()

	elif main_input == "teşekkür ederim" or main_input == "teşekkürler" or main_input == "teşekürler" or main_input == "teşekür ederim" or main_input == "sağol":
		chat.tesekur()
	elif main_input == "teşekürler program" or main_input == "teşekür ederim program" or main_input == "sağol program":
		chat.tesekur()

	elif main_input == "mal" or main_input == "sen malsın" or main_input == "malsın":
		chat.sinir()
	
	elif main_input == "otistik" or main_input == "geri zekalı" or main_input == "salak" or main_input == "oruspu" or main_input == "aptal":
		chat.sinir()
		
	elif main_input == "sen bir malsın" or main_input == "sen aptalsın" or main_input == "sen geri zekalısın":
		chat.sinir()
		
	elif main_input == "sen çok akıllısın" or main_input == "sen çok iyisin" or main_input == "sen çok güzelsin":
		print(f"{veri.prgm}     :D")

	elif main_input == "özür dilerim" or main_input == "üzgünüm" or main_input == "kusura bakma" or main_input == "afedersin":
		chat.affet()
	elif main_input == "paron":
		chat.affet()

	elif main_input == "neler biliyorsun" or main_input == "ne biliyorsun" or main_input == "bildiğin birşey var mı":
		chat.bilmek()
	elif main_input == "bilmek" or main_input == "senin bir bilgin var mı" or main_input == "biliyormusun" or main_input == "biliyor musun":
		chat.bilmek()

	elif main_input == "nerdesin" or main_input == "sen nerdesin" or main_input == "nerede sin" or main_input == "şu an nerdesin" or main_input == "neredesin":
		chat.konum()

	elif main_input == "sen yemek yer misin" or main_input == "sen yemek yermisin":
		print(f"{veri.prgm}Ben yemek yemem :/")

	elif main_input == "sen yaşıyor musun" or main_input == "sen yaşıyormusun" or main_input == "sen canlı mısın" or  main_input == "sen canlımısın":
		chat.canli_degil()

	elif main_input == "senin duyguların var mı" or main_input == "senin duygun var mı" or main_input == "duyguların var mı" or main_input == "sende duygu var mı":
		chat.duygu()
	elif main_input == "duyguların var mı senin" or main_input == "duyguların varmı senin":
		chat.duygu()
	elif main_input == "duyguların var mıdır senin" or main_input == "duygun var mı" or main_input == "duygun varmı":
		chat.duygu()

	elif main_input == "senin görevin var mı" or main_input == "senin görevin ne " or main_input == "görevin ne" or main_input == "görevin ne senin":
		chat.gorev()
	elif main_input == "senin görevin var mıdır" or main_input == "senin başka görevin var mı" or main_input == "senin görevin nedir":
		chat.gorev()

	elif main_input == "sen robot musun" or main_input == "sen yapay zeka mısın" or main_input == "sen nasıl bir şeysin" or main_input == "sen nasıl bir program sın":
		chat.nesin()
	elif main_input == "sen nasıl bir programsın" or main_input == "sen nasıl birşey sin" or main_input == "nasıl birşeysin sen":
		chat.nesin()

	elif main_input == "yiğit kim" or main_input == "yiğit çıtak kim":
		komut.yigit()
	elif main_input == "yiğit kimdir" or main_input == "yiğit çıtak kimdir":
		komut.yigit()

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
		komut.yardim()

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

	elif main_input[0:13] == "km-güncelle: ":
		komut.paket_update(main_input,13)

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



#---------------------------------------------------------------------------------------------[Komut



#---------------------------------------------------------------------------------------------[Sistem

	elif main_input == "sil" or main_input == "clear":
		sistem.clear()

	elif main_input == "komut":
		komut.komut_lock()

	elif main_input == "sürüm":
		print(veri.prgm,veri.sürüm)

	elif main_input == "data_çek":
		sistem.data_cek()



	



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