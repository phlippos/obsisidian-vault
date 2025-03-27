#### **Was ist ein Prozess?**
>Ein Prozess ist ein Programm in Ausführung.
>![[Pasted image 20240416144035.png]]
>![[Pasted image 20240416144056.png]]
>Während das Programm läuft, werden Ressourcen wie Stack-Speicher, Heap-Speicher, Verweise auf Dateien usw. zugewiesen.
>
>Wenn der Prozess beendet wird, werden diese Ressourcen vom System zurückverlangt
>
>Unterstützung der Inter-Prozess-Kommunikation



#### **Thread**
>Anwendungen müssen mehrere Tasks gleichzeitig ausführen
>–Anwendung besteht aus mehreren »leichtgewichtigen Prozessen« (Threads)
>
>-Ein Prozess kann aus mehreren Threads bestehen
>
>- Threads besitzen einen gemeinsamen Adressraum.
>- Alle Threads eines Prozess teilen sich Zustand und Ressourcen des Prozesses
>
>- Kommunikation zwischen Threads ist einfacher als zwischen Prozessen
>Vorteile von Threads :
>- Ein Thread kann innerhalb eines Prozess schneller erzeugt werden, als ein neuer Prozess.
>- Thread kann schneller terminiert werden, als ein Prozess.
>- Schneller Wechsel zwischen Threads eines Prozesses, als der Wechsel zwischen Prozessen.
>- Threads erhöhen die Effizienz der Kommunikation.
>	- Da Threads Speicher und Dateien gemeinsam nutzen, können sie ohne Kernelfunktionen kommunizieren.

##### **Two Extreme Designs**
>40 RTOS tasks
>**First Design: 40 Individual Processes**
>	Vorteile : 
>		1. **Isolation** : Jede Aufgabe läuft in ihrem eigenen Prozess .Wenn eine Aufgabe abstürzt, ist es weniger wahrscheinlich, dass dies andere betrifft.
>		2. **Einfachheit** : Jedes Programm kann unabhängig voneinander entwickelt und debuggt werden.
>	Nachteile : 
>		1. **Komplexität der IPC** : Die Implementierung und Verwaltung von IPC erhöht die Komplexität des Systems
>		2. **Ressourcenoverhead** : Jeder Prozess benötigt seinen eigenen Speicherplatz
>		3. **Kommunikations-Overhead** : Die Kommunikation zwischen Prozessen ist langsamer als die Kommunikation zwischen Threads innerhalb eines einzigen Prozesses.
>
>**Zweites Design: 40 Threads innerhalb eines einzigen Prozesses**
>	Vorteile : 
>		1. **Effizienz** : Threads innerhalb eines einzigen Prozessen teilen sich einen gemeinsamen Specheirbereich und deshalb ist die Kommunikation zwischen Threads schneller. Das reduziert auch die Speciher-Overhead.
>		2. **Geringer Overhead** : Der Kontextwechsel zwischen Threads innerhalb desselben Prozesses ist in der Regel schneller. 
>	Nachteile : 
>		1. **Mangelnde Isolation** : Wenn ein Fehler oder eine Absturz in einem Thread auftritt, kann dieses Problem das gesamte System beeinträchtigen, weil sich Threads innerhalb desselben Prozesses ressourcen teilen.
>		2. Komplexität des Multithreading : Multithreading bringt die Komplexitäten wie Deadlock, Wettlaufsituation oder Verhungern mit sich, die shcwer zu verwalten.
>		3. **Schwierigkeiten beim Debuggen**

###### **Erzeugung eines Prozesses**
>fork() wird verwendet, um ein Prozess zu erstellen.
>- für jeden erfolgreichen Aufruf gibt es zwei Rückgaben :
>	- eine für Parent(id > 0) und eine für Child (id == 0),die neu erzeugt wird
>- Der Childprozess ist eine Kopie des Elternteils.
>- Er hat die gleiche Stack,Heap und file descriptors
>- Er führt die gleiche code nach fork().


###### **Terminierung eines Prozesses**
>Ein Prozess kann freiwillig durch den Aufruf der exit() Funktion beendet werden.
>
>Ein Prozess kann auch unfreiwillig mit einem Signal beendet werden, das nicht behandelt wird.Z.B.
>SIGKILL wird nicht behandelt und beendet immer den Prozess.
>
>Wird ein Prozess irgendeineweise terminiert, dann wird File descriptor geschlossen, Speicherbereich freigegeben und alle Threads gestoppt.
>
>Das System sendet ein Signal SIGCHLD an den Elternprozess, damit dieser darüber informiert ist.
>Prozesse haben einen Rückgabewert:
>	- Entweder das Argument für `exit`, wenn der Prozess normal beendet wurde, oder
>	- Die Signalnummer, wenn er durch ein Signal beendet wurde.
>Der Elternprozess kann den Rückgabewert mit `wait()` oder `waitpid()` abrufen.
>![[Pasted image 20240416153336.png]]
>![[Pasted image 20240416154452.png]]
>![[Pasted image 20240416155328.png]]

