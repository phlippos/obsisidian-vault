
Besonderheiten von Software : 
1. Software ist immateriell
2. Software ist leicht änderbar
3. Software schwer zu vermessen
4. Software veraltet

Eigenschaften von Software : 
Externe & Interne Qualität
1. Funktionalität : sicher, richtig
2. Effizienz : Speicherbedarf, rechenintensiv
3. Portierbarkeit : initialisierbar, austauschbar
4. Zuverlässigkeit : wiederherstellbarkeit
5. Benutzbarkeit :verständlich, erlernbar
6. 
Gebrauchsqualität : 
1. Zufriedenheit : Zufriedenheit der Benutzer bei der Verwendung
2. Effektivität : Aufgabenerfüllung innerhalb der Genauigkeitsgrenzen
3. Produktivität : Aufgabenerfüllung innerhalb der Aufwandsgrenzen (Zeit, Kosten)
4. Sicherheit : innerhalb der Risikogrenzen



> Software Engineering ist ein Bereich der Informatik, der sich mit dem systematischen Entwicklungsprozess befasst.

>Um ein hochwertiges Produkt zu erstellen, werden Ingenieurprinzipien verwendet.

Ingenieurdisziplin : 
> systematisches Lösen von Problemen
> Anwendung geeigneter Theorien
> organisatorische & finanzielle Randbedingungen


Gesamter Lebenszyklus der Software
* Anforderungsanalyse : Anforderungen und Ziele werden festgelegt und Ressourcen werden zugewiesen.
* Design : hier wird die Softwarearchitekturen entworfen(Algorithmen, Datenstrukturen,Schnittstellen)
* Entwicklung : Während dieser Phase wird die eigentliche Code geschrieben.
* Wartung : Nach der Bereitstellung kann ein Fehler auftretten oder neue Anforderungen soll hinzugefügt werden.  

>Spannungsdreieck bei der Produktentwicklung
1. Time
2. Cost
3. Qualität
	1. Korrektheit
	2. Zuverlässigkeit
	3. Leistung
	4. Sicherheit
	5. Nutzbarkeit
	6. Verständlichkeit
	7. Weiterentwickelbarkeit
	8. Anpassbarkeit
	9. Wartbarkeit


# #Standish-Report 

![[Pasted image 20240317125735.png]]

> 20% bis 30% der Projekten schlagen komplett fehl. (Misserfolg)
> Hauptgründe  : 
> 	1. zu wenig Nutzer Input
> 	2. unvollständige Anforderungen
> 	3. geänderte Anforderungen




# #Vorgehensmodelle
>systematische Ansätze, die den Entwicklungsprozess organisieren und strukturieren.

> 1. Strukturierung des Projekts
> 2. Kommunikation und Verantwortlichkeiten
> 3. Vorhersage des PRojektergebnis
> 4. Projektkontrolle und Analyse
> 5. Erfahrungssamlung

### *WASSERFALL-MODELL*

>Das Modell ist ein sequentielles Modell, bei dem die Phasen nacheinander abgearbeitet werden, wobei jede Phase auf der vorherigen aufbaut.
>	Die Phasen:
>		1. Analyse (Anforderungen)
>		2. Entwurf
>		3. Implementierung
>		4. Testen
>		5. Wartung
>		
>	Die Vorteile : 
>		1. Einfach zu verstehen, zu managen und zu überwachen
>		
>	Die Nachteile :
>		1. Änderungen in vorherigen Phasen sind shwierig
>		2. Anforderungen müssen klar sein


### *V-MODELL*

>V-Modell ist eine Erweiterung vom Wasserfallmodell.
>Zusätzlich wird zu jeder Entwurfsphase des Modells parallel eine Testphase durchgeführt, die im bottom-up-Prinzip abläuft.
>
>![[Pasted image 20240317134530.png]]
>Für kleinere und einfache Projekte geeignet.
>
>1. **Anforderungsanalyse**: In dieser Phase werden die Anforderungen an die Software gesammelt, analysiert und dokumentiert. Dies bildet die Grundlage für den gesamten Entwicklungsprozess.
    
2. **Grobentwurf**: In dieser Phase wird die Architektur der Software definiert. Es werden Designentscheidungen getroffen, um sicherzustellen, dass die Software die Anforderungen erfüllen kann.
    
