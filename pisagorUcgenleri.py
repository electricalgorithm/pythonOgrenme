print("""

===================================
            ----
Pisagor Üçgen Bulucu:
Bir sayı girin ve bütün üçgenleri gösterelim.
            ----
===================================


""")

son = input("Sayı gir:")
son = int(son)

liste = list(range(1,son+1))

for a in liste:
    for b in liste:
        for c in liste:
            if (a**2) + (b**2) == (c**2):
                print("{}^2 + {}^2 = {}^2".format(a,b,c))
