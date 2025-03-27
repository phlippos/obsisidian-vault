1. Mikroprozessor (μP, Microprocessor, MPU)
	1. Ein **Mikroprozessor** ist das Herzstück eines Rechensystems und wird oft als **<mark style="background: #FFF3A3A6;">CPU (Central Processing Unit)</mark>** bezeichnet. Er verarbeitet Daten und führt Befehle aus, besitzt jedoch keine eigenen Speicher- oder Peripheriekomponenten. Alle notwendigen Funktionen wie Speicher, Ein-/Ausgabeeinheiten (I/O) und Schnittstellen müssen extern über einen Systembus angebunden werden.
	2. Merkmale eines Mikroprozessors:
		1. Besteht aus einem ALU (Arithmetic Logic Unit), Registern und einer Steuerlogik.
		2. Erfordert externe RAM-, ROM-, I/O- und Peripheriegeräte.
		3. Hochgradig flexibel, da er in verschiedenen Anwendungen mit variabler Peripherie genutzt werden kann.
		4. Wird in Computern, Servern und Hochleistungsrechnern verwendet.
2. Mikrocontroller (μC, Microcontroller Unit)
	1. Ein **Mikrocontroller** ist eine Weiterentwicklung des Mikroprozessors und enthält neben der CPU auch integrierte Komponenten wie RAM, ROM (Flash-Speicher), I/O-Schnittstellen, Timer, ADC (Analog-Digital-Converter), DAC (Digital-Analog-Converter), Kommunikationsschnittstellen (UART, SPI, I2C, CAN) und oft eine Stromsparlogik.
	2. Merkmale eines Mikrocontrollers:
		1. Enthält CPU, Speicher und Peripherie in einem einzigen Chip.
		2. Entwickelt für eingebettete Systeme mit festgelegten Funktionen
		3. Kostengünstig und energieeffizient.
		4. Wird für Echtzeitanwendungen eingesetzt.
3. System-on-a-Chip (SoC)
	1. Ein **System-on-a-Chip** integriert neben der CPU auch Grafikprozessoren (GPU), DSPs (Digital Signal Processors), Speichercontroller, Kommunikationsschnittstellen und andere Peripherie auf einem einzigen Chip. SoCs werden vor allem in **Smartphones, Tablets, eingebetteten Systemen, IoT-Geräten und modernen Computern** verwendet.
	2. Merkmale eines SoCs:
		1. Hochintegrierte Architektur mit verschiedenen Hardwarekomponenten auf einem einzigen Chip.
		2. Oft optimiert für spezifische Anwendungen (Mobile Computing, KI, Embedded Systems).
		3. Enthält oft Hardware-Beschleuniger für maschinelles Lernen (z. B. NPU – Neural Processing Unit).
4. System-on-a-Programmable-Chip (SoPC)
	1. Ein **System-on-a-Programmable-Chip (SoPC)** kombiniert die Eigenschaften eines Mikrocontrollers mit einem **FPGA (Field Programmable Gate Array)**. Dies ermöglicht eine hochflexible Architektur, da die Hardware über Software nachträglich anpassbar ist.
	2. Merkmale eines SoPC:
		1. Enthält eine CPU (oft ARM), FPGA-Bausteine und Peripherie.
		2. Ideal für anpassbare und spezialisierte Anwendungen.
		3. Wird für **Signalverarbeitung, industrielle Automatisierung, KI-Beschleunigung und Hochgeschwindigkeitskommunikation** genutzt.
![[Pasted image 20250221145846.png]]
# Mikrocontroller
- ![[Pasted image 20250221150023.png]]
- MSP430F5529
- ![[Pasted image 20250221150043.png]]


# Mikroprozessorarchitekturen
- **Complex Instruction Set Computer**
	- Der Begriff **Complex Instruction Set Computer (CISC)** bezeichnet eine Prozessorarchitektur, die eine Vielzahl komplexer Maschinenbefehle unterstützt. CISC-Prozessoren sind so konzipiert, dass sie mit **weniger Maschinenbefehlen** auskommen, indem sie leistungsstarke und spezialisierte Befehle anbieten, die in einem einzigen Taktzyklus mehrere Operationen ausführen können.
	- CISC wurde ursprünglich entwickelt, um die **Effizienz des Speicherverbrauchs** zu maximieren, da Speicher früher teuer war und Programme mit kompakteren Maschinenbefehlen effizienter waren.
	- Merkmale der CISC-Architektur
		- Großer Befehlssatz:
			- Enthält komplexe Befehle, die direkt auf Speicher oder Register zugreifen können.
			- Beispiel: Ein einziger Maschinenbefehl kann eine Multiplikation und Speicherung in einem Schritt durchführen.
		- Mikrocode-Steuerung:
			- Viele Befehle werden intern in kleinere Mikrooperationen zerlegt.
			- Führt zu komplexerer Hardware, aber einfacherer Software.
		- **Variable Befehlslängen:**
			- Befehle haben unterschiedliche Längen, wodurch die Dekodierung aufwändiger wird.
		- Direkter Speicherzugriff:
			- Viele Befehle ermöglichen direkten Speicherzugriff (z. B. `MOV A, [B]` anstelle von `LOAD` und `STORE` in RISC).
		- Effizienz für kompilierte Hochsprachen:
			- CISC-Prozessoren erleichtern die direkte Übersetzung von Hochsprachen wie C oder Pascal in Maschinenbefehle, da weniger Befehle für komplexe Operationen benötigt werden.
		- Eine Instruktion kann mehr als einen einzelnen Taktzyklus zur Ausführung benötigen.
		- Weniger allgemeine Register, da Operationen direkt im Speicher ausgeführt werden.
		- Komplexe Adressierungsmodi.
	- ![[Pasted image 20250221151215.png]]
	- **Beispiele für CISC-Prozessoren**
	- **Intel x86 (8086, Pentium, Core i7, Core i9)**
	- **AMD Ryzen (x86-64 Architektur)**
	- **IBM System/360, System z (Mainframe)**
	- **Motorola 68000 (Amiga, Atari ST, Macintosh 68k-Serie)**
