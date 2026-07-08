import random

vorhersagen = [
    "Du bestehst die nächste Prüfung.",
    "Heute gibt es gratis Pizza.",
    "Dein WLAN wird genau dann ausfallen, wenn du es brauchst.",
    "Du findest heute 5 €.",
    "Heute solltest du besser keinen Kaffee trinken.",
    "Du wirst heute 3 Stunden auf TikTok verschwenden.",
    "Dein Code funktioniert beim ersten Versuch. (Sehr unwahrscheinlich.)"
]

name = input("Wie heißt du? ")

print(f"\nHallo {name}!")

weiter = "ja"

while weiter == "ja":
    print("\nDeine Vorhersage:")
    print(random.choice(vorhersagen))

    weiter = input("\nNoch eine Vorhersage? (ja/nein): ").lower()

print("\nScherz, du hast das doch nicht echt geglaubt, oder?")