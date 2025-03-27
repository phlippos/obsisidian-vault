### Message Passing
- Ein Prozess, der eine Nachricht senden möchte, erstellt die Nachricht und verwendet dann eine Kommunikationsschnittstelle, um die Nachricht an einen anderen Prozess zu senden. Der empfangende Prozess wartet auf den Eingang der Nachricht und verarbeitet sie dann entsprechend.
- **Synchrones Messaging**: Der sendende Prozess wartet, bis die Nachricht vom empfangenden Prozess bestätigt wird. Dies stellt sicher, dass die Nachricht erfolgreich übermittelt wurde, führt jedoch zu Wartezeiten, wenn der empfangende Prozess nicht sofort verfügbar ist.
    
- **Asynchrones Messaging**: Der sendende Prozess sendet die Nachricht und fährt fort, ohne auf eine Bestätigung zu warten. Die Nachricht wird in einer Warteschlange gespeichert, bis der empfangende Prozess bereit ist, sie zu verarbeiten. Dieses Modell ist effizienter, da der sendende Prozess nicht blockiert wird.
    
- **Nachrichtenwarteschlangen**: Nachrichten können in speziellen Warteschlangen gespeichert werden, wo sie aufbewahrt werden, bis der empfangende Prozess sie abruft. Dies ermöglicht eine Entkopplung von Sender und Empfänger, da sie nicht gleichzeitig aktiv sein müssen.
- Pro : 
	- Möglichkeit, dass Sender und Empfänger auf unterschiedlichen Maschinen oder sogar in verschiedenen Netzwerken arbeiten können.
	- Nachrichtenübermittlung kann relativ sicher gestaltet werden, insbesondere wenn Nachrichten verschlüsselt und Authentifizierungsmechanismen implementiert werden.
	- Möglichkeit für den Empfänger, die eingehenden Nachrichten zu überprüfen, bevor sie weiterverarbeitet werden. Dies ermöglicht eine bessere Kontrolle und Validierung der Daten und stellt sicher, dass nur korrekte und relevante Nachrichten verarbeitet werden.
- Contra:
	- Für jeden Datentransfer müssen sowohl eine send()- als auch eine receive()-Operation ausgeführt werden. Dies kann den Kommunikationsprozess verlangsamen.
	- Der empfangende Prozess muss darauf vorbereitet sein, Nachrichten zu empfangen. Dies kann dazu führen, dass der empfangende Prozess blockiert wird.

### Shared Memory
- Gemeinsamer Speicher (Shared Memory) ist eine Technik, bei der mehrere Prozesse direkt auf denselben Speicherbereich zugreifen können, um Daten auszutauschen.
- Pro:
	- Sehr schnell
	- Geringer Overhead
	- Effiziente Kommunikation großer Datenmengen
- Contra :
	- Es erfordert eine sorgfältige Synchronisation der Zugriffe, um sicherzustellen, dass keine Datenkorruption auftritt. Dies kann durch die Verwendung von Sperren (Locks) oder anderen Synchronisationsmechanismen erreicht werden.
	- Sender und Empfänger müssen sich auf derselben Maschine befinden
	- ,Weniger sicher
	-  Direkter Zugriff

