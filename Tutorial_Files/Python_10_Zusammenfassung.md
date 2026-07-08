## We came so far

Durchatmen.

Fast geschafft. :D

Lasst uns nochmal alles recappen und die Best-Practises anschauen.

Hier gibt es keine Aufgabe mehr. Die Welt ist jetzt deine Aufgabe.

Hast du einen Anwendungsfall für Python? Dann ist das deine Aufgabe. Gehe dahin, Soldat.

<img width="875" height="595" alt="image" src="https://github.com/user-attachments/assets/b87a9c3b-6624-440d-b2ec-868be03f4e5c" />

(Bildquelle: [pt.memedroid.com](https://pt.memedroid.com/memes/detail/3953834/SQL-PYTHON-DATAFRAME))

## Zusammengefasst…

Das solltest du jetzt können!

### Datentypen

Python besitzt verschiedene Datentypen.

| Datentyp | Beispiel    |
|----------|-------------|
| Integer  | 5           |
| Float    | 3.14        |
| String   | “Hallo”     |
| Boolean  | True, False |
| Liste    | \[1,2,3\]   |

Beispiel:

```python
zahl = 5  
preis = 3.99  
name = "Max"  
aktiv = True
```

---

### 

Variablen

Variablen speichern Werte.

```python
name = "Anna"  
alter = 20  
  
print(name)  
print(alter)
```

---

### 

Ein- und Ausgabe

```python
name = input("Name: ")  
  
print("Hallo", name)
```

---

### 

Operatoren

#### Arithmetische Operatoren

```python
+ # Addition  
- # Subtraktion  
* # Multiplikation  
/ # Division  
// # Ganzzahldivision  
% # Rest  
** # Potenz
```

#### 

Vergleichsoperatoren

```python
==  
!=  
<  
<=  
>  
>=
```

#### 

Logische Operatoren

```python
and  
or  
not
```

### Bedingungen

```python
alter = 18  
  
if alter >= 18:  
 print("Volljährig")  
else:  
 print("Minderjährig")
```

#### 

Mehrere Bedingungen

```python
note = 2  
  
if note == 1:  
 print("Sehr gut")  
elif note == 2:  
 print("Gut")  
else:  
 print("Andere Note")
```

### 

Schleifen

#### for-Schleife

```python
for i in range(5):  
 print(i)
```

#### while-Schleife

```python
zahl = 1  
  
while zahl <= 5:  
 print(zahl)  
 zahl += 1
```

---

### 

Funktionen

```python
def begruessung(name):  
 print("Hallo", name)  
  
begruessung("Max")
```

#### 

Mit Rückgabewert

```python
def addieren(a, b):  
 return a + b  
  
ergebnis = addieren(4, 6)
```

#### 

Listen

```python
obst = ["Apfel", "Birne", "Banane"]  
  
print(obst[0])  
  
obst.append("Orange")
```

### 

Debugging

Der Debugger hilft beim Finden von Fehlern.

Wichtige Tasten:

| Taste       | Funktion                              |
|-------------|---------------------------------------|
| F5          | Debugger starten                      |
| F10         | Step Over (Eine Zeile weiter)         |
| F11         | Step Into (in die Funktion reingehen) |
| Shift + F11 | Step out (aus der Funktion rausgehen) |

Verwende Breakpoints, um dein Programm Zeile für Zeile auszuführen.

---

### Fehlerbehandlung

```python
try:  
 zahl = int(input())  
  
except ValueError:  
 print("Bitte eine Zahl eingeben.")  
  
finally:  
 print("Programm beendet.")
```

---

### 

Module

Module erweitern Python um zusätzliche Funktionen.

```python
import random  
  
print(random.randint(1,10))
```

Oder

```python
from math import sqrt  
  
print(sqrt(25))
```

### 

Häufig verwendete Funktionen

```python
len()  
input()  
print()  
range()  
int()  
float()  
str()  
type()
```

## Best Practises

Programme sollen nicht nur funktionieren, sondern auch leicht lesbar und wartbar sein.

Diese Regeln helfen dir dabei.

---

### Aussagekräftige Variablennamen

Schlecht

```python
x = 5
y = 20
```

Besser

```python
anzahl_studenten = 5
gesamtpreis = 20
```

Schon nach einigen Tagen weißt du sonst oft nicht mehr, was `x` eigentlich bedeutet.

---

### Keine kryptischen Abkürzungen

Schlecht

```python
gp = 25
```

Besser

```python
gesamtpreis = 25
```

---

### Kommentare sinnvoll einsetzen

Kommentare erklären **warum** etwas gemacht wird.

Nicht **was** passiert.

Schlecht

```python
# Variable auf 0 setzen
summe = 0
```

Gut

```python
# Summe für alle Bestellungen speichern
summe = 0
```

---

### Funktionen klein halten

Wenn eine Funktion mehrere Bildschirme lang wird, sollte sie meistens aufgeteilt werden.

Gut

```python
def berechne_preis():
    ...

def drucke_rechnung():
    ...
```

---

### Doppelten Code vermeiden

Schlecht

```python
print("Hallo Max")
print("Hallo Anna")
print("Hallo Peter")
```

Besser

```python
def begruessung(name):
    print("Hallo", name)

begruessung("Max")
begruessung("Anna")
begruessung("Peter")
```

---

### Einrückungen beachten

Python verwendet Einrückungen zur Strukturierung.

Falsch

```python
if zahl > 5:
print("Hallo")
```

Richtig

```python
if zahl > 5:
    print("Hallo")
```

---

### Nicht alles mit try/except lösen

Schlecht

```python
try:
    ...
except:
    pass
```

Fehler verschwinden dadurch einfach.

Fange nur Fehler ab, die tatsächlich auftreten können.

---

### Debugger statt viele print()

Viele Anfänger machen das:

```python
print(x)
print(y)
print(z)
```

Für kleine Programme ist das in Ordnung.

Bei größeren Programmen hilft der Debugger deutlich mehr.

---

### Code ordentlich formatieren

Leerzeilen helfen beim Lesen.

Schlecht

```python
name=input()
alter=int(input())
print(name)
print(alter)
```

Besser

```python
name = input()

alter = int(input())

print(name)
print(alter)
```

---

### Magic Numbers vermeiden

Schlecht

```python
preis = menge * 7
```

Woher kommt die 7?

Besser

```python
PREIS_PRO_STUECK = 7

preis = menge * PREIS_PRO_STUECK
```

---

### Programme testen

Probiere nicht nur "normale" Eingaben aus.

Teste auch:

- 0
- negative Zahlen
- sehr große Zahlen
- falsche Eingaben
- leere Eingaben

---

### Fehlermeldungen lesen

Viele Anfänger ignorieren Fehlermeldungen.

Dabei verrät Python meistens bereits:

- welche Datei betroffen ist
- in welcher Zeile der Fehler liegt
- welcher Fehlertyp aufgetreten ist

Lies Fehlermeldungen daher immer vollständig.

---

### Schrittweise entwickeln

Schreibe nicht 200 Zeilen Code auf einmal.

Arbeite lieber in kleinen Schritten:

1. Eine Funktion schreiben.
2. Testen.
3. Nächste Funktion schreiben.
4. Wieder testen.

So lassen sich Fehler deutlich schneller finden.

---

### Hab keine Angst vor Fehlern

Jeder Programmierer macht Fehler – auch Profis.

Fehlermeldungen gehören zum Programmieren dazu. Sie helfen dir dabei, deinen Code zu verbessern und neue Dinge zu lernen.

Mit etwas Übung wirst du viele Fehler schon erkennen, bevor du das Programm startest.

---

### Die 10 wichtigsten Regeln

Hier eine Checklist, die dir am Anfang helfen kann

Ich habe:  
- [ ] Aussagekräftige Variablennamen  
- [ ] Funktionen klein gehalten  
- [ ] Doppelten Code vermieden  
- [ ] Einrückungen korrekt genutzt  
- [ ] Einen Debugger genutzt (keine print() Statements für Troubleshooting im Code)  
- [ ] Erwartbare Fehler mit `try / except` abgefangen  
- [ ] Mir Fehlermeldungen aufmerksam durchgelesen und auf die Fehler korrekt reagiert  

Mein Code ist:
- [ ] Gut lesbar  
- [ ] Getestet, auch mit Fällen die zu Fehler führen könnten  

Falls du das alles drinnen hast ist jetzt nur mehr Üben wichtig.

Immerhin kann man auch keine Schlangen über nacht zähmen - noch viel weniger eine Python.
