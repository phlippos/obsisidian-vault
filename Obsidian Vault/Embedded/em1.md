Ein Embedded-System ist eine spezialisierte Computerplattform, die entwickelt wurde, um spezifische Aufgaben auszuführen
Komponenten :
1- Mikrocontroller (MCU) / Mikroprozessor (MPU)
	1- Speicher
	2- Timer
	3- ADC
	4- DAC
	5- serielle Kommunikationsschnittstellen
2- Stromversorgung
3- Eingabe-/Ausgabeschnittstellen
	1-Sensoren
	2- Aktoren
	3-Kommunikationsschnittstellen :Ermöglichen die Datenübertragung zwischen dem Embedded-System und anderen Systemen oder Geräten (z.B. USB, Ethernet, CAN-Bus, Bluetooth, Wi-Fi)
4-Speicher
	1-**Flüchtiger Speicher (RAM)**: Temporärer Speicher für die Laufzeitdaten und Zwischenergebnisse.
	2-**Nichtflüchtiger Speicher (ROM/Flash)**: Dauerhafter Speicher für das Betriebssystem, Firmware und Anwendungen.
5-Software
	1-Firmware
	2- **Betriebssystem (optional)** :Ein Echtzeitbetriebssystem (RTOS) oder Embedded Linux kann verwendet werden, um die Verwaltung von Hardware-Ressourcen und die Ausführung von Anwendungen zu ermöglichen.
	 3- **Anwendungssoftware**: Spezifische Programme, die die Aufgaben und Funktionen des Embedded-Systems implementieren.
6- Bus-System:
	1-**Datenbus**: Transportiert Daten zwischen den Komponenten des Systems.
	 2-**Adressbus**: Übermittelt die Adressen der Speicherorte, auf die zugegriffen wird.
	 3-**Steuerbus**: Übermittelt Steuerinformationen und Signale zwischen den Komponenten.
Merkmale eines Embedded-Systems :
1-Kompakte Größe und geringes Gewicht
2-**Niedriger Energieverbrauch**:
3-**Zuverlässigkeit und Robustheit**
4-Echtzeitfähigkeit

### Der Mikrocontroller:
- Ein Mikrocontroller ist das Herzstück eines Embedded-Systems und integriert die wesentlichen Funktionen eines Computers auf einem einzigen Chip.
- besteht aus drei Hauptkomponenten: dem Kern, dem Speicher und den Peripheriegeräten.
- Kern :
	- CPU
	- ALU
	- Steuereinheit : Verarbeitet Befehle und steuert den Ablauf von Programmen.
- **Speicher**:
	- **ROM (Read-Only Memory)**: Nichtflüchtiger Speicher, der das Programm (Firmware) enthält, das beim Start des Mikrocontrollers ausgeführt wird.
	- **Flash-Speicher**: Eine Art von ROM, der wiederbeschreibbar ist und zur Speicherung der Firmware verwendet wird.
	- **RAM (Random-Access Memory)**: Flüchtiger Speicher, der zur Speicherung von temporären Daten und Variablen während der Programmausführung verwendet wird.
	- **EEPROM (Electrically Erasable Programmable Read-Only Memory)**: Ein nichtflüchtiger Speicher, der für das Speichern von Daten genutzt wird, die zwischen den Neustarts erhalten bleiben müssen.
- Peripheriegeräte:
	- - **E/A-Ports (Input/Output Ports)**: Schnittstellen für die Verbindung des Mikrocontrollers mit externen Geräten wie Sensoren, Aktoren und anderen digitalen oder analogen Komponenten.
	- **Timer/Counter**: Module zur genauen Zeitmessung und Ereigniszählung.
	- **ADC (Analog-Digital-Wandler)**: Wandelt analoge Signale in digitale Signale um, die vom Mikrocontroller verarbeitet werden können.
	- **DAC (Digital-Analog-Wandler)**: Wandelt digitale Signale in analoge Signale um.
	- **Serielle Kommunikationsschnittstellen**: UART, SPI, I2C und andere Schnittstellen zur seriellen Kommunikation mit anderen Geräten.
### Echtzeitbetrieb
 - Echtzeitbetrieb bedeutet, dass das System nicht nur korrekt, sondern auch innerhalb einer bestimmten Zeitvorgabe reagieren muss.
 - **Timing-Korrektheit** ist ein wesentlicher Bestandteil der Systemkorrektheit.
 - Harte Echtzeitsysteme:
	 - Verpassen einer Deadline führt zu einem vollständigen Systemversagen.
	 - Beispiele: Flugsteuerungssysteme, Anti-Blockier-Systeme (ABS) in Autos, medizinische Überwachungsgeräte.
- Weiche Echtzeitsysteme:
	- Verpassen einer Deadline führt zu einer verschlechterten Systemleistung, aber nicht zu einem vollständigen Versagen.
	- Beispiele: Videostreaming, Online-Gaming.
- Merkmale :
	- Determinismus
	- **Jitter**: Schwankungen in der Ausführungszeit sollten minimal sein
	- **Prioritäten**: Aufgaben werden nach ihrer Wichtigkeit priorisiert, wobei höhere Prioritäten zeitkritische Aufgaben erhalten.

#### Top-Down
Beim Top-Down-Design-Ansatz beginnt der Entwicklungsprozess mit einer abstrakten, hochrangigen Beschreibung des gesamten Systems. Anschließend wird das System schrittweise in immer detailliertere Komponenten und Module unterteilt.
#### Bottom-up
Beim Bottom-Up-Design-Ansatz wird der Entwicklungsprozess von den kleinsten, grundlegendsten Komponenten und Modulen aus begonnen.Diese Basiskomponenten werden schrittweise zu größeren und komplexeren Systemen zusammengesetzt.

