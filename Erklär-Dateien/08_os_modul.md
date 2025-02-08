# Arbeiten mit dem `os`-Modul

Empfohlene Skills: [Datentypen und Operatoren](01_datentypen_operationen.md) und Grundkenntnisse in [Listen](04_listen.md)

---

Das `os`-Modul in Python bietet eine Schnittstelle zu Betriebssystem-Funktionen, die uns ermöglicht, 
Dateien und Verzeichnisse zu verwalten, das Arbeitsverzeichnis zu ändern, Pfade zu überprüfen und vieles mehr.

Eines vorab: Sollte man Pfade brauchen, um beispielweise Dateien einzulesen, ist es dringend zu empfehlen, diejenigen
Pfade, die im Programmcode stehen (z.B. wo eine Konfigurationsdatei zu finden ist), als relative Pfade zu verwenden, da
absolute Pfade auf anderen Rechnern ggf. nicht funktionieren.

## Aktuelles Arbeitsverzeichnis ermitteln

Die Funktion `getcwd()` (get current working directory) gibt das aktuelle Arbeitsverzeichnis zurück, in dem das Programm läuft.

### Beispiel:

```python
import os
print(os.getcwd())
```

Das Ergebnis dieser Funktion ist der **absolute Pfad** des aktuellen Verzeichnisses.


## Arbeitsverzeichnis ändern

Mit `chdir()` (change directory) kann das aktuelle Arbeitsverzeichnis geändert werden. Man gibt entweder einen 
**relativen** oder **absoluten Pfad** an.

### Beispiel:

```python
os.chdir("sub_dir")
print(os.getcwd())
```

Hier wird das Arbeitsverzeichnis in den Unterordner `sub_dir` geändert. Analog zum Beispiel eben gibt `os.getcwd()`
dennoch den absoluten Pfad zurück.

## Inhalte eines Verzeichnisses auflisten

Die Funktion `listdir()` gibt alle Dateien und Ordner im angegebenen Verzeichnis als Liste zurück.

### Beispiel:

```python
print(os.listdir())
```

Diese Funktion gibt eine unsortierte Liste der Dateien und Ordner im aktuellen Arbeitsverzeichnis zurück. Um die Liste 
alphabetisch zu sortieren, kann die Methode `sort()` angewendet werden. 

### Sortieren der Liste:

```python
file_list = os.listdir()
file_list.sort()
print(file_list)
```


## Überprüfen, ob eine Datei existiert

Mit `os.path.isfile()` kann überprüft werden, ob am angegebenen Pfad eine Datei existiert. Analog dazu prüft 
`os.path.isdir()`, ob es sich um einen Ordner handelt.

### Beispiel:

```python
print(os.path.isfile("file1.txt"))  # Gibt True zurück, wenn die Datei existiert
print(os.path.isdir("dir"))         # Gibt True zurück, wenn "dir" ein Ordner ist
```


## Existenz eines Pfades prüfen

Die Funktion `os.path.exists()` prüft, ob ein Pfad (Datei oder Verzeichnis) existiert. Das ist nützlich, um 
sicherzustellen, dass der Pfad gültig ist, bevor darauf zugegriffen wird.

### Beispiel:

```python
print(os.path.exists("file1.txt"))  # Gibt True zurück, wenn die Datei existiert
print(os.path.exists("file4.txt"))  # Gibt False zurück, wenn die Datei nicht existiert
```


## Verzeichnis erstellen

Mit `os.mkdir()` kann ein neues Verzeichnis erstellt werden, wenn es noch nicht existiert.

### Beispiel:

```python
os.mkdir("dir2")
```

Dieser Code erstellt einen Ordner namens `dir2` im aktuellen Arbeitsverzeichnis. Der Pfad kann relativ oder 
absolut angegeben werden.

### Mehrere Verzeichnisse auf einmal erstellen:

```python
os.makedirs("dir3/sub")
```

Dies erstellt sowohl das Verzeichnis `dir3` als auch das Unterverzeichnis `sub` darin, falls diese noch nicht existieren.


## Verzeichnis löschen

Mit `os.rmdir()` kann ein Verzeichnis gelöscht werden, jedoch **nur, wenn es leer ist**.

### Beispiel:

```python
os.rmdir("dir2")
```

Wenn der Ordner Dateien oder Unterordner enthält, muss erst alles darin gelöscht werden, bevor der Ordner 
selbst gelöscht werden kann.


## Datei oder Verzeichnis umbenennen

Die Funktion `os.replace()` wird verwendet, um eine Datei oder ein Verzeichnis umzubenennen.

### Beispiel:

```python
os.replace("dir3", "test_name")
```

Dieser Code benennt den Ordner `dir3` in `test_name` um, der Inhalt des Ordners bleibt dabei unverändert.


## Dateien löschen

Mit `os.remove()` können Dateien gelöscht werden. Wie bei `rmdir()` gibt es keine Wiederherstellung, 
sobald die Datei gelöscht ist, es wird nichts in den Papierkorb verschoben ;-)

### Beispiel:

```python
os.remove("file1.txt")
```

## Zusammenfassung

- **`os.getcwd()`**: Gibt das aktuelle Arbeitsverzeichnis zurück.
- **`os.chdir()`**: Ändert das aktuelle Arbeitsverzeichnis.
- **`os.listdir()`**: Listet alle Dateien und Ordner in einem Verzeichnis auf.
- **`os.path.isfile()`**: Überprüft, ob ein Pfad eine Datei ist.
- **`os.path.isdir()`**: Überprüft, ob ein Pfad ein Verzeichnis ist.
- **`os.path.exists()`**: Überprüft, ob ein Pfad existiert.
- **`os.mkdir()`**: Erstellt ein neues Verzeichnis.
- **`os.makedirs()`**: Erstellt mehrere Verzeichnisse gleichzeitig.
- **`os.rmdir()`**: Löscht ein leeres Verzeichnis.
- **`os.remove()`**: Löscht eine Datei.
- **`os.replace()`**: Benennt eine Datei oder einen Ordner um.

---

[vorherige Seite](07_dateien.md)  
[Zurück zum Inhaltsverzeichnis](00_inhaltsverzeichnis.md)  
[nächste Seite](09_funktionen.md)