- **Reduced Instruction Set Computer (RISC)**
	- Der Begriff **Reduced Instruction Set Computer (RISC)** bezeichnet eine Prozessorarchitektur, die im Gegensatz zur **Complex Instruction Set Computer (CISC)**-Architektur auf eine reduzierte Anzahl <mark style="background: #FFB86CA6;">einfacher und effizienter Maschinenbefehle</mark> setzt. Das Ziel von RISC ist eine **<mark style="background: #FFB86CA6;">höhere Geschwindigkeit und Effizienz</mark>**, indem jeder Befehl in einem einzigen oder <mark style="background: #FFB86CA6;">wenigen Taktzyklen</mark> ausgeführt wird.
	- RISC wurde in den 1980er Jahren als Alternative zu CISC entwickelt, um die **Prozessorleistung zu optimieren, den Energieverbrauch zu senken und die Parallelverarbeitung durch Pipelining zu verbessern**.
	- Merkmale der RISC-Architektur
		- Kleiner und einfacher Befehlssatz:
			- Enthält nur grundlegende Befehle (Load, Store, Add, Sub, Branch usw.).
			- Jeder Befehl führt nur eine Operation aus.
		- Einheitliche Befehlslänge:
			- Alle Befehle haben die gleiche Länge, was eine **schnelle Dekodierung** ermöglicht.
		- Registerbasierte Architektur:
			- Viele **Allzweckregister (General Purpose Registers, GPRs)** minimieren Speicherzugriffe.
			- Speicherzugriffe erfolgen nur über **Load/Store-Befehle**.
		- Ein-Befehl-pro-Takt-Prinzip:
			- Befehle werden so optimiert, dass sie in einem einzigen Taktzyklus verarbeitet werden können.
		- Effizientes Pipelining:
			- Durch die einheitliche Befehlslänge und einfache Dekodierung können mehrere Befehle gleichzeitig verarbeitet werden.
		- Wenige und einfache Adressierungsmodi:
			- Im Gegensatz zu CISC gibt es nur eine begrenzte Anzahl von Speicheradressierungsarten, was die Hardware vereinfacht.
	- ![[Pasted image 20250221152235.png]]
	- Beispiele für RISC-Prozessoren
		-  **ARM (Cortex-A, Cortex-M, Cortex-R)** – Smartphones, Tablets, Embedded Systeme
		- **RISC-V** – Open-Source-Architektur, eingebettete Systeme, Forschung
		- **PowerPC (IBM Power, Freescale PowerPC)** – Server, Spielekonsolen (z. B. PlayStation 3)
		- **MIPS** – Netzwerkgeräte, Router, eingebettete Systeme
		- **SPARC (Sun/Oracle SPARC)** – High-End-Server
- ![[Pasted image 20250221152354.png]]


### ## **Festkommazahlen (Fixed Point Numbers)**
- Eine **Festkommazahl** ist eine binäre Darstellung einer Zahl, bei der die Dezimalstelle (das Komma) an einer festen Position bleibt. Dies ermöglicht eine **schnelle Berechnung**, da keine exponentielle Skalierung erforderlich ist.
- ### **Merkmale:**
	- Eine Festkommazahl besteht aus:
	    - **V**: Ein Vorzeichenbit (0 = positiv, 1 = negativ)
	    - **I**: Ganzzahliger Anteil (Integer-Bits)
	    - **F**: Gebrochener Anteil (Fractional-Bits)
	- Das Format wird als **(I, F)-Format** beschrieben.
	- ![[Pasted image 20250221153559.png]]
	- ### **Zahlenbereich in (I, F)-Format**
		- Der **darstellbare Wertebereich** ist: −(2^I−2^F)≤Z≤(2^I−2^F)
		- ![[Pasted image 20250221153729.png]]
- Gleitkommazahlen (Floating Point Numbers)
	- Gleitkommazahlen ermöglichen einen **größeren Zahlenbereich und höhere Präzision**, indem sie eine **dynamische Skalierung** nutzen. Die **IEEE 754-Standard** ist das am häufigsten verwendete Format.
	- IEEE 754 Gleitkommazahlen:
		- Eine **32-Bit-Gleitkommazahl (float)** besteht aus:
			- - **1 Bit**: **Vorzeichenbit V**
			- **8 Bits**: **Exponent E**
			- **23 Bits**: **Mantisse M (gebrochener Anteil)**
		- Die Darstellung erfolgt nach der Formel:
			- Z=(−1^)V×M×2^E
		- **Exponent-Berechnung:**
			- Der **Exponent E** speichert eine **verschobene Darstellung** mit **127 als Bias** (für 32-Bit).
			- Tatsächlicher Exponent: `E = gespeicherter Exponent - 127`
		- **Mantisse:**
			- Die Mantisse wird durch **m0 = 1** ergänzt:
			    - **M = 1 + gebrochener Anteil (Mantisse)**
		- ![[Pasted image 20250221154022.png]]
		- ![[Pasted image 20250221154030.png]]