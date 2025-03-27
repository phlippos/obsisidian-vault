#### **Virtual Memory**
><mark style="background: #D2B3FFA6;">Virtual Memory bezieht sich auf die Technik, mit der ein Computersystem den physikalischen Arbeitsspeicher (RAM) erweitert, indem es einen Teil der Daten auf die Festplatte auslagert.</mark> Das ermöglicht es, mehr Programme gleichzeitig auszuführen, als der physische Arbeitsspeicher allein unterstützen könnte. In virtuellen Speichern wird der RAM als Hauptspeicher bezeichnet, während die Festplatte als virtueller Speicher dient.
>
><mark style="background: #ADCCFFA6;">Linux konfiguriert die Memory Management Unit (MMU) der CPU so, dass sie einem laufenden Programm einen virtuellen Adressraum präsentiert</mark>:
> - Der virtuelle Adressraum beginnt bei Null und endet bei der höchsten Adresse, 0xffffffff, auf einem 32-Bit-Prozessor.
> - Er ist in Seiten von 4 KiB unterteilt
> 
>Dieser virtuellen Adressraum wird in Benutzerraum und Kernelraum unterteilt.
>
>Der Benutzeradressraum wird pro Prozess zugewiesen, sodass <mark style="background: #D2B3FFA6;">jeder Prozess in einer Sandbox getrennt von den anderen läuft.</mark>
>
>Seiten in diesem virtuellen Adressraum werden von der MMU auf physische Adressen abgebildet
>
>  
Jede Seite des virtuellen Speichers kann wie folgt sein:

- Nicht zugeordnet (unmapped): Versuche, auf diese Adressen zuzugreifen, führen zu einem SIGSEGV-Fehler <mark style="background: #D2B3FFA6;">(Segmentation Fault)</mark>.
- Zu einer Seite des physischen Speichers zugeordnet, die nur für den Prozess privat ist.
- Zu einer Seite des physischen Speichers zugeordnet, die mit anderen Prozessen geteilt wird.
- Zugeordnet und gemeinsam genutzt, wobei die Kopier-Schreib-Sperre (Copy on Write, CoW) aktiviert ist: Ein Schreibzugriff wird vom Kernel abgefangen. Dieser erstellt eine Kopie der Seite und ordnet sie dem Prozess zu, anstatt die ursprüngliche Seite zu überschreiben.
- Zu einer Seite des physischen Speichers zugeordnet, die vom Kernel verwendet wird.
- Der Kernel kann außerdem Seiten zu reservierten Speicherbereichen zuordnen, beispielsweise um auf Register und Speicherpuffer in Gerätetreibern zuzugreifen.
>Diese Zuordnungen werden durch die MMU und die Seitenverzeichnisse verwaltet, um den virtuellen Adressraum auf den physischen Speicher abzubilden.
> **Warum virtueller Speicher?**
> Vorteile : 
> 	1. <mark style="background: #FFB86CA6;">Ungültige Speicherzugriffe werden erkannt (segmentation fault)</mark>.
> 	2. <mark style="background: #FFB86CA6;">Prozesse isoliert voneinander</mark>
> 	3.<mark style="background: #FFB86CA6;"> die Erhöhung der Effizienz von RAM.</mark>
> Nachteile : 
> 	1. <mark style="background: #FFB86CA6;">Out-of-Memory</mark>
> 	2. <mark style="background: #FFB86CA6;">Verzögerungen bei der Behandlung von Ausnahmen Seitenfehler verursacht werden
</mark>

**Kernel space Memory Layout**
>   1. **Kernel Code und Daten**: Dieser Bereich enthält den eigentlichen Kernelcode sowie Datenstrukturen, die vom Kernel verwendet werden, wie zum Beispiel Tabellen für Prozesse, Dateisysteme und Gerätetreiber.
>   2. **Kernel Heap**: Ähnlich wie im Userspace gibt es im Kernelspace einen Heap, der für die dynamische Speicherallokierung verwendet wird. Hier werden zum Beispiel Kernelobjekte wie Prozesskontrollblöcke (PCBs) oder Puffer für E/A-Operationen allokiert.
>   3. **Kernel Stack**: Jeder Kernelthread hat seinen eigenen Stack, der für die Speicherung von lokalen Variablen und Funktionsaufrufparametern verwendet wird. Der Stack wächst normalerweise von oben nach unten.
>   4. **Kernel Module Bereich**: Dieser Bereich ist für geladene Kernelmodule reserviert. Wenn Module geladen werden, werden ihre Code- und Datensegmente in diesem Bereich platziert.
>   5. **Speicher für Kernel-Strukturen und -Tabellen**: Der Kernelspace enthält verschiedene Tabellen und Datenstrukturen, die für die Verwaltung des Systems erforderlich sind, wie zum Beispiel Tabellen für Prozesse, Dateisysteme, Netzwerkverbindungen und Hardwaregeräte.
>Code-Segment : enthält den ausführbaren Maschinencode des Programms
>Data : enthält initialisierte globale und statische Variablen.
>BSS : enthält uninitialisierte globale und statische Variablen.
>######################################################
>size command : Dieser Befehl gibt die Größe jedes Segments im Programmcode aus.