### Direct Communication
- Das grundlegende System der Nachrichtenübermittlung arbeitet ohne Vermittler. Die Kommunikation erfolgt direkt zwischen den beteiligten Prozessen.
- Bei der Nachrichtenübermittlung in Betriebssystemen werden häufig Systemaufrufe verwendet, um Daten zwischen Prozessen zu senden und zu empfangen. Diese Aufrufe spezifizieren immer die beteiligten Prozesse als Ziel oder Quelle.
- Jedes Telefon ist mit einem anderen Telefon fest verdrahtet. (z.B.)
- Die Verwendung von `send` und `receive` Systemaufrufen zur Nachrichtenübermittlung hat erhebliche Einschränkungen, insbesondere für Server, die Anfragen von verschiedenen Prozessen bearbeiten müssen.
- Empfangsprozess muss alle potenziellen Sender kennen.
![[Pasted image 20240624210312.png]]
### Indirect Communication
- Mailboxen sind Systemobjekte, die vom Betriebssystemkern auf Anfrage eines Benutzerprozesses erstellt werden. Sie ermöglichen eine effizientere und flexiblere Kommunikation zwischen Prozessen, indem sie als Zwischenspeicher für Nachrichten dienen.
- **send(mailbox, msg, size)**: Dieser Systemaufruf wird verwendet, um eine Nachricht an eine Mailbox zu senden. Der Aufruf spezifiziert die Ziel-Mailbox, die Nachricht und deren Größe. Der sendende Prozess übermittelt die Daten an die Mailbox, wo sie zwischengespeichert werden, bis sie vom empfangenden Prozess abgerufen werden.
- **receive(mailbox, msg, size)**: Mit diesem Systemaufruf empfängt ein Prozess eine Nachricht aus einer Mailbox. Der empfangende Prozess gibt die Mailbox an, aus der die Nachricht abgerufen werden soll, sowie den Speicherbereich und die Größe, in dem die Nachricht gespeichert werden soll.
- ![[Pasted image 20240624210536.png]]
- Unterschiedliche Prozesse können Nachrichten an eine gemeinsame Mailbox senden.
- Ein Prozess, der auf Nachrichten aus einer Mailbox wartet, muss die Identität der sendenden Prozesse nicht kennen.
- Ein Prozess kann in einer Mailbox auf Nachrichten von mehreren Sendern warten.
- Der empfangende Prozess bearbeitet die erste Nachricht, die in der Mailbox eingeht.
- #### Private Mailboxes
	- Nur der Prozess, der die Erstellung der Mailbox angefordert hat, und seine Kindprozesse können Nachrichten über diese Mailbox empfangen.
	- Private Mailboxen existieren nur solange, wie der Prozess, der ihre Erstellung angefordert hat, und alle seine Kindprozesse aktiv sind.
	- Private Mailboxen werden häufig als Ports bezeichnet. Ein bekanntes Beispiel für die Implementierung von Ports sind BSD-Sockets.
	- erhöhte Sicherheit
	- Isolation und Kontrolle
- #### Public Mailboxes
	- ein Mechanismus zur Inter-Prozess-Kommunikation (IPC), der von allen berechtigten Prozessen gemeinsam genutzt wird.
	- Diese Mailboxen sind im Besitz des Systems
	- Öffentliche Mailboxen werden vom System verwaltet und sind nicht an einen spezifischen Prozess gebunden.
	- Alle Prozesse, die die entsprechenden Berechtigungen besitzen, können Nachrichten über diese Mailboxen senden und empfangen
	- Öffentliche Mailboxen bleiben auch dann bestehen, wenn der Prozess, der ihre Erstellung angefordert hat, beendet wird. Dadurch wird sichergestellt, dass die Kommunikation fortgesetzt werden kann, selbst wenn einzelne Prozesse nicht mehr aktiv sind.
	- Effizienz bei Prozessen auf derselben Maschine
### Blocking Primitives
- Blockierende Primitiven in der Inter-Prozess-Kommunikation (IPC) sind Mechanismen, bei denen der sendende oder empfangende Prozess wartet (blockiert), bis die Operation abgeschlossen ist. Diese Primitiven bieten eine direkte und synchrone Methode zur Nachrichtenübermittlung.
- Ein blockierendes `send` kehrt erst zurück, wenn der empfangende Prozess die Nachricht erhalten hat. Dies bedeutet, dass der sendende Prozess während der Wartezeit blockiert ist und keine weiteren Aufgaben ausführen kann.
- Keine Pufferung erforderlich
	- Da der sendende Prozess auf die Bestätigung des Empfangs wartet, ist keine zusätzliche Pufferung der Nachricht erforderlich. Die Nachricht wird direkt vom Sender an den Empfänger übermittelt.
- blockierende Empfangen, bei dem der empfangende Prozess wartet, bis eine Nachricht eingetroffen ist. 
- Ein blockierender `receive`-Aufruf kehrt erst dann zurück, wenn der empfangende Prozess tatsächlich eine Nachricht erhalten hat. Der Prozess bleibt in einem Wartezustand, bis die Nachricht eintrifft.

### Non-Blocking Primitives
- Nicht-blockierende Primitives sind Mechanismen zur Nachrichtenübermittlung, die es Prozessen ermöglichen, Nachrichten zu senden und zu empfangen, ohne auf den Abschluss der Übermittlung warten zu müssen.
- Ein nicht-blockierender `send`-Aufruf kehrt sofort zurück, nachdem das Betriebssystem die Nachricht zur Zustellung akzeptiert hat. Der sendende Prozess muss nicht warten, bis die Nachricht vom empfangenden Prozess tatsächlich empfangen wird.
- Das Betriebssystem speichert die Nachricht in einem Puffer, bis sie vom empfangenden Prozess abgeholt wird.
- Ein nicht-blockierender `receive`-Aufruf kehrt sofort zurück, entweder mit einer Nachricht, falls vorhanden, oder mit der Information, dass die Mailbox leer ist. Der empfangende Prozess wird nicht blockiert, wenn keine Nachricht vorliegt.
- ![[Pasted image 20240624212930.png]]


