## Einführung in die Programmierung: Wintersemester 24/25

### Disclaimer
> Die Inhalte dieses Repositories sind nicht von offizieller Stelle, sondern werden auf freiwilliger Basis
> zusätzlich zur Verfügung gestellt!
> 
> Erklär-Dateien könnten Fehler enthalten. Solltest du einen Fehler finden, gib bitte Bescheid.
> Selbiges gilt auch für Musterlösungen.
> 
> Musterlösungen erstelle ich, sofern ich genug Zeit habe. Es gibt KEINE Garantie, dass es welche gibt.
> 
> Erklär-Dateien sind KEIN Ersatz der Vorlesung und haben auch nicht die Intention, dies zu sein, sondern dienen lediglich
> als Ergänzung und bieten ggf. die Möglichkeit, über den Tellerrand hinauszuschauen.
> Es gibt KEINE Garantie, dass alle Themen der Vorlesung hier abgedeckt werden, aber möglicherweise werden hier Themen
> abgedeckt, die nicht in der Vorlesung drankamen und nicht klausurrelevant sind. Es kann gut sein, dass es in der Vorlesung
> eine andere Reihenfolge der Themen gibt, daher am Anfang jeder Datei ein Vermerk, was man für das Verständnis dieser Datei
> bereits wissen sollte.
> 
> Zur Vorbereitung auf die Klausur gibt es ebenfalls Aufgaben. Diese repräsentieren möglicherweise nicht alles, was für 
> die Klausur relevant ist oder Themen, die nicht klausurrelevant sind. Diese Aufgaben sind NICHT dazu gedacht, die 
> alleinige Klausurvorbereitung zu sein, sondern dienen als Hilfe, die eigenen Programmierkenntnisse zu verbessern und 
> ein Gefühl für die Art von Aufgaben zu bekommen, die ggf. drankommen könnten.
> 
> Da auch wir Übungsleiter die Klausur NICHT vorher sehen, können wir Fragen wie "Ist das klausurrelevant?" oder "Kommt das dran?"
> gar nicht oder nur teilweise beantworten.
> 
> Auch wichtig: Die Antworten auf einige der untenstehenden Fragen (soweit nicht technisch), enthalten Meinungen. Du
> darfst das gerne anders sehen. Nichts ist in Stein gemeißelt. Du solltest kritisch hinterfragen, was du hier liest.


### Was erwartet mich hier?
> Wie eben bereits angedeutet, wird es hier Erklär-Dateien, Aufgaben (zur Klausurvorbereitung) und (wenn genug Zeit)
> Musterlösungen von Übungsblättern geben. Diese sind jeweils auf die drei Ordner aufgeteilt und werden im Laufe
> des Semesters mit Material gefüllt.


### Welche Literatur und Tutorials sollte ich kennen?
> Das Standardwerk zu Python 3 im deutschsprachigen Raum ist "Python 3" von Johannes Ernesti und Peter Kaiser, das du
> [hier](https://openbook.rheinwerk-verlag.de/python/) kostenlos digital lesen kannst.
> Alternativ gibt es einige gedruckte Exemplare in der MINT-Bereichsbibliothek
> (ggf. ältere Auflagen, aber das ist egal).  
> Außerdem gibt es im Web einige nützliche Seiten, z.B. [w3schools](https://www.w3schools.com/python/default.asp).  
> Auf YouTube gibt es ein 12 Stunden Video von [Bro Code](https://www.youtube.com/watch?v=ix9cRaBkVe0) (das Video geht teilweise über die Vorlesung hinaus und behandelt ggf. auch Themen,
> die hier erst in "Einführung in die Softwareentwicklung" thematisiert werden)
> 
> Tutorials bzw. Erklär-Dateien gibt es auch hier.
> 
> Auch ChatGPT kann gut erklären, aber bitte lass dir davon nicht die Aufgaben lösen. 
> Auch wir Übungsleiter können ChatGPT nutzen und schauen, ob eure Lösung daher kommt :)
> 
> Es gibt natürlich noch viele andere tolle Möglichkeiten, mehr zu lernen.


### Was bedeutet IDE? Wo schreibe ich meinen Code?
> IDE bedeutet Integrated Development Environments. Es bezeichnet Software, die dazu gedacht ist, andere Software zu entwickeln.
> IDEs bieten einige nützliche Features, die über normale Texteditoren hinausgehen, kommen aber oft mit einem höheren
> Konsum an Speicher und Arbeitsspeicher einher.
> Für Python gibt es PyCharm, VS Code, Zed und für die Hartgesottenen Vim, Sublime Text etc.
> Im Grunde ist es egal, was man nutzt, solange man damit klarkommt und es kein Papier ist!


### Wo finde ich Altklausuren?
> Es gibt Altklausuren auf der [Website der Fachschaft](https://fachschaft.mathe-informatik.uni-mainz.de) und im Moodle-Kanal
> der Fachschaft. Bei Moodle auf die Startseite gehen, dann "Kurse suchen" und "Fachschaft Mathematik+Informatik" suchen.
> In dem Moodle-Kanal gibt es unter dem Reiter "Informationen" Altklausuren.
> Wichtig: Es gibt bei Moodle und auf der Webseite ggf. andere Altklausuren!


### Wie führe ich Python-Code aus?
> Wenn du eine Python Datei (Suffix .py) erstellt und deinen Code geschrieben hast, kannst du sie ausführen.
> In IDEs wie PyCharm oder VSCode (ggf. Plugin nötig) gibt es die Möglichkeit, auf einen Run-Button zu klicken,
> der die Arbeit für dich übernimmt. Wenn das nicht geht, kannst du die Datei über das Terminal ausführen.
>
> Öffne das Terminal (in deinem Texteditor oder als App) und stelle sicher, dass du dich in dem Ordner befindest, in dem
> auch die Python-Datei liegt.
> Wenn das nicht der Fall ist, kannst du mit dem Befehl `cd Pfad/zu/dem/Ordner` dein Verzeichnis ändern.
> Gib dann folgenden Befehl ein: `python3 Name_deiner_datei.py` (Unix) oder `python Name_deiner_datei.py` (Windows)


### Wie installiere ich externe Module, die nicht in der Python-Standardbibliothek sind?
> Das hängt vom Betriebssystem ab. Wenn das Package bei pypy hochgeladen wurde, kannst du es via
> `pip install package_name` oder ggf. `pip3 install package_name` installieren (sollte unter macOS und Windows funktionieren,
> kann je nach Linux-Distro abweichen). Wichtig ist, dass du eine passende Python-Version installiert hast.
