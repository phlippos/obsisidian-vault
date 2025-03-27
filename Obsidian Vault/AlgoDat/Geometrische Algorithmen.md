- Problem 1 : Bestimmung der konvexen Hülle eines Objekts
	- Man nennt eine Punktmenge in einer euklidischen Ebene konvex, wenn mit jeden zwei Punkten P1 und P2 der Menge auch das ganze Verbindungsstück zwischen P1 und P2 zur Menge gehört.Die konvexe Hülle einer gegebenen Punktmenge ist die kleinste konvexe Menge, die diese Punkte enthält.
	- Eigenschaften 
		- Punkte mit den grössten und kleinsten x- und y- Koordinaten teil der konvexen Hülle (Extrempunkte)
		- Mindestens drei, maximal n Punkten erzeugt wenn die Menge n Punkte beinhaltet
## Gift-Wrapping Algorithmus
- Im zweidimensionalen Fall startet das Algorithmus an einem Extrempunkt, zB Punkt der kleinsten x-Koordinate. Dann halten wir eine Schnur nach unten und notieren die Schnur gegen den Uhrzeigersinn bis ein Punkt angetroffen wird.
- Wie findet man den nächsten Punkt in der Ausgabe, wenn als aktueller Punkt ein Punkt p angegeben ist?
	- Als nächster Punkt wird der Punkt ausgewählt, der alle anderen Punkte bei Ausrichtung gegen den Uhrzeigersinn schlägt, d. h. der nächste Punkt ist q, wenn für jeden anderen Punkt r gilt: „orientation(p, q, r) = gegen den Uhrzeigersinn.
	-   
	- Also alle Geraden durch andere Punkte werden angeschaut. Diejenige Gerade, die am schwächsten nach links abbiegt ist mein neuer Punkt.
	- Bei h Punkten auf der Hülle O(N.h)  , im Worst Case O(N^2)
	- Algorithm : 
		- process of finding the minimum element in array : We assume that the first element is the minimum, then for each element, if it is smaller than min, element becomes the new min.
		- process of finding the next point to insert on the hull : we assume that the first point is the next point of the hull, then for each point, if orientation(on_hull,next,point) is counterclockwise, point becomes new next.
		- orientation : we have three points and compare the slopes of (p1,p2) and (p2,p3)
			- counterclockwise : if the slope of (p2,p3) > (p1,p2)
			- clockwise : if the slope of (p2,p3) < (p1,p2)
			- collinear if the slope of (p2,p3) = the slope of (p2,p3)
			- ![[Pasted image 20240526000602.png]]
			- ![[Pasted image 20240526000618.png]]
```python 
def orientation(p1,p2,p3):
	x1 = p1[0]
	y1 = p1[1]
	x2 = p2[0]
	y2 = p2[1]
	x3 = p3[0]
	y3 = p3[1]
	diff = (y2-y1)*(x3-x2) - (y3-y2)*(x2-x1)
	if diff > 0 :
		return 1 # counterclockwise
	elif diff < 0 :
		return -1 # clockwise
	else : 
		return 0 # colllinear
def gift_wrapping(points):
	on_hull = min(points)
	hull = []
	while True : 
		hull.append(on_hull)
		next_point = points[0]
		for point in points:
			o = orientation(on_hull,next_point,point)
			if next_point == on_hull or o  == 1:
				next_point = point
		on_hull = next_point
		if on_hull == hull[0]:
			break
	return hull	
points = [[0,3],[2,2],[1,1],[2,1,],[3,0],[0,0,],[3,3]]
print(gift_wrapping(points))
```

## Graham's Scan
-   Der Algorithmus sucht zunächst den Punkt mit der kleinsten y-Koordinate. Dieser Punkt liegt immer auf der konvexen Hülle. Anschließend sortiert der Algorithmus die verbleibenden Punkte nach ihrem Polarwinkel in Bezug auf den Startpunkt.
-   Der Algorithmus fügt dann iterativ Punkte zur ****konvexen Hülle**** hinzu. Bei jedem Schritt prüft der Algorithmus, ob die letzten beiden zur konvexen Hülle hinzugefügten Punkte eine Rechtskurve bilden. Wenn dies der Fall ist, wird der letzte Punkt aus der konvexen Hülle entfernt. Andernfalls wird der nächste Punkt in der sortierten Liste zur konvexen Hülle hinzugefügt.
-  Der Algorithmus endet, wenn alle Punkte zur konvexen Hülle hinzugefügt wurden.
- Algorithm : 
	-  ****Phase 1 (Sort points):****
		- Der erste Schritt bei der Implementierung des Graham-Scan-Algorithmus besteht darin, die Punkte nach ihrem Polarwinkel in Bezug auf den Startpunkt zu sortieren.
		- Sobald die Punkte sortiert sind, wird der Startpunkt zur konvexen Hülle hinzugefügt. Sobald die Punkte sortiert sind, bilden sie einen einfachen geschlossenen Pfad.
	-  ****Phase 2 (Punkte akzeptieren oder ablehnen):****
		- Sobald wir den geschlossenen Pfad haben, besteht der nächste Schritt darin, den Pfad zu durchlaufen und konkave Punkte auf diesem Pfad zu entfernen. Wie entscheiden wir, welche Punkte entfernt und welche behalten werden sollen?
		- Die Orientierung.
		- Die ersten beiden Punkte in einem sortierten Array sind immer Teil der konvexen Hülle. Für die verbleibenden Punkte behalten wir die letzten drei Punkte im Auge und ermitteln den von ihnen gebildeten Winkel. Lassen Sie die drei Punkte ****prev(p)**** , ****curr(c)**** und ****next(n) sein.**** Wenn die Orientierung dieser Punkte (in derselben Reihenfolge betrachtet) nicht gegen den Uhrzeigersinn verläuft, verwerfen wir c, andernfalls behalten wir es.
		- Time Complexity : 
			- Jede Kante kann höchstens 1 Mal aus der Liste entfernt werden → O(N)
			- Laufzeit wird durch die Sortierung der Geraden abhängen ➔ also O(N.logN)
```python
def graham_scan(points):
	p0 = min(points,key = lambda p: (p[1],p[0]))
	points.sort(key = lambda p: (polar_angle(p0,p),dist(p0,p)))
	hull = []
	for i in range(len(points)):
		while len(hull) >= 2 and orientation(hull[-2],hull[-1],points[i]) != 1:
			hull.pop()
		hull.append(points[i])
	return hull
```

## Problem der Sichtbarkeit
- VLSI-design (Schaltkreis Design)
- Anwendung: Abstandsbedingungen zwischen relevanten Bauelementen müssen eingehalten werden.
- Zwei horizontale Segmente s und s’. Diese Segmente sehen sich, wenn eine vertikale Gerade existiert, die s und s’ schneidet aber kein weiteres Segment schneidet.
- ![[Pasted image 20240526125021.png]]
- ![[Pasted image 20240526130235.png]]
- ![[Pasted image 20240526130402.png]]
- ![[Pasted image 20240526131724.png]]
- 