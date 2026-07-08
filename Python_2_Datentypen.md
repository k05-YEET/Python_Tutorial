## Allgemeines

In der Programmierwelt gibt es verschiedene Arten und weisen wie man Daten abspeichern kann. Dabei geht es bei den Daten um die Speicherstruktur, die man [Datentypen](https://de.wikipedia.org/wiki/Datentyp) nennt. Hier handelt es sich grundsätzlich um etwas das man “Primitive Datenstruktur” nennt.

Dafür gibt es eine Art Templates, die man verwenden kann:

- **Integer** - Für Ganze Zahlen
- **Floats** (etc.) - Für Gleitkomma Zahlen
- **Char** - Für einen Buchstaben
- **Boolean** - Wahr oder Falsch, logischer Operator
- …

<img width="559" height="358" alt="image" src="https://github.com/user-attachments/assets/3e6b3374-93aa-4a4a-b590-c3a1aca282e5" />  
Datenstrukturhierarchie  (Bildquelle: [techtarget.com](https://www.techtarget.com/rms/German/Datenstrukturhierarchie-deutsch-f_mobile.png)  

Jeder Datentyp hat seinen Nutzen und eigenen Anwendungsfall und variiert bei Definition von Programmiersprache zu Programmiersprache.

## Datentypen in Python

Datentypen in Python werden meistens direkt von Python definiert, und das automatisch.

Im besten Fall muss man nicht angeben, welchen Datentyp man für was haben will. Man kann das aber trotzdem um Missverständnisse zu vermeiden (die durch das Interpretieren beim Code passieren können) indem man den Typ angibt oder bei bedarf “[konvertiert](https://www.w3schools.com/python/python_numbers.asp#:~:text=Try%20it%20Yourself%20%C2%BB-,Type%20Conversion,-You%20can%20convert)”.

Manche Datentypen sind aufgrund von ihrer Struktur und ihrem Aufbau nur bis zu einem gewissen Wert fähig, Zahlenwerte zu speichern. Bei einem Integer beispielsweise gibt es eine Range von -2147483648 bis 2147383648.

::: info
Warum diese Zahlen?  
Integer setzen sich auf einer Mathematischen Ebene folgenderweise zusammen:

2³² = 4.294.957.296

Wenn man das durch 2 teilt (da man negative Zahlen ebenfalls darstellen will) kommt man auf die 2147… Werte.

Die 32 steht hier für die Anzahl der Bits, die jeweils 0 oder 1 darstellen können alleine.

:::

::: info
Falls dich die Struktur von Datentypen auf einem tieferen Level (Binär Ebene) interessiert kannst du hier mehr dazu lesen:

<https://exercism.org/tracks/python/concepts/binary-octal-hexadecimal>

… oder wie eine Binärdarstellung funktioniert:

<https://youtu.be/ruolmC7dbj8?si=AIw4nJgSfz9os1nd>

:::

Ein Überblick zu den wichtigsten Datentypen die du kennen solltest in dieser Sprache:

| Datentyp                                                                                                                              | Name       | Beschreibung                                                                               | Beispiel                |
|---------------------------------------------------------------------------------------------------------------------------------------|------------|--------------------------------------------------------------------------------------------|-------------------------|
| [int](https://www.w3schools.com/python/python_numbers.asp#:~:text=Try%20it%20Yourself%20%C2%BB-,Int,-Int%2C%20or%20integer)           | Integer    | Ganze Zahlen                                                                               | x = 5                   |
| [float](https://www.w3schools.com/python/python_numbers.asp#:~:text=Try%20it%20Yourself%20%C2%BB-,Float,-Float%2C%20or%20%22floating) | Float      | Fließkommazahlen (Dezimalzahlen mit Punkt)                                                 | pi = 3.14               |
| [str](https://www.w3schools.com/python/python_strings.asp#:~:text=Next%20%E2%9D%AF-,Strings,-Strings%20in%20python)                   | String     | Zeichenkete, Text in Anführungszeichen                                                     | text = “Yo, ich code”   | \
|                                                                                                                                       |            | Du kannst hier auch nur einen Buchstaben abspeichern - Python hat keinen “char” Datentypen |                         |
| [bool](https://www.w3schools.com/python/python_booleans.asp)                                                                          | Boolean    | Wahrheitswerte, True or False, 1 oder 0                                                    | ist_valide = True       |
| [list](https://www.w3schools.com/python/python_lists.asp)                                                                             | Listen     | Veränderbare, geordnete Liste                                                              | liste = \[1, 2, 3\]     |
| [tuple](https://www.w3schools.com/python/python_tuples.asp)                                                                           | Tupels     | Unveränderbare, geordnete Liste                                                            | tupel = (1, 2, 3)       |
| [set](https://www.w3schools.com/python/python_sets.asp)                                                                               | Sets       | Ungeordnete Menge, keine Duplikate                                                         | menge = {1, 2, 3}       |
| [dict](https://www.w3schools.com/python/python_dictionaries.asp)                                                                      | Dictionary | Wörterbuch, Schlüssel-Wert Paare                                                           | dict = {“name”: “Igor”} |

::: info
Fällt dir bei der Gleitkommadarstellung bei Floats etwas auf?

In Python wird ein Komma bei einer Zahl (z.B.: 2,3 = zweikommadrei) mit einem Punkt angegeben.

Das ist in anderen Programmiersprachen ähnlich, da man eine Kommazahl unbedingt von einem Argument, dass man bspw. wie bei der list angeben würde in einer Klammer, unterscheiden können muss.

Du wirst hier den Fehler öfters machen, wenn du es noch nicht gewohnt bist.

Das ist okay. Aller Anfang ist schwer.

:::

Nun gut… jetzt kennst du das einmal in der Theorie. Aber wo muss man die angeben?

Im Normalfall? - Gar nicht.

Datentypen werden für Variablen hergenommen. Diese kannst du befüllen wie du willst und abrufen wann du sie brauchst.

#### Anhand eines Beispiels

Sagen wir, wir wollen 3 Sachen abspeichern:

> - Name ⟶ “Norbert”
> - Age ⟶ 54
> - Height ⟶ 1.72

Die Werte, die Name, Age und Height zugeordnet werden sollten definieren bereits den Datentyp. Du musst die Variabel einfach richtig von der Formatierung her befüllen:

```python
# Erstelle und befülle (= "initiieren") eine Variabel
name = "Norbert"

age = 54

height = 1.72
```

So würdest du sie dann in der Konsole ausgeben und überprüfen können:

```python
# Füge diese Lines darunter ein
print(name)
print(age)
print(height)
```

Die Variablen müssen nicht vordefiniert werden da Python das regelt. Was allerdings “blöd” ausgehen kann ist wenn man folgendes versucht:

```python
name = "Norbert"
name = 3
```

Wenn man Glück hat, konvertiert Python den Datentyp von “name” richtig. Aber auch wenn das richtig ausschaut am Ende kann es zu ungewolltem Verhalten führen. Im Zweifelsfall kannst du daher den Datentyp dennoch angeben:

```python
name: str = "Norbert"
age: int = 54
height: float = 1.75
```

… aber das ist eher selten sinnvoll für alle Variablen. Halte es einfach.

Wenn du vergessen hast, welcher Typ eine Variable ist gibt es folgende Funktion (mehr zu Funktionen später), die dir zeigt was sich in der Variabel befindet:

```python
print(type(name))
```

#### Rechnen mit numerischen Variablen

Natürlich bringen dir die Werte alleine nichts. Man muss mit der Variabel wenn es sich um Nummer handelt rechnen können.

##### Additionen

```python
a = 5
b = 3

ergebnis = a + b

print(ergebnis)
```

Das sollte dann “8” ausgeben.

##### Subtraktion

```python
a = 10
b = 4

ergebnis = a - b

print(ergebnis)
```

Das sollte dann “6” ausgeben.

##### Multiplikation

```python
a = 3
b = 5

ergebnis = a * b

print(ergebnis)
```

Das sollte dann “15” ausgeben.

##### Division

```python
a = 10
b = 5

ergebnis = a / b

print(ergebnis)
```

Das sollte dann “2” ausgeben.

::: info
Funfact!

Divisionen funktionieren auf Prozessor-Ebene nicht wie wir es im Kopf rechnen. Da die Architektur mit seinem System damit Probleme haben rechnet der Computer eigentlich etwas komplett anderes als 10 durch 5 in unserem Dezimalsystem.

:::

#### Fortgeschrittene Operationen

Es gibt noch mehr, aber das solltest du dann nachlesen wenn du es brauchst.

| Name                                                                                                  | Schreibweise in Code | Was macht das?                                  | BSP          |
|-------------------------------------------------------------------------------------------------------|----------------------|-------------------------------------------------|--------------|
| [Floor Division](https://www.learndatasci.com/solutions/python-double-slash-operator-floor-division/) | //                   | Nimmt die nächste Ganze Zahl (Bibliothek: math) | 15 // 4 = 3  |
| [Modulus](https://www.geeksforgeeks.org/python/what-is-a-modulo-operator-in-python/)                  | %                    | Behaltet nur den Rest                           | 10 % 3 = 1   |
| [Exponent](https://www.datacamp.com/de/tutorial/exponents-in-python)                                  | \*\*                 | Exponent, bspw.: 2²                             | 2 \*\* 3 = 8 |

#### Das gibt es nicht nur für Zahlen!

Man verwendet [Rechenoperatoren](https://www.ionos.at/digitalguide/websites/web-entwicklung/python-operatoren/) auch dafür um zum Beispiel Wörter zu kombinieren.

Anhand eines Strings (= [str](https://www.w3schools.com/python/python_strings.asp#:~:text=Next%20%E2%9D%AF-,Strings,-Strings%20in%20python)) kann man das einfach sehen:

```python
erster_name = "John"
zweiter_name = "Wick"

voller_name = erster_name + " " + zweiter_name
# + " " fügt ein Lehrzeichen zwischen den Wörter ein!

print(voller_name)
```

Das sollte dann “John Wick” ausgeben.

Man kann auch einfach ein Wort, das noch in keiner Variabel ist anhängen (= “[append](https://www.datacamp.com/de/tutorial/exponents-in-python)”).

```python
nachricht = "Hallo, "

nachricht = nachricht + "Admin!"

print(nachricht)
```

Das sollte dann “Hallo, Admin!” ausgeben. Geht natürlich auch verkehrt herum.

Multiplikation funktioniert ebenfalls. Wenn du Strings verbinden oder bearbeiten (nur einen Buchstaben ändern (mehr dazu in Arrays und Lists), rausschneiden oder auch die Länge eines Wortes auslesen) willst gibt es in Python immer [viele Ansätze](https://www.w3schools.com/python/python_ref_string.asp).

## Aufgabe

Aufgabenstellung:

Du bist ein neuer Mitarbeiter, und dir fehlt dein Ausweis. Du solltest ihm trotzdem dem System übergeben.  
Wichtige Informationen, die da drauf stehen sollten, sind:

> - First Name
> - Last Name
> - Age
> - Height
> - Hobby

Der Output, der vom System erwartet wird ist in folgendem Format:

```
----- NAME BADGE -----
Name: John Smith
Age: 35
Height: 1.85
Hobby: Chess

Welcome, JOHN SMITH!
Your name has 10 letters.
Your username is john.smith
```

Benutze Python um genau dieses Format von Variablen aus im Terminal auszugeben! Achte auf Groß- und Kleinschreibung. Der Username muss von dir generiert werden und dem Namen im Format entsprechen.

Die Challenge hier?

Der Benutzer soll das alles selbst eingeben können. **Frag also nach den Inhalt der Variablen und lese die jeweils richtig ein.** Was du dafür brauchen wirst: [input()](https://www.w3schools.com/python/ref_func_input.asp)