### BARE-METAL VS OPERATING SYSTEM
- Bare-Metal-Programmierung bezieht sich auf das direkte Schreiben von Software, die direkt auf der Hardware ohne Unterstützung eines Betriebssystems ausgeführt wird.
- Dies ist oft in eingebetteten Systemen der Fall, bei denen eine minimale Laufzeitumgebung erforderlich ist.
- Vorteile:
	- Direkter Zugriff auf Hardware-Ressourcen ermöglicht maximale Leistung und minimale Latenzzeiten.
	- Geringe Komplexität für kleine Anwendungen
	- Zuverlässigkeit
- Nachteile
	- Komplexität bei großen Systemen
	- Mangel an Standardfunktionen : Funktionen wie Multithreading und Speicherverwaltung müssen vom Entwickler selbst implementiert werden.Funktionen wie Multithreading und Speicherverwaltung müssen vom Entwickler selbst implementiert werden.
	- Wartbarkeit: Änderungen und Wartungen können schwierig und zeitaufwändig sein
	- No multi-threading

### Verwendung eines Betriebssystems
- Die Verwendung eines Betriebssystems in eingebetteten Systemen bietet eine Abstraktionsschicht, die den Zugriff auf Hardware-Ressourcen verwaltet und viele Standarddienste bereitstellt.
- Vorteile:
	- **Skalierbarkeit**
	- **Multithreading und Prioritäten**
	- Treiberunterstützung
	- Community-Unterstützung
- Nachteile:
	- Leistungsaufwand : zu höheren Latenzzeiten und geringerem Wirkungsgrad führen
	- Komplexität
	- Hardwareanforderungen : Betriebssysteme benötigen oft leistungsfähigere Hardware mit mehr Speicher und Rechenleistung

### Embedded Systems vs. General-Purpose Systems
- Ein Embedded System ist ein spezialisiertes Computersystem, das als Teil eines größeren Systems entwickelt wurde.
- Merkmale von Embedded Systems:
	- Spezifische Aufgaben
	- Integration
	- Echtzeitfähigkeit
	- Ressourcenbeschränkungen
	- Zuverlässigkeit
	- Kostenoptimiert
- Ein General-Purpose System ist ein Computersystem, das für eine Vielzahl von Anwendungen und Aufgaben entwickelt wurde.
- flexibel
- Merkmale von General-Purpose Systems:
	- **Vielfältige Anwendungen**
	- Programmierung durch Endbenutzer
	- Hohe Leistung
	- Erweiterbarkeit
	- Betriebssystem

### COMPILER und CROSS-COMPILER
- Ein Compiler ist ein Werkzeug, das Quellcode in Maschinencode übersetzt, der von einem Computer ausgeführt werden kann.
- Ein Cross-Compiler ist eine spezielle Art von Compiler, der Code auf einem Entwicklungssystem (Host) erzeugt, der auf einem anderen Zielsystem (Target) ausgeführt werden soll.
- #### Compiler
- **Definition:**
	- Ein Compiler ist ein Programm, das Quellcode, der in einer höheren Programmiersprache geschrieben ist, in Maschinencode (auch als Objektcode bezeichnet) umwandelt, der direkt von der CPU eines Computers ausgeführt werden kann.
- #### Cross-Compiler
- **Definition:**
	- Ein Cross-Compiler ist ein Compiler, der Quellcode auf einem Host-System (z.B. einem Desktop-Computer) kompiliert, um den generierten Maschinencode auf einem anderen Zielsystem (z.B. einem Embedded-System) auszuführen.

### Linker
- Ein Linker ist ein Werkzeug , das verschiedene Objektdateien zusammenführt und ein ausführbares Programm erzeugt.
	- Verknüpfung von Objektdateien
	- Auflösung von Symbolreferenzen
	- Erstellung der Executable and Linkable Format (ELF)
- **Statischer Linker**:
	- Ein statischer Linker verknüpft alle benötigten Bibliotheken zur Compile-Zeit direkt in die ausführbare Datei.
- **Dynamischer Linker (Lader)**:
	- Ein dynamischer Linker verknüpft Bibliotheken zur Laufzeit.
### Build Automation
- Build Automation bezieht sich auf den Prozess der Automatisierung der Erstellung von Software-Builds und der damit verbundenen Prozesse wie Kompilierung, Verknüpfung und Testen.
- Zeit zu sparen
- Konsistenz zu gewährleisten
- Fehler zu reduzieren
- Kontinuierliche Integration
- **Make**: Ein Standard-Tool in UNIX und POSIX-Umgebungen, das mit Makefiles arbeitet, um Abhängigkeiten und Build-Regeln zu definieren.
- Phasen des Build-Prozesses
	- Quellcode-Verwaltung
	- Kompilierung
	- Assemblierung
	- Verknüpfung (Linking)
	- Build-Automatisierung
	- Tests
	- Paketierung
	- Bereitstellung (Deployment)


### debugger
- das verwendet wird, um Fehler im Code zu identifizieren und zu beheben. 
- Ein Debugger ermöglicht es Entwicklern, Programme zu starten, zu stoppen und ihren Ablauf zu kontrollieren, um den Zustand des Programms zu untersuchen und Fehler zu diagnostizieren.