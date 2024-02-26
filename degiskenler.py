#Yazan Yiğit çıtak




prgm = "Program: >"
sen = "Sen: >"
ben = "Yiğit: >"
sif = "Şifre: >"
yaz = "Yazılacak: >"
hata = "Error: >"
komut = "km>"

sürüm = "1.0"



Kaynak_kod = "https://github.com/Yigit-2023/konsol_Y"


logo = """
               /\\
              /  \\
             /    \\
            /      \\
           /        \\
          /          \\
         / \\         /\\
        /   \\       /  \\
       /     \\     /    \\
      /       \\   /      \\
     /         \\ /        \\
    /           |          \\
   /            |           \\
  /             |            \\
 /              |             \\
/______________________________\\
"""


komutlar_lock = """
geçmiş --> Yazma geçmişinizi gösterir
rastgele --> Rastgele sayı oluşturur
klos --> Bir klasör oluşturur
ışınlan --> Konum değiştirir 
konum --> Bulunduğunuz konumu gösterir
klos+ --> Klasör dizisi oluşturur
klsil --> Klasör siler
klsil+ --> Klasör dizisini siler
gir --> Bir sonraki klasöre gider
ls --> Linux terminali gibi listeler
işletim sistemi --> İşletim sistemi bilgilerini verir (neofetch)
git kopyala --> Git deponuzu içeri aktarır (Bunun için deponun linkini girmelisiniz)
git kopyala+ --> Sadece git kullanıcı adını ve depo adını yazmanız yeterli örnek: "kullanıcı_adı/depo_adı"
kur --> Paketleri kurar
kaldır --> Paketlari kaldırır
güncelle: --> Paketleri günceller
sistem güncelle --> Sistemi günceller
linux komut= -->Linux komutlarını çalıştırmaya yarar (Bazı komutlar çalışmayabilir)
gui-apt --> Bu komut APT paket yöneticisini gui(kullanıcı arayüzü) versiyonunu açar
yip-kur -- > Yip paket yöneticisi çalışmıyorsa bunu yazın. Bu komut Yip için gerekli paketleri indirir
yip temizle -- > Bu komut bütün Yip paketlerini temizler
komut kilitle= --> KM moduna kilitler. "komut kilitle=açık" veya "komut kilitle=açık"
yip kur (paket adı) --> paketleri kurar
yip kaldır (paket adı) --> paketileri kaldırır 
yip paketler --> yüklü olan paketleri gösterir

"""



komutlar = """
km-geçmiş --> Yazma geçmişinizi gösterir
km-rastgele --> Rastgele sayı oluşturur
km-klos --> Bir klasör oluşturur
km-ışınlan --> Konum değiştirir 
km-konum --> Bulunduğunuz konumu gösterir
km-klos+ --> Klasör dizisi oluşturur
km-klsil --> Klasör siler
km-klsil+ --> Klasör dizisini siler
km-gir --> Bir sonraki klasöre gider
km-ls --> Linux terminali gibi listeler
km-işletim sistemi --> İşletim sistemi bilgilerini verir (neofetch)
km-git kopyala --> Git deponuzu içeri aktarır (Bunun için deponun linkini girmelisiniz)
km-git kopyala+ --> Sadece git kullanıcı adını ve depo adını yazmanız yeterli örnek: "kullanıcı_adı/depo_adı"
km-kur --> Paketleri kurar
km-kaldır --> Paketlari kaldırır
km-güncelle: --> Paketleri günceller
km-sistem güncelle --> Sistemi günceller
km-linux komut= -->Linux komutlarını çalıştırmaya yarar (Bazı komutlar çalışmayabilir)
km-gui-apt --> Bu komut APT paket yöneticisini gui(kullanıcı arayüzü) versiyonunu açar
km-yip-kur -- > Yip paket yöneticisi çalışmıyorsa bunu yazın. Bu komut Yip için gerekli paketleri indirir
km-yip temizle -- > Bu komut bütün Yip paketlerini temizler
km-komut kilitle= --> KM moduna kilitler. "komut kilitle=açık" veya "komut kilitle=açık"
km-yip kur (paket adı) --> paketleri kurar
km-yip kaldır (paket adı) --> paketileri kaldırır 
km-yip paketler --> yüklü olan paketleri gösterir

"""







