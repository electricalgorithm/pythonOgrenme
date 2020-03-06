import sqlite3

## This file contains app's backgroud process.
## Translations have been done in main

class Product():

    def __init__(self):
        pass

    def addProduct(self, name, category, stock, price, barcode):
        with sqlite3.connect("productBase.db") as databaseConnection:
            cursor = databaseConnection.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS " + category + "(name TEXT, category TEXT, stock INT, price INT, barcode INT)")
            cursor.execute("SELECT * FROM {} WHERE name = '{}'".format(category, name))
            askedData = cursor.fetchall()
            if len(askedData) == 0:
                SQLcmd = "INSERT INTO " + category + " VALUES (?,?,?,?,?)"
                cursor.execute(SQLcmd, (name, category, stock, price, barcode))
            else: print("There's a product with that name. Please use update section.")

    def addStock(self, name, cat, stockNum):
        with sqlite3.connect("productBase.db") as databaseConnection:
            cursor = databaseConnection.cursor()
            cursor.execute("SELECT name, stock FROM {} WHERE name = '{}'".format(cat, name))
            askedData = cursor.fetchall()
            if len(askedData) == 0:
                print("Product not found.")
            else:
                print("Old stock:", askedData[0][1])
                try:
                    cursor.execute("UPDATE {} SET stock = {} WHERE name = '{}'".format(cat, int(stockNum)+int(askedData[0][1]), name))
                except sqlite3.OperationalError:
                    print("Something went wrong.")
                else:
                    databaseConnection.commit()
                    print("New stock:", int(askedData[0][1])+int(stockNum))

    def editProduct(self, name, category):
        with sqlite3.connect("productBase.db") as databaseConnection:
            cursor = databaseConnection.cursor()
            cursor.execute("SELECT * FROM {} WHERE name = '{}'".format(category, name))
            askedData = cursor.fetchall()
            if len(askedData) == 0:
                print("Product not found.")
            else:
                print("""
                | Product Details ------------------
                |   name =  {}
                |   category = {}
                |   stock = {}
                |   price = {}
                |   barcode = {}
                | ----------------------------------
                """.format(askedData[0][0], askedData[0][1], askedData[0][2], askedData[0][3], askedData[0][4]))
                print("Please reinput the correct data.")
                print("Note that, you can't change category.")
                inputOnname = input("> Name: ")
                inputOnstock = input("> Stock: ")
                inputOnprice = input("> Price: ")
                inputOnbarcode = input("> Barcode: ")
                cursor.execute("UPDATE {} SET name = '{}', stock = '{}', price = '{}', barcode = '{}' WHERE name = '{}'".format(category, inputOnname, inputOnstock, inputOnprice, inputOnbarcode, name))
                databaseConnection.commit()
                cursor.execute("SELECT * FROM {} WHERE name = '{}'".format(category, inputOnname))
                askedData = cursor.fetchall()
                print("""
                | (NEW) Product Details ------------
                |   name =  {}
                |   category = {}
                |   stock = {}
                |   price = {}
                |   barcode = {}
                | ----------------------------------
                """.format(askedData[0][0], askedData[0][1], askedData[0][2], askedData[0][3], askedData[0][4]))

    def raiseOrNeg(self, cat, cond, data, rate):
        rate = float(rate)
        with sqlite3.connect("productBase.db") as databaseConnection:
            cursor = databaseConnection.cursor()
            if data == "all" or cond == "all" :
                cursor.execute("SELECT name, price FROM {}".format(cat))
                askedData = cursor.fetchall()
                for index in askedData:
                    oldPrice = int(index[1])
                    newPrice = oldPrice + oldPrice*rate
                    cursor.execute("UPDATE {} SET price = '{}' WHERE name = '{}'".format(cat, newPrice, index[0]))
                    databaseConnection.commit()
            else:
                cursor.execute("SELECT name, price FROM {} WHERE {} = '{}'".format(cat, cond, data))
                askedData = cursor.fetchall()
                for index in askedData:
                    oldPrice = int(index[1])
                    newPrice = oldPrice + oldPrice*rate
                    cursor.execute("UPDATE {} SET price = '{}' WHERE {} = '{}' AND name = '{}'".format(cat, newPrice, cond, data, index[0]))
                    databaseConnection.commit()
