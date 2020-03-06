# Fonksiyonlarımızı tanımlayalım. ------------------------

def asalSayi(sayi):
    if (sayi == 1): return False
    elif (sayi == 2): return True
    elif (sayi == 3): return True
    else:
        sayinin_karekoku = sayi**(1/2)
        # print("Sayının karekokü: ", sayinin_karekoku)
        sayinin_karekoku = int(sayinin_karekoku)
        denenecekBolenler = list(range(2,sayinin_karekoku+1))
        # print("Denenecek bölenler: ", denenecekBolenler)
        for eleman in denenecekBolenler:
            if (sayi % eleman == 0):
                asallık = False
                # print("Bölüm sıfır olan bulundu: ", eleman)
                break
            else:
                asallık = True
                continue
        return asallık

def mukemmelSayiBulma(sayi):
    bolecek_liste = list(range(1, sayi))
    # print("bolecek_liste tanımı", bolecek_liste) Kontrol noktası (1)
    bolunen_liste = list()
    for deneme in bolecek_liste:
        if (sayi % deneme == 0):
            bolunen_liste.append(deneme)
            # print("if blogunun içindeki çıktı: ", deneme) Kontrol noktası (2)
    toplam = int()
    for listeIcindekiSayi in bolunen_liste:
        toplam += listeIcindekiSayi
    # print("Toplam: ", toplam)  Kontrol noktası (3)
    if (toplam == sayi):
        return True
    else:
        return False

def armstrongSayiBulma(sayi):
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
        return True
    else:
        return False


def ebobBulma():
    print("")
    ebobIlkSayi = int(input("İlk sayıyı giriniz: "))
    ebobIkinciSayi = int(input("İkinci sayıyı giriniz: "))

    ebobIlkDeneneceklerListesi = list(range(1, ebobIlkSayi+1))
    ebobIkinciDeneneceklerListesi = list(range(1, ebobIkinciSayi+1))

    ebobIlkBolunenListesi = list()
    for ebobIlkDenenen in ebobIlkDeneneceklerListesi:
        if (ebobIlkSayi % ebobIlkDenenen == 0):
            ebobIlkBolunenListesi.append(ebobIlkDenenen)
        else: continue

    ebobIkinciBolunenListesi = list()
    for ebobIkinciDenenen in ebobIkinciDeneneceklerListesi:
        if (ebobIkinciSayi % ebobIkinciDenenen == 0):
            ebobIkinciBolunenListesi.append(ebobIkinciDenenen)
        else: continue

    ebobBulunanlarListesi = list()
    for ebobDenenen1 in ebobIlkBolunenListesi:
        for ebobDenenen2 in ebobIkinciBolunenListesi:
            if ebobDenenen1 == ebobDenenen2:
                ebobBulunanlarListesi.append(ebobDenenen1)
            else: continue

    ebobBulunanlarListesiUzunluk = len(ebobBulunanlarListesi)
    print("""
----------------------------------------------------------
Seçtiğiniz sayıların en büyük ortak böleni {} sayısıdır.
----------------------------------------------------------      
    """.format(ebobBulunanlarListesi[ebobBulunanlarListesiUzunluk-1]))

def yardim():
    print("""

************************************************************************

             ==== Matematik Programı (belgrad v4) ====

              Bu program ile düşündüğünüz sayıların
                matematiksel olaylarını görebilir,
            bunlar hakkında bilgi sahibi olabilirsiniz.


                    -- Menü ---------------
                    1) Asallık Testi
                    2) Asal Sayı Bulucu
                    3) Mükemmel Sayı Testi
                    4) Mükemmel Sayı Bulucu
                    5) Armstrong Sayı Testi
                    6) Armstrong Sayı Bulucu
                    7) Çarpım Tablosu
                    8) EBOB / EKOK Bulucu
                    h) Hakkında
                    y) Yardım
                    q) Çıkış
                    -----------------------


************************************************************************

    """)


# Programımızı kuralım --------------------------------

#Program açılışında yardım menüsünü göster.
yardim()

