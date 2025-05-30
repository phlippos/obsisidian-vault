- **Qualitãt** : Gesamtheit von Eigenschaften und Merkmalen eines Produkts oder einer Tätigkeit, die sich auf deren Eignung zur Erfüllung gegebener Erfordernisse bezieht
	- Merke : 
		- Qualität bezieht sich auf Produkt & Prozess.
		- Qualitäts-Anforderungen ändern sich mit der Zeit!
		- Qualität muss gegenüber Kosten und Zeit abgewogen werden!
- **Verifikation & Validierung** :
	- Validierung : Entwickeln wir das richtige Produkt?
	- Verifikation: Entwickeln wir das Produkt richtig?
- Fehlerkette
	- Alle Fehlerzustände & Mängel treten während der Fertigstellung auf:
		- die <mark style="background: #FFF3A3A6;">Fehlerwirkung (failure)</mark> tritt bei der Ausführung des Programms auf,
		- die Fehlerwirkung wird durch einen <mark style="background: #FFF3A3A6;">Fehlerzustand (faults)</mark> in der Software erzeugt,
		- der Fehlerzustand wird durch die <mark style="background: #FFF3A3A6;">Fehlerhandlung (error)</mark> eines Menschen (Programmierer) ausgelöst.
	- Um einen Fehlerzustand zu erkennen muss die Normalsituation definiert sein.
- Testen
	- Testen ist ein Prozess, welcher statisch oder dynamisch ist, in die Planung, Vorbereitung und Evaluation eines Programmes mit einbezogen wird.
	- Ein Testfall besteht aus:
		- Vorbedingung
		- Aktion / Schritte
		- Erwartetes Ergebnis
		- Nachbedingung
	- Software wird evaluiert mit dem Ziel
		- zu prüfen ob der Zweck erfüllt wird,
		- zu prüfen ob Anforderungen erfüllt werden,
		- Fehler zu finden.
	- Testen erfasst die Qualität von Software, z.B. durch die Anzahl gefundener Fehler.
	- Testen verbessert die Qualität schon während des Entwicklungsprozesses, indem Fehler gefunden und behoben werden.
	- Testen verbessert die Prozessqualität, da Fehlerwirkungen dokumentiert und nachvollzogen werden können, das verhindert diese Fehler in der Zukunft.
	- Testen verbessert das Vertrauen in Softwarequalität, wenn keine oder nur wenige Fehler gefunden wurden.
- Grundlagen des Testens
	- Testen sollte so früh wie möglich in den Entwicklungsprozess einbezogen werden.
	- je eher Fehler gefunden werden, desto geringer sind die Kosten
	- Test in der Programmierumgebung != Test auf dem Endgerät
	- Gute Tests heute können in 6 Monaten ungenügend sein
	- Testaufwand sollte proportional zu den erwarteten / beobachteten Fehlern sein
	- 80% der Fehler sind in 20% der Module zu finden
	- Auch wenn keine Fehler vorhanden sind, kann die Benutzererwartungen verfehlt werden.
- Aktivitäten des fundamentalen Testprozesses
	- Aktivitäten werden zeitlich überlappend oder parallel ausgeführt
	- der fundamentale Testprozess kann zur Gestaltung aller Teststufen genutzt werden
- V-Modell
	- Erste Testphase - Unit Test
		- jede Komponente wird einzeln in Isolation getestet.
		- implementierte Softwareeinheiten werden systematisch getestet.
		- Unit Test basierend
			- Komponentens
			- Quellcode
			- allen zugehörig Dokumenten
	- Zweite Testphase - Integrationstest
		- Vorbedingung: 
			- Unit tests sind erfolgreich abgeschlossen
		- Ziel:
			- Fehler in den Interfaces und Interaktionen zwischen den Komponenten finden
		- ıntegration:
			- Komponentengruppen werden in Subsysteme integriert
			- durchgeführt von: Entwicklern, Testern, Integrations-Teams
		- Integrationstest:
			- Testet,ob die Kommunikation zwischen den Komponenten funktioniert.
		- Integrationsstrategien
			- Problemstellung:
				- In welcher Reihenfolge werden die Komponenten integriert?
				- Wann ist es so effektiv und effizient wie möglich?
				- Komponenten sind zu unterschiedlichen Zeit fertig
				- Tester sollten nicht im Leerlauf sein, nur weil Komponenten nicht fertig sind
			- Top-Down
				- Idee:
					- Komponente die nur andere anspricht aber nicht selber angesprochen wird. Andere Komponenten werden durch Dummys ersetzt.
				- Pro: 
					- Kaum oder keine Treiber benötigt, da High Level Komponenten als Testumgebung genutzt werden.
				- Kontra: 
					- kann teuer werden
					- Low Level Komponenten müssen durch Dummys ersetzt werden
				- ![[Pasted image 20240616013908.png]]
			- Bottom-Up
				- Idee: 
					- Komponente die keine anderen Komponenten aufruft größere Subsysteme werden schrittweise erstellt.
				- Pro:
					- Keine Dumms benötigt.
				- Kontra:
					- benötigt Treiber für Hıgh level Komponenten
				- ![[Pasted image 20240616013922.png]]
			- Ad-Hoc
				- Idee : 
					- Komponenten werden integriert wenn sie fertig sind.
				- Pro : 
					- keine Wartezeiten
				- Kontra :
					- braucht Dummys und Treiber
				- ![[Pasted image 20240616013950.png]]
			- Big Bang 
				- Idee : 
					- Alles wird auf einmal zusammengefügt
					- ![[Pasted image 20240616014003.png]]
				- Pro : 
					- keine
				- Kontra:
					- alle Fehler auf einmal
					- Fehlerquelle finden erschwert
					- Zeit bis Integration verschwendet
		- **Dritte Testphase - Systemtest**
			- Vorbedingung: 
				- Integrationstests sind erfolgreich abgeschlossen
			- Ziel: 
				- Erfüllt das System die Anforderungen
			- Grundgedanke: 
				- Erste Test-Phasen testen gegen die technische Spezifikation
				- Das System wird aus Benutzersicht getestet.
				- Die meisten Funktionen werden erst in einem fertig integrierten System nutzbar.
		- **Vierte Testphase - Akzeptanztest**
			- Vorbedingung:
				- Systemtest von Entwickler durchgeführt und abgeschlossen
			- Ziel: 
				- Fokus liegt nicht auf Fehler finden, sondern Vertrauen in das Produkt zu erzeugen.
			- Grundgedanke:
				- Akzeptanztest umfasst Sicht und Meinung des Kunden
				- Einzige Testphase die den Kunden direkt mit einbindet
				- Wird beim Kunden in der neuen Systemumgebung durchgeführt
