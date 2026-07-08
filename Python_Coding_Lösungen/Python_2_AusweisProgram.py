# Frag den Benutzer für die notwendigen Informationen
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age in number representation: ")
height = input("Enter your height in metres: ")
hobby = input("Enter your favorite hobby: ")

# Kombiniere den vollen Namen
full_name = first_name + " " + last_name

username = first_name.lower() + "." + last_name.lower()

# Gebe den Ausweis im Terminal aus
print()
print("----- NAME BADGE -----")
print("Name:", full_name)
print("Age:", age)
print("Height:", height)
print("Hobby:", hobby)
print()

# Welcome message
print("Welcome,", full_name.upper() + "!")
print("Your name has", len(full_name) - 1, "letters.")
print("Your username is", username)