## Einfache Funktionen

1.  Schreiben Sie eine Funktion, die eine Liste von Ints übergeben bekommt und nur die geraden Zahlen in einer Liste zurückgibt.  
    Verwenden Sie nicht den %-Operator.
2.  Schreiben Sie eine Funktion, die einen Int übergeben bekommt und die Anzahl der Ziffern zurückgibt.  
    Sie dürfen den Datentyp der Zahl nicht ändern. Es ist nicht Sinn der Aufgabe, 
    eine built-in-Funktion für den Zehnerlogarithmus zu verwenden.
3.  Schreiben Sie die Funktion aus 2 rekursiv (mit denselben Einschränkungen).
4.  Schreiben Sie eine Funktion, die eine Liste von Strings übergeben bekommt und die Anzahl der Worte zurückgibt, 
    die mehr als 5 Buchstaben enthalten.
5.  Schreiben Sie eine Funktion, die eine Liste von Strings übergeben bekommt und die Anzahl der Worte zurückgibt, 
    die ein 'e' enthalten und mehr als 5 Buchstaben haben. Die Groß-/Kleinschreibung soll ignoriert werden.
6.  Schreiben Sie eine Funktion, die eine Liste von Ints übergeben bekommt und die Anzahl der Zahlen zurückgibt, die 
    durch 3 oder 5 teilbar sind, aber nicht durch beide.

[Hier](../Muster/Klausur/simple_funcs.py) finden Sie die Musterlösung.

---

## Finanzanalyse

In der Datei [DAX.csv](../resources/DAX.csv) finden Sie Informationen zum Kurs des Global X DAX Germany ETF (DAX) in den letzten 10 Jahren.
Das ist ein ETF, der in etwa den DAX abbildet.

1.  Schreiben Sie eine Funktion, die die Datei einliest und in einem geeigneten Format speichert.
2.  Schreiben Sie eine Funktion, die den niedrigsten, höchsten und durchschnittlichen Eröffnungspreis berechnet.
3.  Schreiben Sie eine Funktion, die den Tag mit dem größten Preissprung (Differenz zwischen Tief und Hoch) findet.
4.  Schreiben Sie eine Funktion, die die Gesamtzahl der Handelstage berechnet, an denen der Schlusspreis höher war als der Eröffnungspreis.

[Hier](../Muster/Klausur/financial_analysis.py) finden Sie die Musterlösung.

---

## Autos

1.  Schreiben Sie eine Klasse Car mit Attributen für Marke, Modell und Baujahr. Implementieren Sie Getter und Setter für diese
    Attribute.
2.  Schreiben Sie eine Methode, die das Alter eines Autos berechnet. Mit date.today() aus dem datetime-Modul können Sie 
    das aktuelle Datum in der Form YYYY-MM-DD abrufen.
3.  Schreiben Sie eine geeignete str- und repr-Methode für die Car-Klasse
4.  Schreiben Sie eine lt-Methode, die die Baujahre von 2 Autos vergleicht.
5.  Erstellen Sie eine Klasse Garage, die eine Liste von Autos enthält. Implementieren Sie Methoden, um Autos hinzuzufügen 
    und zu entfernen, sowie eine Methode, die das älteste Auto in der Garage zurückgibt.
6.  Schreiben Sie eine geeignete str-Methode für die Garage-Klasse

[Hier](../Muster/Klausur/car.py) finden Sie die Musterlösung.

---

## Potenzieren

In dieser Aufgabe wollen wir die Potenz einer gegebenen Zahl berechnen. Offensichtlich sind der **-Operator und
Funktionen, die genau das berechnen, nicht erlaubt. Sie können davon ausgehen, dass beide Zahlen, die ihre Funktion bekommt,
positive natürliche Zahlen sind.

1.  Schreiben Sie eine iterative Funktion, die die Potenz einer gegebenen natürlichen Zahl n berechnet.
2.  Schreiben Sie die Funktion rekursiv.

[Hier](../Muster/Klausur/power.py) finden Sie die Musterlösung.