- Statisches vs. Dynamisches Testen im Entwicklungsprozess
	- Statische Tests
		- verifizieren Dokumente & Spezifikationen
		- informelle Dokumente werden durch Reviews verifiziert
		- formale dokumente werden durch statische Analysen verifiziert
	- Dynamische Tests
		- validieren in jeder Phase anhand der entsprechenden Dokumente
- Qualitätssicherung für Analyse & Entwurf
	- Hohe Bedeutung früher Phasen für Produktqualität!
	- Alle Dokumente frühzeitig überprüfen("Validation").
	- Anfordeungskatalog
		- Echte Benutzer einbeziehen
		- Anforderungskatalog auf Vollständigkeit und Korrektheit prüfen
	- Prototyping
		- Prototyp auf der Basis der Analyse/Entwurfs-Dokumente
	- Use-Case-Szenarien
		- “Funktionsfähigkeit” der abstrakten Modelle demonstrieren
	- Abgleich
		- Entwurf mit UseCases/Anforderungskatalog Erste verifizierende Tätigkeiten
- Dynamisches Testen vs. Statisches Testen
	- **Statische Tests** testen das Testobjekt, z.B. informelle Beschreibungen, Modelle, SourceCode, an sich.
	- **Dynamische Tests** testen das lauffähige System, während der Ausführung. Variablen werden verändert und Ausgabewerte beobachtet.
	- ![[Pasted image 20240528143444.png]]
	- ![[Pasted image 20240528143510.png]]
	- ![[Pasted image 20240528143703.png]]
	- ![[Pasted image 20240528143956.png]]
	- Black-Box Test
		- Testen basierend auf Spezifikationen
		- Besonderheiten: 
			- Keine Informationen über innere Strukturen oder Source Code
			- Ausführung ist basiert auf Eingabewerten
			- Verhalten des Testobjekts wird extern überwacht
			- estfälle werden aus Modellen und Anforderungsdokumenten erzeugt
		- ![[Pasted image 20240528144245.png]]
		- Äquivalenzklasse
			- Teilmenge möglicher Eingabeparameter
			- Annahme: Programm reagiert für alle Werte aus der Äquivalenzklasse gleich
			- Teste je einen Repräsentanten aus den Äquivalenzklassen
		- Finden von Äquivalenzklassen:
			- Auswahlkriterien für Werte entwickeln; evtl. kombinieren.
			- zulässige & unzulässige Teilbereiche der Datenwerte ermitteln
			- Unterteilung der zulässigen Bereiche nach verschiedenen Ausgabewerten
			- ![[Pasted image 20240528144845.png]]
			- ![[Pasted image 20240528144959.png]]
			- ![[Pasted image 20240528145100.png]]
		- **Grenzwertanalyse**
			- Randfälle der Spezifikation
			- -**Werte, bei denen:**
				- **"gerade noch"** ein gleichartiges Ergebnis zum Nachbarwert erzielt wird: Dies bezieht sich auf den höchsten Wert, bei dem das System noch ein erwartetes Verhalten zeigt, das dem Nachbarwert ähnelt.
				- **"gerade schon"** ein andersartiges Ergebnis zum Nachbarwert erzielt wird: Dies bezieht sich auf den niedrigsten Wert, bei dem das System ein anderes Verhalten zeigt als der Nachbarwert.
			- Test spezieller Werte
				- Zahlenwert 0
				- negative Zahlen
				- sehr große/kleine Zahlen
				- leere Felder / Sequenzen
				- einelementige Felder / Sequenzen
				- Null-Referenzen
				- Sonderzeichen(Steuerzeichen, Tabulator)
				- Ränder von Zahl-Intervallen
				- Schwellenwerte
			- ![[Pasted image 20240528150051.png]]
			- ![[Pasted image 20240528150124.png]]