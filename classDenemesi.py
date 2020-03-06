class Yazılımcı():
    def __init__(self, isim, soyisim, numara, maaş, diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.maaş = maaş
        self.diller = diller

    def printIt(self):
        print("""
        İ:{}
        S:{}
        N:{}
        M:{}
        D:{}
        """.format(self.isim, self.soyisim, self.numara, self.maaş, self.diller))


aa = Yazılımcı("Gö", "Ko", 12345, 1000, ("P", "C"))
aa.printIt()

"""
Bİr kızın problemi için aldım kodu
"""
