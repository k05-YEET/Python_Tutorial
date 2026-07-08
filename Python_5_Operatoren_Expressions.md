## Allgemeines

### Expressionen

**Was ist eine “Expression”?** Etwas, dass einen Wert ergibt.

Im Endeffekt ist alles, was einer Variabel oder Ähnlichem übergeben wird, eine Expression.

```python
5 # ergibt 5
```

```Python
2 + 5 # ergibt 7
```

```Python
"Hello " + "World" # ergibt "Hello World" 
```

Das ist ein Fachbegriff und in der Regel nicht wichtig für die tägliche Verwendung von Python.

### Operatoren

Das sind Zeichen, oder Schlüsselwörter, mit denen man Berechnungen oder Operationen an Variablen vornehmen kann.

Insgesamt gibt es 6 Operatoren in Python.

## Operatoren

### 1) Arithmetische Operatoren

Wie der Name bereits andeutet wird mit diesen gerechnet.

Hier eine Übersicht von denen was es gibt, einige wurden schon in den vorigen Einheiten besprochen:

| Zeichen | Name             | Beispiel        |
|---------|------------------|-----------------|
| +       | Addition         | 2 + 3 # = 5     |
| \-      | Subtraktion      | 5 - 2 # = 3     |
| \*      | Multiplikation   | 2 \* 5 # = 10   |
| /       | Division         | 6 / 3 # = 2     |
| //      | Ganzzahldivision | 5 // 2 # = 2    |
| %       | Modolus          | 5 % 2 # = 1     |
| \*\*    | Potenz           | 5 \*\* 2 # = 25 |

### 2) Vergleichsoperatoren

Diese werden hergenommen, um 2 oder mehrere Variablen zu vergleichen. Wenn die Bedingung erfüllt wurde bekommt man eine Expression die ‘True’ oder 1 ist zurück. Wenn nicht, dann bekommt man ‘False’ oder 0.

Diese Operatoren werden meistens in Verbindung mit IF Abfragen (später dazu mehr) benutzt.

Hier eine Übersicht:

| Zeichen | Namen         | Beispiel      |
|---------|---------------|---------------|
| ==      | Gleich        | 1 == 1 # True |
| !=      | Ungleich      | 1 != 3 # True |
| \>      | Größer        | 2 > 1 # True  |
| <       | Kleiner       | 1 < 2 # True  |
| \>=     | Größergleich  | 2 >= 2 # True |
| <=      | Kleinergleich | 2 <= 6 # True |

### 3) Logische Operatoren

Diese verknüpfen mehrere Verbindungen. Pro Programmiersprache leicht anders.

Hier, die die du am meisten brauchst:

| Zeichen | Name  | Erklärt                                                 | Beispiel               |
|---------|-------|---------------------------------------------------------|------------------------|
| and     | Und   | Dann TRUE, wenn beide Bedingungen erfüllt sind          | True and False # False |
| or      | Oder  | Dann TRUE, wenn eine der beiden Bedingungen erfüllt ist | True or False # False  |
| not     | Nicht | Dann TRUE, wenn die Bedingung nicht erfüllt ist         | not x # False          |

### 4) Zuweisungsoperatoren

Werden verwendet, um Variablen einen Wert zuzuweisen. Man kann diese mit arithmetischen Operatoren verbinden.

Hier eine Übersicht:

| Zeichen | Beispiel | Ausgeschrieben |
|---------|----------|----------------|
| =       | x = 5    | x = 5          |
| +=      | x += 5   | x = x + 5      |
| \-=     | x -= 5   | x = x - 5      |
| \*=     | x \*= 5  | x = x \* 5     |
| /=      | x /= 5   | x = x / 5      |

### 5) Membership Operatoren

Manchmal muss man auch überprüfen, ob sich etwas in einer Liste oder in einem String etc. befindet. Hierzu verwendet man folgende Operatoren:

| Name   | Beispiel          | Ergebnis |
|--------|-------------------|----------|
| in     | “a" in “Hallo"    | True     |
| not in | 10 in \[2, 4, 6\] | False    |

### 6) Identitätsoperatoren

Hier etwas tricky - “is" ist nicht das gleiche wie “==".

“is" vergleicht nicht den Inhalt, sondern **das Objekt selbst.**

"==” vergleicht den **Inhalt**, nicht das Objekt selbst.

Veranschaulicht:

```python
x = [1, 2]
y = x
z = [1, 2]

x is y      # True
x is z      # False
x == z      # True
```

## Aufgabe - Erstelle ein Monster!

Schreibe ein Programm, das den Benutzer nach folgenden Werten fragt:

> - Name des Monsters
> - Angriff (Zahl)
> - Verteidigung (Zahl)

Gib anschließen folgendes aus:

```
1) Gesamtstärke = Angriff + Verteidigung
2) Unterschied = Angriff - Verteidigung
3) Kampfkraft = Angriff * Verteidigung
4) Angriff geteilt durch Verteidigung
5) Rest von Angriff % Verteidigung
5) Angriff hoch 2

Überprüfe:
--> Ist Angriff größer als Verteidigung?
--> Sind Angriff und Verteidigung gleich?
```

Beispielseingabe:

```
Name: Drachenlord
Angriff: 8
Verteidigung: 3
```

Beispielsausgabe:

```
Monster: Drachenlord

Gesamtstärke: 11
Unterschied: 5
Kampfkraft: 24
Division: 2.6666666666666665
Rest: 2
Angriff²: 64

Angriff größer als Verteidigung? True
Angriff gleich Verteidigung? False
```