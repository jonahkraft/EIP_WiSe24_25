## Aufgaben zum Lernen für die Klausur

### Aufgabe 1

i) Schreiben Sie eine Funktion, die eine Liste von Ints übergeben bekommt und nur die geraden Zahlen in einer Liste zurückgibt. Verwenden Sie nicht den %-Operator.

ii) Schreiben Sie eine Funktion, die einen Int übergeben bekommt und die Anzahl der Ziffern zurückgibt. Sie dürfen den Datentyp der Zahl nicht ändern.

iii) Schreiben Sie die Funktion aus ii rekursiv.

iv) Schreiben Sie eine Funktion, die eine Liste von Strings übergeben bekommt und die Anzahl der Worte zurückgibt, die mehr als 5 Buchstaben enthalten.

v) Schreiben Sie eine Funktion, die eine Liste von Strings übergeben bekommt und die Anzahl der Worte zurückgibt, die ein 'e' enthalten und mehr als 5 Buchstaben haben. Die Gross-/Kleinschreibung soll ignoriert werden.

vi) Schreiben Sie eine Funktion, die eine Liste von Ints übergeben bekommt und die Anzahl der Zahlen zurückgibt, die durch 3 oder 5 teilbar sind, aber nicht durch beide.

vii) Schreiben Sie eine Funktion, die eine Liste von Ints und eine Zahl n übergeben bekommt und die Liste in Teillisten unterteilt, sodass die Summe jeder Teilliste höchstens n beträgt.

---

### Aufgabe 2

In der Datei [DAX.csv](../resources/DAX.csv) finden Sie Informationen zum Kurs des Global X DAX Germany ETF (DAX) in den letzten 10 Jahren.
Das ist ein ETF, der in etwa den DAX abbildet.

i) Schreiben Sie eine Funktion, die die Datei einliest und in einem geeigneten Format speichert.

ii) Schreiben Sie eine Funktion, die den niedrigsten, höchsten und durchschnittlichen Eröffnungspreis berechnet.

iii) Schreiben Sie eine Funktion, die den Tag mit dem größten Preissprung (Differenz zwischen Tief und Hoch) findet.

iv) Schreiben Sie eine Funktion, die die Gesamtzahl der Handelstage berechnet, an denen der Schlusspreis höher war als der Eröffnungspreis.

v) Schreiben Sie eine Funktion, die das durchschnittliche Wachstum des DAX berechnet, also den Durchschnitt der prozentualen Änderung zwischen Eröffnungs- und Schlusspreis.
Sie können davon ausgehen, dass der Eröffnungspreis nie 0 ist.

---

### Aufgabe 3

i) Schreiben Sie eine Klasse Car mit Attributen für Marke, Modell und Baujahr. Implementieren Sie Getter und Setter für diese
Attribute.

ii) Schreiben Sie eine Methode, die das Alter eines Autos berechnet. Mit date.today() aus dem datetime-Modul können Sie das aktuelle Datum in der Form YYYY-MM-DD abrufen.

iii) Schreiben Sie eine geeignete str- und repr-Methode für die Car-Klasse

iv) Schreiben Sie eine lt-Methode, die die Baujahre von 2 Autos vergleicht.

v) Erstellen Sie eine Klasse Garage, die eine Liste von Autos enthält. Implementieren Sie Methoden, um Autos hinzuzufügen und zu entfernen, sowie eine Methode, die das älteste Auto in der Garage zurückgibt.

vi) Schreiben Sie eine geeignete str-Methode für die Garage-Klasse

---

## Aufgabe 4

In dieser Aufgabe wollen wir die Potenz einer gegebenen Zahl berechnen. Offensichtlich sind der **-Operator und
Funktionen, die genau das berechnen, nicht erlaubt. Sie können davon ausgehen, dass beide Zahlen, die ihre Funktion bekommt,
positive natürliche Zahlen sind.

(i) Schreiben Sie eine iterative Funktion, die die Potenz einer gegebenen natürlichen Zahl n berechnet.

(ii) Schreiben Sie die Funktion aus (i) rekursiv.

Hinweis: Wenn in der Aufgabenstellung steht, dass eine Funktion rekursiv sein soll, bedeutet das, dass es nicht der Sinn
der Aufgabe ist, eine rekursive Hilfsfunktion zu schreiben und die dann aufzurufen.

---

## Aufgabe 5

In dieser Aufgabe wollen wir Listen umdrehen. Das heisst, die Funktion bekommt eine Liste wie [1, 2, 3] und gibt
manipuliert sie so, dass die Elemente rückwärts darin stehen,
also hier [3, 2, 1]. Offensichtlich sind liste[::-1], liste.reverse() und reversed(liste) verboten.

(i) Schreiben Sie die Funktion iterativ.

(ii) Schreiben Sie die Funktion rekursiv.

---

## Aufgabe 6

In der Datei [index.html](../resources/index.html) finden Sie die Struktur einer (sehr simplen) Webseite. Schreiben Sie eine Funktion, die den Dateinamen
übergeben bekommt und eine Liste zurückgibt, die alle Überschriften enthaelt. In html kann man diese folgendermassen erkennen.
Es gibt einen Opening-Tag, dann steht da die Überschrift und dann der Closing-Tag.
Der Opening-Tag steht in <>. Darin steht (in unserem Fall, im Allgemeinen komplexer) erst der Buchstabe h und dann eine Zahl.
Der Closing-Tag sieht in dem Fall prinzipiell genauso aus, aber hinter dem < ist ein /.
Aus `<h1>Hauptüberschrift</h1>` soll also nur "Hauptüberschrift" extrahiert werden.

---

## Aufgabe 7

In dieser Aufgabe widmen wir uns dem [Zipfschen Gesetz](https://de.wikipedia.org/wiki/Zipfsches_Gesetz).
[Hier](../resources/faust.txt) finden Sie die benötigte Datei faust.txt.

(i) Schreiben Sie eine Funktion, die den Dateinamen als übergeben bekommt. 
Legen Sie ein Dictionary an, das für alle Wörter deren Häufigkeit speichern sollen (Dict[str, int])
Die Funktion soll die Datei zeilenweise einlesen. Ignorieren Sie den Vorspann (Zeilen 1-23). Zunächst sollen sie alle Sonderzeichen aus der Zeile entfernen.
Hinweis: Sie können das string-Modul importieren. string.punctuation ist ein String, der alle ASCII-Sonderzeichen enthält.
Ignorieren Sie ferner Groß- und Kleinschreibung. Die Funktion soll das Dictionary zurückgeben. Bestimmen Sie anschliessend 
die häufigsten 100 Wörter und beurteilen Sie, ob das Zipfsche Gesetz zutrifft.

---

[Hier](../Muster/klausur_aufgaben_muster.py) finden Sie die Musterlösung.