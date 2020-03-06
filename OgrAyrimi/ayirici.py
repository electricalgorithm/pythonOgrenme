# -*- coding: utf-8 -*-

def ekle(x, y):
    file = open(x+".txt","a", encoding="utf-8")
    file.seek(2)
    file.write("İsim: " + y + "\n")
    file.close()


##### PROGRAM

anadallar = [] # Bütün anadalların toplanacağı liste

with open("ogr.txt", "r", encoding="utf-8") as dosya:
    icerik = dosya.read() # Dosyanın içindekileri okuttuk.
    liste = icerik.split("\n") # İçerikteki her bir satırı bir list-item olarak parçalattık.
    del liste[-1] # Sondaki boş itemi silmek için kullandık.

    for i in liste:
         # Her bir liste itemini kendi içinde parçalara ayırıp değişken atıyoruz.
        satir = i.split(",")
        isim = satir[0]
        anabilim = satir[1]

        # Anabilim eğer anadallar kategorisinde değilse eklemesini söyledik.
        # Ayrı anabilimlerin, ayrı dosyalara yazılmalarını sağlayıyoruz.
        if anabilim in anadallar:
            ekle(anabilim, isim)
            continue
        else:
            ekle(anabilim, isim)
            anadallar.append(anabilim)
            anadallar.sort()
