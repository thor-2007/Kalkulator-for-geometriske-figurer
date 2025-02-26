import math

    # Funksjoner for alle 2D dimensjonale figurer (Areal):
def startProgram():
    def arealFunksjoner():
        def arealRektangel():
            def spørOmMål():
                lengde = float(input("Hva er lengden?"))
                bredde = float(input("Hva er bredden?"))
                return lengde, bredde
            
            def regnAreal(lengde, bredde):
                areal = lengde * bredde
                return areal
            
            lengde, bredde = spørOmMål()
            areal = regnAreal(lengde, bredde)
            print(f"Arealet av rektangelet er {areal:.2f} måle-enhet^2")

        def arealKvadrat():
            def spørOmMål():
                side = float(input("Hva er siden?"))
                return side
            
            def regnAreal(side):
                areal = side * side
                return areal
            
            side = spørOmMål()
            areal = regnAreal(side)
            print(f"Arealet av kvadratet er {areal:.2f} måle-enhet^2")

        def arealTrekant():
            def spørOmMål():
                grunnlinje = float(input("Hva er grunnlinjen?"))
                høyde = float(input("Hva er høyden?"))
                return grunnlinje, høyde
            
            def regnAreal(grunnlinje, høyde):
                areal = (grunnlinje * høyde)/2
                return areal
            
            grunnlinje, høyde = spørOmMål()
            areal = regnAreal(grunnlinje, høyde)
            print(f"Arealet av trekanten er {areal:.2f} måle-enhet^2")

        def arealParallellogram():
            def spørOmMål():
                grunnlinje = float(input("Hva er grunnlinjen?"))
                høyde = float(input("Hva er høyden?"))
                return grunnlinje, høyde
            
            def regnAreal(grunnlinje, høyde):
                areal = grunnlinje * høyde
                return areal
            
            grunnlinje, høyde = spørOmMål()
            areal = regnAreal(grunnlinje, høyde)
            print(f"Arealet av parallellogrammet er {areal:.2f} måle-enhet^2")

        def arealTrapes():
            def spørOmMål():
                a = float(input("Hva er 'a' (den nederste delen)?"))
                b = float(input("Hva er 'b' (den øvereste delen?"))
                høyde = float(input("Hva er høyden?"))
                return a, b, høyde
            
            def regnAreal(a, b, høyde):
                areal = ((a+b)*høyde)/2
                return areal
            
            a, b, høyde = spørOmMål()
            areal = regnAreal(a, b, høyde)
            print(f"Arealet av trapeset er {areal:.2f} måle-enhet^2")

        def arealSirkel():
            def spørOmMål():
                radius = float(input("Hva er radiusen?"))
                return radius
            
            def regnAreal(radius):
                areal = math.pi * radius * radius
                return areal
            
            radius = spørOmMål()
            areal = regnAreal(radius)
            print(f"Arealet av sirkelen er {areal:.2f} måle-enhet^2")

        # Spør hvilke figur innenfor kategorien "areal" brukeren har lyst å finne.
        print(" ")
        print("1) Rektangel")
        print("2) Kvadrat")
        print("3) Trekant")
        print("4) Parallellogram")
        print("5) Trapes")
        print("6) Sirkel")
        print(" ")
        hvilkeFigur = input("Hvilken figur har du lyst å finne arealet til?  ('Skriv inn tall fra listen over')")

        if hvilkeFigur == "1":
            arealRektangel()
        elif hvilkeFigur == "2":
            arealKvadrat()
        elif hvilkeFigur == "3":
            arealTrekant()
        elif hvilkeFigur == "4":
            arealParallellogram()
        elif hvilkeFigur == "5":
            arealTrapes()
        elif hvilkeFigur == "6":
            arealSirkel()
        else:
            print("Du må skrive ett tall fra listen over, start programmet på nytt.")


    # Funksjoner for alle 2D dimensjonale figurer (Omkrets):

    def omkretsFunksjoner():
        def omkretsRektangel():
            def spørOmMål():
                lengde = float(input("Hva er lengden?"))
                bredde = float(input("Hva er bredden?"))
                return lengde, bredde
            
            def regnOmkrets(lengde, bredde):
                omkrets = 2 * (lengde + bredde)
                return omkrets
            
            lengde, bredde = spørOmMål()
            omkrets = regnOmkrets(lengde, bredde)
            print(f"Omkretsen av rektangelet er {omkrets:.2f} måle-enhet")

        def omkretsKvadrat():
            def spørOmMål():
                side = float(input("Hva er siden?"))
                return side
            
            def regnOmkrets(side):
                omkrets = 4 * side
                return omkrets
            
            side = spørOmMål()
            omkrets = regnOmkrets(side)
            print(f"Omkretsen av kvadratet er {omkrets:.2f} måle-enhet")

        def omkretsSirkel():
            def spørOmMål():
                radius = float(input("Hva er radiusen?"))
                return radius
            
            def regnOmkrets(radius):
                omkrets = 2 * math.pi * radius
                return omkrets
            
            radius = spørOmMål()
            omkrets = regnOmkrets(radius)
            print(f"Omkretsen av sirkelen er {omkrets:.2f} måle-enhet")

        # Spør hvilke figur innenfor kategorien "omkrets" brukeren har lyst å finne.
        print(" ")
        print("1) Rektangel")
        print("2) Kvadrat")
        print("3) Sirkel")
        print(" ")
        hvilkeFigur = input("Hvilken figur har du lyst å finne omkretsen til? ('Skriv inn tall fra listen over')")

        if hvilkeFigur == "1":
            omkretsRektangel()
        elif hvilkeFigur == "2":
            omkretsKvadrat()
        elif hvilkeFigur == "3":
            omkretsSirkel()
        else:
            print("Du må skrive ett tall fra listen over, start programmet på nytt.")


    # Funksjoner for alle 3D dimensjonale figurer (Volum):

    def volumFunksjoner():
        def volumFirkantetPrisme():
            def spørOmMål():
                høyde = float(input("Hva er høyden?"))
                lengde = float(input("Hva er lengden?"))
                bredde = float(input("Hva er bredden?"))
                return høyde, lengde, bredde
            
            def regnVolum(høyde, lengde, bredde):
                grunnflate = (lengde * bredde)
                volum = (grunnflate * høyde)
                return volum

            høyde, lengde, bredde = spørOmMål()
            volum = regnVolum(høyde, lengde, bredde)
            print(f"Volumet av firkantet prisme er {volum:.2f} måle-enhet^3")

        def volumAvSylinder():
            def spørOmMål():
                høyde = float(input("Hva er høyden?"))
                radius = float(input("Hva er radiusen?"))
                return høyde, radius
            
            def regnVolum(høyde, radius):
                grunnflate = (math.pi * radius * radius)
                volum = (grunnflate * høyde)
                return volum

            høyde, radius = spørOmMål()
            volum = regnVolum(høyde, radius)
            print(f"Volumet av sylinderen er {volum:.2f} måle-enhet^3")

        def volumAvTrekantetPyramide():
            def spørOmMål():
                høyde = float(input("Hva er høyden?"))
                grunnlinje = float(input("Hva er grunnlinja?"))
                return høyde, grunnlinje

            def regnVolum(grunnlinje, høyde):
                volum = (grunnlinje * høyde)/3
                return volum
            
            høyde, grunnlinje = spørOmMål()
            volum = regnVolum(høyde, grunnlinje)
            print(f"Volumet av trekantet pyramide er {volum:.2f} måle-enhet^3")

        def volumAvKule():
            def spørOmMål():
                radius = float(input("Hva er radiusen?"))
                return radius

            def regnVolum(radius):
                volum = (4/3)*(math.pi * radius**3)
                return volum
            
            radius = spørOmMål()
            volum = regnVolum(radius)
            print(f"Volumet av kulen er {volum:.2f} måle-enhet^3")

        def volumAvKjegle():
            def spørOmMål():
                radius = float(input("Hva er radiusen?"))
                høyde = float(input("Hva er høyden?"))
                return radius, høyde

            def regnVolum(radius, høyde):
                volum = (1/3)*(math.pi * radius**2 * høyde)
                return volum
            
            radius, høyde = spørOmMål()
            volum = regnVolum(radius, høyde)
            print(f"Volumet av kjeglen er {volum:.2f} måle-enhet^3")

        def volumAvTetraeder():
            def spørOmMål():
                side = float(input("Hva er lengden på en av sidene? "))
                return side

            def regnVolum(side):
                volum = (side**3) / (6 * math.sqrt(2))
                return volum
            
            side = spørOmMål()
            volum = regnVolum(side)
            print(f"Volumet av tetraederen er {volum:.2f} måle-enhet^3")

        def volumAvFirkantetPyramide():
            def spørOmMål():
                side = float(input("Hva er lengden på en side av kvadratet (grunnflate)? "))
                høyde = float(input("Hva er høyden på pyramiden? "))
                return side, høyde

            def regnVolum(side, høyde):
                volum = (1/3) * (side**2) * høyde
                return volum

            side, høyde = spørOmMål()
            volum = regnVolum(side, høyde)
            print(f"Volumet av firkantet pyramide er {volum:.2f} måle-enhet^3")

        def volumAvKube():
            def spørOmMål():
                side = float(input("Hva er lengden på en av sidene "))
                return side

            def regnVolum(side):
                volum = side**3
                return volum

            side = spørOmMål()
            volum = regnVolum(side)
            print(f"Volumet av kuben er {volum:.2f} måle-enhet^3")

        # Spør hvilke figur innenfor kategorien "volum" brukeren har lyst å finne.
        print(" ")
        print("1) Firkantet prisme")
        print("2) Sylinder")
        print("3) Trekantet pyramide")
        print("4) Kule")
        print("5) Kjegle")
        print("6) Tetraeder")
        print("7) Firkantet pyramide")
        print("8) Kube")
        print(" ")
        hvilkeFigur = input("Hvilken figur vil du finne volumet til? ('Skriv inn tall fra listen over')")

        if hvilkeFigur == "1":
            volumFirkantetPrisme()
        elif hvilkeFigur == "2":
            volumAvSylinder()
        elif hvilkeFigur == "3":
            volumAvTrekantetPyramide()
        elif hvilkeFigur == "4":
            volumAvKule()
        elif hvilkeFigur == "5":
            volumAvKjegle()
        elif hvilkeFigur == "6":
            volumAvTetraeder()
        elif hvilkeFigur == "7":
            volumAvFirkantetPyramide()
        elif hvilkeFigur == "8":
            volumAvKube()
        else:
            print("Error")


    # Funksjoner for alle 3D dimensjonale figurer (Overflateareal):

    def overflatearealFunksjoner():
        def overflatearealFirkantetPrisme():
            def spørOmMål():
                høyde = float(input("Hva er høyden?"))
                lengde = float(input("Hva er lengden?"))
                bredde = float(input("Hva er bredden?"))
                return høyde, lengde, bredde
            
            def regnOverflateareal(høyde, lengde, bredde):
                overflateareal = 2 * (lengde * bredde + lengde * høyde + bredde * høyde)
                return overflateareal
            
            høyde, lengde, bredde = spørOmMål()
            overflateareal = regnOverflateareal(høyde, lengde, bredde)
            print(f"Overflatearealet av firkantet prisme er {overflateareal:.2f} måle-enhet^2")

        def overflatearealSylinder():
            def spørOmMål():
                radius = float(input("Hva er radiusen?"))
                høyde = float(input("Hva er høyden?"))
                return radius, høyde
            
            def regnOverflateareal(radius, høyde):
                overflateareal = 2 * math.pi * radius * (radius + høyde)
                return overflateareal
            
            radius, høyde = spørOmMål()
            overflateareal = regnOverflateareal(radius, høyde)
            print(f"Overflatearealet av sylinderen er {overflateareal:.2f} måle-enhet^2")

        def overflatearealKule():
            def spørOmMål():
                radius = float(input("Hva er radiusen?"))
                return radius

            def regnOverflateareal(radius):
                overflateareal = 4 * math.pi * radius**2
                return overflateareal
            
            radius = spørOmMål()
            overflateareal = regnOverflateareal(radius)
            print(f"Overflatearealet av kulen er {overflateareal:.2f} måle-enhet^2")

        def overflatearealKube():
            def spørOmMål():
                side = float(input("Hva er lengden på en av sidene?"))
                return side

            def regnOverflateareal(side):
                overflateareal = 6 * (side**2)
                return overflateareal
            
            side = spørOmMål()
            overflateareal = regnOverflateareal(side)
            print(f"Overflatearealet av kuben er {overflateareal:.2f} måle-enhet^2")

        # Spør hvilke figur innenfor kategorien "overflateareal" brukeren har lyst å finne.
        print(" ")
        print("1) Firkantet prisme")
        print("2) Sylinder")
        print("3) Kule")
        print("4) Kube")
        print(" ")
        hvilkeFigur = input("Hvilken figur vil du finne overflatearealet til? ('Skriv inn tall fra listen over')")

        if hvilkeFigur == "1":
            overflatearealFirkantetPrisme()
        elif hvilkeFigur == "2":
            overflatearealSylinder()
        elif hvilkeFigur == "3":
            overflatearealKule()
        elif hvilkeFigur == "4":
            overflatearealKube()
        else:
            print("Error")


    #Starten av programmet som spør om jeg vil finne volum eller areal.

    #Dekorere terminalen:
    print(" ")
    print("Velkommen til geometri kalkulatoren.")
    print("Laget av Thor Alexander Ånderå den 26.02.2025")
    print("")
    print("Hvilke handling vil du gjøre? Venligst skriv ett tall fra listen under:")
    print("1) Areal")
    print("2) Omkrets")
    print("3) Volum")
    print("4) Overflateareal")
    print(" ")

    spørsmål = input("")

    if spørsmål == "1":
        arealFunksjoner()
    elif spørsmål == "2":
        omkretsFunksjoner()
    elif spørsmål == "3":
        volumFunksjoner()
    elif spørsmål == "4":
        overflatearealFunksjoner()
    else:
        print("Error")

startProgram()