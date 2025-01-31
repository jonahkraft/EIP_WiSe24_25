## Einfache Funktionen

1.  Schreiben Sie eine Funktion, die eine ganze Zahl $n$ übergeben bekommt. Die Funktion soll eine $n \times n$ Matrix
    zurückgeben, bei der in jeder Zelle (i, j) steht, ob $i + j$ durch 3 teilbar ist.
2.  Schreiben Sie eine Funktion, die alle Elemente in einer Liste um 1 nach links verschiebt. Ihre Lösung soll in-place
    arbeiten, das heißt, Sie dürfen keine weitere Liste verwenden.
3.  Schreiben Sie eine rekursive Funktion, die eine Liste übergeben bekommt und eine tiefe
    Kopie dieser Liste zurückgibt (analog zu deepcopy aus dem copy-Modul).
4.  Schreiben Sie eine rekursive Funktion, die den ggT von zwei Zahlen a, b berechnet.
5.  Schreiben Sie eine rekursive Funktion, die eine Liste von Ganzzahlen übergeben bekommt und das arithmetische Mittel zurückgibt.
6.  Schreiben Sie eine rekursive Funktion, die die Länge einer gegebenen Liste zurückgibt.
7.  Schreiben Sie eine rekursive Funktion, die die Anzahl der geraden Zahlen in einer Liste zurückgibt.
8.  Schreiben Sie eine rekursive Funktion, die die Anzahl der Primzahlen in einer Liste von Zahlen zurückgibt.

[Hier](../Muster/Bonusaufgaben/simple_funcs.py) finden Sie die Musterlösung.

---

## Dynamische Programmierung

Bei dynamischer Programmierung speichern wir Zwischenergebnisse zwischen, die sonst mehrfach berechnet werden.

### Aufgabe 1
Sie kennen bereits die Fibonacci-Funktion. Implementieren Sie diese rekursiv. Skizzieren Sie den Aufrufbaum von Fibonacci(10).
Überlegen Sie sich eine Möglichkeit, Zwischenergebnisse zwischenzuspeichern, um keine redundanten Berechnungen mehr auszuführen
und die Laufzeit so drastisch zu verringern (das wird bei größeren Eingabewerten deutlich) und implementieren Sie diese.

### Aufgabe 2
Schreiben Sie eine rekursive Funktion, die den Binomialkoeffizienten nCk mit der Formel nCk = (n-1)C(k-1) + (n-1)C(k)
berechnet. Analog zu Aufgabe 1 sollen Sie sich überlegen, wie man mithilfe von dynamischer Programmierung die Laufzeit verbessern
kann und dies implementieren.

[Hier](../Muster/Bonusaufgaben/dynamic_programming.py) finden Sie die Musterlösung.

---

## Automatisiertes Inhaltsverzeichnis

Sie sind Übungsleiter in EiP und haben für Ihre Gruppe einige Erklär-Dateien angelegt, in denen Sie die Grundlagen
von Python erklären. Jetzt fehlt aber noch ein Inhaltsverzeichnis. Das händisch zu erzeugen, wäre nervig. Stattdessen
wollen Sie es mit Code erzeugen.

Ziel der Aufgabe ist es, ein Inhaltsverzeichnis analog zu der Datei "00_inhaltsverzeichnis.md" zu erzeugen.

Lesen Sie dazu alle Dateien (außer dem Inhaltsverzeichnis selbst) aus dem Ordner "Erklär-Dateien" ein. Verwenden Sie dazu das
os-Modul (siehe unten). Es ist nicht Sinn der Aufgabe, die Dateinamen in den Programmcode zu schreiben. Stattdessen soll lediglich
das Verzeichnis angegeben werden und Ihr Programm findet die entsprechenden Dateien dann selbstständig in dem Verzeichnis.

