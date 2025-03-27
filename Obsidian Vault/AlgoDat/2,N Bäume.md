> 2,N Bäume sind auch balancierte Suchbäume

Größeneigenschaft  : Alle internen Knoten haben 2 bis 4 kinder und 1 bis 3 werte

![[Pasted image 20240308211702.png]]

> Alle Blatknoten haben dieselbe Tiefe, deswegen garantiert O(logn) Laufzeit
> für die Sucheoperation

Hinzufügen von k:
Suche nach k in Baum terminiert in einem Blattknoten z mit Vater w erfolglos
füge k in w ein und füge ein neues Kind y auf der linken Seite von z ein
![[Pasted image 20240308212934.png]]

wenn Grösseneigenschaft verletzt wird -> overflow

Lösung : Split
![[Pasted image 20240308215523.png]]
![[Pasted image 20240308215538.png]]
![[Pasted image 20240308215553.png]]

Löschen von k:
Größeneigenschaft womöglich verletzt  -> underflow
Lösungen : Transfer , Fusion

>Transfer : Schiebe ein Kind von s nach Vater u, und ein Wert von u nach w
>Fusion : Füge einen Bruder s mit w zusammen und erzeuge neuen Knoten w' und schiebe einen wert von Vater u nach w'
>Beide sind O(logn)

![[Pasted image 20240308221259.png]]
![[Pasted image 20240308221311.png]]


