### **Approximative Suche Fuzzy Suche**
>Anwendungsbereich : Spellchecking (nicht exakte String , sonder ähnliche)
>Zwei Formen der approximativen Suche:
	1) Gegeben sei ein Text T und ein Muster P. Gesucht sind alle Vorkommen von P’ in T derart, dass sich P und P’ in höchsten k Positionen unterscheiden. Für k=0 haben wir die exakte Suche, wie bis jetzt besprochen. Für k>0 könnten diese Algorithmen modifiziert angewendet werden.
	2) Suche nach Vorkommen des Musters P’ im Text derart, dass die Editierdistanz minimal ist. Statt die unterschiedlichen Zeichen zu zählen, prüfen wir wie viele Editier-operationen durchgeführt werden müssen um ein String in das Muster über zu führen. Jeder Operation wird ein Kosten zugewiesen.
> Editieroperationen: Löschen, Einfügen, Verändern.
> ![[Pasted image 20240411181753.png]]
> ![[Pasted image 20240411181915.png]]
> ![[Pasted image 20240411181938.png]]


### **Trie Datenstruktur(Retrieval)**
>Bis jetzt das gesuchte Muster analysiert um die Suche zu optimieren. Jetzt wollen wri einen Ansatz kennenlernen, wo der Suchtext selber vorverarbeitet wird. Wenn wir einen Text haben auf der mehrmals gesucht werden soll, dann ist so eine Vorverarbeitung sinnvoll.
>--Eine Trie ist eine Baumstruktur um Strings zu speichern so, dass eine Suche nach einem Muster schnell durchgeführt werden kann.
>
>Ein Trie T ist ein geordneter Baum mit folgenden Eigenschaften:
>	1. Jeder Knoten ausser dem Wurzelknoten hat ein Zeichen aus ∑
>	2. T hat n Blätter so dass die Konkatenation aller Zeichen in den Knoten von der Wurzel bis zu den Blättern einen String in S bildet.
>	![[Pasted image 20240411182632.png]]
>	-Die Höhe eines Tries ist also gleich der Länge des längsten Strings in der Menge S.
>	-Worst Case: Wenn keine Strings einen gemeinsamen Präfix haben, also internen Knoten nur ein Kind haben.
>	-Laufzeit der Suche nach einem Muster der Länge M wäre O(M|∑|), weil wir höchstens M Knoten besuchen und bei jedem Knoten höchstens |∑| Vergleiche gemacht werden müssen um das nächste Kind zu bestimmen.
>	
>**Compressed Trie**
>Beobachtung: in einem normalen Trie kann es viele interne Knoten mit nur einem Kind geben.
>Compressed Trie: alle internen Knoten haben mindestens zwei Kinder
>![[Pasted image 20240411183253.png]]
>![[Pasted image 20240411183424.png]]
>**Suffix Trie**
>![[Pasted image 20240411183618.png]]