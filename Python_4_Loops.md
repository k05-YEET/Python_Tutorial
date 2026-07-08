## Allgemeines

> “Not all chains are metal. Not all cages have locks.” - N. von Wolf, The Chain Loop

Schleifen (oder Loops) sind in der Programmierung Kontrollstrukturen. In ihnen können Codeblöcke wiederholt ausgeführt werden, Zeit abgewartet werden, gezählt werden und so weiter.

Man verwendet sie um Aufgaben zu wiederholen, bis eine festgelegte Bedingung für einen Abbruch erfüllt wurde.

### Wann braucht man Schleifen?

- Unbekannte Anzahl von Wiederholungen sind nötig (bspw.: Datenverarbeitung, Social-Media Feed laden, …)
- Automatisierte Datenverarbeitung (Arrays/Listen) (Anwendung auf viele Files oder große Datenmengen)
- Dauerhafte Status-Abfragen (Event-Loops) (Programm soll endlos laufen, jede Sekunde etwas abfragen, …)
- Validierung von Eingaben (bspw.: Benutzer soll Zahl eingeben gibt aber nur Buchstaben ein ⟶ soll solange abgefragt werden bis eine Zahl kommt)

… und wann definitiv *nicht*?

- Feste, lineare Abläufe (bspw.: Datenbank öffnen, schreiben und schließen)
- Einfache Fehlerunterscheidungen (if / else, dazu mehr später)
- Mathematische Berechnungen mit Formeln wenn eine direkte Berechnung möglich ist
- Es sich um Zeitkritische Abläufe handelt (Jeder Loop verbraucht Zeit in Millisekunden)
- Verfügbarkeit von Vektor-Operationen  (Unwichtig für dich erstmal)
- Existenz von eingebauten Funktionen die die Aufgabe eines Loops bereits übernehmen würden

## Die wichtigsten Schleifen in Python

### 1) [for](https://www.w3schools.com/Python/python_for_loops.asp) Loop

Die For-Schleife ist dafür gedacht über eine Variable zu “[iterieren](https://www.dwds.de/wb/iterieren#:~:text=besonders%20Mathematik)”. Das bedeutet, dass man Positionsbezogen eine Variabel durchgehen kann, sie mehrmals verändern sodass die Bedingung erfüllt ist oder sie hochzählen.

Das klingt erstmal kompliziert… also nochmal kurz gefasst:

::: info
“Eine For-Schleife in Python wird verwendet, um eine Sequenz (wie eine Liste, ein Tupel oder einen String) Element für Element zu durchlaufen. Für jeden Eintrag wird der definierte Code-Block einmal ausgeführt, was sich ideal zur Automatisierung wiederkehrender Aufgaben eignet.” - Definition laut [IONOS.at](https://www.ionos.at/digitalguide/websites/web-entwicklung/for-loop-in-python/)

:::

Aber das versteht man besser wenn man sich einen Code dazu anschaut. Es gibt mehrere Arten eine For-Schleife zu verwenden:

1. Simples Zählen via Variabel “i”

```python
for i in range(1, 6):
    print(i)
```

Output:

```
1
2
3
4
5
```

Na, verwirrt?  
Verständlich. Auf den ersten Blick schaut es so aus, als ob “i” bis 6 geht. Aber das ist nicht ganz richtig, schauen wir uns doch die Schleifen-Definition genauer an!

```Python
for i in range(1, 6):
# Übersetzt: Zähle "i" von 1 solange, bis du auf die Zahl 6 kommst.
 
# Wenn i = 6, breche ab und führe die Schleife nicht mehr aus.

# Nachdem die Schleife 5 mal durchlaufen ist springt "i" auf
# 6 um, und die Schleife wird nicht noch einmal ausgeführt.
```

Das kann man mit etwas Experimentieren im Terminal selbst besser beobachten.

1. Ausgeben von einer Liste mit Elementen

```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
```

Output:

```
apple
banana
cherry
```

For-Schleifen kann man an jeden Datentyp direkt anpassen. Das merkt man am Besten in der Praxis!

### 2) While Loop

Die [While-Schleife](https://www.w3schools.com/python/python_while_loops.asp) ist simpel - bleib in diesem Codeblock solange, bis die angegebene Bedingung erfüllt wurde.

Schauen es uns wir anhand eines Beispiels an:

```python
i = 1
while i < 6:
  print(i) # den Inhalt von "i" in der Konsole ausgeben
  i += 1 # +1 zu "i" dazu
```

Sobald “i” den Wert 5 erreicht hat wird die Schleife abgebrochen.  
Warum?

```python
while i < 6
# i muss kleiner als 6 sein
# aufgeschlüsselt heißt das, dass i folgende Werte erreichen kann:
# 1, 2, 3, 4, 5
```

Natürlich gibt es auch für while loops mehrere Ausführungen, ähnlich wie bei for.

### Aufgabe

Wie funktionieren Passwort Abfragen?

Ziemlich einfach. Ohne [Timeout](https://unix.stackexchange.com/questions/382060/change-default-sudo-password-timeout), das das Gerät schützt, fragt man einfach so lange bis das Passwort 1:1 übereinstimmt.

Schreibe ein Programm, dass solange läuft bis der Benutzer “python” eingibt. Wenn die Eingabe falsch war gib “Wrong password.” und danach “Try again: “ aus.