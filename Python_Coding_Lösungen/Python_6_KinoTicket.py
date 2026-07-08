# Das Alter der Person (kann testweise verändert werden)

alter = int(input("Gebe das alter ein:\\n\\n"))

# Die Überprüfung der Bedingungen

if alter < 12:

    preis = 5

    print(f"Kinder-Ticket: Das Ticket kostet {preis} Euro.")

elif alter < 26:

    # Greift nur, wenn das Alter NICHT unter 12 ist, aber unter 26

    preis = 8

    print(f"Jugend-Ticket: Das Ticket kostet {preis} Euro.")

elif alter >= 65:

    preis = 7

    print(f"Senioren-Ticket: Das Ticket kostet {preis} Euro.")

else:

    # Greift für alle zwischen 26 und 64 Jahren

    preis = 11

    print(f"Standard-Ticket: Das Ticket kostet {preis} Euro.")