###### **Running a different Program**
>Die `fork`-Funktion erstellt eine Kopie eines laufenden Programms, aber sie führt kein anderes Programm aus. Um ein anderes Programm auszuführen, benötigen Sie eine der `exec`-Funktionen
>
>Die `exec`-Familie von Funktionen wird verwendet, um ein neues Programm in einem bestehenden Prozess zu laden und auszuführen. Es gibt mehrere Varianten von `exec`, darunter `execl`, `execv`, `execle`, `execve`, usw., die verschiedene Möglichkeiten bieten, Argumente zu übergeben und die Umgebung zu konfigurieren.
>![[Pasted image 20240416163210.png]]

##### **IPC**
>Übertragen von Informationen zwischen Prozessen in einem Computersystem.
>	1. Datenkopie:
>		1. Daten werden aus dem Speicher eines Prozesses in einen anderen kopiert.
>		2. Normalerweise wird die Nachricht zunächst in einen Zwischenspeicher (wie einen Puffer oder eine Warteschlange) kopiert und dann erneut an den Zielprozess übertragen
>		3. Beispiele : Sockets, Pipes und Nachrichtenwarteschlangen
>	2. Geteilter Speciher :
>		1. Bei dieser Methode wird ein Bereich des Speichers erstellt, der von mehreren Prozessen gleichzeitig zugegriffen und gemeinsam genutzt werden kann.
>		2. Geteilter Speicher wird auch als Mittel zur Synchronisierung des Zugriffs auf diesen Speicher zwischen Prozessen verwendet, oft mit Hilfe von Synchronisierungsprimitiven wie Semaphoren oder Mutexen.
>	3. Message-Based IPC :
>		1. Prozesse Nachrichten austauschen, um Daten zu übertragen und zu kommunizieren.
>		2. Der Nachrichtenfluss ist ein- oder zweidirektional
>		3. die maximale Größe einer Nachricht ist wichtig.
>		4. Nachrichten werden mit einer Priorität versehen
>	4. ![[Pasted image 20240416164027.png]]
>1. UNIX SOCKETS
>	1. Unix-Sockets sind eine Form der Interprozesskommunikation (IPC) in Unix-ähnlichen Betriebssystemen, die es Prozessen ermöglicht, miteinander zu kommunizieren, indem sie Datagramme oder Datenströme über das Dateisystem austauschen.
>	2. Unix-Sockets verwenden das Dateisystem als Kommunikationskanal.
>	3. Andere Prozesse können auf den Socket zugreifen, indem sie den Dateipfad verwenden.
>	4. **Datagramm-Sockets vs. Stream-Sockets**:
>		1. Datagramm-Sockets: Diese bieten eine verbindungslose Kommunikation und übertragen Daten als einzelne Pakete (Datagramme).Jedes Paket enthält sowohl die Daten als auch die Zieladresse.
>		2. Stream-Sockets: Diese bieten eine verbindungsorientierte Kommunikation und übertragen Daten als kontinuierlichen Datenstrom.Sie stellen eine bidirektionale Kommunikationsverbindung zwischen den Prozessen her
>		3. Lokale Kommunikation : Unix-Sockets sind auf die Kommunikation innerhalb des gleichen Systems beschränkt
>2. FIFO AND NAMED PIPES
>	1. FIFO ist eine spezielle Datei im Dateisystem, die von mehreren Prozessen zum Kommunizieren verwendet werden kann.
>	2. Pipe, die verwendet wird, um zwischen Eltern- und Kindprozessen zu kommunizieren
>3. POSIX MESSAGE QUEUES
>	1. Die Interaktion mit Nachrichtenwarteschlangen erfolgt typischerweise über die Funktion `mq_open()`
>	2. Diese Funktion wird verwendet, um eine Nachrichtenwarteschlange zu erstellen oder eine Referenz zu einer vorhandenen Nachrichtenwarteschlange zu erhalten.
>	3. `mq_open()` gibt einen Dateideskriptor zurück, der verwendet werden kann, um auf die Warteschlange zuzugreifen.,
>	4. Jede Nachricht in der Warteschlange hat eine Priorität
>	5. Nachrichten werden basierend auf ihrer Priorität und dann auf ihrem Alter aus der Warteschlange gelesen.
>	6. Die maximale Größe einer Nachricht ist durch `/proc/sys/kernel/msgmax` begrenzt
>		1. Standardmäßig beträgt die maximale <mark style="background: #BBFABBA6;">Nachrichtengröße</mark> 8 KiB
>4. POSIX Shared Memory
>	1. es ermöglicht Prozessen , gemeinsam genutzte Speicherbereiche zu erstellen und darauf zuzugreifen
>	2. Die Funktion `shm_open()` wird verwendet, um ein Shared Memory Segment zu erstellen oder auf ein vorhandenes Shared Memory Segment zuzugreifen. Sie nimmt den Namen des Shared Memory Segments als Parameter und gibt einen Dateideskriptor zurück,der verwendet werden kann, um auf das Shared Memory Segment zuzugreifen.
>	3. ![[Pasted image 20240416201418.png]]


