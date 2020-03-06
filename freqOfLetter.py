# -*- coding: utf-8 -*-
#!/usr/bin/env python3

# Main purpose of this application is finding frequancy of letters in a text.
# You can use it for your researchs and languange analyses.

# Use the code wisely and open.
# Thank you for partipication.

#Functions
def mainMenu():
    print("""
-------------------------------------------------------------------------------
                     _______________________________________
                    |                                       |
                    |        Welcome to freqText            |
                    | We make the text more understandible. |
                    |                                       |
                    |       version date: 10.2019.4         |
                    |_______________________________________|

                    // Usage:
                        Main Panel: m (universal)
                        Begin: b
                        Quit: q (universal)

                    // Universal codes:
                        Universals means that they can
                        be used any command panel.

                    // Output:
                        The data output will be an txt file.
                        In the same folder within application.

-------------------------------------------------------------------------------
    """)
def analyze(arg, out):
    listOfChars = [" ", "!", "^", "+", "%", "&", "/", "(", ")", "=", "?", "-",
    "#", "$", "½", "¾", "{", "[", "]","}", "*", "|", "~", "´", ",", ";", ".", ":",
    "@", "\n", "'", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    onlyLettersList = list()
    setsOfLetters = set()
    freq = dict()
    # We try if it's a file there or not.
    try:
        with open(arg + ".txt", "r", encoding="utf-8") as textFile:
            # We save the txt file as listOfLetters list.
            textBook = textFile.read()
            textBook = textBook.lower()
            listOfLetters = list(textBook)
            # For every character in that list, we make sure it's alphabetics.
            # And if it is, we send it to another list.
            for i in listOfLetters:
                if (i in listOfChars): continue
                else: onlyLettersList.append(i)
        onlyLettersList.sort()
    except FileNotFoundError:
        print("\nHey sorry!")
        print("There is no such file called {}.txt.".format(arg))

    else:
        # Making the statitics
        for letter in onlyLettersList:
            # print("İşlem başlatıldı:", letter) || Control Point
            # print("setsOfLetters: ", setsOfLetters) || Control Point
            if letter in setsOfLetters:
                # print(" + in the list.") || Control Point
                freq[letter] = freq[letter] + 1
                # print("freq[q] value:", freq[letter]) || Control Point
            else:
                # print(" - not in the list") || Control Point
                setsOfLetters.add(letter)
                freq[letter] = 1
                # print("freq[q] değeri", freq[letter]) || Control Point

        # Sorting the freq.
        orderedFreq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        # First, sec and third:
        firstLetter = orderedFreq[0][0]
        secLetter = orderedFreq[1][0]
        thirdLetter = orderedFreq[2][0]

        # Statics panel
        print("""

                ____________________________________
               |                                    |
               |    in that List,                   |
               |    we have found {} letters        |
               |    and these are the most          |
               |    used letters in the text.       |
               |    first one: {}                    |
               |    second one: {}                   |
               |    third one: {}                    |
               |                                    |
               |    You can see a list bellow of    |
               |    the statics of letter's repe-   |
               |    tation.                         |
               |____________________________________|

               Statics: """.format(
               len(onlyLettersList),
               firstLetter,
               secLetter,
               thirdLetter))

        for (index, value) in orderedFreq:
            print("""
                # Letter: {} ---> {} times used.
            """.format(index, value), end="")

        # For saving process
        try:
            with open(out + ".txt", "w", encoding="utf-8") as outputFile:
                outputFile.write("""
                    #### LETTER STATICTS OF {}.txt ###

                    Version: 10.2019.4
                    Letter count: {}
                    """.format(arg, len(onlyLettersList)))
                for (i, v) in orderedFreq:
                    outputFile.write("""
                    # Letter: {} ---> {} times used.""".format(i, v))
                outputFile.write("\n                    ### Staticts ended ###\n")
        except:
            print("Saving process has failed. Please save it via copying before closing the application.")


# Main program
mainMenu()
while True:
    # Command input section, opt: b,m,q
    cmd = input("\n>>>>> Insert your command: ")
    # Analyze process
    if cmd == "b":
        print("\nNote: You must place your txt file in application's folder.")
        textLocation = input(">>>>> Enter the name of txt file. (no txt end of it): ")
        print("\nOkey,")
        outputLocation = input(">>>>> Enter the name of OUTPUT txt file: ")
        # Starting the process
        analyze(textLocation, outputLocation)
    elif cmd == "q": # Quiting
        print("\nSee you in another file!")
        break
    elif cmd == "m": mainMenu() # Main panel
    else: print("Command has not found.")
