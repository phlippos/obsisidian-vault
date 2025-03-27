1. Nenne die vier in der Vorlesung vorgestellten Testphasen und erkläre jeweils kurz den Zweck der Phase.
	1. Unit test : 
		1. Jede Module wird unabhängig voneinander getestet
	2. Integration test :
		1. Komponentengruppen werden in Subsysteme integriert
		2. testet, ob die Kommunikation zwischen Komponenten  funktioniert
		3. um Komponente miteinander zu interagieren, gibt es Strategien
			1. Top-Down
			2. Bottom-Up
			3. Ad-Hoc
			4. Big Bang
	3. System test :
		1. Erfüllt das System die Anforderungen
		2. System wird aus Benutzersicht getestet.
	4. Akzeptanz test :
		1. Fokus liegt nicht auf Fehler finden, sondern Vertrauen in das Produkt zu erzeugen.
2. In der zweiten Testphase können verschiedene Strategien verwendet werden. Welche dieser Strategien ist für das Softwareprojekt am besten geeignet? Erkläre kurz die von Dir gewählte Strategie und erläutere warum andere Strategien ungeeignet sind.
	1. Top-Down Strategie ist am besten geeignet, weil höchste Ebene zuerst getestet wird ,z.B. GUI. Danach werden darunterliegende Module ınteragiert und getestet.
	2. Außerdem werden Dummies verwendet, um die noch nicht entwickelten Komponente zu simulieren.
	3. Frühes Testen der Hauptfunktionen
	4.  warum andere Strategien ungeeignet sind? 
		1. Bottom-up testet zuerst die unterste Komponente. Aber die obere Komponente sind wichtiger und deren Fehler sind zerstörend.
		2. Ad-Hoc hat keine bestimmte Struktur und Planung, deshalb ist diese Strategie unzuverlässig.
		3. Big Bang testet die Integration auf einmal. Darum ist die Strategie nicht geeignet für komplexe Projekte.