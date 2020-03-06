"""

Bu kod 10.06.2019'da saat 02:24'de Gökhan Koçmarlı
tarafından Deepin 15.10 işletim sistemi kullanılarak
yazılmıştır. Muziplip yapıp yüksek bir sayı girerseniz
program range fonksiyonundan dolayı hata verecektir.

Kendime not: Umarım mantıklı kararlar almış,
programlama sektöründe ileri seviyeye ulaşmışsındır.
Aksi halde bunca çaba, zaman hepsi boşa gitmiş demektir.
Merve Varlı'ya selam söyle. Onu çok seviyorum.

"""





print("""
*************************************

Mükemmel sayılar, kendisi dışındaki
çarpanlarının toplamı kendisine eşit
olan sayılardır. Bunları bulmak,
insan zekasına aşırı; işlemci hızına
az gelen işlerdir.

Bir sayının mükemmel olup olmadığını
test etmek için bu programı yazdım.
Ayrıca evet, ödevimdi de.

Program sürümü: (alpha_v2)
Yazılım: Gökhan Koçmarlı

Programdan çıkmak için sayı yazma
kısmına "q" harfini yazmanız
yeterlidir.

*************************************
""")

while True:

    # Sayımızı alalım.
    sayi = input("Mükemmel olduğunu düşündüğünüz bir sayı giriniz: ")

    # Çıkış yapılıp yapılmayacağını kontrol edelim.
    if sayi == "q":
        print("Programdan çıkış yapılıyor.")
        break

    # Kullanıcının boşluk girmesine karşı önlem alalım.
    elif sayi == "":
        print("Yeniden giriniz.")

    # İşlevini yerine getirelim.
    else:
        # Sayıyı bölmeyi deneyeceğimiz bütün sayıları bir listeye yazalım.
        sayi = int(sayi)
        bolecek_liste = list(range(1, sayi))
        # print("bolecek_liste tanımı", bolecek_liste) Kontrol noktası (1)

        # Yeni bir bölünenler listesi tanımlayıp kontrolümüzü sağlayalım.
        bolunen_liste = list()
        for deneme in bolecek_liste:
            if (sayi % deneme == 0):
                bolunen_liste.append(deneme)
                # print("if blogunun içindeki çıktı: ", deneme) Kontrol noktası (2)

        # bolunen_liste'deki sayıları toplayıp toplam değişkenine atayalım.
        toplam = int()
        for listeIcindekiSayi in bolunen_liste:
            toplam += listeIcindekiSayi
        # print("Toplam: ", toplam)  Kontrol noktası (3)

        # Sayımız ile toplamda bulduğumuz sayının aynı olup olmadığını kontrol edelim.
        if (toplam == sayi):
            print("Tebrikler, bir mükemmel sayı buldunuz!")
        else:
            print("Girdiğiniz sayı mükemmel olmaktan çok uzak.")

        print("-------------------------------------")