3. **Feinentwurf**: Auf der Grundlage der Systemarchitektur wird das Design der einzelnen Module oder Komponenten der Software erstellt.
    
4. **Implementierung**: Während dieser Phase wird der Code geschrieben und die Software entwickelt, basierend auf den zuvor erstellten Designs.
    
5. **Modultest**: Nach der Implementierung werden die einzelnen Module getestet, um sicherzustellen, dass sie isoliert korrekt funktionieren.
    
6. **Integrationstest**: In dieser Phase werden die verschiedenen Module oder Komponenten zusammengeführt und getestet, um sicherzustellen, dass sie ordnungsgemäß miteinander interagieren.
    
7. **Systemtest**: Die gesamte Software wird als Ganzes getestet, um sicherzustellen, dass sie die Anforderungen erfüllt und korrekt funktioniert.
    
8. **Abnahme- und Benutzertest**: Die Software wird den Endbenutzern zur Verfügung gestellt, um sicherzustellen, dass sie deren Anforderungen erfüllt und benutzerfreundlich ist.
9. ![[Pasted image 20240415212634.png]]
>	Vorteile : 
>		1. Qualitätssicherung
>		2. Klare Verbindung von Anforderungen und Tests : Sicherstellung, dass das System den Anforderungen entspricht und korrekt funktioniert
>		3. Strukturiertes Vorgehen
>		4. Frühe Fehlererkennung
>		
>	Nachteile :
>		1. Hohe Abhängigkeiten von Testaktivitäten : Wenn die Testaktivitäten nicht ausreichend geplant oder durchgeführt werden, kann dies zu Verzögerungen führen und die Effektivität des Modells beeinträchtigen.
>		2. weniger Flexibilität, sondern es folgt den fest vorgegebenen Phasen 

### **SPIRAL-MODELL**
>Der Prozess wiederholt sich in einer Spirale, wobei jede Umdrehung die Software weiterentwickelt und verfeinert. Jede Iteration fügt neue Funktionalitäten hinzu oder verbessert bestehende, basierend auf dem Feedback und den Ergebnissen der vorherigen Iteration.
>
>Hier sind die Hauptphasen des Spiralmodells:

1. **Planung**: In dieser Phase werden Ziele identifiziert, Alternativen analysiert und Einschränkungen festgelegt. Es werden auch Risiken identifiziert und bewertet.
    
2. **Risikoanalyse**: Diese Phase beinhaltet eine gründliche Analyse der identifizierten Risiken. Es werden Strategien entwickelt, um Risiken zu minimieren oder zu vermeiden.
    
3. **Entwicklung von Prototypen**: Basierend auf den identifizierten Risiken und Anforderungen werden Prototypen erstellt. Diese dienen dazu, Konzepte zu validieren und Anforderungen zu verfeinern.
    
4. **Evaluierung**: In dieser Phase werden die Prototypen bewertet und Feedback gesammelt. Es wird überprüft, ob die Anforderungen erfüllt werden und ob Änderungen vorgenommen werden müssen.
    
5. **Planung der nächsten Iteration**: Basierend auf dem Feedback aus der Evaluierung werden Pläne für die nächste Iteration erstellt. Dies kann die Entwicklung eines neuen Prototyps oder die Weiterentwicklung des bestehenden Prototyps beinhalten.
Vorteile : 
1. Für große und komplexe Systeme geeignet
Nachteile :
1. Kosten und Zeit schwer planbar
2. Verfahren für Prototypen nicht festgelegt
### *AGILE-MODELL*

