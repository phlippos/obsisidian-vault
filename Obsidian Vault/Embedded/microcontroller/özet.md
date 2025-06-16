## UART
-  Sie ermöglicht die<mark style="background: #FFB86CA6;"> asynchrone</mark> Datenübertragung zwischen zwei Geräten ohne gemeinsamen Takt. 
- **Tx (Transmit)**: Sendet Daten vom Gerät A zum Gerät B
- **Rx (Receive)**: Empfängt Daten von Gerät B zu Gerät A
- **GND (Ground)**: Gemeinsame Masseleitung als Referenzpotential
- Übertragungsmodi
	- **Simplex**: Unidirektionale Kommunikation, bei der nur ein Gerät sendet und das andere empfängt. Nur eine Datenleitung wird verwendet.
	1. **Half-Duplex**: Bidirektionale Kommunikation über eine gemeinsame Leitung, bei der die Geräte abwechselnd senden und empfangen. Die Leitung muss zwischen Senden und Empfangen umgeschaltet werden.
	2. **Full-Duplex**: Bidirektionale Kommunikation über zwei separate Leitungen (Tx und Rx), die gleichzeitiges Senden und Empfangen ermöglicht. Dies ist die häufigste UART-Konfiguration.+
1. Protokoll
	1.  Im Ruhezustand (keine Übertragung) liegt die Leitung auf High-Pegel (logisch 1)
	2.  Jede Übertragung beginnt mit einem Start-Bit, das durch einen Wechsel von High nach Low (logisch 0) gekennzeichnet ist.
	3. Nach dem Start-Bit folgen die Datenbits (typischerweise 5-9 Bits, meist 8). Diese können vom LSB (Least Significant Bit) oder MSB (Most Significant Bit) zuerst übertragen werden, je nach Konfiguration.
	4. Ein optionales Paritätsbit kann zur einfachen Fehlererkennung hinzugefügt werden
	5. Bei einigen UART-Implementierungen kann ein Adressbit verwendet werden, um zwischen normalen Daten und Adressinformationen zu unterscheiden.
	6. Ein oder zwei Stop-Bits (logisch 1) markieren das Ende der Übertragung. 
2. Die Baudrate definiert die Übertragungsgeschwindigkeit und wird in Bits pro Sekunde (bps) gemessen. Bei UART entspricht 1 Baud genau 1 bps.
3. Sender und Empfänger müssen exakt die gleiche Baudrate verwenden, da keine separate Taktleitung existiert.
4.  **Vorteile:**
			- Einfache Implementierung
			- Benötigt nur wenige Leitungen
			- Weit verbreitet und gut unterstützt
			- Gute Zuverlässigkeit für<mark style="background: #FFB86CA6;"> kurze Distanzen</mark>
			- Flexibel konfigurierbar
- **Nachteile:**
			- Relativ <mark style="background: #FFB86CA6;">geringe Übertragungsraten</mark> im Vergleich zu neueren Protokollen
			- <mark style="background: #FFB86CA6;">Begrenzte Reichweite</mark> (typischerweise <15m)

