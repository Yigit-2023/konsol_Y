#Yazan Yiğit çıtak

import data
import degiskenler as veri




def title(): 
	print(f"""\n Hoş gedldiniz. program Y beta {veri.sürüm} Tüm haklar saklıdır.
	Bu programda büyük harf yasaktır :D
	""")

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




















