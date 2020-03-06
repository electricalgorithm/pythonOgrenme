# EKOK iki sayının katlarının kesiştiği en küçük kattır.
# EBOB iki sayının bölenlerinin kesiştiği en büyük bölendir.

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

def asalBulucu(kacaKadar):
    sayilar = list(range(1, kacaKadar+1))
    asalOlanlar = list()
    for i in sayilar:
        if asalSayi(i) == True:
            asalOlanlar.append(i)
        else:
            continue
    return asalOlanlar


print("""
========================================================

            EBOB/EKOK BULMA SİHİRBAZI
                    (ver dog1)

        En büyük ortak bölen elde etmek için "1"
        En küçük ortak kat elde etmek için "2"
            Çıkmak için ise q basınız.

=======================================================

""")

while True:
    islemGiriniz = input("Komut Numarası giriniz. ")
    if islemGiriniz == "1":
        # ebob olayları
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
        print("EBOB SONUCUNUZ: ", ebobBulunanlarListesi[ebobBulunanlarListesiUzunluk-1])


    elif islemGiriniz == "2":
        # ekok olayları
        sonucSayi = dict()
        ekokIlkSayi = int(input("İlk sayıyı giriniz: "))
        ekokIkinciSayi = int(input("İkinci sayıyı giriniz: "))

        # İlk sayının asal çarpanları bulma işlemi:
        ekokIlkSayiAsalCarpanlari = list()
        ekokIlkSayiDuzenliListe = list()
        ekokDuzenlenmisIlkSayi = ekokIlkSayi
        ilkSayiyaKadarAsallar = asalBulucu(ekokIlkSayi+1)
        while ekokDuzenlenmisIlkSayi > 1:
            for ekokAsalDeneme in ilkSayiyaKadarAsallar:
                if ekokDuzenlenmisIlkSayi % ekokAsalDeneme == 0:
                    ekokIlkSayiAsalCarpanlari.append(ekokAsalDeneme)
                    ekokIlkSayiDuzenliListe.append(ekokAsalDeneme)
                    ekokDuzenlenmisIlkSayi = ekokDuzenlenmisIlkSayi / ekokAsalDeneme
                else:
                    continue
        ekokIlkSayiAsalCarpanlari.sort()

        ekokIkinciSayiAsalCarpanlari = list()
        ekokIkinciSayiDuzenliListe = list()
        ekokDuzenlenmisIkinciSayi = ekokIkinciSayi
        ikinciSayiyaKadarAsallar = asalBulucu(ekokIkinciSayi+1)
        while ekokDuzenlenmisIkinciSayi > 1:
            for ekokAsalDeneme in ikinciSayiyaKadarAsallar:
                if ekokDuzenlenmisIkinciSayi % ekokAsalDeneme == 0:
                    ekokIkinciSayiAsalCarpanlari.append(ekokAsalDeneme)
                    ekokIkinciSayiDuzenliListe.append(ekokAsalDeneme)
                    ekokDuzenlenmisIkinciSayi = ekokDuzenlenmisIkinciSayi / ekokAsalDeneme
                else:
                    continue
        ekokIkinciSayiAsalCarpanlari.sort()

        for ekokHerDeneme in ekokIkinciSayiDuzenliListe:
            if ekokIlkSayiAsalCarpanlari.count(ekokHerDeneme) > ekokIkinciSayiAsalCarpanlari.count(ekokHerDeneme):
                sonucSayi.update({ekokHerDeneme: ekokIlkSayiAsalCarpanlari.count(ekokHerDeneme)})
            else:
                sonucSayi.update({ekokHerDeneme: ekokIkinciSayiAsalCarpanlari.count(ekokHerDeneme)})
        for ekokHerDeneme in ekokIlkSayiDuzenliListe:
            if ekokIlkSayiAsalCarpanlari.count(ekokHerDeneme) > ekokIkinciSayiAsalCarpanlari.count(ekokHerDeneme):
                sonucSayi.update({ekokHerDeneme: ekokIlkSayiAsalCarpanlari.count(ekokHerDeneme)})
            else:
                sonucSayi.update({ekokHerDeneme: ekokIkinciSayiAsalCarpanlari.count(ekokHerDeneme)})

        toplamCikti = 1
        for x,y in sonucSayi.items():
            toplamCikti = toplamCikti * (x**y)
        print("EKOK SONUCUNUZ: ", toplamCikti)


    elif islemGiriniz == "q":
        print("Görüşmek üzere.")
        break

    else:
        print("Yanlış bir komut numarası girdiniz.")


    ## son Komut
    print("")
