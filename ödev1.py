# 1)Python veri türleri
#int:tam sayılar
#float:ondalıklı sayılar
#string:harf, sayı veya birleşimleri
#boolean:True(1) ve False(0)

# 2) Kodlama.io sitesinde değişken olarak kullanıldığını düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz.
#string: kurs isimleri
#int: tamamlama oranı
#bool: kurs içerisinde tamamlayıp tamamlanmadığı kontrolü

# 3) Kodlama.io sitesinde şart blokları kullanıldığını düşündüğünüz kısımları örneklendiriniz ve Python dilinde bu örnekleri koda dökünüz.
#login
kullaniciAdi="mehmetali"
sifre=123

kullaniciAdi_giris=input("Kullanıcı Adı: ")
sifre_giris=int(input("Şifre: "))

if kullaniciAdi==kullaniciAdi_giris and sifre==sifre_giris:
    print("Siteye giriş yapılıyor...")

else:
    print("Hatalı kullanıcı adı veya şifre!")