### Class of Service
#### Datagrams
- Datagramme sind eine Methode zur Nachrichtenübermittlung, bei der jede Nachricht als eigenständige Einheit behandelt wird. Sie werden häufig in Netzwerkkommunikationen verwendet, insbesondere bei Protokollen wie UDP
- Jede Nachricht wird unabhängig von anderen Nachrichten gesendet. Es gibt keine Garantie, dass die Nachrichten in der Reihenfolge ankommen, in der sie gesendet wurden.
- Nachrichten können verloren gehen, dupliziert werden
- Es gibt keine eingebaute Fehlerkorrektur oder Bestätigung, dass die Nachricht angekommen ist.
- Zuverlässige Datagramme
	- Zuverlässige Datagramme werden so lange erneut gesendet, bis der Absender eine Bestätigung vom Empfänger erhält, dass die Nachricht angekommen ist.
- Unzuverlässige Datagramme
	- Unzuverlässige Datagramme werden einmal gesendet und es gibt keine Garantie, dass sie ankommen. Wenn sie verloren gehen oder beschädigt werden, gibt es keine automatische Wiederholung.

#### Virtual Circuits
- Virtuelle Verbindungen sind Kommunikationsmechanismen, bei denen eine logische Verbindung zwischen dem Sender und dem Empfänger hergestellt wird. Diese Verbindungen bieten eine zuverlässige und geordnete Nachrichtenübermittlung.
- Nachrichten, die über eine virtuelle Verbindung gesendet werden, sind garantiert in der Reihenfolge, in der sie gesendet wurden, anzukommen.
- Es gibt keine verlorenen oder duplizierten Nachrichten.
- Virtuelle Verbindungen erfordern die Einrichtung einer Verbindung vor der Datenübertragung. Obwohl sie kostspieliger als Datagramme sind, bieten sie Vorteile, insbesondere beim Senden großer Datenmengen, die aus mehreren Nachrichten bestehen.
- Beispiel
	- File Transfer Protocol (FTP)
	- Hypertext Transfer Protocol (HTTP)

#### Streams 
- Streams sind Kommunikationsmechanismen, die ähnlich wie virtuelle Verbindungen funktionieren, jedoch keine Nachrichten- oder Datensatzgrenzen beibehalten
- bei Streams alle gesendeten Daten als kontinuierlicher Strom von Bytes
- Bei der Übertragung von Daten über Streams zählen die Grenzen zwischen Nachrichten oder Datensätzen nicht. Es gibt keine Trennung oder Markierung, die anzeigt, wo eine Nachricht endet und die nächste beginnt.


### Remote Procedure Calls
- Remote Procedure Calls (RPC) sind eine Methode, mit der ein Programm eine Prozedur oder Funktion in einem anderen Adressraum (oft auf einem anderen Computer in einem gemeinsam genutzten Netzwerk) aufruft, als ob es sich um eine lokale Prozedur handelt.
- RPC ermöglicht es Entwicklern, Funktionen aufzurufen, die auf entfernten Systemen ausgeführt werden, als ob sie lokal wären.
- Client-Server-Architektur:
	- RPC basiert auf einer Client-Server-Architektur, bei der der Client eine Prozeduraufrufanforderung an den Server sendet, der die Prozedur ausführt und das Ergebnis zurückgibt.
	- RPC-Aufrufe können synchron oder asynchron sein.
- Pro:
	- Einfachheit und Abstraktion
	- Versteckt alle Details der Nachrichtenübermittlung
	- Fokus auf die Anwendungslogi
- Contra:
	- Obwohl RPC darauf abzielt, entfernte Funktionsaufrufe wie lokale Funktionsaufrufe erscheinen zu lassen, ist die Illusion nicht immer perfekt.
	- RPCs verhalten sich nicht immer genau wie reguläre Prozeduraufrufe.
		- Netzwerkprobleme, Latenzzeiten, und Fehler bei der Datenübertragung können das Verhalten von RPCs beeinflussen, was bei lokalen Funktionsaufrufen nicht der Fall ist.
	- Client und Server teilen nicht denselben Adressraum. Dies bedeutet, dass Daten zwischen Client und Server serialisiert und deserialisiert werden müssen. Zeiger und Referenzen können nicht direkt übergeben werden, was zusätzliche Programmierarbeit erfordert und zu Leistungseinbußen führen kann.
	- Netzwerkkommunikation ist langsamer als lokale Aufrufe.