l
#### **Warum gibt es Softwarearchitektur**
>Strukturiertes Vorgehen bei der Entwicklung
>Solides Fundament für Software
>Wohldefinierte Punkte für Erweiterung
>keine unkontrollierten Balkonanbauten

#### **Aspekte der Softwarearchitektur**
>Sie bildet die wichtigsten strukturellen Eigenschaften eines Systems präzise und kompakt ab.
>Softwarearchitektur beschreibt die Struktur eines Programms oder Systems.
>	Die Beschreibung beinhaltet die Eigenschaften eines Systems, die sich auf bezogen auf das gesamte System beschreiben und analysieren lassen.
>	
>*<mark style="background: #FFF3A3A6;">*Softwarearchitektur** ist ein Konzept, das den Rahmen und die Überblicksstruktur für die Entwicklung und Organisation von Softwaresystemen bereitstellt. Es befasst sich damit, wie Softwarekomponenten strukturiert und miteinander interagieren, um ein System zu bilden.</mark>


#### **Bestandteile der Softwarearchitektur**
>**Komponenten** :
>				**Softwarearchitektur** teilt ein System in verschiedene Komponenten, die spezifische Aufgaben oder Funktionen erfüllen. Diese Komponenten können einzelne Module, Klassen oder Pakete sein, abhängig von der Größe und Komplexität des Svystems.
>**Verbindungen** :
>				**Softwarearchitektur** beschreibt,wie diese Komponenten miteinander interagieren. Die Verbindungen können durch verschiedene Kommunikationswege wie API-Aufrufe, Nachrichtenübermittlung, Datenflüsse usw. realisiert werden.
>**Schichten und Abstraktion** : 
>				Viele Architekturen sind in Schichten organisiert, wobei jede Schicht eine bestimmte Abstraktionsebene darstellt. Dies hilft dabei, die Komplexität zu reduzieren und die Wartbarkeit zu verbessern.

#### **Ziele von Softwarearchitektur**
>Effiziente Entwicklung
>Wiederverwendung
>Integrationsrahmen
>Bewertung
>Grundlage für Projektplanung
>Risikominimierung
>Kommunikation zwischen Stakeholdern


![[Pasted image 20240430064242.png]]


#### **Sichten auf ein System**
>Eine **Sicht** ist eine Darstellung eines Systems, die nur die Elemente und Beziehungen enthält, die für eine bestimmte Perspektive relevant sind
>![[Pasted image 20240430064645.png]]
>**Statisches strukturelles Modell**: Bildet wesentliche Komponenten und deren Interfaces ab.
>**Dynamisches Prozessmodel**: Diese Sicht beschreibt die Prozesse und Abläufe, die während des Lebenszyklus der Softwareentwicklung auftreten, einschließlich Anforderungsmanagement, Design, Implementierung, Testing und Wartung. Sie bezieht sich auch auf die Methodik der Softwareentwicklung, wie Agile, Scrum oder Waterfall.
>**Deployment Model**: Stellt die Verteilung der Ressourcen dar (Prozessoren,Netzwerkverbindung,...)




<mark style="background: #FFB86CA6;">Architektur hilft sich auf die wichtigen Teile zu konzentrieren und Alternativen schon vor der Entwicklung abzuwägen.</mark>


### **Komponentendiagram**
>![[Pasted image 20240430071554.png]]
>![[Pasted image 20240430072214.png]]

### **Verteilungsdiagram**
>![[Pasted image 20240430072521.png]]
>![[Pasted image 20240430072548.png]]
>![[Pasted image 20240430072602.png]]



#### **Bekannte Architekturstile**
>![[Pasted image 20240430072834.png]]
>![[Pasted image 20240430073122.png]]
>**2-tier-Architektur**
>	Problem: Mehrere Clients greifen auf dieselben Daten zu
>	Lösung: Trennung von Anwendung und Datenhaktung
>**3-Tier-Architektur**
>	**Trennung von Anliegen**
Durch die Aufteilung der Präsentation, Geschäftslogik und Datenhaltung in separate Schichten wird das Prinzip der Trennung von Anliegen (Separation of Concerns) umgesetzt. Jede Schicht konzentriert sich auf eine spezifische Aufgabe:
 - **Präsentationsschicht**: Verantwortlich für die Darstellung der Benutzeroberfläche und die Interaktion mit dem Benutzer.
 - **Geschäftslogikschicht**: Behandelt alle geschäftsrelevanten Prozesse und Regeln.
 - **Datenschicht**: Managt die Datenpersistenz und den Datenzugriff.

 - Problem: Unterschiedliche Clients sollen die gleiche Funktionalität bieten Präsentation der Daten soll austauschbar sein 
 - Lösung: Implementierung der Präsentation in einer eigenen Schicht
> **Peer-to-Peer**
> Peers übernehmen Client-ähnliche und/oder Serverähnliche Aufgaben beliebige Topologie dezentralisierte Berechung mit Kontroll- und Datenfluss zwischen Peers robust gegen Ausfall einzelner Knoten skalierbar bzgl. Resourcen und Rechnerkapazität Beispiele: BitTorrent, Napster, Gnutella, …
> **Pipes and Filters**
> In einem System durchlaufen Datenströme verschiedene Bearbeitungsstufen.
> Der Datenfluß soll leicht änderbar sein.
> Bearbeitungsstufen sollen austauschbar, erweiterbar und wiederverwendbar sein.
> Stil: Beschreibung von Bearbeitungsstufen durch Filters und Datenströme durch Pipes.
> 	Filter-Komponenten haben Ein/Ausgänge und bearbeiten einen Datenstrom.
> 	Pipes: Datenstrom von einem Filter-Ausgang zu einem Filter-Eingang.
> 	Filter bearbeiten Eingangsdaten kontinuierlich.