Fügen Sie für alle Dateien den Titel und einen Link zu der Datei hinzu. In Markdown erzeugt man Titel, indem man
Hashtags davor schreibt (mind. 1, max. 6, je mehr, desto kleiner). Links erzeugt man, indem man in eckigen Klammern
den blau markierten Text schreibt und direkt dahinter in runden Klammern den Pfad (in dem Fall einfach der Dateiname,
weil sich das Inhaltsverzeichnis im selben Verzeichnis wie die anderen Dateien befindet).

Alle relevanten Überschriften in den Dateien werden mit # oder ## gekennzeichnet. Für alle diese Überschriften soll es
einen Bullet Point geben (indem man - davor schreibt). Achtung: In den Codeblöcken werden Kommentare auch mit
einem Hashtag eingeleitet. Diese sollen ignoriert werden. Auch gibt es Überschriften, die mit ### beginnen. Diese sollen auch
ignoriert werden.

Denken Sie an Zeilenumbrüche.
Speichern Sie das Ergebnis als Datei "00_inhaltsverzeichnis.md".

Hinweis: Schauen Sie sich an, wie das os-Modul funktioniert. Eine kurze (ausreichende) Einführung gibt es [hier](../../Erklär-Dateien/08_os_modul.md)

[Hier](../Muster/Bonusaufgaben/generate_table_of_content.py) finden Sie die Musterlösung.

---

## Conway's Game of Life

