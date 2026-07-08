## Allgemeines

Was bedeutet “[Debugging](https://code.visualstudio.com/docs/introvideos/debugging)” eigentlich?

Beim Programmieren macht man Fehler - das ist komplett normal. Wenn dann aber le Chefe den Code trotzdem funktionierend haben will ists eher blöd.

Daher sucht man den Fehler in einer Struktur, um so wenig Zeit wie möglich zu verbrauchen.

Das bedeutet:

- Das Programm Schritt für Schritt auszuführen
- Den Inhalt von Variablen sehen
- Verstehen, warum etwas nicht funktioniert

“Aber hey, das geht eh alles mit print() Befehlen” - Ja, nein. Nein nein.

!["I use print() statements btw"](.attachments.32123266/image.png)

Naja gut, wenn man es *unbedingt* will...  
Auch wenn das für kleine Programme gut funktionieren kann tut es im Normalfall GAR nicht bei Programmen, die mehr als eine Funktion besitzen oder ganze Klassen.

Dafür gibt es bessere Methoden die wir jetzt gemeinsam besprechen!

## Breakpoints

[Breakpoints](https://stackoverflow.com/questions/38923386/add-breakpoint-in-visual-studio-code) == Haltestelle für dein Programm

Das macht man indem man neben der Zeilennummer einen roten Punkt setzt.

1. Zeile auswählen, die man in Verdacht hat
2. Links neben der Zeile 1x klicken
3. Es erscheint ein roter Punkt

![Das sollte dann so aussehen](.attachments.32123266/image%20%282%29.png)

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

![Breakpoint - Schritt für Schritt](.attachments.32123266/image%20%283%29.png)

::: info
Der Debugger wird immer dort anhalten, wo dein Breakpoint gesetzt wurde.

:::

Von dort aus kannst du dann über die Pfeile im Menü (oder bspw. über F10) einen Schritt vor, zurücl und über Codeblöcke springen. Mit F11 kann man auch in eine Funktion hineinspringen um zu sehen, was dort so abgeht.

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