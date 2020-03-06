# -*- coding: utf-8 -*-
#!/usr/bin/env python3

print("""

        --- Programa hoşgeldiniz. ---
Çift sayı kontrol etmek için doğru yerdesiniz.
            Çıkmak için q yazınız.
""")

def ciftSayiBulucu(girdi):
    try:
        girdi = int(girdi)
    except (TypeError, ValueError):
        print("Girdiğiniz bir sayı değildir.")
    else:
        if (girdi % 2 == 0):
            print("Girdiğiniz sayı çift sayıdır.")
        else:
            raise ValueError("Girdiğiniz sayı tek sayıdır.")

while True:
    print("")
    alinanDeger = input("Merak ettiğiniz sayıyı giriniz: ")
    if (alinanDeger == "q"):
        break
    else:
        try:
            ciftSayiBulucu(alinanDeger)
        except (ValueError):
            print("Girdiğiniz sayı tek sayıdır.")
