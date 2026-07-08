def add(a, b):
    return a + b

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = add(num1)

print("The result is:", result)

# 1) Das Problem liegt bei "add(num1)" auf Zeile 7. 
# Die Funktion erwartet 2 Argumente, bekommt aber nur "num1" als eines

# Error Meldung:
# Traceback (most recent call last):
#  File "/home/user/Downloads/t.py", line 7, in <module>
#    result = add(num1)
# TypeError: add() missing 1 required positional argument: 'b'

# Man kann es beheben indem man "add(num1)" auf "add(num1, num2)" ändert.