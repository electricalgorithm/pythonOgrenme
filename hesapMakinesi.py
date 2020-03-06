# -*- coding: UTF-8 -*- #

import math

def degToRad(deg):
    rad = (deg * math.pi) / 180
    return rad
def radToDeg(rad):
    deg = (180 * rad) / math.pi
    return deg

print("""
            ====================================================
            ----------------------------------------------------

                                HESAP MAKİNESİ

             Yapacağınız işlemleri aşağıdaki gibi göre kodlayınız:

                            # Toplama: top
                            # Çarpma: car
                            # Kök alma: kok
                            # Üs alma: us
                            # Logaritma: log
                            # Trigonometri Paneli: tri

            ----------------------------------------------------

                                Çıkış: q
                   (Küçük harf olmasına dikkat ediniz.)

                        Yayımcı: Gökhan Koçmarlı
                              (versiyon 4)

            ---------------------------------------------------
            ===================================================t

""")

while True:
    print("")
    sonuc = 0
    girdi_islem = str()
    girdi_islem = input("Bir işlem giriniz: ")

    if girdi_islem == "top":
        a = int(input("İlk sayıyı giriniz: "))
        b = int(input("İkinci sayıyı giriniz: "))
        sonuc = a + b
        print("")
        print(sonuc)



    elif girdi_islem == "car":
        a = int(input("İlk sayıyı giriniz: "))
        b = int(input("İkinci sayıyı giriniz: "))
        sonuc = a*b
        print("")
        print(sonuc)

    elif girdi_islem == "kok":
        a = int(input("Sayıyı giriniz: "))
        b = int(input("Kökün Derecesini giriniz: "))
        sonuc = a**(1/b)
        print("")
        print(sonuc)

    elif girdi_islem == "us":
        a = int(input("Sayıyı giriniz: "))
        b = int(input("Üssünü giriniz: "))
        sonuc = a**b
        print("")
        print(sonuc)

    elif girdi_islem == "log":
        a = int(input("Logaritma tabanını giriniz: "))
        b = int(input("Sayıyı giriniz: "))
        sonuc = math.log(b,a)
        print("")
        print(sonuc)

    elif girdi_islem == "tri":

        print("""

=============================================

Trigonometrik panelden aşağıdaki işlemleri yapabilirsiniz:

# cosinus: cos, arccosinus: acos
# sinus: sin, arcsinus: asin
# tanjant: tan, arctanjant: atan
# cotanjant: cot, arccotanjant: acot

Geri dönmek için: q

============================================

        """)

        while True:
            print("")
            girdi_ikincil_input = input("İşlem giriniz: ")

            if girdi_ikincil_input == "cos":
                a = input("Derece cinsinden giriniz: ")
                if a.isdigit():
                    a = int(a)
                    a = degToRad(a)
                    sonuc = math.cos(a)
                    print("")
                    print(sonuc)
                else:
                    print("Tam sayı girmediniz. Doğru yazdığınızdan emin misiniz? İsterseniz tekrar deneyin.")

            elif girdi_ikincil_input == "acos":
                a = input("Sayı cinsinden giriniz: ")
                if a.isdigit():
                    a = int(a)
                    sonuc = radToDeg(math.acos(a))
                    print("")
                    print(sonuc)
                else:
                    print("Tam sayı girmediniz. Doğru yazdığınızdan emin misiniz? İsterseniz tekrar deneyin.")

            elif girdi_ikincil_input == "sin":
                a = input("Derece cinsinden giriniz: ")
                if a.isdigit():
                    a = int(a)
                    a = degToRad(a)
                    sonuc = math.sin(a)
                    print("")
                    print(sonuc)
                else:
                    print("Tam sayı girmediniz. Doğru yazdığınızdan emin misiniz? İsterseniz tekrar deneyin.")

            elif girdi_ikincil_input == "asin":
                a = input("Sayı cinsinden giriniz: ")
                if a.isdigit():
                    a = int(a)
                    sonuc = radToDeg(math.asin(a))
                    print("")
                    print(sonuc)
                else:
                    print("Tam sayı girmediniz. Doğru yazdığınızdan emin misiniz? İsterseniz tekrar deneyin.")

            elif girdi_ikincil_input == "tan":
                a = input("Derece cinsinden giriniz: ")
                if a.isdigit():
                    a = int(a)
                    a = degToRad(a)
                    sonuc = math.tan(a)
                    print("")
                    print(sonuc)
                else:
                    print("Tam sayı girmediniz. Doğru yazdığınızdan emin misiniz? İsterseniz tekrar deneyin.")

            elif girdi_ikincil_input == "atan":
                a = input("Sayı cinsinden giriniz: ")
                if a.isdigit():
                    a = int(a)
                    sonuc = radtodeg(math.acos(a))
                    print("")
                    print(sonuc)
                else:
                    print("Tam sayı girmediniz. Doğru yazdığınızdan emin misiniz? İsterseniz tekrar deneyin.")

            elif girdi_ikincil_input == "cot":
                a = input("Derece cinsinden giriniz: ")
                if a.isdigit():
                    a = int(a)
                    a = degToRad(a)
                    sonuc = 1 / (math.tan(a))
                    print("")
                    print(sonuc)
                else:
                    print("Tam sayı girmediniz. Doğru yazdığınızdan emin misiniz? İsterseniz tekrar deneyin.")


            elif girdi_ikincil_input == "acot":
                a = input("Sayı cinsinden giriniz: ")
                if a.isdigit():
                    a = int(a)
                    sonuc = 1 / radToDeg((math.atan(a)))
                    print("")
                    print(sonuc)
                else:
                    print("Tam sayı girmediniz. Doğru yazdığınızdan emin misiniz? İsterseniz tekrar deneyin.")


            elif girdi_ikincil_input == "q":
                break

            else:
                print("Yanlış bir komut girdiniz. Tekrar deneyin.")
                continue

    elif girdi_islem == "q":
        print("")
        print("Program kapatılıyor.")
        break

    else:
        print("Yanlış bir işlem girdiniz. Lütfen baştan başlayınız.")
        continue
