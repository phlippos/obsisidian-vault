- Aufgabe1 : 
	- - Was sind _Coding Conventions_?
		- Dateiorganisation
		- Einrückungen
		- Kommentare
		- Deklarationen
		- Anweisungen
		- Leerzeichen
		- Namenskonventionen
	- - Warum ist es sinnvoll sich innerhalb eines Teams auf gemeinsame _Coding Conventions_ zu einigen?
		- um die Lesbarkeit des Quellcodes zu verbessern und die Softwarewartung zu erleichtern.
- Aufgabe2 : 
	- SQL-Coding-Richtlinien
		- Großschreibung für SQL-Schlüsselwörter
		- Einrückung für verschachtelte Abfragen
			- SELECT column1 
			 FROM table1 
			 WHERE column2 IN (
				 SELECT column2
				 FROM table2
				 WHERE condition
			 );
		 - Vermeidung von zu langen Zeilen
		 - Namenskonventionen
			 - Verwendung von sinnvollen und beschreibenden Namen
			 - Konsistenz in der Benennung
				 -  Tabellen: Singular (z.B. `employee` statt `employees`)
				 -  Spalten: snake_case (z.B. `first_name`)
		-  Abfrageoptimierung
			- Verwendung von Joins statt von Unterabfragen, wenn möglich
			- Indexierung :  Indizes für Spalten, die häufig in `WHERE`-Klauseln oder Joins verwendet werden.
			- Vermeidung von `SELECT *
		-  Sicherheit und Best Practices
			- SQL-Injection vermeiden
		-  Kommentare
			- Verwendung von Kommentaren zur Erklärung komplexer Abfragen
	- Python coding Richtlinien
		- Verwendung von einheitlichem Einrückungsstil (4 Leerzeichen)
		- Einfügen von Leerzeilen zur Trennung von Codeblöcken
		- Namenskonventionen
			- Verwendung von sinnvollen und beschreibenden Namen:
				- Variablen: `snake_case`
				- Funktionen: `snake_case`
				- Klassen: `CamelCase`
			- Vermeidung von Ein-Buchstaben-Variablen (außer in Schleifen)
		-  Dokumentation und Kommentare
			- Verwendung von Docstrings für Module, Klassen und Funktionen
				- def my_function(param1, param2):
				     """ Diese Funktion macht etwas.
				     Args:
					     param1 (int): Die erste Parameterbeschreibung.
					     param2 (str): Die zweite Parameterbeschreibung.
				     
				     Returns: 
					     bool: Die Rückgabebeschreibung.
				     """ 
				     pass
			- Verwendung von Kommentaren zur Erklärung komplexer Logik
		- Fehlerbehandlung
			- Verwendung von Ausnahmen für Fehlerbehandlung: (try, except)
			- Spezifische Ausnahmen verwenden, nicht allgemeine
		- Code-Strukturierung
			- Verwendung von Funktionen und Klassen zur Modularisierung des Codes
			- Vermeidung von zu langen Funktionen und Methoden (idealerweise max. 50 Zeilen)