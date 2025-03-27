Randomisierte Algorithmen in DSA sind die Algorithmen, die bei ihren Berechnungen Zufälligkeit nutzen, um ein gewünschtes Ergebnis zu erzielen. <mark style="background: #ADCCFFA6;">Diese Algorithmen führen Zufälligkeiten ein, um die Effizienz zu verbessern.</mark>

- Durch die Verwendung zufälliger Entscheidungen können randomisierte Algorithmen im Vergleich zu deterministischen Algorithmen häufig schnellere Lösungen oder bessere Näherungen liefern.
- Sie sind besonders nützlich in Situationen, in denen es schwierig ist, genauere Lösungen zu finden oder wenn ein probabilistischer Ansatz akzeptabel ist.
- z.B. bei randomized Quick Sort kann Pivot zufällig ausgewählt werden.
- Bogo sort
- **Vorteile**
	- Zeit- oder Raumkomplexität zu reduzieren
	- Für viele Probleme sind randomisierte Algorithmen viel schneller
	- einfach zu implementieren
	- Die gleiche Eingabe kann beim mehrmaligen Ausführen zu unterschiedlichen Ausgaben führen

- Laufzeit und Speicherbedarf hängt nicht immer von der Problemgrösse ab
	- Die Ausgabe ist eine Zufallsvariable
	- Die Laufzeit/Speicherbedarf ist eine Zufallsvariable
	- Für diese Zufallsvariablen werden wir Erwartungswerte haben wollen
- Ein Algorithmus, dass entweder true oder false zurückgibt
	- wenn alle möglichen Antworten gleich wahrscheinlich sind.(wir möchten es nicht)
	- wenn die Wahrscheinlichkeit, dass true kommt wahrscheinlicher ist. (ja)


### Las Vegas Algorithmen
- Ein "Las Vegas Algorithmus" ist ein probabilistischer Algorithmus, der immer ein korrektes Ergebnis liefert oder anzeigt, dass er gescheitert ist.
- Sie nutzen Zufälligkeit, um ihre Laufzeit zu beeinflussen, was zu unterschiedlichen Laufzeiten bei verschiedenen Ausführungen führen kann.
- Sie haben eine erwartete Laufzeit, die oft günstiger ist als die schlechteste Fall-Laufzeit eines deterministischen Algorithmus.
- Ein bekanntes Beispiel für einen Las Vegas Algorithmus ist der Randomized Quicksort. Hier wird das Pivotelement zufällig gewählt, was im Durchschnitt zu einer besseren Laufzeit führt als das deterministische Quicksort.
```python
import random

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return randomized_quicksort(less) + equal + randomized_quicksort(greater)
array = [3, 6, 8, 10, 1, 2, 1]
sorted_array = randomized_quicksort(array)
print(sorted_array)
```

### Monte-Carlo
- Ein Monte-Carlo-Algorithmus ist ein probabilistischer Algorithmus, der Zufälligkeit nutzt, um Ergebnisse zu berechnen. Im Gegensatz zu Las Vegas Algorithmen können Monte-Carlo-Algorithmen falsche Ergebnisse liefern, haben jedoch eine festgelegte Laufzeit.
- Sie sind besonders nützlich, wenn die exakte Berechnung zu aufwendig oder unmöglich ist und eine Näherungslösung ausreichend ist.
- Sie nutzen Zufallszahlen, um das Ergebnis zu berechnen.
- Die Korrektheit des Ergebnisses ist mit einer bestimmten Wahrscheinlichkeit garantiert.
- Die Laufzeit ist konstant oder hängt von einem vorgegebenen Parameter ab, aber sie variieren nicht während der Ausführung.
- True/False-Ausgaben
	- Bei true/false Ausgaben gibt es zwei Arten von Fehlern:
		- **Beidseitige Fehler (two-sided errors)**: Für beide Antworten (true oder false) besteht die Wahrscheinlichkeit, dass sie falsch sind, und diese Wahrscheinlichkeit ist größer als 0.
		- **Einseitige Fehler (one-sided errors)**: Eine der Antworten hat eine Fehlerwahrscheinlichkeit von 0, das heißt, wenn die Antwort beispielsweise "true" ist, dann ist diese Antwort immer korrekt.
- #### Beispiel: Identitätstest von großen Objekten
	- Idee1
		- Schaue auf die Länge der Strings.
		- Gib "true" zurück, falls L(a)=L(b).
		- Wenn a≠b (korrekt) ist, dann false → Fehlerwahrscheinlichkeit ist hoch.
		- Wenn true, dann Fehlerwahrscheinlichkeit ist hoch.
	- Idee 2 
		- Betrachte zufällig ausgewählte Positionen.
		- Falls a[i] == b[i] → true, sonst false.
		- Verbesserung: Wähle mehrere zufällige Positionen.
	- Idee 3
		- ![[Pasted image 20240621154730.png]]
```python
import random

def string_to_polynomial(string, x):
    """ Wandelt einen String in ein Polynom um und bewertet es bei x. """
    n = len(string)
    result = 0
    for i in range(n):
        result += ord(string[i]) * (x ** i)
    return result

def are_strings_equal(a, b, m):
    """ Überprüft, ob die Strings a und b gleich sind, durch Bewertung ihrer Polynome bei einem zufälligen r. """
    if len(a) != len(b):
        return False

    r = random.randint(0, m - 1)
    a_eval = string_to_polynomial(a, r)
    b_eval = string_to_polynomial(b, r)

    return a_eval == b_eval

# Beispielnutzung
a = "hello"
b = "hello"
m = 1000  # Großer Wert für m

if are_strings_equal(a, b, m):
    print(f"Die Strings '{a}' und '{b}' sind gleich.")
else:
    print(f"Die Strings '{a}' und '{b}' sind nicht gleich.")

# Test mit ungleichen Strings
a = "hello"
b = "world"

if are_strings_equal(a, b, m):
    print(f"Die Strings '{a}' und '{b}' sind gleich.")
else:
    print(f"Die Strings '{a}' und '{b}' sind nicht gleich.")

```
- Fingerabdruck
	- Komprimieren die Dateien genug, sodass Vergleich von Fingerabdrücken schnell geschehen kann.
	- Enthält möglichst viel Information aus der Original-datei
	- Schnell berechnen
	- ![[Pasted image 20240621164000.png]]
	- ![[Pasted image 20240621164017.png]]