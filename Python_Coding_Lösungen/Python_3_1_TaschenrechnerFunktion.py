# Funktion, die zwei Zahlen addiert
def add(a, b):
    return a + b

# Funktion, die zwei Zahlen subtrahiert
def subtract(a, b):
    return a - b

# Funktion, die zwei Zahlen multipliziert
def multiply(a, b):
    return a * b


# Dein Hauptprogramm
num1 = float(input("Bitte die erste ganze Zahl eingeben: "))
num2 = float(input("Bitte die zweite ganze Zahl eingeben: "))

print()
print("Ergebnisse:")
print("Addition:", add(num1, num2))
print("Subtraktion:", subtract(num1, num2))
print("Multiplikation:", multiply(num1, num2))