import sqlite3

# Veritabanı ile bağlantı kurulması
with sqlite3.connect("./databaseDosyalari/veritabaniIlkders.db") as db:
    print("Veritabanı bağlantısı kuruldu.")

    cr = db.cursor()
    try:
        cr.execute("CREATE TABLE kisiler(isim TEXT, soyisim TEXT, cinsiyet TEXT, cinselYonelim TEXT, dogumTarihi INT, girdiTarihi INT)")
    except sqlite3.OperationalError:
        print("### Tablo daha önceden yaratılmış. ###")
    else:
        print("### Tablo yaratıldı. ###")

    # Fonskiyonlar

    def veriEkle():
        print("--- VERİ EKLEME PANELİ ---")
        isim = input("İsim giriniz: ")
        soyisim = input("Soy isim giriniz: ")

        # Cinsiyet seçimi
        cinsiyet = input("Cinsiyeti seçiniz (1: Erkek, 2: Kadın): ")
        if cinsiyet == "1":
            cinsiyet = "Erkek"
        elif cinsiyet == "2":
            cinsiyet = "Kadın"
        else:
            print("### Hatalı bir kod girdiniz. ###")
            return False

        # Cinsel yönelim
        cinselYonelim = input("Cinsel yönelimi belirtiniz (1: Hetero, 2: Homo, 3: Bi, 4: A, 5: Trans, 0: Belirsiz): ")
        if cinselYonelim == "1":
            cinselYonelim = "Heteroseksüel"
        elif cinselYonelim == "2":
            cinselYonelim = "Homoseksüel"
        elif cinselYonelim == "3":
            cinselYonelim = "Biseksüel"
        elif cinselYonelim == "4":
            cinselYonelim = "Aseksüel"
        elif cinselYonelim == "5":
            cinselYonelim = "Transseksüel"
        elif cinselYonelim == "0":
            cinselYonelim = "Belirsiz"
        else:
            print("### Hatalı bir kod girdiniz. ###")
            return False

        dogumTarihi = input("Doğum tarihini giriniz: ")
        girdiTarihi = input("Girdi tarihini giriniz: ")
        try:
            cr.execute("INSERT INTO kisiler VALUES(?,?,?,?,?,?)", (isim, soyisim, cinsiyet, cinselYonelim, dogumTarihi, girdiTarihi))
            db.commit()
        except Exception as e:
            print("### Bir sorun oluştu! ###")
            return False
        else:
            print(" ### Veri başarı ile eklendi. ###")
            return True
    def veriOku(arg):
        if arg == "all":
            cr.execute("SELECT * FROM kisiler")
            return cr.fetchall()
        else:
            try:
                cr.execute("SELECT "+arg+" FROM kisiler")
            except sqlite3.OperationalError:
                print("İstenen veriler bulunamadı.")
                return False
            else:
                return cr.fetchall()
    def veriSorgula(col, data):
        try:
            cr.execute("SELECT * FROM kisiler WHERE "+col+" = "+"'"+data+"'")
        except sqlite3.OperationalError:
            print("Bir sorun oluştu. Sebebini biz de bilmiyoruz.")
            return False
        else:
            return cr.fetchall()
    def ozelKomut(sql,type):
        cr.execute(sql)
        if type == "alış":
            return cr.fetchall()
        elif type == "veriş":
            db.commit()
            return True


    # Programın kendisi
    print("""

     _______________________________________________________________
    |                                                               |
    | ### Gökhan Koçmarlı'nın Kişi Defteri                          |
    | Bu defter kişilerin akılda kalıcılığını arttırmak             |
    | amacı ile 15 Eylül'de oluşturulmuştur.                        |
    | Bu deftere erişim izniniz yok ise kullanmanız yasadışıdır.    |
    | _____________________________________________________________ |

    Komutlar:
                1 - Kişi ekleme
                2 - Kişi görüntüleme
                3 - Kişi sorgulama
                4 - Kişi silme/düzenleme
                4 - Özel SQL Komutu
                q - Çıkış
    """)

    while True:
        print("")
        print("")
        cmd = input(">>> Yapmak istediğiniz işlemi seçiniz: ")
        if cmd == "1":
            veriEklemeSonuc = veriEkle()
            if veriEklemeSonuc == "False":
                continue
            else:
                continue
        elif cmd == "2":
            okunacakVeri = input("""
Çekilebilir veriler: all, isim, soyisim, cinsiyet, cinselYonelim, dogumTarihi, girdiTarihi
>>> Hangi veriyi çekmek istersiniz? İki ve daha fazla veri seçmek için virgül kullanınız: """)
            veri = veriOku(okunacakVeri)
            if veri == False:
                continue
            else:
                for index in veri:
                    print(index)
        elif cmd == "3":
            sorgulanacakTur = input("""
Çekilebilir veriler: isim, soyisim, cinsiyet, cinselYonelim, dogumTarihi, girdiTarihi
>>> Hangi veri kümesinde sorgulamak istersiniz? """)
            aranacakVeri = input("Aranacak girdi: ")
            veri = veriSorgula(sorgulanacakTur, aranacakVeri)
            if veri == False:
                continue
            else:
                if len(veri) == 0:
                    print("Veri bulunamadı.")
                else:
                    for index in veri:
                        print(index)
        elif cmd == "4":
            sqlSorgusu = input("Sorguyu giriniz: ")
            sqlSorguTipi = input("Sorgu tipini giriniz: (alış, veriş)")
            fonksiyonCevap = ozelKomut(sqlSorgusu, sqlSorguTipi)
            if fonksiyonCevap == True:
                print("Komut işlenmiştir.")
            else:
                print("Komut işlenmiştir. Çıktısı aşağıdadır.\n")
                print(fonskiyonCevap)
        elif cmd == "q":
            print("Programdan çıkış yapılmıştır.")
            break
