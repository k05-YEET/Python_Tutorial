def preis_berechnen(gericht):
    if gericht == "bigmac":
        return 4.50
    elif gericht == "mcflurry":
        return 3.20
    elif gericht == "pommes":
        return 2.50
    else:
        return -1


try:
    anzahl = int(input("Wie viele Personen bestellen? "))

    gesamtpreis = 0

    for i in range(anzahl):
        print(f"\nBestellung {i + 1}")

        name = input("Name: ")
        gericht = input("Gericht (BigMac, McFlurry oder Pommes): ").lower()

        preis = preis_berechnen(gericht)

        if preis == -1:
            print("Dieses Gericht gibt es leider nicht.")
        else:
            gesamtpreis += preis
            print(f"{name} bestellt einen {gericht.title()} für {preis:.2f} €.")

    print("\n---------------------------")
    print(f"Heute haben {anzahl} Personen bestellt.")
    print(f"Gesamtpreis: {gesamtpreis:.2f} €")

except ValueError:
    print("Fehler: Bitte eine gültige Zahl eingeben.")

finally:
    print("\nProgramm beendet. Vielen Dank!")