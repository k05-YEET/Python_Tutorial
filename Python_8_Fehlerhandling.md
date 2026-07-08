## Allgemeines

> “Es ist dieselbe Straße / Die wir schon damals gegangen sind / Und dieselben Fehler **/** Die wir immer wieder machen / Doch wir bereuen nichts” - Altes Fieber, die toten hosen

Man kann nicht immer alles absichern. Manchmal wird sich ein Benutzer halt vor den Bildschirm hinsetzen und etwas absolut gottloses eintippen an das du nie gedacht hättest.

Aber das WAS dir einfällt, solltest du absichern.

Ein Beispiel wäre:

```python
alter = int(input("Alter: "))
```

Was ist an dem Code falsch? Grundsätzlich gar nichts.

Aber glaub mir. Irgendjemand würde es versuchen “zwanzig” einzugeben, und dann geht das Programm über mit einem ValueError.

Wie gesagt, man kann ja nicht alles abfangen, aber so etwas eben schon.

Von provokanten Benutzer abgesehen hat das ganze auch ein Security Grund. Wenn man eine Anwendung für ein Unternehmen schreibt, dass beispielsweise Daten von einem Sensor einliest - darf das Programm nicht die ganze Produktion anhalten nur weil kurz die Spannung weg war und eine 0 zu viel angekommen ist.

## [try](https://www.w3schools.com/python/python_try_except.asp)

Nein, wirklich, try als Expression.

Wenn du Code verdächtigst, der eventuell zu einem Problem werden könnte, kannst du ihn in Python einfach in einen “try”-Block werfen. Wenn hier etwas schief geht brauchst du nicht endlos eine while() Schleife laufen lassen oder ähnliches.

Hier ein Beispiel:

```python
try:
    alter = int(input("Alter: "))
```

Das alleine wird nicht ausgeführt werden. Denn wenn man einfach alles probieren würde ohne Konsequenz kann man es sich doch gleich sparen.

## [except](https://docs.python.org/3/tutorial/errors.html)

Das ELSE zu dem IF was in unserem Fall “try” heißt.

```python
try:
    alter = int(input("Alter: "))
except:
    print("Bitte eine Zahl eingeben.")
```

Wenn der try hier jetzt schief geht oder einen Fehler generiert:

![Output](.attachments.32123307/image.png)

… wird das ganze clean abgefangen und man kann den Fehler so behandeln als hätte man ihn kommen sehen.

## Bestimmte Fehler abfangen

Etwas schwerer, aber wenn man bereits weiß auf was man schauen muss eine logische Reaktion.

Beispiel:

```python
try:
    alter = int(input("Alter: "))
except ValueError: # Es wird hier der Error Name nach except angegeben
    print("Bitte nur Zahlen eingeben.")
```

Man kann auch mehrere except Statements hintereinander anführen:

```python
 try:
    zahl = int(input("Zahl: "))
    print(10 / zahl)

except ZeroDivisionError:
    print("Durch 0 darf nicht geteilt werden.")

except ValueError:
    print("Bitte eine Zahl eingeben.")
```

### In Kombination mit else

Für den Fall dass der spezielle Case mit except nicht eingetreten ist:

```python
try:
    zahl = int(input("Zahl: "))
except ValueError:
    print("Ungültige Eingabe.")
else:
    print("Eingegeben:", zahl)
```

::: info
Else wird nur DANN ausgeführt, wenn try fehlgeschlagen und except nicht durch den exakten Fehler “ValueError” ausgelöst wurde.

:::

### [finally](https://www.w3schools.com/python/ref_keyword_finally.asp)

… nein, wir haben noch nicht Pause. /jk 

“finally” wird immer ausgeführt, egal wie das obere ausgeht.

```python
try:
    print(10 / 2)
except:
    print("Fehler")
finally:
    print("Programm beendet.")
```

## Aufgabe

Das wars, du arbeitest doch beim MacDonalds. Python zu programmieren war zu schwer.

![... oder Python.](.attachments.32123307/image%20%282%29.png)

Allerdings geht dir das Eintippen von jedem Menü schon echt auf den Zeiger, und die Selbstbedien-Portale sind außer Betrieb. Deswegen hast du dir vorgenommen, etwas Arbeitszeitbetrug durchzuführen um ~~dir selbst~~ deinem wunderbaren Arbeitgeber zu helfen.

Das Programm soll mehrere Bestellungen entgegennehmen und am Ende die Gesamtkosten berechnen.

Leider denken manche Teenager, dass es cool ist einfach irgendwas einzugeben.    
Zerstöre ihr Selbstvertrauen in ihren Methoden indem dein Programm **nicht abstürzt**.

| Gericht            | Preis |
|--------------------|-------|
| BigMac             | 4.50€ |
| McFlurry           | 3.20€ |
| Pommes + SourCreme | 2.50€ |

Das Programm soll:

> 1) Den Benutzer fragen, wie viele Leute bestellen
>
> ⟶ Falls keine gültige Zahl eingegeben wird soll das Program eine Fehlermeldung ausgeben und beendet werden!
>
> 2) Für jede Person den Namen und Gericht abfragen
>
> 3) Danach das gewünschte Essen eingeben lassen
>
> 4) Je nach Auswahl den Preis addieren
>
> 5) Bei einer ungültigen Eingabe soll ausgegeben werden:
>
> ⟶ “Dieses Gericht gibt es leider nicht.”
>
> 7) Am Ende ausgeben:
>
> “Heute haben X Personen bestellt.  
> Gesamtpreis: XX.XX €"
>
> 8) Zum Schluss soll unabhängig davon, ob Fehler aufgetreten sind oder nicht folgende Meldung erscheinen:
>
> “Programm beendet. Mahlzeit!”

Hinweise:

- Verwende mindestens einen try-Block
- Fange mindestens einen ValueError ab
- Verwende außerdem einen finally-Block