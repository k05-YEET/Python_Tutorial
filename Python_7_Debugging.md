## Allgemeines

Was bedeutet “[Debugging](https://code.visualstudio.com/docs/introvideos/debugging)” eigentlich?

Beim Programmieren macht man Fehler - das ist komplett normal. Wenn dann aber le Chefe den Code trotzdem funktionierend haben will ists eher blöd.

Daher sucht man den Fehler in einer Struktur, um so wenig Zeit wie möglich zu verbrauchen.

Das bedeutet:

- Das Programm Schritt für Schritt auszuführen
- Den Inhalt von Variablen sehen
- Verstehen, warum etwas nicht funktioniert

“Aber hey, das geht eh alles mit print() Befehlen” - Ja, nein. Nein nein.

<img width="860" height="596" alt="image" src="https://github.com/user-attachments/assets/625d13bd-7910-4fde-a660-698ad286edc7" />    

"I use print() statements btw" (Bildquelle: [reddit.com](https://www.reddit.com/r/ProgrammerHumor/comments/op764d/print_breakpoints/))  

Naja gut, wenn man es *unbedingt* will...  
Auch wenn das für kleine Programme gut funktionieren kann tut es im Normalfall GAR nicht bei Programmen, die mehr als eine Funktion besitzen oder ganze Klassen.

> [!TIP]
> Wenn du doch vor hast `print()`-Statements stattdessen zu benutzen vergesse es nicht, diese wieder auszukommentieren bevor man den Code veröffentlicht / jemanden zeigt / in die Produktion einsetzt.  
> Ein vollgemülltes Server-Output File im Terminal kann schnell peinlich werden.

Dafür gibt es bessere Methoden die wir jetzt gemeinsam besprechen!

## Breakpoints

[Breakpoints](https://stackoverflow.com/questions/38923386/add-breakpoint-in-visual-studio-code) == Haltestelle für dein Programm

Das macht man indem man neben der Zeilennummer einen roten Punkt setzt.

1. Zeile auswählen, die man in Verdacht hat
2. Links neben der Zeile 1x klicken
3. Es erscheint ein roter Punkt

<img width="548" height="188" alt="image (2)" src="https://github.com/user-attachments/assets/0a58d087-627d-4be7-b3db-366d82a11c49" />  

↑ Das sollte dann so aussehen.

Wenn der rote Punkt erreicht wurde, bricht in dieser Zeile das Programm ab.

## Starten des Debuggers

Dafür gibt es logischerweise mehrere Möglichkeiten:

- Taste F5 (Linux approved)
- Menü RUN ⟶ Start Debugging
- Das ▶ Symbol im Debug-Bereich

Beim ersten Start erstellt VS Code in der Regel automatisch eine passende Konfiguration. Diese kann man natürlich nach Lust und Liebe abändern - aber bitte auch nur, wenn es Sinn ergibt das zu tun.

Falls der Wunsch entstanden ist *wäre es sinnvoll*, zuerst von der automatisch generierten Konfiguration ein Backup zu machen.

## Während das Programm pausiert

Aber was bringt uns das jetzt eigentlich?

Man kann jetzt:

- Variablen einsehen
- Zeilen einzeln ausführen
- Funktion betreten
- Bis zum nächsten Breakpoint weiterlaufen

## Schritt für Schritt…

Manchmal verliert man den Überblick wie ein Programm überhaupt abläuft. Und das ist okay - passiert den Besten von uns,

Dafür gibt es eine Funktion in VS Code die dich einen Code Zeile für Zeile ausführen lässt.

<img width="900" height="188" alt="image (3)" src="https://github.com/user-attachments/assets/b46dd4e8-43dd-460e-82b1-9d1ef9ed8fe7" />

> [!IMPORTANT]
> Der Debugger wird immer dort anhalten, wo dein Breakpoint gesetzt wurde.

Von dort aus kannst du dann über die Pfeile im Menü (oder bspw. über F10) einen Schritt vor, in Funktionen hinein / hinaus und über Codeblöcke springen. Mit F11 kann man auch in eine Funktion hineinspringen um zu sehen, was dort so abgeht.  
Variablen, die du geschaffen hast findest du im Grund unter den `special variables` Tab auf der Seite.  

## Variablen beobachten

Während VS Code  das Programm aufhaltet werden links all die Variablen angezeigt, so wie ihr Wert. Falls man irgendwo einen Rechenfehler hat kann das ganz praktisch sein, um zu verstehen wo was hinein geschrieben wird.

Schau es dir anhand eines Beispiels an!

```python
preis = 20
rabatt = 30

endpreis = preis - rabatt

print(endpreis)
```

Setze den Breakpoint auf die 4 Zeile (“endpreis …”) und schaue dir den Wert von Preis und Rabatt an.

## Typische Anfängerfehler

- Breakpoint auf der falschen Stelle
- Programm ohne Debugger gestartet
- Falsche Datei ausgeführt
- Variablen noch nicht berechnet

## Aufgabe

Das folgende Programm soll den Durchschnitt mehrerer Zahlen berechnen.

Leider enthält es zwei Fehler.

Nutze den Debugger in VS Code und finde beide Fehler.

```python
def durchschnitt_berechnen(zahlen):
    summe = 1

    for zahl in zahlen:
        summe += zahl

    durchschnitt = summe / len(zahlen) - 1

    return durchschnitt


zahlen = [12, 18, 25, 30, 15]

ergebnis = durchschnitt_berechnen(zahlen)

print(f"Der Durchschnitt beträgt {ergebnis}")
```

Beantworte folgende Fragen:

- [ ] Welchen Wert hat summe nach jeder Schleifenrunde?
- [ ] Welchen Wert besitzt durchschnitt?
- [ ] Warum stimmt das Ergebnis nicht?
- [ ] Welche zwei Zeilen müssen geändert werden?
