print("Program'a hoş geldiniz.")
liste = ["345","sadas","324a","14","kemal"]
cikti_liste = []
for e in liste:
    if (isinstance(e, str)):
        try:
            ekle = int(e)
            cikti_liste.append(ekle)
        except ValueError:
            continue
    else:
        cikti_liste.append(e)
print(cikti_liste)
