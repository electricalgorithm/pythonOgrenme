def ozelAritmatik(func):
    def wrapper(arg):
        ciftSayilar = list()
        tekSayilar = list()
        ciftSayilarToplami = 0
        tekSayilarToplami = 0

        x = func(arg)
        for num in arg:
            if int(num)%2 == 0:
                ciftSayilar.append(int(num))
                ciftSayilarToplami += int(num)
            else:
                tekSayilar.append(int(num))
                tekSayilarToplami += int(num)

        print("\nÇift sayılar toplamı:", ciftSayilarToplami, "|| Tek sayılar toplamı:", tekSayilarToplami)
        return x
    return wrapper

@ozelAritmatik
def aritmatikOrtalama(arg):
    toplam = 0
    for num in arg:
        try:
            num = int(num)
        except Exception as e:
            print("Yeniden düşünün. {} hatalı bir sayı.".format(num))
        else:
            toplam += num
    return toplam/len(arg)

## PROGRAM ##
print("""
    - Aristomatik -
    Aritmatik ortalamayı hesaplar, çıktı olarak verir.
""")
girdi = input("Sayıları virgül ile giriniz.")
girdi = list(girdi.split(","))
print("Girdiğiniz sayılar:", girdi)
snc = aritmatikOrtalama(girdi)
print("Aritmatik ortalamları:", snc)
