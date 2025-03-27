>**Greedy-Algorithmen*** sind eine Klasse von Algorithmen, die bei jedem Schritt **lokal optimale*** Entscheidungen treffen, in der Hoffnung, eine **global optimale*** Lösung zu finden.
>
 Bei diesen Algorithmen werden Entscheidungen auf der Grundlage der aktuell verfügbaren Informationen getroffen, ohne die Konsequenzen dieser Entscheidungen für die Zukunft zu berücksichtigen.
>
>Es versucht, die beste Lösung zu finden, indem es bei jedem Schritt die beste Wahl trifft, ohne zukünftige Schritte oder die Konsequenzen der aktuellen Entscheidung zu berücksichtigen.


### *Eigenscahften des Greedy Algorithmus*

>--eine geiegnete Liste von Ressourcen (Gewinn, Kosten, Wert usw.)
>--maximaler Gewinn, maximaler Wert 
>--beispielsweise fraktionierte Rucksackproblem


### *Fraktionaler Rucksack*

>{Gewinn, Gewicht} in einen Rucksack mit der Kapazität W
>$$  arr[] = [[100, 20],[60, 10],[120, 30]], W = 50 $$
> Sortieren wir Array nach dem Gewinn/Gewicht
> wer viel Geld pro KG gibt, kommt erst
>$$ arr = [[60,10],[100,20],[120,30]]$$
> Durch Nehmen von Gegenständen mit einem Gewicht von 10 und 20 kg und 2/3 Bruchteil von 30 kg.
> $$ 60+100 +(2/3)*120 = 240 $$
> Dadurch wird immer der maximale Gewinn erzielt, da in jedem Schritt ein Element hinzugefügt wird, sodass dies der maximal mögliche Gewinn für dieses Gewicht ist.


### *Fraktionaler Rucksack Abfragen*

>Ermitteln Sie anhand eines ganzzahligen Arrays, das aus positiven Gewichten „W“ bzw. ihren Werten „V“ als Paar besteht, und einigen Abfragen, die aus einer Ganzzahl „C“ bestehen, die das Fassungsvermögen des Rucksacks angibt, den maximalen Wert der Produkte, die hineingesteckt werden können der Rucksack, wenn das Zerbrechen von Gegenständen erlaubt ist.
```python
W = 10
profit = [10, 15, 10, 12, 8]
weight = [3, 3, 2, 5, 1]
n = len(weight) # number of items
wp = []
for i in range(n):
	wp.append([weight[i],profit[i]])
print("weight and profit array : ", wp)
```
>1. Sortieren wir das Array nach seinem Wert-/Gewichtsverhältnis in absteigender Reihenfolge.
>2. Nehmen wir dann das Element mit dem höchsten Verhältnis und fügen wir so viele wie möglich hinzu (es kann das gesamte Element oder ein Bruchteil davon sein).
```python
wpSorted = sorted(wp,key = lambda x : -x[1]/x[0])
print(wpSorted)

i = 0
ans = [0]
while W > 0 and i < n : 
	weightVal = wpSorted[i][0]
	profitVal = wpSorted[i][1]
	if weightVal <= W : 
		W -= weightVal
		ans.append(ans[len(ans)-1]+profitVal)
	else :
		#percent = 1-W/profitVal		
		#W -= percent*weightVal
		ans.append(ans[len(ans)-1]+W*(profitVal/weightVal))
		W = 0
		
	i+=1
	print(weightVal,W,i)
print(ans)
```

### *0/1 Rucksackproblem*

