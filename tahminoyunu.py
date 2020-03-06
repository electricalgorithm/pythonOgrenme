print(
"""
-------------------------------------------------------------

================ Tahmin oyununa hoşgeldiniz! ================

Bilgisayarın rastgele (rastgele?) seçtiği sayılar arasından
tahmin yapmanız gerekmektedir. Her seferinizde 10 hakkınız
                bulunacaktır. İyi şanslar!

            Sayı aralığı: [1, 2, (...), 39, 40]

------------------------------------------------------------
"""
)


import random
import time

sayi = random.randint(1, 40)
denemeHakki = 10
print(sayi)

while denemeHakki >= 0:
    print("")

    while True:
        tahmin = input("Tahmininizi giriniz: ")
        if tahmin.isdigit():
            tahmin = int(tahmin)
            break
        else:
            print("Dostum dalga mı geçiyorsun?")
            time.sleep(1)
            print("Yeniden dene.")
            time.sleep(1)
            print("Mümkünse sayı gir.")
            time.sleep(0.5)
            print(" -__- ")

        print("")

    if tahmin == sayi:
        print("")
        print("Acaba buldun mu lan?")
        time.sleep(0.5)
        print(" O_o ")
        time.sleep(1)
        print("İçimden bir ses doğru gibi diyor.")
        time.sleep(2)
        print("Ah emin olamıyorum. Acaba? Yoksa?")
        time.sleep(1)
        print("Evet!")
        time.sleep(0.5)
        print(" *_* ")
        time.sleep(0.5)
        print("")
        time.sleep(0.2)
        print("Tebrikler, sayıyı buldun kereta! Programdan çıkmaya hak kazandın eşek sıpası seni. Ehehehe.")
        print("")
        break

    elif (tahmin > sayi):
        print("Küçül de cebime gir.")
        time.sleep(1)
        print("Yeni nesil ölmüş be!")
        time.sleep(0.5)
        print("Kalan hakkın:", denemeHakki)

    elif (tahmin < sayi):
        print("Gel, gel, gel, yan yap da gel...")
        time.sleep(0.7)
        print("Bu ne oğlum? Büyü azıcık, sayı ile birlikte...")
        time.sleep(0.5)
        print("Kalan hakkın:", denemeHakki)

    else:
        print("")
        print("Lan naptın programa? Ne bok yedin de benim tanımım dışına çıktın?")
        time.sleep(1)
        print("Beyaz şapkıları çağırmadan ben ayağını denk al koçum.")
        time.sleep(1)
        print("Bunu da düşüyorum hakkından. Kalanı da söylemiyorum. İt.")

    denemeHakki -= 1