help_1 = """ 
------------------------------------------------------------------------------------------------------
Git Komutları:

km-git kopyala (depo linki) --> Git deponuzu içeri aktarır (Bunun için deponun linkini girmelisiniz)
km-git kopyala+ (kullanıcı_dı/depo_adı) --> Sadece git kullanıcı adını ve depo adını yazmanız yeterli

------------------------------------------------------------------------------------------------------
Apt paket yöneticisi:

km-kur (paket adı) --> apt Paketlerini kurar
km-kaldır (paket adı) --> apt Paketlarini kaldırır
km-güncelle: (paket adı) --> apt Paketlerini günceller
km-gui-apt --> Bu komut APT paket yöneticisini gui(kullanıcı arayüzü) versiyonunu açar
km-sistem güncelle --> Sistemi günceller

------------------------------------------------------------------------------------------------------
Klasör işlemleri:

km-klos (oluşturkam istediğiniz klasör adı) --> Bir klasör oluşturur
km-klos+ (oluşturkam istediğiniz dizi adı. örnek: Yigit/citak/17) --> üst üste klasör oluşturur
km-klsil (klasör adı) --> boş bir klasörü siler
km-klsil+ (dizi klsör adı) --> klos+ ile oluştururmuş bir diziyi siler
km-klsil++ (klasör adı) --> içerisi dolu olan klasörleri siler (silemeyeceği hiç bir klasör yok)

------------------------------------------------------------------------------------------------------
Yip paket yöneticisi:

km-yip kur (paket adı) --> paketleri kurar
km-yip-kur -- > Yip paket yöneticisi çalışmıyorsa bunu yazın. Bu komut Yip için gerekli paketleri indirir
km-yip temizle -- > Bu komut bütün Yip paketlerini temizler
km-yip kaldır (paket adı) --> Paketileri kaldırır 
km-yip paketler --> Yüklü olan yip paketlerini gösterir
km-yip depo --> yip deposunda bulunan tüm paketleri gösterir

------------------------------------------------------------------------------------------------------

Dosya işlemleri:

km-sil (dosya adı) --> dosya siler
km-konum --> Bulunduğunuz konumu gösterir
km-ls --> Bulunduğunuz konumdaki klasörleri ve dosyaları görüntüler
km-ışınlan (konum girin. örnek: /home/kullanıcı_adınız/Msaüstü) --> Konum değiştirir
km-gir (klasör adı) --> cd komutu ile aynı şeye yarar

------------------------------------------------------------------------------------------------------

Diğer:

km-temizle --> Konsoldaki yazıları siler
km-başlat (paket adı) --> Yüklü olan paketleri çalıştırır
km-geçmiş --> Yazma geçmişinizi gösterir
km-linux komut=(linux terminal komutu) -->Linux komutlarını çalıştırmaya yarar (Bazı komutlar çalışmayabilir)
km-komut kilitle=açık/kapalı --> KM moduna kilitler. "komut kilitle=açık" veya "komut kilitle=açık"
km-işletim sistemi --> İşletim sistemi bilgilerini verir (neofetch)

--------------------------------------------------------------------------------------
"""


help_2 = """ 
------------------------------------------------------------------------------------------------------
Git Komutları:

git kopyala (depo linki) --> Git deponuzu içeri aktarır (Bunun için deponun linkini girmelisiniz)
git kopyala+ (kullanıcı_dı/depo_adı) --> Sadece git kullanıcı adını ve depo adını yazmanız yeterli

------------------------------------------------------------------------------------------------------
Apt paket yöneticisi:

kur (paket adı) --> apt Paketlerini kurar
kaldır (paket adı) --> apt Paketlarini kaldırır
güncelle: (paket adı) --> apt Paketlerini günceller
gui-apt --> Bu komut APT paket yöneticisini gui(kullanıcı arayüzü) versiyonunu açar
sistem güncelle --> Sistemi günceller

------------------------------------------------------------------------------------------------------
Klasör işlemleri:

klos (oluşturkam istediğiniz klasör adı) --> Bir klasör oluşturur
klos+ (oluşturkam istediğiniz dizi adı. örnek: Yigit/citak/17) --> üst üste klasör oluşturur
klsil (klasör adı) --> boş bir klasörü siler
klsil+ (dizi klsör adı) --> klos+ ile oluştururmuş bir diziyi siler
klsil++ (klasör adı) --> içerisi dolu olan klasörleri siler (silemeyeceği hiç bir klasör yok)

------------------------------------------------------------------------------------------------------
Yip paket yöneticisi:

yip kur (paket adı) --> paketleri kurar
yip-kur -- > Yip paket yöneticisi çalışmıyorsa bunu yazın. Bu komut Yip için gerekli paketleri indirir
yip temizle -- > Bu komut bütün Yip paketlerini temizler
yip kaldır (paket adı) --> Paketileri kaldırır 
yip paketler --> Yüklü olan yip paketlerini gösterir
yip depo --> yip deposunda bulunan tüm paketleri gösterir

------------------------------------------------------------------------------------------------------

Dosya işlemleri:

sil (dosya adı) --> dosya siler
konum --> Bulunduğunuz konumu gösterir
ls --> Bulunduğunuz konumdaki klasörleri ve dosyaları görüntüler
ışınlan (konum girin. örnek: /home/kullanıcı_adınız/Msaüstü) --> Konum değiştirir
gir (klasör adı) --> cd komutu ile aynı şeye yarar

------------------------------------------------------------------------------------------------------

Diğer:

temizle --> Konsoldaki yazıları siler
başlat (paket adı) --> Yüklü olan paketleri çalıştırır
geçmiş --> Yazma geçmişinizi gösterir
linux komut=(linux terminal komutu) -->Linux komutlarını çalıştırmaya yarar (Bazı komutlar çalışmayabilir)
komut kilitle=açık/kapalı --> KM moduna kilitler. "komut kilitle=açık" veya "komut kilitle=açık"
işletim sistemi --> İşletim sistemi bilgilerini verir (neofetch)

--------------------------------------------------------------------------------------
"""




yip_paketleri = """ Yip deposundaki paketler:

|-Minecraft:
|----Tür: Oyun
|----Hazırlayanlar: tl legacy
|----Kurmak için gerekli komut: yip kur minecraft

|-Simple Text Editor:
|----Tür: Metin düzenleyeci
|----Hazırlayanlar: chat gpt
|----Kurmak için gerekli komut: yip kur simple_text-editor



bulunan program sayısı: 2

Sizlerde kendi yaptığınız programları buraya ekleyebilirsiniz :D
Yapmanız gereken bana e-posta göndermeniz ve programınzın bulunduğu
git deposunun linkini atmanız yeterli

yigitcitak.1817@gmail.com

"""






hata_masaji_1 = """Programın sistem dosyasında değilsin. Bu yüzden bu komutu kullanabilmen için sistem klasörüne geri dönün
programın sistem klasörüne geri dönek için ışınlan komutunu kullanabilirsin"""



























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