---

## Listen umdrehen

In dieser Aufgabe wollen wir Listen umdrehen. Das heisst, die Funktion bekommt eine Liste wie `[1, 2, 3]` und gibt
manipuliert sie so, dass die Elemente rückwärts darin stehen, also hier `[3, 2, 1]`.  
Offensichtlich sind `liste[::-1]`, `liste.reverse()` und `reversed(liste)` verboten.

1.  Schreiben Sie die Funktion iterativ.
2.  Schreiben Sie die Funktion rekursiv.

[Hier](../Muster/Klausur/lists.py) finden Sie die Musterlösung.

---

## Arbeiten mit Dateien

### Überschriften
In der Datei [index.html](../resources/index.html) finden Sie die Struktur einer (sehr simplen) Webseite. Schreiben Sie eine Funktion, die den Dateinamen
übergeben bekommt und eine Liste zurückgibt, die alle Überschriften enthält. In html kann man diese folgendermassen erkennen.
Es gibt einen Opening-Tag, dann flogt die Überschrift und schlussendlich der Closing-Tag.
Der Opening-Tag steht in `<>`. Darin steht (in unserem Fall, im Allgemeinen komplexer) erst der Buchstabe h und dann eine Zahl.
Der Closing-Tag sieht in dem Fall prinzipiell genauso aus, aber hinter dem `<` ist ein `/`.
Aus `<h1>Hauptüberschrift</h1>` soll also nur "Hauptüberschrift" extrahiert werden.

### Zipfsches Gesetz
Nun widmen wir uns dem [Zipfschen Gesetz](https://de.wikipedia.org/wiki/Zipfsches_Gesetz).

1.  Schreiben Sie eine Funktion `count_words_from_file(path)`, die einen Dateinamen als Argument bekommt. 
    Sie können [faust.txt](../resources/faust.txt) verwenden.
    Legen Sie ein Dictionary an, das für alle Wörter deren Häufigkeit speichert. Die Funktion soll die Datei zeilenweise einlesen. 
    Ignorieren Sie den Vorspann (Zeilen 1-23). Zunächst sollen sie alle Sonderzeichen aus der Zeile entfernen.
    Hinweis: Sie können das string-Modul importieren. `string.punctuation` ist ein String, der alle ASCII-Sonderzeichen enthält.
    Ignorieren Sie ferner Groß- und Kleinschreibung. Die Funktion soll das Dictionary zurückgeben.  


2.  Schreiben Sie eine Funktion `get_most_common_words(amount_words)`, die das Dictionary aus Aufgabe 2.2 als Argument erhält und
    die häufigsten 100 Wörter bestimmt. Beurteilen Sie, ob das Zipfsche Gesetz zutrifft.


[Hier](../Muster/Klausur/files.py) finden Sie die Musterlösung.

---

## Palindrome

Ein Palindrom ist ein Wort, das vorwärts oder rückwärts gelesen gleich ist z.B. Anna, Lagerregal oder Radar. 
Eine Möglichkeit, zu testen, ob ein Wort ein Palindrom ist, nutzt einen Stapel als Datentyp.
Der Algorithmus aus der Datei [palindrom_algorithm.txt](../resources/palindrom_algorithm.txt) kann entscheiden, ob ein Wort ein Palindrom ist.

Bemerkung: Der Algorithmus simuliert das Verhalten eines deterministischen Kellerautomaten (mehr dazu im Modul FSB).

1.  Begründen Sie die Korrektheit des Algorithmus. Eine Erklärung in eigenen Worten ist ausreichend
2.  Schreiben Sie eine Klasse Stack, die alle notwendigen Operationen des Stapelspeichers beinhaltet.
3.  Schreiben Sie aus dem [Pseudocode](../resources/palindrom_algorithm.txt) ein Python-Programm, das entscheidet, ob ein gegebenes Wort ein Palindrom ist.
    Denken Sie an Groß- und Kleinschreibung.

[Hier](../Muster/Klausur/dka_palindrom.py) finden Sie die Musterlösung.
