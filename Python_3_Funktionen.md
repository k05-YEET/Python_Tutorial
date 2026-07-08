## Allgemeines

[Funktionen](https://www.w3schools.com/python/python_functions.asp).

Im Grunde ist eine Funktion ein Code Block. Man kann sie aufrufen und Argumente übergeben.

> Vergleich: Eine Funktion ist wie eine Kaffemaschiene (ja echt jetzt)
>
> - Du drückst einen Knopf (= “Function Call”)
> - Die Maschine arbeitet
> - Kaffee kommt als Ergebnis zurück (= “result”, “return”)

In den vorigen Übungen hast du Funktionen bereits verwendet. 

Funktionen werden so dargestellt:

```python
funktionsname()
```

Das bedeutet du hast schon folgende Funktionen angewandt:

```python
print("wassup")
name = input("Dein Name bitteschön")
length = len(name)
```

Das Beste an Funktionen? Du kannst sie selbst schreiben und definieren was darin passiert.

## Python Funktionen

Eine Funktion muss man zuerst definieren, wo das im Code machst ist in dieser Sprache irrelevant. Dafür benutzt du das Keywort “def”.

```python
def say_hello():
			print("hi!")
```

Etwas das wichtig ist hier ist die Verschiebung zwischen def und print. Print ist eingerückt. Aber warum?

In Python eröffnet der Doppelpunkt (“:”) eine unsichtbare Klammer. Alles was danach kommt gehört zur Funktion - *es sei denn* die Linie startet wieder auf der gleichen Höhe wie die mit “def”, d.h. nicht mehr eingerückt (machbar via [Tabulator Taste](https://en.wikipedia.org/wiki/Tab_key) auf der Tastatur) ist.

```python
def say_hello():
			print("hi!")

print("Ich gehöre nicht mehr zur Funktion say_hello()")
```

Du kannst deine selbstgemachte Funktion dann von überall aufrufen.

```python
def say_hello():
			print("hi!")

say_hello() # Das ruft die Funktion auf
```

### Parameter

Nun, eine Funktion kann man dynamisch rechnen oder arbeiten lassen wenn man die wichtigen Parameter mit übergeben kann. Wenn diese als Platzhalter agieren nennt man sie “[Parameter](https://www.w3schools.com/python/python_arguments.asp)”.

Das ist relativ einfach:

```python
def greet(name):
			print("Hello", name)
```

Ohne irgendetwas wäre “name” noch nie definiert worden. Das muss die Variabel auch nicht! Hier handelt es sich um etwas das wir “Platzhalter” nennen. Die Variabel bleibt leer und undefiniert bis die Funktion mit einem Wert aufgerufen wird. 

Rufen wir die Funktion einmal mit Eingabe vom Benutzer auf.

```python
def greet(name):
			print("Hello", name)

greet(input("Wie heißt du? "))
```

Wenn der Benutzer jetzt “Leon Kennedy” eingibt sollte “Hello Leon Kennedy” ausgegeben werden.

### Argumente

Das was man beim aufrufen einer Funktion in die Klammern (“()”) schreibt oder übergibt.

```
def greet(name): # <-- Name ist ein Parameter
			print("Hello", name)

greet("Spiderman") # <-- Spiderman ist ein Argument
```

Hier handelt es sich grundsätzlich nur um Begriffe. Argumente und Parameter sind [nicht das gleiche](https://www.w3schools.com/python/python_arguments.asp#:~:text=Parameters%20vs%20Arguments).

### Returns

> “It's more blessed to give than to receive - especially kittens." - Bill Cosby

Man kann nicht nur Argumente mit übergeben, sondern auch etwas aus einer Funktion zurück bekommen. Das ist sehr praktisch, vor allem bei Rechenoperationen.  Das macht man wenn man die Funktion beenden will am ende mit dem Keyword “[return](https://www.geeksforgeeks.org/python/python-return-statement/)”.

Hier ein Beispiel:

```python
def addition(a, b):
			return a + b # Man kann auch einen Befehl statt eine Variabel zurück geben
```

So rufst du sie dann auf:

```python
ergebnis = addition(2, 5)
print("2 Plus 5 ergibt:", ergebnis)

def addition(a, b):
			return a + b # Man kann auch einen Befehl statt eine Variabel zurück geben
```

## Wann machen Funktionen auch wirklich Sinn?

Sicher, man kann für jede Operation eine eigene Funktion schreiben, aber das macht den Code lang und unleserlich. Hier sind Anwendungsbeispiele, wo es sich allerdings lohnt eine extra Funktion zu definieren und zu verwenden:

- Du verwendest eine Reihe an Codezeilen (die gleichen) immer wieder
- Der Codeblock hat eine klar definierte Aufgabe (Addieren, Subtrahieren, Daten einlesen, …)
- Du willst, dass dein Code leicht zu überblicken ist
- Spezielle Sicherheitsgründe ([global](https://stackoverflow.com/questions/27930038/how-to-define-global-function-in-python) and [private](https://www.geeksforgeeks.org/python/private-methods-in-python/), **für dich noch nicht wichtig**)

… wann sollte man dann auf keinen Fall extra Funktionen für etwas machen?

- 1-3 Linien Code
- Wenn es den Code unnötig kompliziert macht
- Der Code nur einmal aufgerufen wird

## Aufgabe

Schreibe ein Programm das folgendes macht:

> 1\.  Den Benutzer um eine Eingabe von 2 ganzen Nummern bittet      
> 2. Erstelle jeweils eigene Funktionen und gebe dann die Ergebnisse bezogen auf die Nummern aus:  
>       - Addition  
>       - Subtraktion    
>       - Multiplikation    
> 3. Das Ergebnis ausgibt

Versuche es erst wie einen simplen Taschenrechner aufzubauen im Kopf.     
Der Output sollte am Ende ca so aussehen:

```
Bitte die erste ganze Zahl eingeben: 2
Bitte die zweite ganze Zahl eingeben: 3

Ergebnisse:
Addition: 5.0
Subtraktion: -1.0
Multiplikation: 6.0
```

## Aufgabe 2

Leider ist man nicht immer der Autor eines Codes, aber es funktioniert dennoch etwas nicht.

In dem Folgenden Code hat sich ein Fehler eingeschlichen:

```python
# Addition program
def add(a, b):
    return a + b

num1 = float(input("first number: "))
num2 = float(input("second number: "))

result = add(num1)

print("The result is:", result)
```

- [ ] Kannst du das Problem erkennen?
- [ ] Welche Fehlermeldung gibt dir Python wenn du den Code trotzdem ausführst in VS Code?
- [ ] Wie richtest du das Problem, sodass der Code das macht was er sollte?