**User space Memory Layout**
>In Linux wird eine verzögerte Zuweisungsstrategie für den Benutzerraum angewendet. Das bedeutet, dass physische Speicherseiten nur dann zugeordnet werden, wenn das Programm darauf zugreift.
>
>Anstatt physischen Speicher für den gesamten virtuellen Adressraum eines Prozesses im Voraus zuzuweisen, ordnet Linux nur physischen Speicherseiten zu, wenn sie vom Programm verwendet werden.
>
>`malloc()` reserviert lediglich den benötigten Speicherplatz im virtuellen Adressraum des Prozesses und gibt einen Zeiger auf den Anfang dieses reservierten Speicherblocks zurück. Dieser Speicherblock wird zunächst als "virtueller Speicher" betrachtet, da er noch nicht tatsächlich auf physischen Speicher abgebildet ist. Erst wenn dein Programm auf diesen reservierten Speicherbereich zugreift, werden die entsprechenden Seiten des virtuellen Speichers in physische Speicherseiten (RAM) abgebildet.
>
>**page fault** : Ein Seitenfehler tritt auf, wenn ein Prozess versucht, auf eine Seite des virtuellen Speichers zuzugreifen, die noch nicht im physischen Speicher (RAM) vorhanden ist. Wenn ein solcher Zugriff erfolgt, löst der Prozessor eine Ausnahme aus, die vom Betriebssystem behandelt wird. Das Betriebssystem erkennt dann den Seitenfehler und versucht, die benötigte Seite vom Speichergerät in den RAM zu laden, bevor sie dem Prozess zur Verfügung gestellt wird.


#### **SWAPPING**
>Wenn der physische Speicher (RAM) eines Computers vollständig ausgelastet ist und zusätzlicher Speicher benötigt wird, können nicht benötigte Daten oder Prozesse auf die Festplatte ausgelagert werden, um Platz für aktive Prozesse im RAM freizugeben.
>
>**paging**
>Beim Swapping werden die inaktiven Teile des Arbeitsspeichers auf die Festplatte verschoben.
>
>Wenn ein Prozess oder eine Anwendung dann wieder auf die ausgelagerten Daten zugreifen muss, werden sie vom Betriebssystem zurück in den RAM geladen.
>
>Nachteile : 
>es kann auch ***die Leistung des Systems beeinträchtigen**, wenn **zu häufig** auf die Festplatte zugegriffen werden muss, da die Zugriffszeiten auf die Festplatte im Vergleich zum RAM deutlich langsamer sind.
>
>Auf eingebetteten Geräten wird der Swap-Speicher selten verwendet.
>	- <mark style="background: #D2B3FFA6;">Die kontinuierliche Schreibaktivität, die mit dem Swapping verbunden ist, kann dazu führen, dass der Flash-Speicher schnell abnutzt.</mark>


##### **COMPRESSED MEMORY (ZRAM)**
>ZRAM kann besonders nützlich sein, wenn der physische Speicher begrenzt ist, wie zum Beispiel bei eingebetteten Geräten oder Systemen mit geringer Speicherkonfiguration.
>
>Es ist jedoch zu beachten, dass ZRAM in bestimmten Szenarien zwar vorteilhaft sein kann, aber auch eine CPU-Belastung durch die Kompressions- und Dekompressionsoperationen mit sich bringt.
>
>ein komprimiertes Blockgerät im RAM , das als Swap-Gerät verwendet werden kann.
>
>ZRAM komprimiert Daten von Speicherseiten, die weniger genutzt werden, und speichert sie in ZRAM.
>
>Mit Kompressionsraten im Bereich von 30% bis 50%


**MAPPING MEMORY WITH MMAP**
>die wird verwendet, um einen Speicherbereich eines Prozesses auf eine Datei oder ein anderes Objekt im Dateisystem abzubilden.
>
>Der Speicher eines Prozesses direkt mit einem Dateisystemobjekt oder anderen Ressourcen verbunden wird.
>
>`mmap` in C steht für "Memory Map" und ist eine Systemfunktion in Unix-ähnlichen Betriebssystemen wie Linux. <mark style="background: #D2B3FFA6;">Sie ermöglicht es, Dateien oder Geräte direkt in den Speicher abzubilden. Dadurch können Sie auf den abgebildeten Speicherbereich über Zeiger zugreifen, als ob es sich um ein Array im Adressraum des Programms handelt.</mark>


