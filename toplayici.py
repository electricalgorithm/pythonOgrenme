print("""

Toplayıcı'ya hoş geldiniz!
Bu programın tek amacı,
girdiğiniz sayıları sonsuza kadar toplamaktır.
Çıkış yapmak için "q" basınız.

""")

toplam = 0

while True:
    girdi = input("Eklenecek sayıyı giriniz: ")

    if girdi == "q":
        break
    elif girdi == "":
        print("Yeniden giriniz.")
    else:
        girdi = int(girdi)
        print("""
        Eklenecek sayı: {}
        Önceki toplam: {}
        Sonraki toplam: {}
        """.format(girdi, toplam, toplam+girdi))
        toplam += girdi