while True:

    # Menü dolaşma komutları
    menuSecenegi = input("Seçmek istediğiniz komut numarası: ")

    # Kullanıcının asallık testi istemesi durumu:
    if menuSecenegi == "1":
        denenecekSayi = input("Kontrol etmek istediğiniz sayıyı giriniz: ")
        if asalSayi(int(denenecekSayi)) == True:
            print("Girdiğiniz sayı bir asal sayıdır.")
        else: print("Girdiğiniz sayı bir asal sayı değildir.")
        print("")

    # Kullanıcın asal sayı bulucu istemesi durumu:
    elif menuSecenegi == "2":
        kacaKadar = int(input("Kaça kadar aramak istediğinizi giriniz: "))
        sayilar = list(range(1, kacaKadar+1))
        asalOlanlar = list()
        for i in sayilar:
            if asalSayi(i) == True:
                asalOlanlar.append(i)
            else:
                continue
        print("Girdiğiniz sayıya kadar olan asalların listesi şudur: ")
        print("------------------------------------------------------")
        print(asalOlanlar)
        print("------------------------------------------------------")
        print("")

    # Kullanıcının mükemmel sayı testi istemesi durumu:
    elif menuSecenegi == "3":
        mukemmelSayiDenenecekSayi = int(input("Kontrol etmek istediğiniz sayıyı giriniz: "))
        if (mukemmelSayiBulma(mukemmelSayiDenenecekSayi) == True):
            print("Girdiğiniz sayı bir mükemmel sayıdır.")
        else: print("Girdiğiniz sayı bir mükemmel sayı değildir.")
        print("")

    # Kullanıcının mükemmel sayı bulucu istemesi durumu:
    elif menuSecenegi == "4":
        mukemmelsayiKacaKadar = int(input("Kaça kadar aramak istediğinizi giriniz: "))
        mukemmelsayiSayilar = list(range(1, mukemmelsayiKacaKadar+1))
        mukemmelsayiOlanlar = list()
        for j in mukemmelsayiSayilar:
            if mukemmelSayiBulma(j) == True:
                mukemmelsayiOlanlar.append(j)
            else: continue
        print("Girdiğiniz sayıya kadar olan mükemmel sayıların listesi şudur: ")
        print("------------------------------------------------------")
        print(mukemmelsayiOlanlar)
        print("------------------------------------------------------")
        print("")

    # Kullanıcın armstrong sayı testi istemesi durumu:
    elif menuSecenegi == "5":
        armgstrongSayiDenenecekSayi = input("Kontrol etmek istediğiniz sayıyı giriniz: ")
        if (armstrongSayiBulma(armgstrongSayiDenenecekSayi) == True):
            print("Girdiğiniz sayı bir armstrong sayıdır.")
        else: print("Girdiğiniz sayı bir armstrong sayı değildir.")
        print("")

    # Kullanıcın armstrong sayı bulucu istemesi durumu:
    elif menuSecenegi == "6":
        armstrongsayiKacaKadar = int(input("Kaça kadar aramak istediğinizi giriniz: "))
        armstrongsayiSayilar = list(range(1, armstrongsayiKacaKadar+1))
        armstrongsayiOlanlar = list()
        for j in armstrongsayiSayilar:
            j = str(j)
            if armstrongSayiBulma(j) == True:
                armstrongsayiOlanlar.append(j)
            else: continue
        print("Girdiğiniz sayıya kadar olan armstrong sayıların listesi şudur: ")
        print("------------------------------------------------------")
        print(armstrongsayiOlanlar)
        print("------------------------------------------------------")
        print("")

    # Kullanıcın çarpım tablosu istemesi durumu:
    elif menuSecenegi == "7":
        rakamlarListe = list(range(0,10))
        print("""

**** ÇARPIM TABLOSU ARACI ***
1) Rakama özel çarpım tablosu
2) Tüm çarpım tablosu

        """)
        carpimtablosuMenuSecenegi = input("Seçmek istediğiniz komut numarası: ")
        if carpimtablosuMenuSecenegi == "1":
            carpimtablosuRakamSeceneği = int(input("İstediğiniz rakamı giriniz: "))
            if (carpimtablosuRakamSeceneği > 9 or carpimtablosuRakamSeceneği < 0):
                print("Hatalı bir giriş yaptınız. Rakam girmelisiniz.")
            else:
                for rakam in rakamlarListe:
                    print("{} x {} = {}".format(carpimtablosuRakamSeceneği, rakam, carpimtablosuRakamSeceneği*rakam))
            print("")
        elif carpimtablosuMenuSecenegi == "2":
            for sayi1 in rakamlarListe:
                for sayi2 in rakamlarListe:
                    print("{} x {} = {}".format(sayi1, sayi2, sayi1*sayi2))
                print("----------------")
        print("")

    # Kullanıcının ebob/ekok bulucusunu seçme durumu:
    elif menuSecenegi == "8":
        print("""

**** EBOB/EKOK BULUCU ARACI ***
1) EBOB Bulucu
2) EKOK Bulucu

        """)
        ebobEkokBulucuSecenegi = input("Seçmek istediğiniz komut numarası: ")
        if ebobEkokBulucuSecenegi == "1":
            ebobBulma()
        elif ebobEkokBulucuSecenegi == "2": ekokBulma()
        else: print("Tekrar deneyiniz.")
        print("")


    # Kullanıcının yardımı seçme durumu:
    elif menuSecenegi == "y":
        yardim()

    # Kullanıcının program hakkında bilgi istemesi durumu:
    elif menuSecenegi == "h":
        print("""
        Program, 10 Haziran 2019'da yazılmıştır. Başlangıç amacı asal bulmak için
        hazırda program bulundurmak iken daha sonraları (belgrad_v4 sonrası) bir çok
        fonksiyonu bir araya getiren matematik programı yazmaktır. Daha detaylı bilgi
        sonraki sürümlerde programa dahil edilecektir.

        Python sürümü: 3
        Derleme numarası: 4.3.2
        """)
        print("")

    # Kullanıcının çıkmak istemesi durumu:
    elif menuSecenegi == "q":
        print("")
        print("Programımızı kullandığınız için teşekkür ederiz.")
        print("İyi günler dileriz.")
        print("")
        break

    # Diğer durumları çözümleyelim:
    else:
        print("Yeniden deneyiniz.")
        print("Aradığınızı bulamıyor iseniz 'y' komutunu kullanınınz.")
        print("")
