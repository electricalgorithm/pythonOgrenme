print("Sisteme giriş başarılı.")
print("---")
ePostaListesi = list()
eKarakter = list()
postalar = list()
cmd = input("Dosya /txt/ adını giriniz: ")
try:
    with open(cmd+".txt", "r", encoding="utf-8") as dosya:
        ePostaListesi = dosya.read()
        ePostaListesi= ePostaListesi.split("\n")
        ePostaListesi.pop()
        for index in ePostaListesi:
            dogrulamaKodu = int()
            eKarakter = list(index)
            if ("@" in eKarakter):
                dogrulamaKodu = dogrulamaKodu + 1
            if ("." in eKarakter):
                dogrulamaKodu = dogrulamaKodu + 1
            if dogrulamaKodu == 2:
                postalar.append(index)
except FileNotFoundError:
    print("Dosya bulunmadı.")
print(postalar)
