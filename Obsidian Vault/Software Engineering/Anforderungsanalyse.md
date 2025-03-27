
>-- Probleme bei der Anforderungsanalyse : 
>	1. Kunden wissen nicht was sie wollen
>	2. Kunden sprechen ihre eigene Sprach
>	3. verschiedene Stakeholder können widersprüchliche Anforderungen haben
>	4. politische und organisatorische Faktoren können Anforderungen beeinflussen
>	5. Anforderungen ändern sich während der Analyse und Entwicklung

- Stakeholder : Stakeholder sind Personen oder Organisationen, die von den Aktivitäten eines Unternehmens betroffen sind oder davon beeinflusst werden. Dazu gehören unter anderem **Kunden**, **Lieferanten, Mitarbeiter, Investoren oder die Gesellschaft als Ganzes**.

**Was ist eine Anforderung ?**
+ Eine Bedingung oder Fähigkeit, die ein Benutzer benötigt, um ein Problem zu lösen oder ein Ziel zu erreichen.
+ eine dokumentierte Darstellung eines Zustandes oder einer Fähigkeit gemäß


>--Benutzeranforderungen : 
>	1. Aussagen in natürlicher Sprache, sowie Diagramme zur Beschreibung der Dienste, die das System leisten soll,
>--Systemanforderungen :
>	1.Detaillierte Festlegung von Funktionen, Diensten und Beschränkungen. Beschreibung, was implementiert werden soll.

- Funktionale Anforderungen : was das System tun soll, um die Bedürfnisse oder Erwartungen des Benutzers zu erfüllen.
	+ // Ein Benutzer muss sich mit seinem Benutzernamen und Passwort beim System anmelden können.
	+ //Das System berechnet die Umsatzsteuer für den Einkauf des Benutzers.
	+ //Das System sendet eine Bestätigungs-E-Mail an den Benutzer, nachdem er eine Bestellung erfolgreich aufgegeben hat.
+ Nicht-funktionale Anforderungen : Wie soll das System arbeiten? Wie sollen einzelne Funktionen arbeiten? Diese Anforderungen definieren die Qualitäten, Eigenschaften und Einschränkungen des Systems und nicht seine spezifischen Merkmale. Qualitätsanforderungen : Performanz, Zuverlässigkeit, usw.
	+ Das System sollte eine Webseite in weniger als 3 Sekunden laden.
	+ Die Anwendung sollte in der Lage sein, innerhalb von sechs Monaten einen Anstieg des Benutzerverkehrs um 50 % ohne Leistungseinbußen zu bewältigen.
	+ “Die Software soll in C++ geschrieben sein.
![[Pasted image 20240415231939.png]]
**Anforderungsanalyse**
+ Eine Anforderungsanalyse hilft, Software von Anfang an richtig zu entwickeln und <mark style="background: #ABF7F7A6;">Zeit und Kosten zu sparen</mark>.
+ Der Prozess der Untersuchung der Bedürfnisse von Nutzer und eine Definition von System-, Hardware oder Software-Anforderungen zu erlangen
+ In der Anforderungsanalyse identifizieren wir, alle funktionalen und nicht-funktionalen Anforderungen.
![[Pasted image 20240323215304.png]]
1. **Ermitteln** : Hier wird verschiedene Techniken genutzt, um die Anforderungen der Stakeholder festzustellen. Außerdem wird hier auch Konflikte zwischen verschiedenen Stakeholdern aufgedeckt und diese aufgelöst.
	1. Methoden : 
		1. Interview
		2. Focus Group
		3. Fragebogen
		4. Prototyping
		5. Beobachtung
		6. DOkumentenanalyse
	2. Anforderungen formulieren:
		1. eindeutig
		2. konsistent
		3. vollständig
		4. änderbar
		5. korrekt
		6. nachvollziehbar
