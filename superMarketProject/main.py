import sMapp
import sqlite3

productBase = sMapp.Product()

print("""
     ________________________________
    |                                |
    |      = superiorSTOCK =         |
    |       version -- alpha         |
    |                                |
    |     Made your work easier.     |
    |________________________________|
    |                                |
    |   Menu:                        |
    |      - Product List       (L)  |
    |      - Add Product        (P)  |
    |      - Add Stock          (S)  |
    |      - Edit Product       (E)  |
    |      - Raise or Discount  (R)  |
    |      - Quit               (Q)  |
    |________________________________|


""")

# MAIN
while True:
    cmd = input("\n--> Please insert command letter: ")
    cmd = cmd.lower()

    #Command selector mechnaism
    if cmd == "q":
        print("Program has quitted.")
        break
    elif cmd == "l":
        print("""
     ------------------------------
     Product List:
     ------------------------------
        """)
    elif cmd == "p":
        print("""
    ------------------------------
    Product Adding Panel:
    ------------------------------
        """)
        pName = input("> Name: ")
        pCat = input("> Category: ")
        pStock = input("> Stock: ")
        pPrice = input("> Price: ")
        pBarcode = input("> Barcode: ")
        try:
            productBase.addProduct(pName, pCat, pStock, pPrice, pBarcode)
        except sqlite3.OperationalError:
            print("Something went wrong.")
        else:
            print("""
    ----- Product has added. -----
    ------------------------------
            """)
    elif cmd == "s":
        print("""
    ------------------------------
    Stock Adding Panel:
    ## You can write negative numbers as adding number.
    ------------------------------
        """)
        sName = input("> Name: ")
        sCat = input("> Category: ")
        sNum = input("> Adding Number: ")
        try:
            productBase.addStock(sName, sCat, sNum)
        except sqlite3.OperationalError:
            print("Something went wrong.")
        else:
            print("""
    ----- Stock has changed. -----
    ------------------------------
            """)
    elif cmd == "e":
        eName = input("> Name: ")
        eCate = input("> Category: ")
        try:
            productBase.editProduct(eName, eCate)
        except sqlite3.OperationalError:
            print("Something went wrong.")
        else:
            print("""
    ----- Product has edited. -----
    ------------------------------
            """)
    elif cmd == "r":
        rCat = input("> Category: ")
        rCon = input("> Condition: ")
        rData = input("> Condition equals to: ")
        rRatio = input("> Ratio: ")
        productBase.raiseOrNeg(rCat, rCon, rData, rRatio)
        print("""
    ----- Rai/Dis has made.  -----
    ------------------------------
        """)
    else:
        print("Wrong commend letter. Try again.")