## I2C
- eine serielle Schnittstelle, die mit einer Zwei-Draht-Verbindung implementiert wird und mehrere Master sowie mehrere Slaves unterstützen kann.
- eine Taktleitung (SCL = serieller Takt) und eine Datenleitung (SDA = serielle Daten).
-  arbeitet immer im Halbduplex-Modus, was bedeutet, dass alle Geräte die Datenleitung gemeinsam nutzen
- pullup-widerstände an scl und sda
- ![[Pasted image 20250616142018.png]]
-  Nachdem der Master die START-Bedingung erzeugt hat, sendet er zunächst die Slave-Adresse, mit der er kommunizieren möchte. I²C-Slave-Adressen können entweder 7 Bit (Standard) oder 10 Bit sein. Auf die Slave-Adresse folgt das Lese-/Schreibsignal, das angibt, welche Art von Transaktion in der Nachricht angefordert wird. Die START-Bedingung, die Slave-Adresse und das Lese-/Schreibsignal umfassen die Perioden 1-8.
- Periode 9 der Nachricht ist für das Slave-Acknowledge (ACK) oder No-Acknowledge (NACK) Signal reserviert. Nachdem der Master die Slave-Adresse und das Lese-/Schreibsignal gesendet hat, überprüft jeder Slave auf dem Bus, ob er adressiert wird. Wenn ein Slave mit der angegebenen Slave-Adresse existiert, sendet er ein ACK-Signal zurück an den Master, indem er SDA auf LOW zieht. Wenn der Master das ACK-Signal sieht, weiß er, dass ein Slave mit der angegebenen Adresse existiert und fährt mit der Nachricht fort.
- Wenn kein Gerät auf dem Bus mit der angegebenen Slave-Adresse existiert, wird kein Gerät SDA herunterziehen. Dies führt dazu, dass Periode 9 auf HIGH bleibt und als NACK interpretiert wird. Ein NACK in Periode 9 teilt dem Master mit, dass kein Slave mit der angegebenen Adresse existiert. Der Master erzeugt dann eine STOPP-Bedingung und beendet die Nachricht.
-  Nach einer erfolgreichen ACK-Bestätigung vom Slave werden die Daten dann 8 Bit auf einmal gesendet, beginnend mit dem MSB (Most Significant Bit).Nach dem Senden jedes Bytes sendet das empfangende Gerät ein ACK-Signal, das anzeigt, dass es die Daten erfolgreich empfangen hat.
,


## SPI
- ein synchrones serielles Kommunikationsprotokoll
- für die Datenübertragung zwischen Mikrocontrollern und peripheren Geräten verwendet wird
- verwendet SPI mehr Anschlusspins (mindestens drei)
- SPI basiert auf einem Master-Slave-Konzept:
	- Der Master erzeugt das Taktsignal (SCLK), das alle Geräte für die Datenübertragung verwenden
	- Die Datenleitungen werden als SIMO (Slave In, Master Out) und SOMI (Slave Out, Master In) bezeichnet
- DatenÜbertragung
	- Der Standard-SPI-Datenrahmen ist 8 Bit lang, wobei das niedrigwertigste Bit (LSB) zuerst gesendet wird
	- ![[Pasted image 20250616142632.png]]
	- Bei der Übertragung werden die Daten an der steigenden Flanke von SCLK ausgeschoben
	- Beim Empfang werden die Daten an der fallenden Flanke von SCLK eingelesen
	- Wenn keine Übertragung stattfindet, befindet sich SCLK in einem Ruhezustand
	- ![[Pasted image 20250616142813.png]]
## USCI
- eUSCI_Ax:
	- UART
	- SPI
- eUSCI_Bx:
	- SPI
	- I2C


- UART TRANSMIT
	- ![[Pasted image 20250427154216.png]]
	- TAKT WÄHLE
	- baudrate einstellen
	- übertragungsparameter einstellen
	- zu übertragendes byte in den puffer schreiben
	- ![[Pasted image 20250616143455.png]]
	- Empfang:
	- das übertragene BYTE aus dem puffer lesen (UCAxRXBUF)
	- Interrupt flag register
		- zeigt an, wenn
		- der Sendeprozess abgeschlossen ist
		- ein start-bit empfangen wurde
		- der sendepuffer leer ist
		- ein byte komplett empfangen wurde

## I2C Master mode, write to slave
![[Pasted image 20250520064242.png]]
- control register konfigurieren
- **UCBxI2CSA** (eUSCI_B I2C Slave-Adresse)
- **UCBxTXBUF** (eUSCI_B Sendepuffer) –zu übertragendes Byte in das Register geschrieben
- Startbedingung generieren (UCTXSTT = 1 in UCBxCTLW0)
- Stop-bedingung automatisch generieren lassen oder mit UCTXSTP = 1

## I2C Master mode, read from slave
- control register konfigurieren
- **UCBxI2CSA** (eUSCI_B I2C Slave-Adresse)
- Startbedingung generieren (UCTXSTT = 1 in UCBxCTLW0)
- **UCBxRXBUF** (eUSCI_B Empfangspuffer) – übertragenes Byte aus Register lesen, wenn vollständig empfangen (UCRxIFG = 1)
-  Stop-bedingung automatisch generieren lassen oder mit UCTXSTP = 1


