print("""
*********************************************************************

            = Armgstrong Sayı Bulucusuna Hoşgeldiniz. =
             Sürüm: aa    ||  Yazılım: Gökhan Koçmarlı

            Armgstrong sayısı, bir sayının her rakamının
             basamak sayısındaki katlarının toplamının
                   kendisine eşit olmasıdır.

                 Çıkış yapmak için "q" basınız.

*********************************************************************
""")

while True:
    sayi = input("Kontrol etmek istediğiniz sayıyı giriniz: ")
    if sayi == "q":
        print("##  Programdan çıkışınız yapıldı. İyi günler dileriz.  ##")
        break
    elif sayi == "":
        print("##  Yanlışlıkla entera basmış olabilirsiniz.  ##")
        print("##  Tekrar deneyiniz.  ##")
    else:
        sozcuktekiHarfler = list()
        for harf in sayi:
            sozcuktekiHarfler.append(harf)
        uzunluk = len(sozcuktekiHarfler)
        toplam = int()
        for deger in sozcuktekiHarfler:
            deger_int = int(deger)
            toplam += (deger_int ** uzunluk)
        sayi = int(sayi)
        if (toplam == sayi):
            print(" ##  Tebrikler, bir Armgstrong sayısı buldunuz.  ##")
        else:
            print("##  Girdiğiniz sayı Armgstrong sayısı değildir. ##")
        print("--------------------------------------------")
