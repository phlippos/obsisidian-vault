Wichtige Begriffe:
1. **Substring**: Eine Folge von aufeinander folgenden Zeichen in einem String. Ein String der Länge n hat n*(n+1)/2 Substrings.
2. **Subsequence**: Eine Folge von nicht unbedingt aufeinander folgenden Zeichen im String. Ein String der Länge n hat 2^n - 1 Subsequences.
3. Prefix: Ein Substring, der am Start des Strings ist.
	1. ABCD -> A,AB,ABC,ABCD
4. Suffix: Ein Substring, der am Ende des Strings ist.
5. **Border**: Ein Substring,der gleichzeitig ein Prefix und ein Suffix ist.
	1. ABCAB -> AB

**Suche in Strings**
1. **Naiver Algorithmus**
	1. T und P ein String und P ein Muster
	2. T.length = n
	3. P.length = m
	4. m < n 
	5. die Elemente in T und P kommen aus dem gleichen Alphabet 
```python
t = "abcabdcef"
p = "abdcf"
n = len(t)
m = len(p)
for i in range(n-m+1):
	counter = 0
	for j in range(m):
		if t[i+j] == p[j]:
			counter+=1
		else : 
			break
	if counter == m:
		print(f"Substring start im Index {i} und endet im Index {i+j}")
		break
if counter != m:
	print("Substring existiert nicht")
```
	6. Laufzeit = O(N.m)
	7. problematisch besonders wenn M groß wird -> O(N^2)
2. **Robin-Karp Algorithmus**
	1. Im [Naive String Matching-](https://www.geeksforgeeks.org/searching-for-patterns-set-1-naive-pattern-searching/) Algorithmus prüfen wir nacheinander, ob jeder Teilstring des Texts in der Größe des Musters mit dem Muster übereinstimmt oder nicht.
	2. Idee: Berechne Hashwert von Muster P. Führe ein Fenster über dem Text und Hashwert von P mit dem Hashwert vom Fenster. Falls gleich → kontrolliere Zeichenweise
	3. **Wie wird der Hash-Wert in Rabin-Karp berechnet**
		1. **Der Hash-Wert*** wird verwendet, um effizient nach potenziellen Übereinstimmungen zwischen einem ***Muster*** und Teilzeichenfolgen eines größeren **Textes*** zu suchen
			1. Schritt 1: Wählen Sie eine geeignete Basis b(Größe des Zeichensatzes  ,256 for ASCII characters) und einen Modul p(primzahl)
			2. Schritt 2: Inıtialisieren Sie den Hashwert : 0
			3. Schritt 3: Berechnen Sie den anfänglichen Hash-Wert für das **Muster***
				1. - Durchlaufen Sie jedes Zeichen im ****Muster**** von ****links**** nach ****rechts**** .
				2. - Berechnen Sie für jedes Zeichen ****„c“**** an Position ****„i“**** seinen Beitrag zum Hash-Wert als   „c*(b^(pattern_length – i – 1) ) % p“ und fügen Sie ihn zu „ ****hash**** “ hinzu.
			4. Schritt 4: Schieben Sie das Muster über den Text:     Beginn mit der berechnung des Hash-Werts für den ersten Teilstring des Textes, der die glieche Länge wie das Muster hat.
			5. Schritt 5: Aktualisieren Sie den Hash-Wert für jeden nachfolgenden Teilstring :
				1. - Um das ****Muster**** um eine Position nach rechts zu verschieben, entfernen Sie den Beitrag des Zeichens ganz links und fügen den Beitrag des neuen Zeichens rechts hinzu.
				2. hash = (hash - (text[i - Musterlänge] *          (b^(Musterlänge - 1))) % p) * b + Text[i]
			6. Schritt 6: Hashwerte vergleichen:                    
				1. Wenn der Hashwert einer Teilzeichenfolge im Text mit dem Hashwert des Musters übereinstimmt, handelt es sich um eine potenzielle Übereinstimmung.
				2. Wenn die hash-Werte übereinstimmen,sollten wir einen zeichenweisen Vergleich durchführen, um die Übereinstimmung zu bestätigen, da es zu Hash-Kollisionen kommen kann.
	4. ![[Pasted image 20240330151559.png]]
```python
Text = "315265"
Pattern = "26"
n = len(Text)
m = len(Pattern)
hash_pattern = 0
hash_text = 0
b = 256
p = 101
h = pow(b,m-1) % p
for i in range(m):
	hash_pattern = (b*hash_pattern + ord(Pattern[i]))%p
	hash_text = (b*hash_text + ord(Text[i]))%p

for s in range(n-m):
	if hash_pattern == hash_text:
		for i in range(m):
			if Text[s+i] == Pattern[i]:
				pass
			else : 
				break
		if i == m-1 :
			print(f"Pattern found at index {s}")
	if s < n-m :
		hash_text = (b*(hash_text - ord(Text[s])*h)+ord(Text[s+m])) % p
		


```
	5. Probleme 
		1. Viele Kollisionen
		2. zu größe Hashwerte
	6. Laufzeit : Best O(N+M)
		1. Worst O(N*M) // T = AAAAAAA, P = AAA

![[Pasted image 20240330170616.png]]

![[Pasted image 20240330170511.png]]

3. Bayer-Moore Algorithmus
	1. Looking-Glass Heuristik(good suffix heuristic):
		1. Vergleiche das Muster mit dem Text von rechts nach links
	2. Character-Jump Heuristik (bad character heuristic):
		1. Wenn ein Zeichenvergleich negativ ist: 
			1. Schiebe das Muster vollständig rechts, oder schiebe es so dass ein gemeinsames Zeichen auf die gleiche Position kommt
			2. Um diese Heuristik einzusetzen müssen wir für die Zeichen im Muster bestimmen, wie viele Stellen im Text übersprungen werden müssen.
	3. **Fall-1** Aus Unstimmigkeiten wird Übereinstimmung
		1. Wir suchen nach der Position des letzten Vorkommens des nicht übereinstimmenden Zeichens im Muster. Wenn das nicht übereinstimmende Zeichen im Muster vorhanden ist, verschieben wir das Muster so, dass es am nicht übereinstimmenden Zeichen im Text T ausgerichtet wird.
	4. **Fall-2** Musterbewegung über das Nichtübereinstimmungszeichen hinaus
		1. Wir suchen nach der Position des letzten Vorkommens des nicht übereinstimmenden Zeichens im Muster und verschieben das Muster, wenn es kein Zeichen gibt, über das nicht übereinstimmende Zeichen hinaus.
	5. Bilde eine Tabelle wo für jedes Zeichen z eingetragen, wo es im Muster als letztes (right-most) auftaucht (last(z)) und beschreibe wieviele Stellen übersprungn werden müssen mit.
	6. $$ skip(z) = P.length-last(z)-1$$
	7. Für alle Zeichen,die nicht im Muster vorkommen -> P.length
	8. ![[Pasted image 20240330173157.png]]
4. Knuth-Morris-Pratt Algorithmus
	1. Die Grundidee des KMP-Algorithmus ist: Wann immer wir eine Nichtübereinstimmung feststellen (nach einigen Übereinstimmungen), kennen wir bereits einige der Zeichen im Text des nächsten Fensters. Wir nutzen diese Informationen, um eine Übereinstimmung mit Zeichen zu vermeiden, von denen wir wissen, dass sie ohnehin übereinstimmen.
	2. Verarbeite Muster so, dass eine failure function f verwendet, das besagt wieviele Stellen überspringen werden müssen.
	3. ![[Pasted image 20240330181254.png]]