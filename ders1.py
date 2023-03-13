print("Kodlamaio")
#string => metinsel ifade
baslik = "Taşıt Kredisi"
print(baslik)
baslik = "İhtiyaç Kredisi"
print(baslik)
#int, integer => tam sayı
vade = 36 #int, matematiksel işlem yapılabilir
ekVade = 6
vade2 = "36" #string, işlem yapılamaz

#float, decimal, double
aylikOdeme = 200.50

#bool, boolean => True, False
yukselisteMi = True

#matematiksel operatörler

# +
print(5+5)
print(vade + 12)
print(vade + ekVade)
print(36+6)

# -
print(5-5)
print(vade-12)
print(vade-ekVade)
print(36-6)

# *
print(5*5)
print(vade*2)
print(vade*ekVade)
print(10*10)

# /
print(5/5)
print(vade/2)
print(vade/ekVade)
print(10/2)


yeniVade =vade/2
fiyat=100
indirimliFiyat=fiyat-20

print(yeniVade)
print(indirimliFiyat)

# % => mod operator
print(10%2)
print(vade%5)
print(vade%ekVade)
print(30%10)


#mantıksal operatörler
print(1==1)
print(1==2)

#CTRL + Ö (Yorum satırı yapma ve geri alma)
print(1>2)
print(3>1)
print(1>1)
print(1>=1)

print(1<2)
print(3<1)
print(1<1)
print(1<=1)


print(1 != 1)
print(1 != 2)

# or and

#or => veya
print(1 > 2 or 5 > 2)
print(1>2 and 5 > 2)
print(1>2 or 5>2 and 3>2)

print(1 > 2 and 5 > 2 and 3 > 2)

print(2 > 1 or 1 > 2 and 3 > 2)


#karar yapıları
#if else
sayi1=10
sayi2=15
#sayi1 sayi2'den büyükse ekrana sayi 1 daha büyük yazdır
#condition

#indent (boşluklar)
if sayi1 > sayi2:
    print("Sayi 1 Sayi 2'den büyüktür.")
elif sayi1 == sayi2:
    print("İki sayı eşittir.")
#eğer if ve elif bloklarına girmez ise
else:
    print("Sayi1 sayi2'den küçüktür.")


if sayi1 <= sayi2:
    print("Sayi1 Sayi2'den küçüktür.")
if sayi1 == sayi2:
    print("İki sayi eşittir.")
else:
    print("Sayi1 sayi2'den büyüktür.")
    
print("Burası if bloğunun dışıdır.")



