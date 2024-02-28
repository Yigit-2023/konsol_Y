#Yazan Dinçer Tekin
#Düzenleyen Yiğit çıtak

from difflib import get_close_matches as yakin_sonuclari_getir
from sys import exit
import chat
import data
import json
import degiskenler as veri

def veritabanini_yukle():
	with open('DATA/veritabani.json', 'r') as dosya:
		return json.load(dosya)

def veritabanina_yaz(veriler):
	with open('DATA/veritabani.json', 'w') as dosya:
		json.dump(veriler, dosya, indent=2)

def yakin_sonuc_bul(soru, sorular):
	eslesen = yakin_sonuclari_getir(soru, sorular, n=1, cutoff=0.6)
	return eslesen[0] if eslesen else None

def cevabini_bul(soru, veritabani):
	for soru_cevaplar in veritabani["sorular"]:
		if soru_cevaplar["soru"] == soru:
			return soru_cevaplar["cevap"]
	return None

def chat_bot():
	while True:
		veritabani = veritabanini_yukle()

		soru = input(f"{veri.sen}{veri.chb}")
		try:
			data.data_yaz(soru)
		except:
			pass

		if soru == "çık":
			break

		elif soru == "kapan" or soru == "kapat:":
			exit()
        
		gelen_sonuc = yakin_sonuc_bul(soru, [soru_cevaplar["soru"] for soru_cevaplar in veritabani["sorular"]])
		if gelen_sonuc:
			verilecek_cevap = cevabini_bul(gelen_sonuc, veritabani)
			print(f"{veri.prgm}{verilecek_cevap}")



		else:
			print(f"{veri.prgm}Bunu nasıl cevaplayacağımı bilmiyorum. Öğretir misiniz?")
			yeni_cevap = input(f"Öğretmek için yazabilir veya 'geç' diyebilirsiniz.\n{veri.sen}")

			if yeni_cevap != 'geç':
				veritabani["sorular"].append({
					"soru": soru,
					"cevap": yeni_cevap
				})
				veritabanina_yaz(veritabani)
				print(f"{veri.prgm}Teşekkürler, sayenizde yeni bir şey öğrendim.")








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