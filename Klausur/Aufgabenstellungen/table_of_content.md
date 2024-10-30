## Erstellung eines Inhaltsverzeichnisses für die Erklär-Dateien.

Sie sind Übungsleiter in EiP und haben für Ihre Gruppe einige Erklär-Dateien angelegt, in denen Sie die Grundlagen
von Python erklären. Jetzt fehlt aber noch ein Inhaltsverzeichnis. Das händisch zu erzeugen, wäre nervig. Stattdessen
wollen Sie es mit Code erzeugen.

Ziel der Aufgabe ist es, ein Inhaltsverzeichnis analog zu der Datei "00_inhaltsverzeichnis.md" zu erzeugen.

Lesen Sie dazu alle Dateien (außer dem Inhaltsverzeichnis selbst) aus dem Ordner "Erklär-Dateien ein".
Fügen Sie für alle Dateien den Titel und einen Link zu der Datei hinzu. In Markdown erzeugt man Titel, indem man
Hashtags davor schreibt (mind. 1, max. 6, je mehr, desto kleiner). Links erzeugt man, indem man in eckigen Klammern
den blau markierten Text schreibt und direkt dahinter in runden Klammern den Pfad (in dem Fall einfach der Dateiname).

Alle relevanten Überschriften in den Dateien werden mit # oder ## gekennzeichnet. Für alle diese Überschriften soll es
einen Bullet Point geben (in Markdown einfach, indem man - davor schreibt). Achtung: In den Codeblöcken werden Kommentare auch mit
einem Hashtag eingeleitet. Diese sollen ignoriert werden. Auch gibt es Überschriften, die mit ### beginnen. Diese sollen auch
ignoriert werden.

Speichern Sie das Ergebnis als Datei "00_inhaltsverzeichnis.md".

---

[Hier](../Muster/generate_table_of_content.py) finden Sie die Musterlösung.
