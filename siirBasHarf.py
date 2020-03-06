# -*- coding: utf-8 -*-

print(" Giriş başarılı. ")
cmd = input("Dosya ismi: ")

# Değişken atamaları
satirListesi = list()
harfListesi = list()
sonListe = list()

print("------------------------------------")
try:
    with open(cmd+".txt","r", encoding="utf-8") as dosya:
        satirListesi = dosya.read()
        satirListesi = satirListesi.split("\n")
        satirListesi.pop()

        for satir in satirListesi:
            harfListesi = list(satir)
            print(harfListesi[0])
    print("------------------------------------")
    print("Sistem kapanmıştır.")
except FileNotFoundError:
    print("Dosya bulunamadı.")
