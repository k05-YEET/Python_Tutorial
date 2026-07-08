name = input ("Name des Monsters: ")

angriff = int(input("Angriff: "))
verteidigung = int(input("Verteidigung: "))

print()
print("Monster: ", name)

print("Gesamtstärke: ", angriff + verteidigung)
print("Unterschied: ", angriff - verteidigung)
print("Kampfkraft: ", angriff * verteidigung)
print("Division: ", angriff / verteidigung)
print("Rest: ", angriff % verteidigung)
print("Angriff: ", angriff ** 2)

print()

print("Angriff größer als Verteidigung?", angriff > verteidigung)
print("Angriff gleich Verteidigung?", angriff == verteidigung)
