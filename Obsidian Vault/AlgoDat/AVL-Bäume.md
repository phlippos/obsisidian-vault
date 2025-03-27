> Ein AVL-Baum ,der als selbstaugeglichender binärer Suchbaum definiert ist, wobei der Unterschied zwischen den Höhen des linken und rechten Teilbaums für jeden Knoten nicht mehr als eins betragen darf.

Operationen an einem AVL-Baum : 
>Einfügen O(1)
>Suchen O(logn)
>Entfernen O(1)


Rotieren der Teilbäume in einem AVL-Baum
 4 mögliche Fälle:

>balance(k) = -2 and balance(k.right) = -1:
Linksdrehung : 


![[Pasted image 20240304225747.png]]


> balance(k) = 2 and balance(k.left) = 1
> rechtsdrehung:

![[Pasted image 20240304230022.png]]

>balance(k) = 2 and balance(k.left) = -1
>links und rechts drehung:
>![[Pasted image 20240304230233.png]]

>balance(k) = -2 and balance(k.right) = 1 
>rechts und links drehung:
![[Pasted image 20240304230506.png]]


![[Pasted image 20240304230614.png]]

[[Bäume]]