print("Program başladı.")


def askTheData(func):
    def wrapper():
        data1 = input("Data1: ")
        data2 = input("Data2: ")

        end = func(data1, data2)

        print("Fonksiyona çalışma isteği gönderildi.")
        return end
    return wrapper

@askTheData
def fonksiyon(*args):
    print("Fonksiyon çalıştırıldı.")
    print(args)

fonksiyon()
