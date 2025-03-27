Ein Heap ist eine vollständigen binären Baum, die die Eigenschaften von Heap erfüllt.

> Min Heap
> Alle Parentknoten kleiner als seine Kinder
> 	p.val <= leftChild.val and p.val <= rightChild.val (Das gilt für alle Knoten außerhalb Kinderknoten)
> Der Wurzelknoten ist immer der kleinste.
> 


>Max Heap
>Das ist umgekehrt von Min Heap
>Alle Parentknoten ist größer als seine Kinder oder gleich
>	p.val >= leftChild.val and p.val >= rightChild.val
>Der WurzelKnoten ist immer der größte


Die Höhe des gesamten Binärbaums beträgt immer logn, deshalb die Time Complexity O(logn)



Eigenschaften von Heap : 
> Vollständiger Binärbaum : alle Ebenen des Baums sind vollständig gefüllt außerhalb der letzten Ebene, die von links nach rechts gefüllt wird.
> 
> Eltern-Kind Beziehung: Die beziehung zwischen einem Elternknoten am Index i und seinen Kindernn wird  mit dieser Formeln ausgedruckt, linkes Kind befindet sich am Index 2*i+1 und rechtes Kind befindet sich am Index 2*i+2.
> 
> Effizientes Einfügen und Entfernen : Das eingefügte Element wird an der nächsten verfügbaren Position eingefügt und dann wird wieder Heap-Eigenschaft hergestellt.
> Beim Entfernen wird der Wurzelknoten entfernt und das letzte Element wird Rootelement und dann wieder heapify



Operationen : 
> push()
> pop()
> getMax() and getMin()
> RemoveMin() and RemoveMax()


Vorteile von Heaps:

- Schneller Zugriff auf maximales/minimales Element (O(1))
- Effiziente Einfüge- und Löschvorgänge (O(log n))  
    Flexible Größe
- Kann effizient als Array implementiert werden
- Geeignet für Echtzeitanwendungen

Nachteile von Heaps:
- nicht geeignet für die Such nach einem Element außerhalb min oder max O(logn)
- zusätzliche Speicheraufwand
- langsam


Heap Sort
- Erstellen Sie einen Heap aus dem angegebenen Eingabearray.
- Wiederholen Sie die folgenden Schritte, bis der Heap nur noch ein Element enthält:
    - Tauschen Sie das Wurzelelement des Heaps (das größte Element) mit dem letzten Element des Heaps aus.
    - Entfernen Sie das letzte Element des Heaps (das sich jetzt an der richtigen Position befindet).
    - Heapen Sie die verbleibenden Elemente des Heaps.
- Das sortierte Array wird durch Umkehren der Reihenfolge der Elemente im Eingabearray erhalten.
![[Pasted image 20240304223432.png]]

![[Pasted image 20240304223539.png]]
![[Pasted image 20240304223618.png]]

![[Pasted image 20240304223628.png]]
![[Pasted image 20240304223638.png]]
![[Pasted image 20240304223649.png]]
****Zeitkomplexität:**** O(N log N)  
****Hilfsraum:**** O(log n), aufgrund des rekursiven Aufrufstapels. Für die iterative Implementierung kann der Hilfsraum jedoch O(1) sein.

Vorteile von Heap-Sort :
>Effiziente Zeitkomplexität (langsamer als Quicksort) O(nlogn)
>Speichernutzung ist minimal

Nachteile von Heap-Sort:
>teuer
>instabil





[[Bäume]]