>--Agile ist eine Softwareentwicklungstechnik, bei der **Zusammenarbeit, Kundenzufriedenheit und Flexibilität** im Vordergrund stehen.
>
>--Ein iterativer und inkrementeller Ansatz.
>
>--Es erfordert eine enge Zusammenarbeit zwischen dem Entwiclungsteam und Kunden, um sicherzustellen, dass die entwickelte Software die Erwartungen und die Anforderungen von Kunden erfüllt.
>
>--Auf Veränderungen reagieren statt einem Plan folgen
>
>--Regelmäßige Bereitstellung funktionierender Software, wobei der Schwerpunkt auf der Präferenz für Zeitrahmen liegt.
> 	
> 	-->der-agile-Softwareentwicklungsprozess 
> 		1. Anforderungserfassung : Die Anforderungen des Kunden werden festgestellt und priorisiert.
> 		2. Planung : Erstellung eines Plan für die Bereitstellung der Software
> 		3. Entwicklung : Erstellung der Software
> 		4. Testen : Die Software wird getestet
> 		5. Bereitstellung : Die Software wird verwendet
> 		6. Wartung : ob die Software die Bedürfnissen des Kunden entspricht.
> 		
> 	Vorteile : 
> 		1. besser an sich schnell ändernde Anforderungen anpassen und schneller reagieren
> 		2. sofortiges Feedback erhalten
> 		3. Verbesserte Qualität und Zuverlässigkeit
> 		
> 	Nachteile : 
> 		1. Mangelnde Vorsehbarkeit
> 		2. Mangelnde Betonung auf Test
> 		3. abhängig zu stark von Kundensfeedback
> 		


### *SCRUM*

>--Ein agiles Modell
>
>--Scrum zielt darauf ab, komplexe Projekte in kurzen Iteration(Sprints) abzuschließen. 
>
>--Scrum fördert iterative Entwicklung, Zusammenarbeit im Team und die Fähigkeit sich an verändernde Anforderungen anzupassen.
>
>	--> Hauptakteure : 
>		1. Product Owner : verantwortlich für die Maximierung des Wertes des Produkts und die Priorisierung des Produktbacklogs.
>		2. Scrum Master : Sie helfen dem Team, Hindernisse zu beseitigen, fördern eine effektive Kommunikation und unterstützen die kontinuierliche Verbesserung.
>		3. Entwicklungteam : selbstorganisiert und multifunktional
>		
>	--> Lebenszyklus von Scrum : 
>		1. Sprint : ein Zeitraum, in dem das team seine Arbeit abschließen soll. (2 - 4 Wochen)
>		2. Sprint Rewiev : Am ende eines Sprints präsentiert das Team das Inkrement den Stakeholdern und erhält Feedbacks.
>		3. Sprint Retrospective: In dieser Phase wird die Qualität oder der Status des Produkts überprüft.
>		4. Product Backlog : Product Owner erstellt eine nach Prioritäten geordnete Liste.
>		5. Sprint Planung : Das Team wählt die Aufgaben aus dem Product Backlog und plant die Details des Sprints 
>		6. Sprint Backlog : eine Liste , die die ausgewählte Aufgaben enthält
>		
>	--> Vorteile :
>		1. Hohe Produktivität
>		2. Hohe Anpassungsfähigkeit
>		3. Geringes Risiko
>		
>	--> Nachteile : 
>		1.nur für kleine Teams anwendbar
,

### *KANBAN*

>-- ein agiles Arbeitsframework, das darauf abzielt, den Arbeitsfluss zu visualisieren, Engpässe aufzudecken und eine kontinierliche Verbesserun der Prozesse zu fördern.
>--Visualisierung des Arbeitsflusses über ein Kanban-Board.
>--Ein Kanban-Board  ist in Spalten unterteilt, die den verschiedenen Phasen des Arbeitsprozesses.
>--Kanban-Karten sind Aufgaben, die durch das Board bewegt werden, um ihren aktuellen Status widerzuspiegeln.
>![[Pasted image 20240317151052.png]]
>	-->wichtigtse Konzepten : 
>		1. WIP-LIMITS : Kanban setzt WIP-Lmits für jede Spalte fest, um sicherzustellen, dass das Team nicht überlastet wird und Engpässe deutlich sichtbar werden.
>		2. Flexibilität : anpassungsfähig und Kanban kann leicht an die spezifischen Bedürfnisse und Gegebenheiten eines teams angepasst werden.
>		3. Pull-System : bei Pull-System werden Aufgaben nur dann in den nächsten Scritt des Prozesses gezogen, wenn  die Kapazität dafür verfügbar ist.
>		
>	--> Vorteile : 
>		1. Hohe Produktivität.
>		2. Probleme Werden schnell sichtbar.
>		
>	--> Nachteile
>		1. Spalten lassen nur begrenzte Komplexität zu.