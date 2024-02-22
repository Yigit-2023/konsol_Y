#Yazan Yiğit çıtak

import degiskenler as veri


def data_yaz(x):
	

	sifreleniyor1 = x.replace("q","y0032h210")

	sifreleniyor2 = sifreleniyor1.replace("w","y0031h210")

	sifreleniyor3 = sifreleniyor2.replace("e","y0030h210")

	sifreleniyor4 = sifreleniyor3.replace("r","y0029h210")

	sifreleniyor5 = sifreleniyor4.replace("t","y0028h210")

	sifreleniyor6 = sifreleniyor5.replace("y","y0027h210")

	sifreleniyor7 = sifreleniyor6.replace("u","y0026h210")

	sifreleniyor8 = sifreleniyor7.replace("ı","y0025h210")

	sifreleniyor9 = sifreleniyor8.replace("o","y0024h210")

	sifreleniyor10 = sifreleniyor9.replace("p","y0023h210")

	sifreleniyor11 = sifreleniyor10.replace("ğ","y0022h210")

	sifreleniyor12 = sifreleniyor11.replace("ü","y0021h210")

	sifreleniyor13 = sifreleniyor12.replace("a","y0020h210")

	sifreleniyor14 = sifreleniyor13.replace("s","y0019h210")

	sifreleniyor15 = sifreleniyor14.replace("d","y0018h210")

	sifreleniyor16 = sifreleniyor15.replace("f","y0017h210")

	sifreleniyor17 = sifreleniyor16.replace("g","y0016h210")

	sifreleniyor18 = sifreleniyor17.replace("h","y0015h210")

	sifreleniyor19 = sifreleniyor18.replace("j","y0014h210")

	sifreleniyor20 = sifreleniyor19.replace("k","y0013h210")

	sifreleniyor21 = sifreleniyor20.replace("l","y0012h210")

	sifreleniyor22 = sifreleniyor21.replace("ş","y0011h210")

	sifreleniyor23 = sifreleniyor22.replace("i","y0010h210")

	sifreleniyor24 = sifreleniyor23.replace("z","y0009h210")

	sifreleniyor25 = sifreleniyor24.replace("x","y0008h210")

	sifreleniyor26 = sifreleniyor25.replace("c","y0007h210")

	sifreleniyor27 = sifreleniyor26.replace("v","y0006h210")

	sifreleniyor28 = sifreleniyor27.replace("b","y0005h210")

	sifreleniyor29 = sifreleniyor28.replace("n","y0004h210")

	sifreleniyor30 = sifreleniyor29.replace("m","y0003h210")

	sifreleniyor31 = sifreleniyor30.replace("ö","y0002h210")

	y = sifreleniyor31.replace("ç","y0001h210")



	data_save = open("DATA/DataText.yc","a")
	data_save.write(f"\n{y}\n")
	data_save.close()


def data_oku():
	gecmis_data = open("DATA/DataText.yc","r")
	data_oku = gecmis_data.read()

	cozuluyor1 = data_oku.replace("y0027y0015h2102100032y0015h210210","q")

	cozuluyor2 = cozuluyor1.replace("y0027y0015h2102100031y0015h210210","w")

	cozuluyor3 = cozuluyor2.replace("y0027y0015h2102100030y0015h210210","e")

	cozuluyor4 = cozuluyor3.replace("y0027y0015h2102100029y0015h210210","r")

	cozuluyor5 = cozuluyor4.replace("y0027y0015h2102100028y0015h210210","t")

	cozuluyor6 = cozuluyor5.replace("y0027y0015h210210","y")

	cozuluyor7 = cozuluyor6.replace("y0026y0015h210210","u")

	cozuluyor8 = cozuluyor7.replace("y0025y0015h210210","ı")

	cozuluyor9 = cozuluyor8.replace("y0024y0015h210210","o")

	cozuluyor10 = cozuluyor9.replace("y0023y0015h210210","p")

	cozuluyor11 = cozuluyor10.replace("y0022y0015h210210","ğ")

	cozuluyor12 = cozuluyor11.replace("y0021y0015h210210","ü")

	cozuluyor13 = cozuluyor12.replace("y0020y0015h210210","a")

	cozuluyor14 = cozuluyor13.replace("y0019y0015h210210","s")

	cozuluyor15 = cozuluyor14.replace("y0018y0015h210210","d")

	cozuluyor16 = cozuluyor15.replace("y0017y0015h210210","f")

	cozuluyor17 = cozuluyor16.replace("y0016y0015h210210","g")

	cozuluyor18 = cozuluyor17.replace("y0015h210","h")

	cozuluyor19 = cozuluyor18.replace("y0014h210","j")

	cozuluyor20 = cozuluyor19.replace("y0013h210","k")

	cozuluyor21 = cozuluyor20.replace("y0012h210","l")

	cozuluyor22 = cozuluyor21.replace("y0011h210","ş")

	cozuluyor23 = cozuluyor22.replace("y0010h210","i")

	cozuluyor24 = cozuluyor23.replace("y0009h210","z")

	cozuluyor25 = cozuluyor24.replace("y0008h210","x")

	cozuluyor26 = cozuluyor25.replace("y0007h210","c")

	cozuluyor27 = cozuluyor26.replace("y0006h210","v")

	cozuluyor28 = cozuluyor27.replace("y0005h210","b")

	cozuluyor29 = cozuluyor28.replace("y0004h210","n")

	cozuluyor30 = cozuluyor29.replace("y0003h210","m")

	cozuluyor31 = cozuluyor30.replace("y0002h210","ö")

	cozuldu = cozuluyor31.replace("y0001h210","ç")



	print(f"{veri.prgm}Geçmişiniz:\n\n",cozuldu)
	gecmis_data.close()