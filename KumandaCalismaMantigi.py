class Kumanda():
    def __init__(self, durum="kapalı", kanal_listesi=["trt", "star", "fox"], kanal="star", ses=0):
        self.durum = durum
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal
        self.ses = ses

    def __len__(self):
        print("Kanal sayısı {}, Ses seviyesi {}'dir.".format(len(self.kanal_listesi), self.ses))

    def __str__(self):
        print("Televizyonunuz şu an {}.\nSes seviyesi {}\nSon belirlenmiş kanal {}\nKanal listeniz ise {}".format(self.durum, self.ses, self.kanal, self.kanal_listesi))

    def __del__(self):
        print("Class silinmiştir.")

    def kapat(self):
        if (self.durum == "kapalı"):
            print("Televizyon halihazırda kapalıdır.")
        else:
            self.durum = "kapalı"
            print("Televizyon kapatılmıştır.")

    def kanal_degistir(self):
        istenilen = input("Hangi kanalı açmak istersiniz?\n 1: TRT\n 2: Star\n 3: Fox")
        istenilen = int(istenilen)
        if istenilen == 1:
            if istenilen != self.kanal:
                self.kanal = istenilen
                print("Kanalınız değiştirilmiştir.")
            else: print("Halihazırda o kanaldasınız.")

        if istenilen == 2:
            if istenilen != self.kanal:
                self.kanal = istenilen
                print("Kanalınız değiştirilmiştir.")
            else: print("Halihazırda o kanaldasınız.")

        if istenilen == 3:
            if istenilen != self.kanal:
                self.kanal = istenilen
                print("Kanalınız değiştirilmiştir.")
            else: print("Halihazırda o kanaldasınız.")

    def ses_degistir(self):
        girdi = input("Sesi arttırmak mı azaltmak mı istersiniz?\n + // -")
        if girdi == "+":
            self.ses += 1
        elif girdi == "-":
            self.ses -= 1
        else: print("Hop program buna ayarlanmadı!")

kumanda = Kumanda()

print("""
----------------------------------------------------
----------------------------------------------------
      ^^^^ Kumanda ile ilgili işlemler ^^^^
----------------------------------------------------
----------------------------------------------------

|||  1) Genel Bilgiler                            |||
|||  2) Kanal sayısı / Ses seviyesi               |||
|||  3) Kanal Değiştir                            |||
|||  4) Ses Değiştir                              |||
|||  q) Kapat                                     |||
|||  bırak) Kumanda işlemlerinden vazgeç          |||

----------------------------------------------------
----------------------------------------------------
-------------------- gokkoc. -----------------------
----------------------------------------------------
""")

while True:
    istek = input("İşlem giriniz: ")

    if istek == "1":
        print(kumanda)
    elif istek == "2":
        len(kumanda)
    elif istek == "3":
        kumanda.kanal_degistir()
    elif istek == "4":
        kumanda.ses_degistir()
    elif istek == "q":
        Kumanda.kapat()
    elif istek == "bırak":
        kumanda.kapat()
        print("Program kapatılıyor.")
        break
    else: print("Ne yaptın yahu?!")