## SPI SENDEN
- control register konfigurieren
- UCAxTXBUF (eUSCI_Ax Transmit Buffer) Sendepuffer für zu übertragende Daten

## SPI EMPFANGEN
- control register konfigurieren
- UCAxRXBUF (eUSCI_Ax Receive Buffer) Empfangspuffer, der die über SOMI empfangenen Daten enthält


![[Pasted image 20250616145245.png]] UART
![[Pasted image 20250427170355.png]]![[Pasted image 20250427170355.png]]
![[Pasted image 20250427170546.png]]
![[Pasted image 20250427170553.png]]
![[Pasted image 20250427171014.png]]
![[Pasted image 20250504163316.png]]
![[Pasted image 20250520070757.png]] ![[Pasted image 20250520071045.png]]


# Interrupts
-  **Unterbricht** das laufende Programm an beliebiger Stelle
- Wird durch ein **vorher definiertes Ereignis** ausgelöst
- Nach Auslösen wird die zugehörige **Interrupt-Funktion (ISR)** ausgeführt
- Nach Funktionsausführung kehrt das System zur ursprünglichen Programmstelle zurück
- **2.1 System Reset**
	- **BOR (Brownout Reset)**
	    - Beim Einschalten, Low-Signal am RST-Pin
	    - Wake-up Events, Software BOR Events
	    - Sicherheitsverletzungen (Zugriff auf geschützten Speicher)
	- **POR (Power On Reset)**
	    - Wird durch BOR immer ausgelöst
	    - Spezielle PMM-Events und Software POR Events
	- **PUC (Power Up Clear)**
	    - Wird immer durch POR generiert
	    - Watchdog Timer Überlauf oder falsche Passwörter
- **2.2 Nicht maskierbare Interrupts (NMI)**
	- Werden **nicht** durch das General Interrupt Enable (GIE) Bit maskiert
	- - **System NMI (SNMI)**:
        - Fehlerhafte Versorgungsspannung
        - Zugriff auf leeren Speicher
        - JTAG Mailbox Events
    - **User NMI (UNMI)**:
        - Flanke am NMI Pin
        - Fehlerhafter Oszillator-Takt
        - Zugriffsverletzung im Flash Memory
- **2.3 Maskierbare Interrupts**
	- Werden durch das **GIE Bit** global aktiviert/deaktiviert (`__enable_interrupt()`)
	- Werden durch **interruptfähige Peripherie** ausgelöst
-  **3. Interrupt-Prioritäten**
	- Bei **mehreren gleichzeitigen Interrupts** muss die Reihenfolge geregelt sein
	- **Höchste Priorität**: System Reset (Priorität 63)
	- **Niedrigste Priorität**: Reservierte Interrupts (Priorität 0)
- **4. Interrupt-Ablauf**
	- **Aktuellen Befehl beenden**
	1. **Kontext sichern**: Programmzähler (PC) und Statusregister (SR) auf Stack
	2. **SR löschen** (automatisch durch MCU)
	3. **ISR-Adresse laden** und Interrupt Service Routine ausführen
	4. **Kontext wiederherstellen**: SR und PC vom Stack holen
	5. **Zur ursprünglichen Stelle zurückkehren**
- **Interruptvektoren**
	- **Adressen der ISRs** werden in Interruptvektoren abgelegt
	- **Interrupt-Vektor-Tabelle** liegt außerhalb des Programmspeichers
	- Spezifikation in C mit: `#pragma vector=<VECTOR_LABEL>`
	- Jeder Interrupt hat eine **feste Adresse** in der Vektor-Tabelle
