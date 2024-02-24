#Yazan Yiğit çıtak

import tkinter as tk 
import degiskenler as veri
from os import system



def apt():
	def imza():
		imza_pencere = tk.Tk()
		imza_pencere.minsize(300,400)
		imza_pencere.maxsize(200,400)
		imza_pencere.title("konsol Y")

		imza = tk.Label(imza_pencere,text="Hazırlyan: YİĞİT ÇITAK\n\nProgramda bir hata\nbulursanız lütfen bana bildirin\n\nyigitcitak.1817gmail.com\n\n\n\n")
		imza.pack()
		bosuk = tk.Label(apt_gui_pencere,text="")
		bosuk.pack()
		bosuk2 = tk.Label(apt_gui_pencere,text="")
		bosuk2.pack()
		bosuk3 = tk.Label(apt_gui_pencere,text="")
		bosuk3.pack()
		bosuk4 = tk.Label(apt_gui_pencere,text="")
		bosuk4.pack()
		bosuk5 = tk.Label(apt_gui_pencere,text="")
		bosuk5.pack()
		bosuk6 = tk.Label(apt_gui_pencere,text="")
		bosuk6.pack()
		emoji = tk.Label(imza_pencere,text=":D",font="italic 67")
		emoji.pack()

	def kur():
		system(f"sudo apt install {install_input.get()}")
	def sistemi_guncelle():
		system("sudo apt update")
	def guncelle():
		system(f"sudo apt upgrade {updata_input.get()}")
	def kaldir():
		system(f"sudo apt purge {remove_input.get()}")
	apt_gui_pencere = tk.Tk()
	apt_gui_pencere.title("konsol Y - GUI APT")
	apt_gui_pencere.minsize(600,800)
	apt_gui_pencere.maxsize(600,800)

	imza_buton = tk.Button(apt_gui_pencere,text="- - -",command=imza,bg="grey")
	imza_buton.place(x=1,y=1)

	title_label = tk.Label(apt_gui_pencere,text="APT paket yöneticisi",font="italic 40")
	title_label.pack()

	bosuk01 = tk.Label(apt_gui_pencere,text="")
	bosuk01.pack()

	bosuk02 = tk.Label(apt_gui_pencere,text="")
	bosuk02.pack()

	install_input = tk.Entry(apt_gui_pencere)
	install_input.pack()

	install_buton = tk.Button(apt_gui_pencere,text="KUR",font="italic 30",command=kur)
	install_buton.pack()



	bosuk = tk.Label(apt_gui_pencere,text="")
	bosuk.pack()

	bosuk2 = tk.Label(apt_gui_pencere,text="")
	bosuk2.pack()

	bosuk3 = tk.Label(apt_gui_pencere,text="")
	bosuk3.pack()



	updata_input = tk.Entry(apt_gui_pencere)
	updata_input.pack()

	updata_buton = tk.Button(apt_gui_pencere,text="Güncelle",font="italic 25",command=guncelle)
	updata_buton.pack()

	bosuk00 = tk.Label(apt_gui_pencere,text="")
	bosuk00.pack()

	bosuk200 = tk.Label(apt_gui_pencere,text="")
	bosuk200.pack()

	bosuk300 = tk.Label(apt_gui_pencere,text="")
	bosuk300.pack()



	remove_input = tk.Entry(apt_gui_pencere)
	remove_input.pack()

	remove_buton = tk.Button(apt_gui_pencere,text="Kaldır",font="italic 25",command=kaldir)
	remove_buton.pack()


	bosuk4 = tk.Label(apt_gui_pencere,text="")
	bosuk4.pack()

	bosuk5 = tk.Label(apt_gui_pencere,text="")
	bosuk5.pack()

	bosuk6 = tk.Label(apt_gui_pencere,text="")
	bosuk6.pack()

	bosuk7 = tk.Label(apt_gui_pencere,text="")
	bosuk7.pack()

	bosuk8 = tk.Label(apt_gui_pencere,text="")
	bosuk8.pack()

	sistem_guncelle = tk.Button(apt_gui_pencere,text="Sistem güncelle",font="italic 45",command=sistemi_guncelle)
	sistem_guncelle.pack()


	apt_gui_pencere.mainloop()
