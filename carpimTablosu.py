print("""
********************************************************************************

Çarpım Tablosu
-------------------

1) Sayı girme menüsü
2) Bütün çarpım Tablosu
3) Çıkış


********************************************************************************
""")

while True:

    rakamlarListe = list(range(0,10))

    istek = input("Gerçekleştirmek istediğiniz menü kodu: ")

    if istek == "1":
        print("Sayıya özel çarpım tablosu seçeneğiniz seçtiniz.")
        sayi = input("Bir rakam giriniz: ")
        sayi = int(sayi)
        if (sayi > 9 or sayi < 0):
            print("Hatalı giriş yaptınız. Rakam girmelisiniz.")
        else:
            for rakam in rakamlarListe:
                print("{} x {} = {}".format(sayi, rakam, sayi*rakam))
        print("-----------------------------------------------------------------")
    elif istek == "2":

        for sayi1 in rakamlarListe:
            for sayi2 in rakamlarListe:
                print("{} x {} = {}".format(sayi1, sayi2, sayi1*sayi2))
            print("-----------------")

    elif istek == "3":
        print("Programdan çıkış yapılıyor.")
        break
    else:
        print("Bir şeyler yanlış gitti. Tekrar deneyiniz.")