- **Interruptfähige Ports**
	- Nur **Port 1 und Port 2** sind interruptfähig
	- ![[Pasted image 20250530121520.png]]
	- **P1IV (Interrupt Vector Register)**: Identifiziert die Interrupt-Quelle
	- **P1IES (Interrupt Edge Select)**: Konfiguriert Flankenart
		- - 0b = Low-to-High Transition
	    - 1b = High-to-Low Transition
	    - ![[Pasted image 20250530121607.png]]
	- **P1IE (Interrupt Enable)**: Aktiviert/deaktiviert Port-Interrupts
		- ![[Pasted image 20250530121620.png]]
	- **P1IFG (Interrupt Flag)**: Zeigt pendende Interrupts an
		- ![[Pasted image 20250530121634.png]]
	- **Problem: Taster-Prellen**
	- Mechanische Taster erzeugen beim Betätigen mehrere ungewollte Flanken ("Bounce"):
	- **Idealisiertes Signal**: Sauberer Übergang zwischen HIGH und LOW
	- **Reales Signal**: Mehrfache Übergänge durch mechanisches Prellen
	- ![[Pasted image 20250616185145.png]]
- ### **Lösungsansätze für Entprellen**
	1. **Schaltungstechnisch**: RC-Glied als Tiefpass
	    - Schwierig bei vorhandener Platine
	2. <mark style="background: #FFB86CA6;">**Softwareseitig**</mark>:
	    - Nach Flankenerkennung "Prellzeit" abwarten
	    - Interrupts temporär deaktivieren
	    - Timer-basierte Entprellung
- ![[Pasted image 20250616185432.png]]
# AD Wandler
- Der **Analog-Digitalwandler (ADC)** wandelt kontinuierliche analoge Signale in diskrete digitale Werte um.
- #### **Sampling-Rate**
	- **Definition**: Anzahl der Abtastungen pro Sekunde
	- **Nyquist-Prinzip**: Sampling-Frequenz muss mindestens **2× die höchste Signalfrequenz** betragen
	- **Formel**: fs ≥ 2 × fsignal
- #### **Quantisierung**
	- **Definition**: Aufteilung des analogen Wertebereichs in diskrete Stufen
	- **Auflösung**: Anzahl der Bits bestimmt die Anzahl der Quantisierungsstufen
	- **12-Bit ADC**: 2¹² = 4096 Stufen (0-4095)
- 12 analoge Eingänge
- #### **Referenzspannung**
	- **Definition**: Bestimmt den Messbereich des ADCs
	- **Bedeutung**: Legt fest, welche analoge Spannung dem maximalen Digitalwert entspricht
	- ![[Pasted image 20250530132348.png]]
- ![[Pasted image 20250530132931.png]]
- ![[Pasted image 20250530132935.png]]
- **ADCCTL0**
- Bits 11-8: ADCSHT (ADC Sample-and-Hold Time)**
	- **Zweck**: Bestimmt die **Sample-Zeit** des ADCs
	- **Wichtigkeit**: Kritisch für genaue Messungen
```c
ADCSHT_0  = 0000b = 4 ADCCLK Cycles
ADCSHT_1  = 0001b = 8 ADCCLK Cycles (Standard)
ADCSHT_2  = 0010b = 16 ADCCLK Cycles
ADCSHT_3  = 0011b = 32 ADCCLK Cycles
ADCSHT_4  = 0100b = 64 ADCCLK Cycles
ADCSHT_5  = 0101b = 96 ADCCLK Cycles
ADCSHT_6  = 0110b = 128 ADCCLK Cycles
ADCSHT_7  = 0111b = 192 ADCCLK Cycles
ADCSHT_8  = 1000b = 256 ADCCLK Cycles
ADCSHT_9  = 1001b = 384 ADCCLK Cycles
ADCSHT_10 = 1010b = 512 ADCCLK Cycles
ADCSHT_11 = 1011b = 768 ADCCLK Cycles
ADCSHT_12 = 1100b = 1024 ADCCLK Cycles
ADCSHT_13 = 1101b = 1024 ADCCLK Cycles
ADCSHT_14 = 1110b = 1024 ADCCLK Cycles
ADCSHT_15 = 1111b = 1024 ADCCLK Cycles
```
- **Kurze Sample-Zeit**: Schnellere Wandlung, aber möglicherweise ungenau bei hochohmigen Quellen
- **Lange Sample-Zeit**: Langsamere Wandlung, aber genauer bei hochohmigen Quellen
- 
- ### **Bit 7: ADCMSC (ADC Multiple Sample and Conversion)**
 - **Zweck**: Steuert den **Multiple-Conversion-Modus**
	#### **Modi:**
	- **ADCMSC = 0**:
	    - **Single-Shot Modus**
	    - Nach jeder Wandlung muss ADCSC erneut gesetzt werden
	    - Für einzelne Messungen
	- **ADCMSC = 1**:
	    - **Continuous Modus**
	    - Automatische Wiederholung der Wandlungen
	    - Für kontinuierliche Messungen
	- 
