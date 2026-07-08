## VS Code

**Was ist “VS Code”?**

VS Code steht für “[Visual Studio Code](https://code.visualstudio.com/)” und ist die IDE, die Microsoft gratis zu Verfügung stellt. Es gibt noch andere IDE Optionen sowie [PyCharm](https://www.jetbrains.com/de-de/pycharm/), [Jupyter Notebook/Lab](https://jupyter.org/), [Spyder](https://www.spyder-ide.org/), [Neovim](https://neovim.io/) und mehr. Jeder Entwickler bevorzugt verschiedene IDEs, aber VS Code ist aufgrund von Microsofts Einfluss am meist verbreitetsten und hat mit Abstand die größte Community dahinter.

Im Endeffekt wäre aber auch ein Texteditor wie VIM oder Nano ausreichend, aber für Komfort sind IDEs grundsätzlich super.

Man kann damit nicht nur Code ausführen und entspannt mit Fehlererkennung schreiben, sondern auch Agentic KI Systeme einbinden (siehe bspw. [Copilot via Github](https://github.com/copilot)) sondern auch Gebrauch machen von fast endlosen Extensions die es unter VS Code gibt, die zum Beispiel das Flashen von Mikrocontroller einfach umsetzen lassen. (Vorsicht geboten vor Malware oder infizierten Extensions)

## So setzt du VS Code für Python auf

Für einen komfortablen Gebrauch ist nicht nur Python alleine ausreichend, um in VS Code Python einfach einzubinden. Schritt Nummer 4, 2 und 6 sind optional aber empfohlen.

1. Installiere Python

```bash
sudo apt update && sudo apt install python3
```

```bash
python3 --version
```

1. Installiere PIP

[PIP](https://pip.pypa.io/en/latest/) ist der Standard für [Paketinstallationsmanager ](https://de.wikipedia.org/wiki/Paketverwaltung)für Python. Es ermöglicht dir, externe Bibliotheken und Programme herunterzuladen, zu installieren und zu verwalten.

```bash
sudo apt install python3-pip
```

```bash
pip3 --version # Verify
```

1. Installiere die Extension Python in VS Code

Unter [Extensions](https://marketplace.visualstudio.com/vscode) in der Seitenleiste in dem Programm “Python” eintippen und installieren. Achte darauf, dass der Autor auch wirklich “Microsoft” anzeigt und keinen einzelnen Namen.  
(Zur Verifizierung diese ID abgleichen: ms-python.python)

Was bringt dir das wenn du so oder so Code ausführen hättest können?

- [Syntax](https://de.wikipedia.org/wiki/Syntax) highlighting
- [IntelliSense](https://de.wikipedia.org/wiki/IntelliSense) (Autovervollständing / -korrektur)
- [Debugging](https://de.wikipedia.org/wiki/Debuggen) (= Die Kunst der Fehlersuche)
- Python Files ausführen
- Jupyter Notebook Support (optional)

1. Python Interpreter auswählen (Falls mehrere Python Versionen installiert sind)

   4.1) Auf der Tastatur: Ctrl + Shift + P  
   4.2) Tippe ein: “Python: Select Intepreter”  
   4.3) Python Installation auswählen (erscheint als Option)
2. Testfile ausführen

Aufgabe: Gib "Hello World!” in der Konsole aus!  
Verwende dafür keine KI, Internet Posts sind erlaubt. Schau dir an, wie du ein Script im (Tipp: ||Python im Terminal mit Fileangabe. Du kannst in VS Code das Terminal unter der Leiste “Terminal” mit “New Terminal” aufrufen, achte darauf dass du den Pfad des Files richtig angibst oder dich im gleichen Ordner befindest||) ausführen kannst.

1. Installiere venv

Das Problem mit Paketen oder Bibliotheken ist, dass sich manche Überschneiden auf Systemebene und dann plötzlich nicht mehr funktionieren können.

> “This town ain’t big enough for the both of us” - *The Man from Bar-20*, von Clarence E. Mulford

Damit man aber nicht zwischen Pakete wählen muss gibt es virtuelle Umgebungen.

Stell es dir wie eine Box vor - keiner der Paketen in Box A kommt sich mit Paketen aus Box B in die Quere.

Bei Python heißt die meist umgesetzte Lösung hier [VENV](https://docs.python.org/3/library/venv.html). Hier drinnen kann man Projekte einzeln halten und zwischen ihnen wählen, vor allem wenn man sowieso mit [PIP](https://pip.pypa.io/en/latest/) arbeitet.

Am Anfang würde ich dem noch aus dem Weg gehen wenn nicht unbedingt notwendig. Aber für den Fall, dass du es mal brauchst, so installierst du es:

```bash
sudo apt install python3-venv
```

So verwaltest du dein Projekt dann:

```bash
mkdir myproject # Ordner anlegen
cd myproject # In den Projektordner reingehen

python3 -m venv .venv # Ein venv erstellen für diesen Ordner
source .venv/bin/activate # Das venv "aktivieren", jetzt aktiv nutzen
```

Du solltest dann “(.venv)” angezeigt bekommen.

So installierst du bei Bedarf dann Pakete:

```bash
pip install requests # bspw.: requests
```

Wenn du die Umgebung dann verlassen willst:

```bash
deactivate
```