Wenn es um die Suche und Sortierung von Daten geht, ist der binäre Suchbaum eine der grundlegendsten Datenstrukturen. Allerdings hängt die Leistung eines binären Suchbaums stark von seiner Form ab und im schlimmsten Fall kann er in eine lineare Struktur mit einer Zeitkomplexität von O(n) entarten. Hier kommen Red Black Trees ins Spiel. Sie sind eine Art ausgeglichener binärer Suchbaum, der einen bestimmten Satz von Regeln verwendet, um sicherzustellen, dass der Baum immer ausgeglichen ist.

Dieses Gleichgewicht garantiert, dass die zeitliche Komplexität für Vorgänge wie Einfügen, Löschen und Suchen immer O(log n) beträgt, unabhängig von der ursprünglichen Form des Baums.

Es weist eine gute, effiziente Worst-Case-Laufzeitkomplexität auf.

>>>Der Rot-Schwarz-Baum erfüllt alle Eigenschaften des binären Suchbaums und darüber hinaus die folgenden zusätzlichen Eigenschaften:

1. **Root-Eigenschaft:** Die Wurzel ist schwarz.

2. **Externe Eigenschaft:** Jedes Blatt (Blatt ist ein NULL-Kind eines Knotens) ist im Rot-Schwarz-Baum schwarz.

3. **Interne Eigenschaft:** Die Kinder eines roten Knotens sind schwarz. Daher ist ein möglicher übergeordneter Knoten des roten Knotens ein schwarzer Knoten.

4. **Tiefeneigenschaft:** Alle Blätter haben die gleiche Schwarztiefe.

5. **Pfadeigenschaft:** Jeder einfache Pfad vom Stamm zum untergeordneten Blattknoten enthält die gleiche Anzahl schwarzer Knoten. 



>>>#### **Regeln, denen jeder rot-schwarze Baum folgt:** 

1. Jeder Knoten hat eine Farbe, entweder Rot oder Schwarz.
2. Die Wurzel des Baumes ist immer schwarz.
3. Es gibt keine zwei benachbarten roten Knoten (Ein roter Knoten kann kein rotes übergeordnetes Element oder rotes untergeordnetes Element haben).
4. Jeder Pfad von einem Knoten (einschließlich Root) zu einem seiner Nachkommen-NULL-Knoten hat die gleiche Anzahl schwarzer Knoten.
5.  Jedes Blatt (ein NULL-Knoten) muss SCHWARZ gefärbt sein.



**Vergleich mit** [[AVL-Bäume]]:  
Die AVL-Bäume sind im Vergleich zu Rot-Schwarz-Bäumen ausgeglichener, verursachen jedoch möglicherweise mehr Rotationen beim Einfügen und Löschen. Wenn Ihre Anwendung also häufige Einfügungen und Löschungen erfordert, sollten Rot-Schwarz-Bäume bevorzugt werden. Und wenn die Einfügungen und Löschungen seltener sind und die Suche ein häufigerer Vorgang ist, sollte der AVL-Baum dem Rot-Schwarz-Baum vorgezogen werden.



Einfügen

![[Pasted image 20240308234201.png]]
Links-Links
![[Pasted image 20240308234334.png]]
Links-Rechts
![[Pasted image 20240308234416.png]]
Rechts-Rechts
![[Pasted image 20240308234449.png]]
Rechts-Links
![[Pasted image 20240308234514.png]]
![[Pasted image 20240308234149.png]]
![[Pasted image 20240308234224.png]]