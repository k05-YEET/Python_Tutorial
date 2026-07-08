## Allgemeines

Warum etwas machen, wenn es wer anderer schon vor dir besser gemacht hat?

Auch wenn es viele Entwickler gibt, die selbst Bibliotheken schreiben und diesen dann Leuten zu Verfügung stellen. Aber mal ehrlich, da sind wir noch lange nicht.

## Was ist ein “Modul”?

![Quelle: https://ipcisco.com/wp-content/uploads/2021/04/python-modules-ipcisco-1.jpg](.attachments.32123334/image.png)

Ein [Modul](http://py-tutorial-de.readthedocs.io/de/python-3.3/modules.html) ist eine Python-Datei mit [Funktionen](https://www.python-lernen.de/funktionen-in-python.htm), [Klassen](http://py-tutorial-de.readthedocs.io/de/python-3.3/classes.html) oder [Variablen](https://www.w3schools.com/python/python_variables.asp), die wir in unserem eigenem Programm verwenden können.

Es spart dir Zeit und ermöglicht es dir, dich auf das Wesentliche zu fokussieren.

## Was bedeutet “[import](https://docs.python.org/3/reference/import.html)”?

= Ein Schlüsselwort, mit dem man Module in ein Program hinein “laden” können.

Dafür muss dieses Modul nicht unbedingt vorinstalliert sein.

So schaut es bspw. aus, wenn man das Modul “[math](https://docs.python.org/3/library/math.html)” für fortgeschrittene Matheoperationen importieren will:

```python
import math
```

… crazy, oder. 

Jetzt können Funktionen aus “math” verwendet werden. Diese ruft man mit Angabe des Modulnamens davor ab:

```python
import math

print(math.sqrt(25)) # Gibt die Wurzelbasis von 25 aus
```

Output: 5.0

Was für ein Modul man für was verwenden will hängt stark vom Use-Case ab und variiert je nach Projekt.

## Einzelne Funktionen

Wenn man ein Modul hat (in der Theorie) das beispielsweise TotallyInterestingModuleThatYourMomLikes (gibt es nicht btw) heißt, kann es anstrengend werden bei jedem Funktionen Aufruf das wieder hinzuschreiben wenn man beispielsweise nur eine Funktion daraus braucht.

Das kann man umgehen, denn man kann beim  Importieren direkt angeben welche Funktion man haben will.

Sagen wir “yourmom()” ist eine Funktion von… naja, dem erwähnten Modul.

```python
from TotallyInterestingModuleThatYourMomLikes import yourmom

print(yourmom(69))
```

Und das würde funktionieren.

Vorteil? Alles wird gleich viel übersichtlicher, und man haltet die Programmgröße minimal.

Nachteil? Man kann leicht vergessen wie eine Funktion importiert wurde, oder der Name alleine überschneidet sich mit einem in deinem Programm.

## Selbst Module schreiben

… geht im Grunde genommen. Für dich aber jetzt vorerst unwichtig, da es sich hier eigentlich nur um Konvention und Make-Up handelt.

> Falls es jemanden interessiert: <https://stackoverflow.com/questions/15746675/how-to-write-a-python-module-package>

## Aufgabe - Wahrheitsautomat

Du hast auf dem Flohmarkt einen mysteriösen Wahrsage-Automaten gefunden. Leider funktioniert er nur mit Python.

Schreibe ein Programm, das den Benutzer nach seinem Namen fragt und anschließend eine zufällige Zukunft vorhersagt.

Die Vorhersagen, die dein Program bei Zufall ausgeben sollte:

> - Du bestehst die nächste Prüfung.
> - Heute gibt es gratis Pizza.
> - Dein WLAN wird heute genau dann ausfallen, wenn du es brauchst.
> - Du findest heute 5 €.
> - Heute solltest du besser keinen Kaffee trinken.
> - Du wirst heute 3 Stunden auf TikTok verschwenden.
> - Dein Code funktioniert beim ersten Versuch. (Sehr unwahrscheinlich.)

Dein Programm sollte den folgenden Anforderungen entsprechen:

> 1. Den Benutzer nach seinem Namen fragen.
> 2. Die Vorhersagen in einer Liste speichern.
> 3. Mithilfe des Moduls **random** eine zufällige Vorhersage auswählen.
> 4. Die Vorhersage ausgeben.

Beispielsausgabe:

```
Wie heißt du?
Max

Hallo Max!

Deine Vorhersage:

Du findest heute 5 €.
```