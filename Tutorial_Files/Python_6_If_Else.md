## Allgemeines

> “But in the end, it doesn't even matter" - In the end, Linkin Park

Entscheidungen zu treffen fällt vielen schwer. Zum Glück den Interpretern nicht. Du kannst Dinge abgleichen, Exceptions abfangen und noch mehr.

Und all das mit den magischen "IF” Abfragen. Schon toll, oder?

## Basic Vergleichsoperatoren

### 1) [if](https://www.w3schools.com/python/python_conditions.asp)

Mit einem if-Statement kannst du bestimmen, dass bestimmter Code nur dann ausgeführt wird, wenn eine bestimmte Bedingung erfüllt ist (also True / wahr ist).

In Python werden Codeblöcke nicht durch Klammern, sondern durch Einrückungen (vier Leerzeichen / Tab) definiert.

Beispielsweise:

```Python
a = 2
if a == 2:
    print("a ist 2!")
```

Wenn eine Bedingung (= "[Condition](https://www.geeksforgeeks.org/python/conditional-statements-in-python/)") nicht zutrifft, wird das in der If Schleife gar nicht passieren.

```Python
a = 7
if a == 2:
    print("a ist nicht 2")
```

### 2) [elif](https://www.w3schools.com/python/python_if_elif.asp)

Kurz für "If Else” ⟶ prüft eine weitere Bedingung, wenn die vorherige falsch war. 

Du kannst beliebig viele elif-Blöcke nutzen.

Beispielsweise:

```Python
a = 2
if a == 3:
   print("ich werde nicht ausgegeben")
elif a == 2:
   print("ich werde ausgegeben!")
elif (4 / a) == 2:
   print("ich werde ausgegeben!")
```

### 3) [Else](https://www.w3schools.com/python/python_if_else.asp)

Davor muss eine If Abfrage stehen.

Wird ausgeführt, wenn keine der vorherigen Bedingungen erfüllt war (der "Auffangschirm").

Danach kann keine Elif Abgrage mehr anhängen. Dafür ist erneut ein If nötig.

```Python
a = 2
if a == 4:
   print("ich werde nicht ausgegeben")
else:
   print("a ist alles andere als 4. Ich werde ausgegeben.")
```

### 4) [Match - Case](https://www.geeksforgeeks.org/python/python-match-case-statement/)  

Etwas fortgeschrittener in der Anwendung, in der Funktionsweise etwas anders als if und elifs.

Ein Match Statement sieht von der Schreibweise her so aus:  
```Python
match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block
```

Ausgefüllt könnte das so ausschauen:  
```Python
tag = 7
match tag:
  case 6:
    print("Wochenende! Endlich feiern.")
  case 7: 
    print("Wochenende aber morgen wieder Programm.")
  case _:
    print("Wochentag.")
```
Fällt dir daran etwas auf?  
In den Match - Case Statements befindet sich in der letzten position einfach nur ein `_`. Das nennt man in diesem Fall ["Default Value"](https://www.w3schools.com/python/python_match.asp#:~:text=Try%20it%20Yourself%20%C2%BB-,Default%20Value,-Use%20the%20underscore), dieser Fall wird dann ausgeführt wenn keiner der darübrigen Überprüfung mit der abgefragten Variable übereinstimmen.

Auch ist es möglich, ein IF Statement in einer solchen Abfrage zu verwenden.

```Python
monat = 5
tag = 4
match tag:
  case 1 | 2 | 3 | 4 | 5 if monat == 4:
    print("Ein Wochentag im April.")
  case 1 | 2 | 3 | 4 | 5 if monat == 5:
    print("Ein Wochentag im Mai.")
  case _:
    print("No match")
```

#### Aufgabe - Üben  

Um das gelernte über Match - Case zu festigen mache Folgendes Quiz: https://www.w3schools.com/python/python_match.asp#:~:text=Try%20it%20Yourself%20%C2%BB-,Exercise,-%3F

## Aufgabe

Schreibe ein Programm, das den Ticketpreis für ein Kino berechnet. Das Programm soll das Alter einer Person prüfen und den passenden Preis ausgeben.

Die Regeln:

> 1) Kinder unter 12 Jahren zahlen 5 Euro.
>
> 2) Jugendliche und junge Erwachsene unter 26 Jahren zahlen 8 Euro.
>
> 3) Senioren ab 65 Jahren erhalten Rabatt und zahlen 7 Euro.
>
> 4) Alle anderen (also Personen zwischen 26 und 64 Jahren) zahlen den vollen Preis von 11 Euro.

Achte auf die Reihenfolge beim Abfragen!
