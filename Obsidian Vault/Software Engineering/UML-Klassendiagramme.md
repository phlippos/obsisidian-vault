**Objektorientierte Analyse**
	-->Statisches Modell:
		1. Klassen : Eigenschaften und Aufgaben von Objekten
		2. Beziehungen zwischen Klassen bzw. Objekten
		3. Beziehungen werden durch Vererbung, Assoziationen und Abhängigkeiten abgebildet
	-->Dynamisches Modell:
		1.Zustände & Verhalten von Objekten abgebildet über Funktionen.

**Klassendiagramm**
![[Pasted image 20240327101643.png]]
	>> Assoziation
		>> Objekte, die miteinander in Beziehung stehen
		>> Beziehung der Art : 
			>>benutzt ein/-e
			>>ist zugeordnet zu
			>>hat eine Beziehung zu
	>>Aggregation
		>>Stärkere Beziehung als Assoziation
		>>Beziehung der Art: besitzt ein/-e
		>>//Restaurant / Gast
	>>Komposition
		>>sehr starke Bindung
		>>ist ein Teil von
		>>besteht aus
		>>Gebäude / Raum
**Vererbung/Spezialisierung**
	>>Generalisierung von Objekten
	>>Beziehung der Art : ist ein 
	>>//Fahrzeug / Auto, Bus, Bahn
**Klassenkandidaten & Attribute**
	>> Jede Klasse sollte mindestens ein sinnvolles Attribut tragen oder in mindestens einer Assoziation angebunden sein.


**Zugriff & Sichtbarkeit**
	>>UML
	>> +(public)
	>> #(protected)
	>> -(private)
	>>" "(default)
	
**Makroebene**
- Statische Zusammenhänge werden dargestellt

**Paket & Paketimport**
	>>**Paket** :
	>> Pakete sind Namensräume
	>> Pakete gruppieren semantisch zusammengehörige Elemente
	>> Innerhalb eines Namespaces sollten eindeutige Namen für Elemente genutzt werden, die gleich sind oder zueinander in Beziehung stehen.
	>>die verwendet werden, um die Struktur und Organisation von Modulen oder Paketen in einem Softwaresystem darzustellen.
	>>Diese Diagramme helfen dabei, die Abhängigkeiten zwischen verschiedenen Modulen zu visualisieren und die Gesamtstruktur des Systems zu verstehen.
	>> Paketimport 
		>> Ein Import ist eine direkte Beziehung zwischen dem importierten Namespace und dem importierten Paket.,
		>> **Import**: Ein Import zeigt an, dass ein Paket Elemente aus einem anderen Paket verwendet.
		>> ![[Pasted image 20240327104136.png]]
	Ein Paket…
	 … ist eine Gruppe von Klassen.
	 … ist für sich allein verständlich
	 … hat eine wohldefinierte Schnittstelle
	 … ermöglicht abstrakte Sicht auf das des Systems
	Starke Bindung innerhalb des Pakets
		>> Einheitlicher Themenbereich
		>> Aggregation und Vererbung möglichst nur innerhalb des Pakets
	Schwache Kopplung zwischen Paketen
		>>wenig Assoziation über Paketgrenzen
	Daumenregel:
	10 - 15 Klassen pro Paket
	Wichtigste Möglichkeit: semantische Zusammengehörigkeit sicherstellen
	
	![[Pasted image 20240327104653.png]]