- ### **Bit 4: ADCON (ADC On)**
	- **Zweck**: **Power-Control** für den ADC-Kern
		#### **Funktionen:**
		- **ADCON = 0**: ADC ist **ausgeschaltet** (Stromsparmodus)
		- **ADCON = 1**: ADC ist **eingeschaltet** und betriebsbereit
- ### **Bit 1: ADCENC (ADC Enable Conversion)**
	- **Zweck**: **Master-Enable** für ADC-Wandlungen
 	#### **Funktionen:**
		- **ADCENC = 0**:
		    - Wandlungen sind **deaktiviert**
		    - Konfigurationsänderungen möglich
		    - Sicherheitsmodus
		- **ADCENC = 1**:
		    - Wandlungen sind **aktiviert**
		    - Keine Konfigurationsänderungen möglich
		    - Betriebsmodus
		#### **Wichtiger Hinweis:**
		- **Konfiguration nur möglich wenn ADCENC = 0**
		- Vor Konfigurationsänderungen muss ADCENC gelöscht werden
- ### **Bit 0: ADCSC (ADC Start Conversion)**
- **Zweck**: **Startet** eine ADC-Wandlung
#### **Funktionen:**
- **ADCSC = 0**: Keine Wandlung
- **ADCSC = 1**: **Startet Wandlung** (wird automatisch gelöscht nach Start)
#### **Verhalten:**
- Bit wird **automatisch gelöscht** nach Wandlungsstart
- Muss für jede neue Wandlung gesetzt werden (außer im Continuous-Modus)


# Energieeffizienz

**Geringere Energiekosten**
- Reduzierung der Stromrechnungen in großen Installationen
- Wichtig für IoT-Geräte mit tausenden von Sensoren

**Wärmemanagement**
- Verlustleistung wird hauptsächlich in Wärme umgewandelt
- Weniger Kühlleistung benötigt → geringere Systemkosten
- Verbesserte Zuverlässigkeit durch niedrigere Betriebstemperaturen

**Längere Batterielaufzeiten**
- **Mobiltelefone**: Von Stunden auf Tage
- **Tablets**: Ganztägige Nutzung ohne Aufladen
- **Laptops/Ultrabooks**: 8+ Stunden Akkulaufzeit
- **IoT-Sensoren**: Jahre ohne Batteriewechsel

![[Pasted image 20250616200049.png]]
### Statische Verlustleistung
**Definition**: Verlustleistung, die auch bei inaktiven Transistoren auftritt
**Hauptursachen**:
- **Sub-threshold current**: Schwacher Strom auch bei "ausgeschalteten" Transistoren
- **Gate leakage**: Leckstrom durch das Gate-Oxid
- **Drain junction leakage**: Leckstrom an den pn-Übergängen
**Formel**: P_statisch = U × I_leck

### Dynamische Verlustleistung
**Definition**: Verlustleistung beim Schalten der Transistoren
**Formel**: P_dyn = α × C_eff × V_dd² × f_clk
**Parameter-Erklärung**:
- **α (switching activity)**: Wie oft schalten die Transistoren? (0-1)
- **C_eff**: Effektive Kapazität (Transistoren + Leiterbahnen)
- **V_dd**: Versorgungsspannung
- **f_clk**: Taktfrequenz
**Optimierungsstrategien**:
1. **Spannung reduzieren**: Quadratischer Einfluss! V_dd von 3.3V auf 1.8V → 65% weniger Verlustleistung
2. **Frequenz reduzieren**: Linearer Einfluss
3. **Kapazität minimieren**: Kleinere Transistoren, kürzere Leiterbahnen
4. **Switching Activity reduzieren**: Clock Gating, intelligente Algorithmen



