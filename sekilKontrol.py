# -*- codeing UTF-8 -*- #
print("""
--------------------
Şekil Tanımlama Programına Hoşgeldiniz.
İki tür şekili tanımlayabiliriz:
* Dört kenarlı
* Üç kenarlı

Lütfen cevaplara dikkat ediniz.
""")

sekil_girdi = input("Kaç kenarlı bir şekil istiyorsunuz? (Dört veya Üç) ")

# Dörtkenarlılar için olan kontrol işlemini sağlar.
if (sekil_girdi == "dört" or sekil_girdi == "Dört" or sekil_girdi == "4"):
    solKenar = int(input("Sol kenarı giriniz: "))
    sagKenar = int(input("Sağ kenarı giriniz: "))
    ustKenar = int(input("Üst kenarı giriniz: "))
    altKenar = int(input("Alt kenarı giriniz: "))
    # Kare olup olmadığının kontrolünü sağlar.
    if (altKenar == ustKenar and sagKenar == solKenar and ustKenar == sagKenar):
        print("Girdiğiniz şekil bir kare belirtmektedir.")
    # Dikdörtgen için olasılıkların kontrolünü sağlar.
    elif (
            (solKenar == sagKenar and ustKenar == altKenar and ustKenar != sagKenar)
            or (sagKenar == ustKenar and solKenar == altKenar and sagKenar != solKenar)
            or (sagKenar == altKenar and solKenar == ustKenar and sagKenar != solKenar)
        ):
        print("Girdiğiniz şekil bir dikdörtgen belirtmektedir.")
    # Hiçbiri değilse yamuktur.
    else:
        print("Girdiğiniz şekil bir yamuk belirtmektedir.")
#Üçgenler için kontrol işlemini sağlar.
elif (sekil_girdi == "üç" or sekil_girdi == "Üç" or sekil_girdi == "3"):
    ilkKenar = int(input("İlk kenarı giriniz: "))
    ikinciKenar = int(input("İkinci kenarı giriniz: "))
    ucuncuKenar = int(input("Üçüncü kenarı giriniz: "))
    # Üçgenlik şartlarına uygun kenarlar girilip girilmediğini kontrol eder.
    toplam = ilkKenar + ikinciKenar
    cikarim = ilkKenar - ikinciKenar
    if (ucuncuKenar <= toplam and ucuncuKenar >= cikarim):
        # Eşkenar üçgen olup olmadığının kontrolünü sağlar.
        if (ilkKenar == ikinciKenar and ikinciKenar == ucuncuKenar):
            print("Girdiğiniz şekil bir eşkenar üçgen belirtmektedir.")
        # İkizkenar üçgen olup olmadığının kontrolünü sağlar.
        elif (
                (ilkKenar == ikinciKenar and ikinciKenar != ucuncuKenar)
                or (ilkKenar == ucuncuKenar and ikinciKenar != ucuncuKenar)
                or (ikinciKenar == ucuncuKenar and ikinciKenar != ilkKenar)
            ):
            print("Girdiğiniz şekil bir ikizkenar üçgen belirtmektedir.")
        #Hiçbiri değilse çeşitkenardır.
        else:
            print("Girdiğiniz şekil bir çeşitkenar üçgen belirtmektedir.")
    # Girilen değerler üçgen eşitliğine uymamaktadır.
    else:
        print("Girdiğiniz şekil herhangi bir üçgen belirtemez.")