**Threads**
>Der große Vorteil von Threads besteht darin, dass sie den Adressraum und Speicher variablen teilen können, was es ihnen ermöglicht, auf gemeinsame Daten direkt zuzugreifen und diese zu manipulieren.
>
>Allerdings geht dieser Vorteil auch mit einem erheblichen Nachteil einher: der Notwendigkeit von Synchronisierungsmechanismen zur Gewährleistung der Datenkonsistenz.
>
>Da mehrere Threads gleichzeitig auf gemeinsame Daten zugreifen und diese ändern können, besteht das Risiko von Datenbeschädigungen oder -inkonsistenzen
>
>**Mutex (Mutexe)**: Mutexe dienen dazu, den exklusiven Zugriff auf gemeinsame Ressourcen zu steuern. Threads verwenden Mutexe, um kritische Abschnitte des Codes zu schützen und sicherzustellen, dass nur ein Thread gleichzeitig auf diese Abschnitte zugreift.
>Problems : 
>- **Deadlocks** : weil Threads gegenseitig auf mehrere Mutexe warten.
>- Lösung : **Gleiche Reihenfolge der Sperrung**, Timeout,
>- **Prioritätsinversion**: Dies tritt auf, wenn ein Thread mit hoher Priorität blockiert wird, während er auf einen Mutex wartet, der von einem Thread mit niedrigerer Priorität gesperrt ist.
>- Lösung: **Prioritätsererbung**:Ein Mechanismus, bei dem die Priorität eines blockierten Threads temporär auf die Priorität des Threads erhöht wird, der den Mutex besitzt.
>- **Schlechte Leistung**: Wenn Threads die meiste Zeit auf Mutexe blockieren, kann dies die Gesamtleistung beeinträchtigen
>- Lösung : Überprüfung des Designs
>**Condition Variables (Bedingungsvariablen)**: Bedingungsvariablen ermöglichen es Threads, auf bestimmte Bedingungen zu warten, bevor sie fortgesetzt werden.
>-Das einzige Problem besteht darin, dass die Bedingungsvariable, per Definition, eine gemeinsam genutzte Ressource ist und daher durch einen Mutex geschützt werden muss.



**Scheduling**
>Scheduling ist der Prozess, durch den ein Betriebssystem die Reihenfolge bestimmt, in der Prozesse oder Threads auf der CPU ausgeführt werden.
Jeder Thread hat eine Scheduling-Politik, die entweder zeitgesteuert oder echtzeitbasiert sein kann:

1. **Zeitgesteuerte Threads**: Zeitgesteuerte Threads folgen einer Scheduling-Politik, die auf Zeitanteilen basiert. Diese Threads haben in der Regel einen Wert für die "Netteigkeit" (Niceness), der ihre Priorität im Zeitplan beeinflusst. Ein höherer Wert für die Netteigkeit bedeutet eine niedrigere Priorität und umgekehrt.
2. **Echtzeit-Threads**: Echtzeit-Threads haben eine Priorität, die es ihnen ermöglicht, unterbrechend auf andere Threads zu wirken. Diese Threads haben eine feste oder dynamische Priorität, die bestimmt, wie sie im Vergleich zu anderen Threads ausgeführt werden. Ein Thread mit höherer Priorität wird bevorzugt ausgeführt und kann die Ausführung eines Threads mit niedrigerer Priorität unterbrechen, um seine Aufgabe auszuführen.
>Zeitgesteuerte Threads eignen sich gut für allgemeine Anwendungen, bei denen eine **faire** Verteilung der CPU-Zeit zwischen Threads wichtig ist.
>
>Echtzeit-Threads werden in Anwendungen eingesetzt, die **deterministisches** Verhalten und schnelle Reaktionen erfordern, wie z.B. Echtzeitbetriebssysteme, Signalverarbeitung oder industrielle Steuerungen.