### Taktquellen des MSP430F5529:

**XT1CLK (32.768 kHz)**
- Externer Quarz für präzise Zeitbasis
- Niedrigster Stromverbrauch
- Ideal für RTC (Real-Time Clock)

**VLOCLK (Very Low Oscillator)**
- Interner 10kHz Oszillator
- Sehr stromsparend, aber ungenau
- Für unkritische Timer-Anwendungen

**REFOCLK (Reference Oscillator)**
- Interner 32kHz Referenz-Oszillator
- Kompromiss zwischen Genauigkeit und Stromverbrauch

**DCOCLK (Digitally Controlled Oscillator)**
- Hochfrequenz-Oszillator (bis 25MHz)
- Schnelles Aufwachen aus Sleep-Modi
- Hoher Stromverbrauch

**XT2CLK (Optional)**
- Externer Hochfrequenz-Quarz
- Höchste Genauigkeit bei hohen Frequenzen

### Ausgangstakte:

**ACLK (Auxiliary Clock)**
- Standard: 32.768 kHz
- Für langsame Peripherie (Timer, UART bei niedrigen Baudraten)

**MCLK (Master Clock)**
- Standard: 1 MHz
- CPU-Takt

**SMCLK (Sub-Master Clock)**
- Standard: 1 MHz
- Für schnelle Peripherie (SPI, ADC)

### Active Mode (AM)
**Zustand**: Normaler Betrieb
- CPU aktiv
- Alle Takte verfügbar
- Alle Module können arbeiten
- **Stromverbrauch**: ~315μA @ 1MHz (V_cc = 3V)
**Anwendung**: Aktive Berechnung, Datenverarbeitung
### LPM0 (Low Power Mode 0)
**Zustand**: CPU schläft, Peripherie aktiv
- CPU ausgeschaltet
- MCLK aus
- ACLK und SMCLK aktiv
- FLL (Frequency Locked Loop) aktiv
- **Stromverbrauch**: ~55μA
**Anwendung**: Timer-gesteuerte Operationen, Peripherie arbeitet selbstständig

```c
// Timer startet ADC-Messung alle 100ms
__bis_SR_register(LPM0_bits + GIE);  // Eintritt in LPM0
```

### LPM1 (Low Power Mode 1)
**Zustand**: Wie LPM0, aber FLL aus
- FLL loop control ausgeschaltet
- Schnelleres Aufwachen als LPM2/3
- **Stromverbrauch**: ~32μA
**Anwendung**: Wenn DCO nach Aufwachen nicht sofort benötigt wird

### LPM2 (Low Power Mode 2)
**Zustand**: Nur ACLK aktiv
- DCOCLK ausgeschaltet
- SMCLK ausgeschaltet
- DC-Generator vom DCO bleibt aktiv (schnelles Aufwachen)
- **Stromverbrauch**: ~17μA
**Anwendung**: Nur langsame Timer benötigt (RTC, Watchdog)

### LPM3 (Low Power Mode 3)
**Zustand**: Minimaler Betrieb
- Nur ACLK aktiv
- DC-Generator ausgeschaltet
- Längere Aufwachzeit
- **Stromverbrauch**: ~0.9μA
**Anwendung**: Lang-Zeit-Timer, seltene Ereignisse
```c
WDTCTL = WDT_ADLY_8000;             // 8s Interval
IE1 |= WDTIE;                       // Watchdog Interrupt enable
__bis_SR_register(LPM3_bits + GIE); // Eintritt in LPM3
```

### LPM4 (Low Power Mode 4)
**Zustand**: Tiefschlaf mit Datenhaltung
- Alle Takte ausgeschaltet
- Quarz-Oszillator gestoppt
- Daten bleiben erhalten
- **Stromverbrauch**: ~0.1μA
**Aufwachen nur durch**:
- Externe Interrupts (Port-Pins)
- Reset