Wir wollen [Conways Spiel des Lebens](https://de.wikipedia.org/wiki/Conways_Spiel_des_Lebens) implementieren und in einfacher 
Form visualisieren. Als Datenstruktur für das Spielfeld benutzen wir eine Matrix, dargestellt als zweidimensionale Liste. 
Jeder Eintrag der Liste (im Folgenden Zelle genannt) kann nur zwei verschiedene Werte annehmen: `.` für tot und `o` für lebendig. 
Es gibt vier Regeln, wie sich die Belegung des Spielfeldes von einer Generation zur nächsten verändert:  

1. Wenn eine tote Zelle genau drei lebende Nachbarzellen hat, wird sie zum Leben erweckt.
2. Eine lebende Zelle mit weniger als zwei lebenden Nachbarnzellen stirbt.  
3. Eine lebende Zelle mit zwei oder drei lebenden Nachbarnzellen bleibt am Leben.
4. Eine lebende Zelle mit mehr als drei lebenden Nachbarzellen stirbt.  

### Aufgabe 1
Schreiben Sie eine Funktion, die die Datei [conway.txt](../resources/conway.txt) einliest und eine Matrix zurückgibt,
die das Spielfeld darstellt. Jedes Zeichen in der Datei soll ein Eintrag in der Matrix sein.

### Aufgabe 2
Implementieren Sie nun Conways Spiel des Lebens mit den obenstehenden Regeln. Wenn eine Zelle am Rand der Matrix ist, müssen
Sie nur die Nachbarzellen innerhalb der Grenzen der Matrix beachten.

### Aufgabe 3 (Bonus)
Visualisieren Sie das Spiel des Lebens mit basicIO (hierzu gibt es keine Musterlösung)

[Hier](../Muster/Bonusaufgaben/conway.py) finden Sie die Musterlösung. 

---

## Wächter

Nun simulieren wir ein das Verhalten eines Wächters, der ein Areal bewacht.

### Aufgabe 1
Schreiben Sie zuerst eine Funktion, die die Datei [guard.txt](../resources/guard.txt) einliest und eine Matrix zurückgibt,
die das Spielfeld darstellt. Jedes Zeichen in der Datei soll ein Eintrag in der Matrix sein.

In der Matrix stellt `.` eine leere Zelle dar. `#` ist ein Hindernis und `<`, `>`, `v` und `^` stellen Wächter dar, wobei
diese immer in die Pfeilrichtung schauen.

### Aufgabe 2
In der Matrix ist ein Wächter. Dieser bewegt sich so lange geradeaus (basierend auf seiner Blickrichtung), bis
er auf ein Hindernis trifft. Wenn das passiert, dreht er sich um 90 Grad nach rechts (basierend auf seiner Blickrichtung)
und geht erst im nächsten Frame weiter (als Frame bezeichnen wir einen Iterationsschritt in der while-Schleife, in der
das Spiel läuft). Wenn der Wächter das Spielfeld verlässt, soll er auf der gegenüberliegenden Seite des Spielfelds erscheinen
(seine Richtung ändert er dabei nicht).

<details>
  <summary>Tipp 1</summary>
  Schreiben Sie eine Funktion, die testet, ob sich eine gegebene Position innerhalb der Grenzen der Matrix befindet.  
</details>
<details>
  <summary>Tipp 2</summary>
  Schreiben Sie eine Funktion, die den Wächter in der Matrix bewegt.  
</details>
<details>
  <summary>Tipp 3</summary>
  Schreiben Sie eine Funktion, die die Richtung des Wächters ändert.
</details>

### Aufgabe 3 (Bonus)
Visualisieren Sie das Verhalten des Wächters mit basicIO (hierzu gibt es keine Musterlösung)


[Hier](../Muster/Bonusaufgaben/guard.py) finden Sie die Musterlösung.

---

## Parkettierung

In dieser Aufgabe befassen wir uns mit einem Parkettierungsproblem. Gegeben ist eine $n \times n$ Matrix mit $n = 2^k, k \in \mathbb{N}$.
Eine Zelle der Matrix bleibt ausgespart. Die übrigen Zellen sollen in L-förmigen Kacheln überdeckt werden, die je drei Zellen überdecken.

### Aufgabe 1
Eine notwendige Bedingung dafür, dass dies möglich ist, ist, dass die Zahl n^2 - 1 = (2^k)^2 -1 durch 3 teilbar ist.  
Beweisen Sie dies.

### Aufgabe 2
Die Divide-and-conquer-Strategie ermöglicht uns, dieses Problem zu lösen. Die Idee ist folgende:
Wir teilen den gerade betrachteten Bereich der Matrix (am Anfang ist das die gesamte Matrix) in 4 Quadranten auf. In
genau einem dieser Quadranten ist bereits eine Zelle belegt (überlegen Sie sich, warum das wahr ist).  

Schreiben Sie nun eine Funktion `tile(matrix, m, x, y, counter)`, welche wie folgt arbeiten soll.  

Die Matrix ist die gesamte Matrix, die wir betrachten. Darin repräsentiert `.` eine leere Zelle, `x` die blockierte Zelle und Zellen, die mit einer Zahl versehen sind,
wurden bereits parkettiert. Das Argument `m` sagt aus, dass die gerade betrachtete Teilmatrix eine $m \times m$ Matrix ist.
Die Argumente `x` und `y` sind die x- und y-Koordinate der oberen linken Zelle in der betrachteten Teilmatrix. `counter` zählt die
Anzahl der Parkettierungen von je drei Zellen. Diese werden mit `str(counter)` parkettiert, damit man später erkennen kann,
wann was parkettiert wurde.

<details>
  <summary>Tipp</summary>
  Ihre Funktion soll ermitteln, in welchem der Quadranten die blockierte Zelle ist. In den anderen drei Quadranten soll jeweils
die Zelle parkettiert werden, die der Mitte der betrachteten Teilmatrix am nächsten ist. Dann sollen rekursiv alle vier Quadranten
parkettiert werden. 
</details>

Die Idee von Divide-and-conquer ist es, das Problem in kleinere Teilprobleme aufzuteilen, die einfach gelöst werden können.
In unserem Fall ist es, dass wir das Problem für eine gegebene Teilmatrix lösen und dann rekursiv mit derselben Funktion
die vier Teilprobleme (die Quadranten) lösen.

#### Beispiel:

Gegeben sei die folgende Matrix:

```
 .  .  .  .  .  .  .  . 
 .  .  .  .  .  .  .  . 
 .  .  .  .  .  .  x  . 
 .  .  .  .  .  .  .  . 
 .  .  .  .  .  .  .  . 
 .  .  .  .  .  .  .  . 
 .  .  .  .  .  .  .  . 
 .  .  .  .  .  .  .  . 
```

Schritt 1:

```
 .  .  .  .  .  .  .  . 
 .  .  .  .  .  .  .  . 
 .  .  .  .  .  .  x  . 
 .  .  .  1  .  .  .  . 
 .  .  .  1  1  .  .  . 
 .  .  .  .  .  .  .  . 
 .  .  .  .  .  .  .  . 
 .  .  .  .  .  .  .  .
```

Schritt 2 (Rekursionsaufruf für den oberen rechten Quadranten):

```
 .  .  .  .  .  .  .  . 
 .  .  .  .  .  2  2  . 
 .  .  .  .  .  2  x  . 
 .  .  .  1  .  .  .  . 
 .  .  .  1  1  .  .  . 
 .  .  .  .  .  .  .  . 
 .  .  .  .  .  .  .  . 
 .  .  .  .  .  .  .  . 
```

usw.

Ergebnis:

```
 9  9  8  8  4  4  3  3 
 9  7  7  8  4  2  2  3 
10  7 11 11  5  2  x  6 
10 10 11  1  5  5  6  6 
14 14 13  1  1 19 18 18 
14 12 13 13 19 19 17 18 
15 12 12 16 20 17 17 21 
15 15 16 16 20 20 21 21 
```

[Hier](../Muster/Bonusaufgaben/tiling_problem.py) finden Sie die Musterlösung für Aufgabe 2.

---

## Binäre Suche

Ein Vorteil sortierter Listen ist es, dass wir Elemente darin schnell finden können. Dafür gibt es den Algorithmus
"binäre Suche". Dieser funktioniert wie folgt. Wir vergleichen das mittlere Element der Liste mit unserem gesuchten
Element. Wenn das mittlere Element gleich dem gesuchten Element ist, sind wir fertig. Wenn das gesuchte Element kleiner
als das mittlere Element ist, suchen wir in der linken Hälfte der Liste. Analog suchen wir in der rechten Hälfte der Liste,
wenn das gesuchte Element größer als das mittlere Element ist.

### Aufgabe 1

Implementieren Sie die Funktion `binary_search(a, x)` iterativ. `a` bezeichnet das Array (bzw. die Liste in Python) und
`x` das gesuchte Element. Die Funktion soll den Index (0 basiert) des Elements ausgeben, falls es enthalten ist und
-1, falls es nicht enthalten ist. Sie dürfen kein list slicing verwenden (das ruiniert die Laufzeit)

### Aufgabe 2

Implementieren Sie die Funktion aus Aufgabe 1 vollständig rekursiv, also ohne Verwendung von Schleifen. Sie dürfen nach wie
vor kein list slicing verwenden.

<details>
  <summary>Tipp</summary>
Übergeben Sie Ihrer rekursiven Funktion zusätzlich zwei weitere Argumente "left" und "right".
</details>

[Hier](../Muster/Bonusaufgaben/binary_search.py) finden Sie die Musterlösung


---

## Breitensuche

In dieser Aufgabe wollen wir uns mit dem Suchen des schnellsten Wegs von einem Punkt zu einem anderen Punkt auseinandersetzen.
Dafür verwenden wir den Breitensuche-Algorithmus. Lassen Sie sich nicht von der Aufgabe abschrecken! Es ist (auch für das
Praktikum) sinnvoll, den Algorithmus zu kennen.

### Aufgabe 1
In der Datei [maze.txt](../resources/maze.txt) finden Sie ein Labyrinth. Schreiben Sie eine Funktion `read_maze(path)`,
die den Dateipfad übergeben bekommt und eine Matrix mit allen Zellen des Labyrinths zurückgibt. `█` symbolisiert eine Wand, ein
Leerzeichen symbolisiert eine freie Zelle, `S` ist der Startpunkt und `Z` ist der Zielpunkt.

### Aufgabe 2
Schreiben Sie eine Funktion `draw_maze(maze)`, die das Labyrinth in die Konsole zeichnet.

### Aufgabe 3
Schreiben Sie eine Funktion `find(maze, s)`, der man einen String, z.B. den Startpunkt S übergibt. Die Funktion soll die Koordinaten
dieses Punktes zurückgeben und (-1, -1), falls er nicht enthalten ist.

### Aufgabe 4
Nun wollen wir das Labyrinth lösen. Schreiben Sie eine Funktion `bfs(maze, start, dest)` (bfs ist die englische Abkürzung für Breitensuche),
die überprüft, ob es möglich ist, vom Startpunkt zum Zielpunkt zu kommen und gegebenenfalls den kürzesten Weg zurückgibt 
(in unserem Beispiel existiert ein solcher Weg). `maze` ist die Matrix, die Sie am Anfang einlesen. `start` und `dest` sind
der Start- und Zielpunkt in einem geeigneten Format.

Gehen Sie wie folgt vor:
1.  Legen Sie eine leere Liste `queue` an. Dort speichern wir später die Koordinaten der Zellen, die wir als nächstes betrachten.  
    Legen Sie eine Matrix `visited` an, in der Sie speichern, welche Zellen bereits besucht wurden.  
    Legen Sie eine Matrix `pred` an, in der Sie speichern, welche Zellen welche Vorgängerzelle haben.  
    <details>
      <summary>Tipp</summary>
    In visited[i][j] sollte stehen, ob maze[i][j] bereits besucht wurde. Analog sollte in pred die Vorgängerzelle stehen
    (oder (-1, -1), falls es keine gibt).
    </details>

2.  Falls queue leer ist, gehen Sie zu Schritt 6
3.  Poppen Sie das erste Element aus queue. Aktualisieren Sie visited. Bestimmen Sie alle noch nicht besuchten Nachbarzellen,
    die keine Wand sind.
4. Aktualisieren Sie queue und pred
5. Gehen Sie zu Schritt 2
6. Falls der Zielpunkt nicht besucht wurde, geben Sie `None` zurück.
7. Nun wollen wir den kürzesten Pfad vom Start- zum Zielpunkt extrahieren. Überlegen Sie sich hierfür eine geeignete
   Lösung unter Verwendung von `pred`. Beachten Sie, dass der Weg in der richtigen Reihenfolge ist.
   <details>
      <summary>Tipp</summary>
   Starten Sie beim Zielpunkt und schauen sie sich die vorher besuchte Zelle hiervon an, dann die vorher besuchte Zelle
   der vorher besuchten Zelle usw., bis Sie den Startpunkt erreichen.
    </details>
8. Geben Sie den gefundenen Weg zurück.

### Aufgabe 5
Schreiben Sie eine Funktion `draw_maze_with_path(maze, path)`, die den von bfs berechneten Weg in die übergebene Matrix
einzeichnet (Zellen durch "x" ersetzen). Der Start- und Zielpunkt sollen nicht ersetzt werden. Anschließend soll die
Funktion Ihre `draw_maze`-Funktion aufrufen, um das Labyrinth mit dem nun hinzugefügten Weg zu zeichnen.

### Aufgabe 6 (Bonus)
Visualisieren Sie den Weg mit basicIO (hierzu gibt es keine Musterlösung)

Bemerkung: Abhängig von der Reihenfolge, in der Sie alle möglichen Richtungen testen, kann es passieren, dass sich Ihre
Lösung und meine Musterlösung beim kürzesten Pfad minimal unterscheiden. Der Weg sollte aber gleich lang sein.

[Hier](../Muster/Bonusaufgaben/bfs.py) finden Sie die Musterlösung.