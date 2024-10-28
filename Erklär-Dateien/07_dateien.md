# Dateien in Python einlesen und schreiben

Empfohlene Skills: [Datentypen und Operatoren](01_datentypen_operationen.md), [Kontrollstrukturen](02_kontrollstrukturen.md) und Grundkenntnisse in [Listen](04_listen.md)

---

Python bietet verschiedene Möglichkeiten, Dateien zu öffnen, zu lesen, zu schreiben und zu schließen. Im Folgenden
werden die grundlegenden Techniken zur Dateiverarbeitung vorgestellt.


## Das `open()`-Statement

Das `open()`-Statement wird verwendet, um eine Datei zu öffnen. Es gibt ein Dateihandles zurück, das für Lese- oder
Schreiboperationen verwendet wird.

### Syntax:

```python
file = open("dateiname.txt", "modus")
```

- **`"dateiname.txt"`**: Der Name der Datei, die du öffnen möchtest. Das Suffix muss nicht zwingend txt sein.
- **`"modus"`**: Der Modus, in dem du die Datei öffnest (siehe unten).


## Modi zum Öffnen einer Datei

Python bietet verschiedene Modi zum Öffnen einer Datei:

| Modus  | Beschreibung                                                 |
|--------|--------------------------------------------------------------|
| `'r'`  | Öffnet die Datei zum **Lesen**. Standardmodus.               |
| `'w'`  | Öffnet die Datei zum **Schreiben**. Überschreibt den Inhalt. |
| `'a'`  | Öffnet die Datei zum **Anhängen**. Fügt Daten am Ende hinzu. |
| `'b'`  | Öffnet die Datei im **Binärmodus**. (z. B. Bilder, Audio)    |
| `'r+'` | Öffnet die Datei zum **Lesen und Schreiben**.                |

### Beispiel:

```python
file = open("beispiel.txt", "r")  # Öffnet die Datei im Lesemodus
```


## Mit `with open()` Dateien öffnen

Die empfohlene Methode zum Arbeiten mit Dateien ist die Verwendung von `with open()`. Diese Methode schließt die Datei
automatisch nach der Operation, auch wenn ein Fehler auftritt.

### Syntax:

```python
with open("dateiname.txt", "modus") as file:
    # Operationen mit der Datei
```

### Beispiel:

```python
with open("beispiel.txt", "r") as file:
    content = file.read()
    print(content) 
```


## Methoden zum Lesen einer Datei

Es gibt mehrere Möglichkeiten, den Inhalt einer Datei zu lesen:

### 1. `read()`: Liest den gesamten Inhalt der Datei als String

```python
with open("beispiel.txt", "r") as file:
    content = file.read()
    print(content)
```

### 2. `readline()`: Liest eine Zeile der Datei

```python
with open("beispiel.txt", "r") as file:
    first_line = file.readline()
    print(first_line)
    # wenn man file.readline() wider ausführt, bekommt man die zweite Zeile, dann die dritte usw.
```

### 3. `readlines()`: Liest alle Zeilen der Datei und gibt sie als Liste zurück

```python
with open("beispiel.txt", "r") as file:
    all_lines = file.readlines()
    print(all_lines)
```


## Iterieren über eine Datei

Du kannst auch über die Datei iterieren, um Zeile für Zeile zu lesen:

```python
with open("beispiel.txt", "r") as file:
    for line in file:
        print(line, end="") 
```


## Schreiben in eine Datei

Zum Schreiben in eine Datei kannst du den Schreibmodus (`'w'`) oder den Anfügemodus (`'a'`) verwenden. Wenn die Datei
bereits existiert, überschreibt der Schreibmodus den Inhalt.

### Beispiel: Schreiben in eine Datei

```python
with open("output.txt", "w") as file:
    file.write("Dies ist eine neue Zeile.\n")
```

### Beispiel: Anfügen an eine Datei

```python
with open("output.txt", "a") as file:
    file.write("Dies wird am Ende der Datei hinzugefügt.\n")
```


## Datei schließen

Wenn du `open()` ohne `with` verwendest, musst du die Datei manuell schließen, um sicherzustellen, dass alle Ressourcen
freigegeben werden.

### Beispiel:

```python
file = open("beispiel.txt", "r")
content = file.read()
file.close()  # Datei wird geschlossen
```

---

[vorherige Seite](06_list_comprehension.md)  
[Zurück zum Inhaltsverzeichnis](00_inhaltsverzeichnis.md)  
[nächste Seite](08_os_modul.md)