2. **Dokumentieren** : Durch die Dokumentation werden erarbeitete Anforderungen adäquat beschrieben. Hierfür können unterschiedlich Techniken eingesetzt werden, um Anforderungen in natürlicher Sprache oder in Modellen zu dokumentieren.
3. **Validieren** : Dokumentierte Anforderungen müssen frühzeitig geprüft werden, um zu gewährleisten, dass sie der geforderten Qulität genügen.
4. **Verwalten** : Die Anforderungsverwaltung umfasst alle Maßnahmen, die notwendig sind, um Anforderungen zu strukturieren, für unterschiedliche Rollen aufzubereiten sowie konsistent zu ändern.

> **Priorisierung von Anforderungen**
> -- **essential** : Ohne das geht nicht
> -- **notwendig** : wichtig aber nicht kritisch
> -- **wüschenswert** : wäre schön, muss aber nicht
> 
> Die Priorisierung von Anforderungen im Software Engineering ist ein wichtiger Prozess, der sicherstellt, dass die begrenzten Ressourcen eines Entwicklerteams effektiv genutzt werden, um die wichtigsten Funktionen und Verbesserungen zu implementieren.


> **Validierung von Anforderungen**
> Wird der Bedarf des Kunden vollständig abgedeckt? Verständlich formuliert? Konsistent mit anderen Anforderungen? Realistisch mit Budget und Technologie? Anforderung prüfbar? Änderbar ohne Einfluss auf andere Anforderungen?

+ Traceability
	+ Rückverfolgbarkeit : Nachvollziehbarkeit von Anforderungen über den gesamten Entwicklungsprozess
	+ Teil des Anforderungsmanagements

+ Abgrenzungskriterien 
	+ Warum soll etwas nicht gemacht werden? 
		+ Dem Kunden klar machen, worauf er verzichtet.

+ Anforderung in Textverarbeitung
	+ Anforderungen können in Freitext erfasst werden.
	+ **Nachteile** 
		+ Informell
		+ keine Zugriffsrechte
		+ parallele verarbeitung?
+ Anforderung in einer Tabelle/ Datenbank
	+ Tabelle bietet mehr Möglichkeiten
		+ einheitliches Datenschema
		+ Filter
		+ spezielle Felder (Autor, Status)
	+ Datenbank erweitert das um : 
		+ Zugriffsrechte
		+ paralleles Arbeiten
		+ zentrale Datenhaltung (Konsistenz)


### **Use Cases**
+ Funktionale Zerlegung 
+ Akteure interagieren mit dem System
+ Anwendungsfälle repräsentieren die Anforderungen



| Anwendungsfall/Use Case                         | Akteur                                     |
| ----------------------------------------------- | ------------------------------------------ |
| in sich abgeschlossene zusammenhängende Einheit | Objekt, das mit dem System interagiert     |
| Teil der Funktionalität des Systems             | nicht Bestandteil des Systems              |
| Beschreiben ein Vorgehen aus Sicht des Nutzers  | Personen, externe Geräte usw.              |
| Haben ein Ziel                                  | tauschen mit dem System Nachrichten aus    |
| beschreiben, was gemacht wird                   | können Nachrichten senden/empfangen        |
| beschreiben nicht wie etwas gemacht wird        | oft müssen Daten über sie verwaltet werden |

* Textueller Anwendungsfall:
	Titel,
	Kurzbeschreibung,
	Akteure,
	Vorbedingungen,
	Auslösendes Ereignis,
	Beschreibung des Ablaufs,
	Nachbedingung Erfolg,
	Nachbedingung Fehlschlag,
	Anmerkungen,
	Erweiterungen (optional),
	Alternativen (optional)

Lastenheft : 
Vom Auftraggeber festgelegte Gesamtheit der Forderungen an die Lieferungen und Leistungen eines Auftragnehmers an den Auftrag

Beschreibung des WAS und WOFÜR
Grundlage für das Pflichtenheft

![[Pasted image 20240416003301.png]]
