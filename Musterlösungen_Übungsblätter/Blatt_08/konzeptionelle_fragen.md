## Statische Typisierung
In Python können Typen von Variablen mit Typannotationen versehen (und dann mit mypy geprüft werden).
Nennen Sie je einen Vor- und einen Nachteil davon, Variablen im Programmcode mit festen Typen zu versehen (für ExpertInnen: wir
nutzen keine Generics).

### Antwortvorschläge

#### Vorteile

- macht Code lesbarer (insbesondere bei größeren Projekten), da beispielsweise bei Funktionen
immer klar ist, welche Typen die Argumente haben sollen.
- macht Code sicherer, indem es vermeidet (siehe eben), dass versehentlich falsche Typen verwendet werden
- macht Code sicherer, indem es (je nachdem wie man mypy einstellt) vermeidet, dass es zu unerwartetem Verhalten kommt,
beispielsweise wenn man mit Listen arbeitet, die mehrere Datentypen, z.B. str, bool und int enthalten, da Typprüfungen
notwendig sind (mypy bekommt sonst einen Nervenzusammenbruch, aber man sollte es grundsätzlich aus den genannten Gründen
avoiden, mehrere Datentypen in einer Liste zu speichern)

#### Nachteile

- ist unflexibler, da man ohne Typprüfungen bei Bedarf den Datentyp von Variablen ändern kann, z.B. von int zu float
  (normalerweise aber unerwünscht)
- ist unflexibler, da man ohne Typprüfungen beispielsweise Einstellungen für ein Programm in einem Dictionary speichern
und verwenden kann. In dem angehängten Beispiel ist `is_darkmode_on` offensichtlich immer ein boolscher Wert und
`username` immer ein String, aber mypy erzwingt trotzdem Typprüfungen. `settings: dict[str, bool | str] = {'is_darkmode_on': True, 'username': 'Rainer Zufall'}`
- kann - je nachdem wie intensiv man Typhints verwendet (mypy erzwingt sie nicht überall) - ein Overkill sein, weil es in
einigen Fällen offensichtlich ist. Z.B. `x = "Hello, world"` braucht keinen Typehint, damit man
versteht, dass es sich dabei um einen String handelt.

---

## Objekte und Referenzen

Lesen Sie den folgenden Programmcode und geben Sie das Ergebnis der Vergleiche (a) und (b) (c) und (d) mit
Begründung an

### Antwortvorschlag

`==` verwendet die `__eq__`-Methode der Klasse (hier Frac) und vergleicht, ob der Wert der beiden
Variablen übereinstimmt.  
`is` überprüft, ob der Wert der beiden Variablen am selben Ort im Speicher ist, sie also komplett identisch sind.
Variablen selbst speichern intern einen Verweis auf diese Speicheradresse. Bei `z = x` wird also nicht der Wert kopiert,
sondern nur der "Pointer" auf die Speicheradresse.

Das ist insbesondere bei mutablen Datentypen wie Listen von Bedeutung.

Daher sind die Ergebnisse:
(a) True
(b) False
(c) True
(d) True