### LPM4.5 (Low Power Mode 4.5)
**Zustand**: Tiefster Schlafmodus
- Interner Regulator ausgeschaltet
- **Daten gehen verloren!**
- **Stromverbrauch**: ~0.1μA
**Aufwachen nur durch**:
- RST/NMI Pin
- Bestimmte Port-Pins (P1, P2)


# Vize öncesi
- (PxIN) zum Lesen des Zustands der Eingangspins
	-  **Bit = 0**: Der entsprechende Pin ist auf niedrigem Pegel (LOW/0V)
	- **Bit = 1**: Der entsprechende Pin ist auf hohem Pegel (HIGH/VCC)
- (PxDIR) die Datenrichtung jedes einzelnen Pins eines Ports
	- Bit = 0: Der entsprechende Pin wird als Eingang (Input) konfiguriert
	- Bit = 1: Der entsprechende Pin wird als Ausgang (Output) konfiguriert
-  (PxOUT)
	- Bei Ausgängen (Output-Modus):
		-  Bit = 0: Der Ausgang wird auf logisch Low gesetzt (0V)
		- Bit = 1: Der Ausgang wird auf logisch High gesetzt
	- Bei Eingängen (Input-Modus) mit aktivierten Pull-up/Pull-down Widerständen:
		- Bit = 0: Der interne Pull-down-Widerstand wird aktiviert (Pin wird zu GND gezogen)
		- Bit = 1: Der interne Pull-up-Widerstand wird aktiviert 
- (PxREN)   die Aktivierung der internen Pull-up- oder Pull-down-Widerstände für jeden Pin eines Ports
	- **Bit = 0:** Der interne Pull-up/Pull-down-Widerstand für den entsprechenden Pin ist deaktiviert
	- **Bit = 1:** Der interne Pull-up/Pull-down-Widerstand für den entsprechenden Pin ist aktiviert
- **Schwebende Eingänge (Floating Inputs)**:<mark style="background: #FFB86CA6;"> Wenn ein Pin als Eingang konfiguriert ist, aber nicht angeschlossen wird, kann sein Zustand undefiniert sein.</mark>
- **Ineffiziente Energienutzung**: Während der Schleife läuft der Prozessor mit voller Leistung, führt jedoch keine nützlichen Operationen aus.(delay )
- ## Timer_B
	- besteht das Timer_B-System des MSP430F5529 aus vier unabhängigen Timern
		- **TB0**: Timer_B0 mit drei Capture/Compare-Registern (Timer0_B3)
		- **TB1**: Timer_B1 mit drei Capture/Compare-Registern (Timer1_B3)
		- **TB2**: Timer_B2 mit drei Capture/Compare-Registern (Timer2_B3)
		- **TB3**: Timer_B3 mit sieben Capture/Compare-Registern (Timer3_B7)
	- ### 1. Stop-Modus (MC = 00)
		- Der Timer ist angehalten
	- 2. Up-Modus (MC = 01)
		- Der Timer zählt von 0 bis zum Wert in TBxCCR0
		- Bei Erreichen von TBxCCR0 wird das CCIFG-Flag in TBxCCR0 gesetzt
		- Der Zähler wird auf 0 zurückgesetzt und das TBIFG-Flag gesetzt
	- Continuous-Modus (MC = 10)
		- Der Timer zählt kontinuierlich von 0 bis 0xFFFF
		- Bei Überlauf (Wechsel von 0xFFFF zu 0) wird das TBIFG-Flag gesetzt
	- 4. Up/Down-Modus (MC = 11)
		-  Der Timer zählt von 0 bis zum Wert in TBxCCR0 und dann wieder zurück auf 0
		- Das CCIFG-Flag wird vor Erreichen des Maximalwerts gesetzt
		- Das TBIFG-Flag wird vor Erreichen von 0 gesetzt