**TIME-SHARED POLICIES**
>Zeitgesteuerte (time-shared) Scheduling-Policies basieren auf der Zuteilung von CPU-Zeitanteilen für jeden Thread.
>**SCHED_NORMAL(SCHED_OTHER)**:CFS basiert auf dem Konzept des "fairen Teilen" und versucht, die CPU-Zeit proportional zur Priorität der Threads zuzuweisen.
>**SCHED_BATCH**: Threads mit längeren Zeitquanten auf der CPU werden ausgeführt , was zu weniger Kontextwechseln führt. Die Absicht besteht darin, die Anzahl der Kontextwechsel für Hintergrundverarbeitungsaufgaben zu reduzieren,
>**SCHED_IDLE**: Threads werden nur dann ausgeführt, wenn keine Threads anderer Policies bereit sind, ausgeführt zu werden.

**Niceness**
>je höher die Niceness, desto niedriger ist die Priorität des Prozesses oder Threads und umgekehrt.
>
>Der Niceness-Wert liegt im Bereich von -20 bis 19, wobei -20 die höchste Priorität und 19 die niedrigste Priorität darstellt.(def 0)
>
>Dies bedeutet, dass Prozesse oder Threads mit einer negativen Niceness schneller ausgeführt werden und priorisiert werden.
>
>"Netteigkeit" (Niceness) kann für Threads mit den Scheduling-Policies SCHED_NORMAL und SCHED_BATCH im Linux-Kernel geändert werden.
>
>(nice -n niceness befehl)


**Real-Time Policies**
>Echtzeit-Scheduling-Policies werden verwendet, um die Ausführung von Prozessen oder Threads in Echtzeit-Systemen zu steuern, wo deterministisches Verhalten und schnelle Reaktionen erforderlich sind.
>
>**SCHED_FIFO (First-In, First-Out)**:
>feste Priorität
>
>Ein Thread mit SCHED_FIFO bleibt auf der CPU, bis er entweder freiwillig die CPU freigibt oder von einem höher priorisierten Thread unterbrochen wird.
>
>Threads mit SCHED_FIFO werden in der Reihenfolge ihrer Ankunft in die Warteschlange eingereiht.
>
>**SCHED_RR (Round-Robin)**:Threads mit SCHED_RR haben ebenfalls feste Prioritäten, aber sie erhalten eine bestimmte Zeitquantum auf der CPU. Wenn das Zeitquantum abläuft, wird der Thread in die Warteschlange zurückgesetzt, und ein anderer Thread derselben Priorität wird ausgeführt.
>
>**SCHED_DEADLINE**: Das Betriebssystem verwendet einen Algorithmus zur Garantie von Deadlines, um sicherzustellen, dass Threads ihre CPU-Zeit innerhalb der vorgegebenen Fristen erhalten.
>
>In Echtzeitsystemen hat jeder Echtzeit-Thread eine Priorität im Bereich von 1 bis 99, wobei 99 die höchste Priorität ist.
>
>Die **CAP_SYS_NICE** ist eine Linux-Fähigkeit (capability), die einem Prozess erlaubt, seine Priorität (Netteigkeit) zu ändern, unabhängig von seiner aktuellen Niceness.(root benötigt)
>
>Problem :
>Ein Problem mit dem Echtzeit-Scheduling tritt auf, wenn ein Thread, der normalerweise auf eine Ereignisbearbeitung oder eine externe Eingabe wartet, plötzlich rechenintensiv wird, was dazu führt, dass andere Threads möglicherweise nicht rechtzeitig ausgeführt werden können."compute-bound"
>
>-**Blockieren anderer Threads** Wenn ein Thread rechenintensiv wird und die CPU für längere Zeit beansprucht, können andere Threads mit höherer Priorität möglicherweise nicht rechtzeitig ausgeführt werden, was zu Verzögerungen bei der Ausführung kritischer Aufgaben führt.
>-**Verschwendung von CPU-Ressourcen
>**
>Lösungen:
>-**Reservierung von CPU-Zeit für nicht-echtzeitfähige Threads**:Seit Linux 2.6.25 reserviert der Scheduler standardmäßig einen bestimmten Prozentsatz der CPU-Zeit für nicht-echtzeitfähige Threads.
>
>-**Verwendung eines Watchdogs**:Ein Watchdog kann verwendet werden, um zu erkennen, wenn ein Thread nicht rechtzeitig ausgeführt wird, und entsprechend zu reagieren, z. B. indem er den Thread neu startet oder eine Warnung ausgibt.