>Gegeben sind ***N*** Artikel, bei denen mit jedem Artikel ein gewisses Gewicht und ein gewisser Gewinn verbunden ist, und außerdem ist ein Beutel mit der Kapazität **W*** gegeben [dh der Beutel kann höchstens Gewicht **W** enthalten].
>
Die Aufgabe besteht darin, die Gegenstände so in den Beutel zu legen, dass die damit verbundene Gewinnsumme möglichst groß ist.
>
>Die Einschränkung hier besteht darin, dass wir einen Artikel entweder vollständig in die Tasche stecken können oder überhaupt nicht.
>
>Es ist nicht möglich, einen Teil eines Artikels in die Tasche zu stecken.
>
>**Rekursionansatz für das 0/1-Rucksackproblem**
>
>Eine einfache Lösung besteht darin, alle Teilmengen von Artikeln zu berücksichtigen und das Gesamtgewicht und den Gewinn aller Teilmengen zu berechnen. Betrachten Sie die einzigen Teilmengen, deren Gesamtgewicht kleiner als W ist. Wählen Sie aus allen solchen Teilmengen die Teilmenge mit dem maximalen Gewinn aus.
>
>**Optimale Unterstruktur*** ****:**** Um alle Teilmengen von Elementen zu berücksichtigen, kann es für jedes Element zwei Fälle geben. 
>
>- ***Fall 1:*** Das Element ist in der optimalen Teilmenge enthalten.
>- ***Fall 2:*** Der Artikel ist nicht im optimalen Set enthalten.
>- ![[Pasted image 20240318223309.png]]
```python
def rucksack(Weight,value,n,W):
	if W == 0 or n == 0 :
		return 0

	if Weight[n-1] > W :
		return rucksack(Weight,value,n-1,W)
	else :
		return max(value[n-1] + rucksack(Weight,value,n-1,W-Weight[n-1]),
		rucksack(Weight,value,n-1,W))

gewinn = [1,2,3]
gewicht = [4,5,1]
n = len(gewicht)
W = 5
print(rucksack(gewicht,gewinn,n,W))
```
> **Dynamischer Ansatz für das 0/1-Rucksack**
> 
> Wenn wir zum ersten Mal ein Teilproblem haben, können wir dieses Problem lösen, indem wir ein 2D-Array erstellen, das einen bestimmten Zustand (n, w) speichern kann. Wenn wir nun erneut auf denselben Zustand (n, w) stoßen, anstatt ihn in exponentieller Komplexität zu berechnen, können wir sein in der Tabelle gespeichertes Ergebnis direkt in konstanter Zeit zurückgeben.![[Pasted image 20240318230033.png]]
> $$ dp[i][j] = max(dp[i-1][j],val + dp[i-1][j-w])$$
```python
gewichts = [10,20,30]
gewinn = [60,100,120]
n = len(gewinn)
W = 50
dp = [0]*(W+1)

for i in range(n):
	for j in range(W,-1,-1):
		if gewichts[i] <= j : 
			dp[j] = max(dp[j],gewinn[i] + dp[j-gewichts[i]])
		
print(dp)
```
> $$ Zeitkomplexität = O(n*W)$$
> $$ Speicherkomplexität=O(W)$$


### *Floyd Warshall-Algorithmus*

> Es wird verwendet, um die kürzesten Pfade zwischen allen Knotenpaaren in einem gewichteten Diagramm zu finden.
>
> Dieser Algorithmus ist hocheffizient und kann Diagramme mit sowohl **positiven*** als auch ***negativen Kantengewichten*** verarbeiten. (Im Gegensatz zum Dijkstra Algorithmus)
> 
>geeignet sowohl für gerichtete als auch für ungerichtete Graphen.
>
>Dies funktioniert jedoch nicht für Diagramme mit negativen Zyklen (bei denen die Summe der Kanten in einem Zyklus negativ ist).
>
> **Idee von Floyd Warshall-Algorithmus**
>	1. initialisiere die Gewichtsmatrix
>	![[Pasted image 20240319002952.png]]
>	2. Aktualisiere die Matrix, indem alle Punkte als Zwischenpunkt betrachtet werden
>	$$ dp[i][j] = min(dp[i][j], distanz(i-->K) + distanz(K-->j))$$
>	![[Pasted image 20240319003417.png]]
```python
gewichtsMatrix = [[0,5,float("inf"),10],
				[float("inf"),0,3,float("inf")],
				[float("inf"),float("inf"),0,1],
				[float("inf"),float("inf"),float("inf"),0]]
				
n = len(gewichtsMatrix[0])
for i in range(n):
	for j in range(n):
			for k in range(n): 
				gewichtsMatrix[j][k] = min(gewichtsMatrix[j][k],
				gewichtsMatrix[j][i]+gewichtsMatrix[i][k])
				
	print(gewichtsMatrix)

```