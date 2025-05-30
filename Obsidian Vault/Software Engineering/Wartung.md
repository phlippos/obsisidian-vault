**Wartung**:

- Definition laut IEEE: Änderungen an Software nach der Auslieferung, um Fehler zu beheben, die Leistung zu verbessern oder an geänderte Umgebungen anzupassen.
- Unterscheidung zwischen Wartung und Software-Evolution: Wartung erfolgt nach der Auslieferung, Evolution ist ein kontinuierlicher Prozess während der Entwicklung.
- **Wartungstätigkeiten**:
    - **Reengineering**: Neuentwicklung eines bereits funktionierenden Teils der Software.
    - **Reverse Engineering**: Ableiten von Code oder Modellen aus bestehenden Artefakten.
    - **Refactoring**: Veränderungen im Quelltext ohne Funktionsänderung.
- **Anti-Pattern**:
- Wiederkehrende schlechte Lösungen oder Praktiken, wie z.B. "The Blob" oder "Spaghetti Code".
- allgemeine Lösung für ein Problem, die negative Folgen hat,
- Gründe: Unwissenheit, Unerfahrenheit, Anwendung von Pattern im falschen Kontext, stetige Evolution
- Design Patterns als positive Gegenstücke zu Anti-Patterns.
- ![[Pasted image 20240626204325.png]]
- The Blob
	- Klasse interagiert mit sehr vielen anderen Klassen.
	- Indikatoren: schrecklicher Test-Code sehr viele Initialisierungen/Hilfsmethoden, die vor den Tests durchlaufen
	- Problem: 
	- God class kennt das ganze System
	- “single point of failure” wahrscheinlich
	- Lösung: 
		- Verantwortlichkeiten in mehrere Klassen aufteilen 
		- Refactoring
- Golden hammer
	- "Golden Hammer" beschreibt ein Anti-Pattern in der Softwareentwicklung, bei dem ein bestimmtes Werkzeug oder eine Technologie als universelle Lösung für alle Probleme angesehen wird,unabhängig davon, ob es die beste Lösung ist.
	- Bessere Lösungen für spezifische Probleme, wie etwa Performance oder Skalierbarkeit, werden ignoriert.
	- Das System wird unnötig komplex und schwer wartbar, weil alles um das externe Tool herum gebaut wird.
	- Entstehung:
		- Ignoranz gegenüber besseren, state-of-the-art Lösungen.
	- Lösung:
		- Refactoring
- Spaghetti Code
	- Der Code ist unstrukturiert und enthält viele Sprünge im Programmfluss, was ihn schwer verständlich und wartbar macht.
	- Indikatoren:
		- Prozess-orientierte Implementierung : Anstatt objektorientiert zu sein, folgt der Code einem prozess-orientierten Ansatz.
		- Unstrukturierter Code : Der Code mischt verschiedene Belange und Aufgaben ohne klare Struktur.
		- Lange Methoden ohne Parameter : Methoden verwenden globale Variablen statt Parameter, was den Code schwer nachvollziehbar macht.
	- Probleme
		- Hoher Zeitaufwand für das Verständnis
		- Schwierigkeiten bei der Wartung
		- Hohe Wahrscheinlichkeit von Fehlinterpretationen
	- Entstehung:
		- Fehlendes Design
		- Unkenntnis von objektorientierten Designmechanismen
		- Keine oder unzureichende Code Reviews
		- Isolation
	- Lösung:
		- Refactoring
- Refactoring : 
	- Methoden zur Verbesserung der internen Struktur von Code ohne Änderung des externen Verhaltens.
	- Beispiele: Extract Method, Rename Variable.
	- Ziele des Refactorings: Lesbarkeit, Reduktion von Komplexität, Testbarkeit, Wiederverwendbarkeit und Erweiterbarkeit.
	- Extract Method :
		- Methode ist zu lang
		- Methode braucht Kommentare für Struktur/Verständnis,
		- starke Verzweigung innerhalb der Methode.
		- Vorgehen:
			- Neue Methode mit sinnvollem Namen anlegen.
			- Extrahierten Code in diese Methode kopieren.
			- Zugriffe auf lokale Variablen suchen werden als Parameter übergeben
			- Variablen, die nur im Fragment benutzt werden in neuer Methode definieren.
			- Änderungen von lokalen Variablen
				- Rückgabewert der neuen Methode oder
				- Referenz als Parameter übergeben
			- Originalquelltext mit Methodenaufruf ersetzen

### Reifegradmodelle
- ISO 9000 prüft nicht die Qualität des Produkts, sondern die Qualität der Organisation!
- Ziele von Reifegradmodellen:
	- messen Reife des gesamten SoftwareEntwicklungsprozesses
	- entdecken Schwachstellen und Verbesserungspotenzial
	- schlagen Maßnahmen zur Qualitätsverbesserung vor
	- messen die Wirkung dieser Maßnahmen
- Capability Maturity Model (CMM):
	- Bewertet die Reife von Software-Entwicklungsprozessen in fünf Stufen: adHoc, gesteuert, definiert, überprüfend und optimierend.
	- Stufe 1 (adHoc):
		- Prozesse sind unvorhersehbar und reaktiv.
	- Stufe 2 (repeatable, gesteuert):
		- Grundlegende Projektmanagementprozesse sind etabliert.
		- Projekte können wiederholt erfolgreich durchgeführt werden.
	- Stufe 3 (definiert):
		- Prozesse sind standardisiert, dokumentiert und konsistent in der gesamten Organisation implementiert.
	- Stufe 4 (überprüfend): 
		- Organisation hat detaillierte Messgrößen, um Prozesse und Produkte zu kontrollieren.
		- Prozesse sind quantitativ verstanden und kontrolliert.
	- Stufe 5 (optimierend):
		- Organisation fokussiert auf kontinuierliche Prozessverbesserung.

### CI/CD/CD/DevOps
- Continuous Integration:
	- Integration einzelner Komponenten in ein zentrales Repository mit automatisierten Builds und Tests, um Integrationsprobleme früh zu erkennen.
	- 4 Dinge sind notwendig:
		- Verbindung zur Versionskontrolle
		- automatisiertes Buildscript
		- Mechanismus zur Rückmeldung
		- Prozess, um die Änderungen des Quellcodes zu integrieren
- Continuous Delivery:
	- Software wird regelmäßig auf eine Produktionsumgebung geliefert, der Release erfolgt manuell.
- Continuous Deployment
	- Automatischer Release-Prozess nach jeder Änderung.
- Wall of Confusion
	- Development ist mit der Entwicklung fertig.
	- Entwickler werfen ihren Code über die WoC, ohne sich Gedanken zu machen, wie das System zum Laufen gebracht wird.
	- Operations liefert das Produkt, muss es installieren und zum Laufen bringen.
	- Installation ist of problematisch & unnötig komplex.
	- Auslieferung verzögert sich.
- Development & Operations
	- Kombination von Development und Operations, um Transparenz und Zusammenarbeit zu fördern und schnelle Problemlösungen zu ermöglichen.