```c
//Präzise Zeitsteuerung
TB0CTL = TBSSEL_2 | ID_3 | MC_1;  // SMCLK, /8, Up-Modus
TB0EX0 = TBIDEX_7;               // Zusätzlich /8 = Gesamt /64
TB0CCR0 = 15625 - 1;             // 1 MHz / 64 = 15625 Takte für 1 Sekunde
TB0CCTL0 = CCIE;                 // Compare-Interrupt aktiviere

--------------------------------------------
//PWM-Generierung
TB0CTL = TBSSEL_2 | MC_1;       // SMCLK, Up-Modus
TB0CCR0 = 1000 - 1;             // PWM-Periode
TB0CCR1 = 500;                  // 50% Duty Cycle
TB0CCTL1 = OUTMOD_7;            // Reset/Set Ausgangsmodus
```
- ## Timer_A
	-  Timer_A ist ein 16-bit Timer/Counter, der in praktisch allen MSP430-Mikrocontrollern vorhanden ist.
	- verfügt typischerweise über bis zu 7 Capture/Compare-Register.
		-  **TAxCTL (Timer_A Control Register)**: Steuert die Taktquelle, den Taktteiler, den Betriebsmodus und die Interrupts.
		2. **TAxR (Timer_A Register)**: Enthält den aktuellen Zählwert des Timers.
		3. **TAxCCRn (Capture/Compare Register n)**: Wird für Capture- oder Compare-Operationen verwendet.
		4. **TAxCCTLn (Capture/Compare Control Register n)**: Steuert die Capture/Compare-Funktionen.
		5. **TAxEX0 (Timer_A Expansion Register 0)**: Bietet zusätzliche Taktteiler-Optionen.

- Watchdog Timer 
	- Seine Hauptaufgabe ist es, das System bei Fehlfunktionen oder Software-Hängern automatisch zurückzusetzen.
	- Der Watchdog Timer ist im Grunde ein Zähler, der kontinuierlich hochzählt. Wenn dieser Zähler seinen maximalen Wert erreicht und überläuft, löst er einen Systemreset aus (PUC - Power-Up Clear). Im normalen Betrieb muss die Software den Watchdog regelmäßig zurücksetzen ("füttern"), bevor er überläuft, um anzuzeigen, dass das System ordnungsgemäß funktioniert.
	- ![[Pasted image 20250326135210.png]]
```c
WDTCTL = WDTPW | WDTHOLD; // Passwort (0x5A) und HOLD-Bit setzen
```

- System-on-a-Chip (SoC)
	- Ein **System-on-a-Chip** integriert neben der CPU auch Grafikprozessoren (GPU), DSPs (Digital Signal Processors), Speichercontroller, Kommunikationsschnittstellen und andere Peripherie auf einem einzigen Chip.(smartphones)
- System-on-a-Programmable-Chip (SoPC)
	-  Ein **System-on-a-Programmable-Chip (SoPC)** kombiniert die Eigenschaften eines Mikrocontrollers mit einem **FPGA (Field Programmable Gate Array)**.
- **Complex Instruction Set Computer**
	- Der Begriff **Complex Instruction Set Computer (CISC)** bezeichnet eine Prozessorarchitektur, die eine Vielzahl komplexer Maschinenbefehle unterstützt. CISC-Prozessoren sind so konzipiert, dass sie mit **weniger Maschinenbefehlen** auskommen, indem sie leistungsstarke und spezialisierte Befehle anbieten variabel befehlslänge 1 bis 15 bytes
- **Reduced Instruction Set Computer (RISC)**
	- Der Begriff **Reduced Instruction Set Computer (RISC)** bezeichnet eine Prozessorarchitektur, die im Gegensatz zur **Complex Instruction Set Computer (CISC)**-Architektur auf eine reduzierte Anzahl <mark style="background: #FFB86CA6;">einfacher und effizienter Maschinenbefehle</mark> setzt. Das Ziel von RISC ist eine **<mark style="background: #FFB86CA6;">höhere Geschwindigkeit und Effizienz</mark>**, indem jeder Befehl in einem einzigen oder <mark style="background: #FFB86CA6;">wenigen Taktzyklen</mark> ausgeführt wird. fest befehlslänge 4 bytes
	- 