**USING MMAP TO ACCESS DEVICE MEMORY**
>möglich, dass ein Treiber seinen Geräteknoten (`device node`) für das Mappen mittels `mmap` freigibt und einen Teil des Gerätespeichers mit einer Anwendung teilt. Diese Vorgehensweise wird häufig in der Entwicklung von Treibern verwendet, da sie eine effiziente und direkte Kommunikation zwischen Treiber und Anwendung ermöglicht.

**HOW MUCH MEMORY DOES MY APPLICATION USE?**
>**"Virtual Set Size"** (VSS) und "Resident Memory Size" (RSS) sind zwei Metriken, die verwendet werden, um den Speicherverbrauch eines Prozesses zu messen
>- <mark style="background: #D2B3FFA6;">Die VSS repräsentiert die gesamte virtuelle Speichermenge</mark>, die einem Prozess zugewiesen ist, unabhängig davon, ob der Speicher physisch vorhanden ist oder auf die Festplatte ausgelagert wurde.
>- <mark style="background: #D2B3FFA6;">Die RSS hingegen gibt nur den tatsächlich im Hauptspeicher belegten physischen Speicher an</mark>, der von einem Prozess verwendet wird.


**Memory leak**
>tritt auf, wenn im Verlauf der Programmausführung Speicher dynamisch allokiert wird, dieser jedoch nicht ordnungsgemäß freigegeben wird, wenn er nicht mehr benötigt wird.
>
>Dies führt zu einem allmählichen Anstieg des Speicherverbrauchs im Laufe der Zeit.
>Lösung : mtrace 
>
>**MTRACE**
>Es wird verwendet, um Speicherzugriffe und -lecks zu verfolgen, indem es die dynamische Speicherallokation und -freigabe innerhalb eines Programms überwacht.
>
**Kompilieren mit mtrace**: Um `mtrace` verwenden zu können, müssen Sie Ihre Anwendung mit der Option `-g -lmcheck` kompilieren. Dies aktiviert die Unterstützung für `mtrace` während der Programmausführung.
		gcc -g -lmcheck myprogram.c -o myprogram	
**Aktivieren von mtrace**: Am Anfang Ihres Programms können Sie `mtrace()` aufrufen, um die Verfolgung der Speicherallokationen zu starten.
 **Analysieren der mtrace-Ausgabe**: Nachdem Ihr Programm beendet wurde, wird eine Datei `mtrace.out` im aktuellen Verzeichnis erstellt. Diese Datei enthält Informationen über die Speicherallokationen und -freigaben während der Programmausführung. Sie können die `mtrace.out`-Datei mit einem Texteditor öffnen und analysieren, um potenzielle Speicherlecks oder andere Speicherprobleme zu identifizieren.
>**Over-commit**
>Wenn ein Prozess mehr Speicher anfordert, als physisch vorhanden ist, kann das Betriebssystem die Anforderung zunächst erfüllen, indem es virtuellen Speicher zuweist, ohne ihn sofort physisch zuzuweisen. Dies bedeutet, dass das Betriebssystem mehr Speicher verspricht, als tatsächlich vorhanden ist.
>(**out of memory**),dass ein System oder eine Anwendung nicht genügend verfügbaren Arbeitsspeicher (RAM) hat, um die laufenden Prozesse oder den aktuellen Arbeitsspeicherbedarf zu unterstützen.
>  
Wenn ein System keinen Speicher mehr hat und kein zusätzlicher Speicher allokiert werden kann, kommt der **"Out of Memory (OOM) Killer"** des Kernels zum Einsatz. **OOM Killer** ist verantwortlich , Prozesse auszuwählen und zu beenden, um Speicher freizugeben und dem System das Fortsetzen des Betriebs zu ermöglichen.


>**Memory-mapped I/O (Input/Output)**
>ist eine Technik, bei der Geräte (z. B. Hardware-Peripheriegeräte wie Festplatten, Netzwerkadapter oder GPIO-Pins) direkt in den Adressraum des Prozessors eines Computers gemappt werden, anstatt über spezielle Ein- und Ausgabebefehle wie IN und OUT (bei x86-Architekturen) angesprochen zu werden.
>Daten können direkt an und von den Geräten durch das Lesen und Schreiben von Speicheradressen übertragen werden.v
 
 