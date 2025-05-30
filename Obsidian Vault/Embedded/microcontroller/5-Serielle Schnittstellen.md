

## UART (Universal Asynchronous Receiver/Transmitter)
- Grundprinzip und Aufbau
	- UART ist eine der ältesten und am weitesten verbreiteten seriellen Kommunikationsschnittstellen in der Elektronik. Sie ermöglicht die<mark style="background: #FFB86CA6;"> asynchrone</mark> Datenübertragung zwischen zwei Geräten ohne gemeinsamen Takt. Der Name beschreibt bereits die Hauptfunktionen:
		- **Universal**: Kann mit verschiedenen Geräten und Protokollen verwendet werden
		- **Asynchronous**: Benötigt keine separate Taktleitung zur Synchronisation
		- **Receiver/Transmitter**: Ermöglicht bidirektionale Kommunikation
	- Eine typische UART-Verbindung besteht aus mindestens drei Leitungen:
		- **Tx (Transmit)**: Sendet Daten vom Gerät A zum Gerät B
		- **Rx (Receive)**: Empfängt Daten von Gerät B zu Gerät A
		- **GND (Ground)**: Gemeinsame Masseleitung als Referenzpotential
	- Übertragungsmodi
		- UART unterstützt drei verschiedene Übertragungsmodi:
			1. **Simplex**: Unidirektionale Kommunikation, bei der nur ein Gerät sendet und das andere empfängt. Nur eine Datenleitung wird verwendet.
			2. **Half-Duplex**: Bidirektionale Kommunikation über eine gemeinsame Leitung, bei der die Geräte abwechselnd senden und empfangen. Die Leitung muss zwischen Senden und Empfangen umgeschaltet werden.
			3. **Full-Duplex**: Bidirektionale Kommunikation über zwei separate Leitungen (Tx und Rx), die gleichzeitiges Senden und Empfangen ermöglicht. Dies ist die häufigste UART-Konfiguration.
	- ## Datenrahmen und Protokoll
		- Bei der UART-Kommunikation werden Daten in Frames (Rahmen) übertragen. Ein typischer UART-Frame besteht aus:
			-  **Ruhezustand**: Im Ruhezustand (keine Übertragung) liegt die Leitung auf High-Pegel (logisch 1).(This idle logic level stems from early systems in which they wanted a way to make sure that the transmitting link was still operational.)
			- **Start-Bit**: Jede Übertragung beginnt mit einem Start-Bit, das durch einen Wechsel von High nach Low (logisch 0) gekennzeichnet ist. Dieses signalisiert dem Empfänger, dass eine Datenübertragung beginnt.
			- **Datenbits**: Nach dem Start-Bit folgen die Datenbits (typischerweise 5-9 Bits, meist 8). Diese können vom LSB (Least Significant Bit) oder MSB (Most Significant Bit) zuerst übertragen werden, je nach Konfiguration.
			- **Parity-Bit (optional)**: Ein optionales Paritätsbit kann zur einfachen Fehlererkennung hinzugefügt werden. Es kann gerade Parität (even) oder ungerade Parität (odd) haben.
			- **Address-Bit (optional)**: Bei einigen UART-Implementierungen kann ein Adressbit verwendet werden, um zwischen normalen Daten und Adressinformationen zu unterscheiden.
			- **Stop-Bit(s)**: Ein oder zwei Stop-Bits (logisch 1) markieren das Ende der Übertragung. Sie stellen sicher, dass eine Pause zwischen aufeinanderfolgenden Frames besteht.
	- ## Baudrate
		- Die Baudrate definiert die Übertragungsgeschwindigkeit und wird in Bits pro Sekunde (bps) gemessen. Bei UART entspricht 1 Baud genau 1 bps. Typische Baudraten sind:
			- 9600 bps
			- 19200 bps
			- 38400 bps
			- 57600 bps
			- 115200 bps
		- Wichtig: Sender und Empfänger müssen exakt die gleiche Baudrate verwenden, da keine separate Taktleitung existiert. Eine Abweichung von mehr als 5-10% kann zu Übertragungsfehlern führen.
	- ## Konfiguration und Parameter
		- Eine UART-Verbindung wird durch mehrere Parameter definiert:
			- **Baudrate**: Übertragungsgeschwindigkeit
			- **Datenbits**: Anzahl der Datenbits pro Frame (5-9)
			- **Parität**: Keine, gerade oder ungerade Parität
			- **Stop-Bits**: 1 oder 2 Stop-Bits
			- **Flusssteuerung (optional)**: Hardware (RTS/CTS) oder Software (XON/XOFF)
		- Diese Parameter werden üblicherweise in einem Format wie "9600 8N1" angegeben, was bedeutet: 9600 bps, 8 Datenbits, keine Parität, 1 Stop-Bit.
	- ## Vorteile und Nachteile von UART
		- **Vorteile:**
			- Einfache Implementierung
			- Benötigt nur wenige Leitungen
			- Weit verbreitet und gut unterstützt
			- Gute Zuverlässigkeit für<mark style="background: #FFB86CA6;"> kurze Distanzen</mark>
			- Flexibel konfigurierbar
		- **Nachteile:**
			- Relativ <mark style="background: #FFB86CA6;">geringe Übertragungsraten</mark> im Vergleich zu neueren Protokollen
			- <mark style="background: #FFB86CA6;">Begrenzte Reichweite</mark> (typischerweise <15m)
			- Keine integrierte Adressierung für Mehrgeräte-Netzwerke
			- Keine Taktsynchronisation zwischen Geräten
			- 
In a UART (Universal Asynchronous Receiver-Transmitter) system, the key challenge is that the receiver (Rx) needs to correctly interpret data from the transmitter (Tx) without sharing a common clock signal - that's what makes it "asynchronous."

## Oversampling Mechanism

The oversampling technique works like this:

1. **Transmitter Operation**:
    - The Tx shift register uses D-flip-flops clocked at the baud rate (e.g., 9600 bps)
    - Each clock cycle (TB), one bit shifts out to the communication line
    - The data frame typically includes: start bit (0), data bits (usually 8), optional parity bit, and stop bit(s) (1)
2. **Receiver Operation**:
    - The Rx samples the incoming signal at a <mark style="background: #FFB86CA6;">much higher rate than the transmitter's baud rate</mark>
    - With <mark style="background: #FFB86CA6;">16x oversampling, the Rx samples 16 times during each bit period of the Tx</mark>
3. **Start Bit Detection**:
    - The Rx continuously monitors the line for a high-to-low transition (start bit)
    - When detected, this triggers the sampling process
4. **Sample Timing**:
    - After detecting the start bit, the Rx waits approximately 8 sample clock cycles to reach the middle of the start bit
    - <mark style="background: #FFB86CA6;">This positioning in the middle of the bit provides maximum noise immunity</mark>
    - From there, the Rx samples every 16 clock cycles to hit the middle of each subsequent bit

## Why Sample in the Middle?

Sampling in the middle of each bit period provides the best signal integrity because:

- It's furthest from the transitions between bits
- It allows for some clock drift between Tx and Rx
- It minimizes the effects of noise that might occur during bit transitions

## Detailed Sampling Process

With 16x oversampling for an 8-bit data frame:

- Start bit: 16 Rx clock cycles
- 8 data bits: 8 × 16 = 128 Rx clock cycles
- Total: 144 Rx clock cycles (including stop bit)

The Rx uses a counter to track its position within the frame:

1. Reset counter when start bit detected
2. Sample at count 8 (middle of start bit)
3. Sample at counts 24, 40, 56, 72, 88, 104, 120, 136 (middle of each data bit)
4. Sample at count 152 (middle of stop bit)

## Error Detection

The oversampling also helps detect framing errors:

- If the stop bit isn't detected where expected, it indicates a framing error
- The Rx might also validate multiple samples per bit to ensure signal stability
- Some UARTs implement majority voting on multiple samples around the bit center for better noise immunity

## Clock Tolerance

This oversampling approach allows for clock differences between Tx and Rx. With 16x oversampling, the Rx can tolerate approximately ±4.8% difference in clock rates without losing synchronization (because sampling in the middle gives margin on either side).
![[Pasted image 20250427153706.png]]The drawback of this approach is that the clock frequency used to generate the baud rate on the Tx will never be exactly the same as the clock frequency used to generate the baud rate oversampling ratio on the Rx. This error results in the possibility of the last bit of the frame being shifted either too far left or right of its expected position when the sampling is complete and the received data that is transferred to the Rx buffer being incorrect. This is the reason that a stop bit is necessary. The stop bit allows the receiver to catch up and then start over its sampling upon a new start bit. The clock error between the Tx and Rx is inherent in asynchronous communication and is a limiting factor in how fast the serial communication link can run



## UART Transmit on the MSP430FR2355

![[Pasted image 20250427154216.png]]
- Der MSP430FR2355-Mikrocontroller verwendet das erweiterte Universal Serial Communication Interface (eUSCI) für die UART-Kommunikation.
- Grundlegende UART-Register und deren Funktionen
	- **UCAxCTLW0** (Kontrollwort 0):
		- Steuert grundlegende UART-Funktionen
		- Enthält das UCSWRST-Bit (Software-Reset)
		- <mark style="background: #FFB86CA6;">Definiert Rahmenformat (Datenbits, Parität, Stoppbits)</mark>
		- Konfiguriert Übertragungsmodus und Taktquelle
	- **UCAxBRW** (Baudrate-Kontrollwort):
		- <mark style="background: #FFB86CA6;">Bestimmt die Baudrate durch Teilen der Taktquelle</mark>
		- Zusammen mit UCAxMCTLW ermöglicht es präzise Baudraten
	- **UCAxMCTLW** (Modulationskontrollwort):
		- Enthält Überabtastfaktor und Modulationseinstellungen
		- <mark style="background: #FFB86CA6;">Feinabstimmung der Baudrate durch Bruchteile</mark>
	- **UCAxTXBUF** (Sendepuffer):
		- <mark style="background: #BBFABBA6;">Hier werden die zu sendenden Daten geschrieben</mark>
		- <mark style="background: #D2B3FFA6;">Das Schreiben in dieses Register initiiert die Übertragung</mark>
	- **UCAxRXBUF** (Empfangspuffer):
		- <mark style="background: #BBFABBA6;"> Enthält empfangene Daten</mark>
		- Lesezugriff löscht automatisch das Empfangsflags-Bit
	- **UCAxIE** (Interrupt-Aktivierung):
		- <mark style="background: #FFF3A3A6;">Aktiviert Sende- und Empfangsinterrupts</mark> (UCTXIE, UCRXIE)
		- <mark style="background: #D2B3FFA6;">Ermöglicht ereignisgesteuerte Kommunikation</mark>
	- **UCAxIFG** (Interrupt-Flags):
		- <mark style="background: #D2B3FFA6;">Zeigt Übertragungsereignisse an</mark>
		- UCTXIFG = Sendepuffer bereit für neue Daten
		- UCRXIFG = Daten wurden empfangen
	- ![[Pasted image 20250427155634.png]]
	- ![[Pasted image 20250427155729.png]]
	- ![[Pasted image 20250427155740.png]]
	- **Detaillierter Konfigurationsprozess**
```
UCA0CTLW0 |= UCSWRST; // eUSCI_A0 in Reset-Modus versetzen
/*
Dies ist ein kritischer erster Schritt, der verhindert, dass während der Konfiguration unbeabsichtigte Übertragungen stattfinden.
### 2. Konfigurationsregister initialisieren

**Schritt 2.1: Kontrollwort 0 konfigurieren**
*/

UCA0CTLW0 = UCSWRST |   // Software-Reset aktiv halten
            UCSSEL__SMCLK;  // SMCLK als Taktquelle wählen
/*
**Schritt 2.2: Baudrate konfigurieren** Für eine Baudrate von 9600 bei einem 1MHz SMCLK:
*/

// Baudrate = Taktquelle / (UCA0BR + UCA0MCTLW.BRF/16)
UCA0BRW = 6;       // Ganzzahliger Divisionsfaktor
UCA0MCTLW = 0x2081;  // 0x20: Überabtastmodus, 0x81: Modulationsmuster

/*
Der Wert von UCAxMCTLW enthält:

- Bits 15-8 (UCOS16): Überabtastungsmodus (1=aktiviert)
- Bits 7-4 (UCBRF): Bruchteildivisionsfaktor
- Bits 3-0 (UCBRS): Zweite Modulationsstufe


3. Ports konfigurieren
*/

P1SEL0 |= BIT6 | BIT7;  // P1.6=UCA0TXD, P1.7=UCA0RXD
P1SEL1 &= ~(BIT6 | BIT7);

/*
Die GPIO-Pins müssen für die UART-Funktion konfiguriert werden,
typischerweise durch Ändern der Funktionsauswahlregister (SEL0, SEL1).

4. Software-Reset deaktivieren
*/

UCA0CTLW0 &= ~UCSWRST;  // eUSCI_A0 aus Reset-Modus nehmen
/*
Dies aktiviert den UART und ermöglicht die Kommunikation.
5. Interrupts aktivieren (optional)

*/

UCA0IE |= UCRXIE;  // Empfangsinterrupt aktivieren
// UCA0IE |= UCTXIE;  // Sendeinterrupt aktivieren (falls benötigt)



```

- ## Übertragungsprozess im Detail
1. **Initiierung der Übertragung:**
    - Daten werden in das UCAxTXBUF-Register geschrieben
    - Dies löst automatisch einen Übertragungsprozess aus
2. **Hardware-Verarbeitung:**
    - Der Inhalt von UCAxTXBUF wird in das interne Schieberegister übertragen
    - Ein Startbit (0) wird gesendet
    - Die Datenbits werden serienweise mit der konfigurierten Baudrate gesendet
    - Das Stoppbit (1) wird gesendet
    - Das UCTXIFG-Flag wird gesetzt, um anzuzeigen, dass UCAxTXBUF bereit für neue Daten ist

![[Pasted image 20250427160925.png]]

![[Pasted image 20250427161453.png]]## Fehlerkorrektur bei der Baudratengenerierung

Der MSP430 verwendet einen zweistufigen Ansatz zur präzisen Baudratengenerierung:

1. **Vorteiler (Prescaler)** 
	- Ganzzahlige Division der Taktfrequenz (BRCLK)
    - Der Vorteiler wird durch UCAxBRW konfiguriert
    - Diese Division allein führt zu Timingfehlern bei bestimmten Baudraten
2. **Modulationstechniken** 
	- Feinabstimmung durch zwei Modulationsstufen:
    - **Erste Modulationsstufe (UCBRF)**: Fügt Bruchteile von BRCLK-Perioden hinzu
    - **Zweite Modulationsstufe (UCBRS)**: Erzeugt ein Modulationsmuster für optimale Bit-Übergänge

## Überabtastungsmodus (UCOS16)

Bei aktiviertem Überabtastungsmodus (UCOS16=1):

- Der Vorteiler teilt N durch 16 (wobei N = f_BRCLK/Baudrate)
- Dieser Modus ermöglicht eine präzisere Baudratengenerierung
- Sowohl die erste als auch die zweite Modulationsstufe werden verwendet

## Tabelle 14.1 (in der Abbildung)

Die Tabelle zeigt empfohlene Einstellungen für verschiedene Kombinationen von:

- Taktquelle (BRCLK) - z.B. ACLK bei 32,768 Hz oder SMCLK bei 1 MHz
- Gewünschte Baudrate - von 9600 bis 115200 bps
- Vorteiler (UCBRx) - Ganzzahliger Divisionsfaktor
- Überabtastungsmodus (UCOS16) - 0 oder 1
- Erste Modulationsstufe (UCBRF) - 0 bis 15
- Zweite Modulationsstufe (UCBRS) - Modulationsmuster

## Praktische Anwendung auf dem LaunchPad™

Auf dem MSP430FR2355 LaunchPad™:

- BRCLK kann nur die Werte ACLK oder 1 MHz (SMCLK) annehmen
- Die Tabelle zeigt Einstellungen für häufig verwendete Baudraten
- Bei 1 MHz SMCLK und 9600 Baud: UCBRx=6, UCOS16=1, UCBRF=8, UCBRS=0xF2

## Zusätzliche UART-Konfigurationshinweise

Die Abbildung erwähnt auch, dass:

- Viele UART-Rahmenoptionen werden in UCAxCTLW0 konfiguriert
- Der UCSYNC-Wert bestimmt den Kommunikationsmodus (0=asynchron, 1=synchron)
- Der UCMODEx-Wert wählt zwischen UART und anderen Modi
- Standardmäßig ist UCSYNC=0 und UCMODEx=0 (UART-Modus)

Dies zeigt die komplexe Natur der UART-Konfiguration im MSP430-System, die es ermöglicht, präzise Baudraten trotz der Einschränkungen der verfügbaren Taktquellen zu erreichen.



## Überblick über PIN-Konfiguration

Der MSP430FR2355 verfügt über mehrere eUSCI-Module (enhanced Universal Serial Communication Interface), die für verschiedene serielle Kommunikationsprotokolle wie UART, SPI und I²C verwendet werden können. Um einen PIN für eine bestimmte eUSCI-Funktion zu konfigurieren, müssen die PxSEL1- und PxSEL0-Register entsprechend eingestellt werden.
![[Pasted image 20250427165530.png]]
## eUSCI-Module des MSP430FR2355

Die Tabelle zeigt vier eUSCI-Module:
- **eUSCI_A0**: Pins P1.7 (Tx), P1.6 (Rx) für UART
- **eUSCI_A1**: Pins P4.3 (Tx), P4.2 (Rx) für UART
- **eUSCI_B0**: Pins P1.3 (SCL), P1.2 (SDA) für I²C
- **eUSCI_B1**: Pins P4.7 (SCL), P4.6 (SDA) für I²C

## PIN-Konfiguration

Für jeden PIN gibt es drei wichtige Aspekte:

1. **Physischer PIN**: z.B. P1.7, P4.3
2. **Funktionstyp**: UART (Tx/Rx), SPI (SIMO/SOMI/SCLK/STE), I²C (SCL/SDA)
3. **Register-Einstellungen**: Kombination aus PxSEL1 und PxSEL0

## Register-Einstellungen

Die Tabelle zeigt die genauen Werte für PxSEL1 und PxSEL0, die gesetzt werden müssen:

- Für UART/SPI/I²C-Funktion: PxSEL1=0, PxSEL0=1 (meistens)
- Standardeinstellung für digitale I/O: PxSEL1=0, PxSEL0=0

## Beispiel: UART-Konfiguration (eUSCI_A0)

Um die UART-Funktion für eUSCI_A0 zu konfigurieren:

1. Setze P1.7 als Tx: P1SEL1.7=0, P1SEL0.7=1
2. Setze P1.6 als Rx: P1SEL1.6=0, P1SEL0.6=1

In C-Code würde das so aussehen:

c

```c
// UART für eUSCI_A0 konfigurieren
P1SEL0 |= (BIT7 | BIT6);   // Setze P1SEL0.7 und P1SEL0.6 auf 1
P1SEL1 &= ~(BIT7 | BIT6);  // Setze P1SEL1.7 und P1SEL1.6 auf 0
```

## Zweistufiger Konfigurationsprozess

Die Tabelle erläutert auch den zweistufigen Konfigurationsprozess:

1. **Modulauswahl**: Wählen des eUSCI-Moduls durch Setzen der UCSYNC- und UCMODE-Bits im UCBxCTLW0-Register
2. **PIN-Konfiguration**: Konfigurieren der Pins durch Setzen der entsprechenden Bits in den PxSEL1- und PxSEL0-Registern

Dies ist eine wichtige Änderung gegenüber früheren MSP430-Modellen, bei denen die Standardeinstellung für viele Pins bereits für serielle Kommunikation konfiguriert war. Beim MSP430FR2355 müssen sowohl die Module als auch die Pins manuell konfiguriert werden.



## Übertragungsprozess nach Software-Reset
Nach Deaktivierung des Software-Resets (UCSWRST = 0) ist das eUSCI_Ax-Tx-Modul:

- Aktiviert und im Leerlaufzustand
- Wartebereit für zu übertragende Daten
- Die Baudraten-Generator-Logik ist bereit, aber nicht aktiv (keine Taktgeneration)
## Initiierung der Übertragung

1. Eine Übertragung beginnt durch Schreiben eines Bytes in den Übertragungspuffer (UCAxTXBUF).
2. Bei diesem Schreiben:
    - Wird der Datenwert in das Tx-Schieberegister kopiert
    - Startet der Baudraten-Generator mit der Takterzeugung
    - Beginnt die serielle Übertragung des Datenwerts

## UCTXIFG Flag (Übertragungsstatus)

- Das UCTXIFG-Flag zeigt den Status der Übertragung an
- Wenn UCTXIFG = 0: Daten werden gerade verschoben, keine neuen Daten sollten geschrieben werden
- Wenn UCTXIFG = 1: Neue Daten können in das UCAxTXBUF-Register geschrieben werden

## UCAxTXBUF Register-Details

Die Abbildung zeigt das UCAxTXBUF Register mit:

- Bits 15-8: Reserviert (nicht verwendet)
- Bits 7-0: UCTXBUFx - Daten, die auf die Übertragung warten

Das Register dient als Puffer zwischen der CPU und dem eigentlichen Schieberegister:

1. CPU schreibt Daten in UCAxTXBUF
2. Daten werden in das Schieberegister übertragen
3. Sobald die Übertragung beginnt, wird UCTXIFG = 1 gesetzt
4. Dies signalisiert, dass UCAxTXBUF bereit für neue Daten ist

Dieser Mechanismus ermöglicht eine kontinuierliche Datenübertragung ohne CPU-Engpässe, besonders in Kombination mit Interrupts. Wenn ein Byte übertragen wird, kann der Interrupt-Handler bereits das nächste Byte in den Puffer schreiben, wodurch eine ununterbrochene Datenübertragung gewährleistet wird.
![[Pasted image 20250427170355.png]]
![[Pasted image 20250427170517.png]]
![[Pasted image 20250427170546.png]]
![[Pasted image 20250427170553.png]]

## UART-Empfangssystem Komponenten

1. **Taktquelle und -auswahl (UCSSEL)**:
    - Konfiguriert durch UCAxCTLW0-Register
    - Auswahl zwischen ACLK (32,768 kHz) oder SMCLK (1 MHz)
    - Liefert den Basistakt (BRCLK) für den Baudraten-Generator
2. **Rx-Baudraten-Generator**:
    - Besteht aus zwei Hauptkomponenten: a) **Vorteiler/Divider** (UCAxBRW): Teilt den Basistakt b) **Modulator** (UCAxMCTLW): Feinabstimmung der Baudrate
    - Erzeugt den Überabtastungstakt für das Rx-Schieberegister
    - Typischerweise 16-fache Überabtastung des Datensignals
3. **Rx-Schieberegister**:
    - Besteht aus einer Kette von D-Flip-Flops
    - Nimmt die seriellen Daten vom UCAxRXD-Pin auf
    - Wandelt serielle Daten in parallele Daten um
4. **eUSCI_Ax Empfangspuffer (UCAxRXBUF)**:
    - Speichert die empfangenen parallelen Daten
    - Zugänglich für die CPU zum Auslesen
5. **Rahmenoptionen**:
    - Konfiguriert im UCAxCTLW0-Register
    - Bestimmt Datenbits (UC7BIT), Parität (UCPEN/UCPAR), Stoppbits (UCSPB)
6. **Rx-Zustandsmaschine**:
    - Überwacht das eingehende Signal
    - Erkennt Start- und Stoppbits
    - Steuert das Schieberegister und den Datentransfer
    - Erzeugt Statusflags und Interrupts:
        - UCRXIFG: Daten empfangen
        - UCBRK/UCFE/UCOE/UCPE: Fehlerzustände
        - UCIV: Interrupt-Vektor

## Funktionsablauf des Empfangsprozesses

1. **Einrichtung**:
    - Der Pin UCAxRXD wird über PxSEL1/PxSEL0-Register für UART-Funktion konfiguriert
    - Der Rx-Baudraten-Generator wird mit denselben Einstellungen wie der Tx konfiguriert
    - Überabtastung wird automatisch eingerichtet
2. **Empfangsvorgang**:
    - Die Rx-Zustandsmaschine überwacht den UCAxRXD-Pin kontinuierlich
    - Bei Erkennung eines Startbits (Übergang von 1 auf 0) wird der Empfangsprozess initiiert
    - Die Daten werden mit dem Überabtastungstakt in das Schieberegister eingelesen
    - Nach Empfang aller Bits (8 oder 7, je nach Konfiguration):
        - Wird das Stoppbit überprüft
        - Werden die Daten in UCAxRXBUF transferiert
        - Wird das UCRXIFG-Flag gesetzt
        - Wird ein Interrupt ausgelöst (falls aktiviert)
3. **Fehlerbehandlung**:
    - Die Zustandsmaschine erkennt verschiedene Fehlertypen:
        - Rahmenfehler (kein gültiges Stoppbit)
        - Paritätsfehler
        - Überlauffehler (neues Byte empfangen, bevor das vorherige gelesen wurde)
    - Bei Fehlern werden entsprechende Flags gesetzt

## Überabtastung für zuverlässige Kommunikation

Der Überabtastungsmechanismus ist ein zentraler Aspekt des UART-Empfängers:

- Das eingehende Signal wird 16-mal pro Bitperiode abgetastet
- Die Mitte jedes Bits wird ermittelt für optimale Signalintegrität
- Ermöglicht Toleranz gegenüber Taktabweichungen zwischen Sender und Empfänger

Durch diesen Aufbau kann der MSP430FR2355 zuverlässig serielle Daten empfangen, selbst wenn der sendende Gerät leicht abweichende Taktfrequenzen verwendet.
![[Pasted image 20250427171006.png]]
![[Pasted image 20250427171014.png]]


# Serial Peripheral Interface (SPI)
Das Serial Peripheral Interface (SPI) ist ein synchrones serielles Kommunikationsprotokoll, das für die Datenübertragung zwischen Mikrocontrollern und peripheren Geräten verwendet wird. Im Gegensatz zu UART verwendet SPI mehr Anschlusspins (mindestens drei), ermöglicht jedoch aufgrund der synchronen Natur der Verbindung höhere Datenübertragungsraten.
## Master-Slave-Architektur

SPI basiert auf einem Master-Slave-Konzept:

- Der Master erzeugt das Taktsignal (SCLK), das alle Geräte für die Datenübertragung verwenden
- Die Datenleitungen werden als SIMO (Slave In, Master Out) und SOMI (Slave Out, Master In) bezeichnet
- Manche Geräte verwenden alternative Bezeichnungen: MOSI und MISO
- Die MSP430-Dokumentation verwendet SIMO und SOMI
## Verbindungskonfiguration

Die einfachste Form der SPI-Verbindung wird als "Drei-Draht-Modus" bezeichnet und besteht aus:

1. SCLK (Serial Clock) - Taktleitung vom Master
2. SIMO (Slave In, Master Out) - Datenleitung vom Master zum Slave
3. SOMI (Slave Out, Master In) - Datenleitung vom Slave zum Master


![[Pasted image 20250504161125.png]]

## Datenübertragung
- Der Standard-SPI-Datenrahmen ist 8 Bit lang, wobei das niedrigwertigste Bit (LSB) zuerst gesendet wird
- Sowohl SPI-Tx als auch SPI-Rx-Geräte verwenden Schieberegister zur Übertragung des seriellen Bitstroms
- Bei der Übertragung werden die Daten an der steigenden Flanke von SCLK ausgeschoben
- Beim Empfang werden die Daten an der fallenden Flanke von SCLK eingelesen
- Wenn keine Übertragung stattfindet, befindet sich SCLK in einem Ruhezustand
- Diese Taktung ermöglicht es, dass die vom Empfänger verwendete Taktflanke innerhalb der Bitperiode der Datenbits zentriert ist

![[Pasted image 20250504161354.png]]

## SPI-Kommunikation mit mehreren Slaves
Wenn mehrere Slave-Geräte in einem SPI-System verwendet werden, erzeugt der Master eine Slave Transmit Enable (STE)-Leitung, um zu bestimmen, mit welchem Slave kommuniziert wird. Diese wird bei manchen SPI-Geräten auch als Slave Select (SS) bezeichnet.

## Topologien für Multi-Slave-Systeme

Es gibt zwei Haupttopologien für die Kommunikation mit mehreren Slaves:

### 1. Bus-Konfiguration
- SIMO- und SOMI-Leitungen werden zwischen Master und allen Slaves geteilt
- Jeder Slave erhält eine eigene STE-Leitung
- Nur ein Slave ist zu einem bestimmten Zeitpunkt aktiv
- Wenn mehr als eine STE-Leitung benötigt wird, empfiehlt die MSP430FR2355-Dokumentation die Verwendung von Port-Pins, um dedizierte STE-Leitungen zu erzeugen

### 2. Daisy-Chain-Konfiguration
- Geräte sind so verdrahtet, dass sie eine einzelne, kontinuierliche Datenschleife zwischen allen SPI-Geräten bilden
- Der Master zählt die Anzahl der aufgetretenen Takte, um zu verfolgen, wo in der Schleife sich die aktuellen Daten befinden
- Diese Anordnung ermöglicht eine effiziente Verkettung mehrerer Geräte mit weniger Steuerleitungen

Die SPI-Topologien, die STE-Leitungen verwenden, bieten unterschiedliche Vor- und Nachteile hinsichtlich Hardware-Komplexität, Softwareimplementierung und Übertragungseffizienz.

Die Bus-Konfiguration erfordert mehr GPIO-Pins (für die separate STE-Leitung jedes Slaves), bietet aber eine einfachere Steuerung und direkten Zugriff auf jeden Slave. Die Daisy-Chain-Konfiguration spart Hardware-Ressourcen, erfordert jedoch eine komplexere Bit-Timing-Steuerung und kann in einigen Anwendungen höhere Latenzzeiten aufweisen.


![[Pasted image 20250504161854.png]]
# SPI-Grundkonzept und Betrieb

## Grundlegendes Betriebskonzept

Das grundlegende Betriebskonzept des SPI-Systems besteht darin, dass wir es zunächst mit der gewünschten Bitrate und den Rahmencharakteristiken konfigurieren. Danach werden die zu übertragenden Daten in einen Tx-Puffer gespeichert, und ein Schieberegister sendet die Daten automatisch in einem seriellen Muster über den SIMO-Pin.

## Master-Funktion

Der Master sendet acht Taktübergänge auf SCLK, die jedem auf SIMO gesendeten Bit entsprechen. Im Drei-Pin-Modus wird STE nicht verwendet. Im Vier-Pin-Master-Modus kann der STE-Pin so konfiguriert werden, dass er entweder als aktiver High- oder Low-Ausgangsfreigabe für die Slaves fungiert.

## Interruptfunktionalität

Das SPI-Übertragungssystem kann auch einen Interrupt namens Transmit Interrupt (UCTXIFG) bereitstellen, der anzeigt, wenn der Tx-Puffer leer ist.

## Konfigurationsregister

Die SPI-Peripheriegeräte werden mit verschiedenen Registern konfiguriert, die mit der UART (oder I2C) Peripherie geteilt werden. Im SPI-Modus nehmen einige der Bitfelder innerhalb der Register unterschiedliche Funktionalitäten an. Dies ist besonders deutlich im UCAxCTLW0-Register, in dem viele der UART-Einstellungen nicht auf das SPI-Protokoll anwendbar sind.

Die vollständige Liste der SPI-Konfigurationsregister umfasst:

### 1. UCAxCTLW0 (eUSCI_Ax Control Word 0)

Dieses Hauptkonfigurationsregister steuert das Verhalten des SPI-Moduls mit folgenden wichtigen Bitfeldern im SPI-Modus:

- UCCKPH: Taktphasenauswahl (bestimmt, ob Daten an steigender oder fallender Flanke übertragen werden)
- UCCKPL: Taktpolarität (definiert den Ruhezustand des Taktsignals)
- UCMSB/UCLSB: Bestimmt, ob das MSB oder LSB zuerst gesendet wird
- UC7BIT/UC8BIT: Legt die Datenlänge fest (7 oder 8 Bit)
- UCMST: Konfiguriert das Gerät als Master oder Slave
- UCMODE: Wählt den SPI-Modus (3-Pin oder 4-Pin)
- UCSYNC: Muss für SPI auf 1 gesetzt werden (synchroner Modus)
- UCSWRST: Software-Reset-Bit zum Zurücksetzen des Moduls
### 2. UCAxBRW (eUSCI_Ax Bit Rate Control Word)
Steuert die Taktfrequenz des SPI-Busses:
- Wird verwendet, um den Takt zu teilen und die gewünschte Übertragungsrate einzustellen
- Berechnet als: SPI-Takt = Systemtakt / UCAxBRW
### 3. UCAxSTATW (eUSCI_Ax Status)
Statusregister, das den aktuellen Zustand des SPI-Moduls anzeigt:
- UCBUSY: Zeigt an, ob eine Übertragung läuft
- UCOE: Overrun-Error-Flag (wird gesetzt, wenn neue Daten empfangen werden, bevor alte gelesen wurden)
- UCFE: Framing-Error (im SPI-Modus normalerweise nicht verwendet)
### 4. UCAxRXBUF (eUSCI_Ax Receive Buffer)
Empfangspuffer, der die über SOMI empfangenen Daten enthält:
- Enthält die letzten vom Slave empfangenen 8 Bit Daten
- Lesezugriff auf dieses Register löscht das UCRXIFG-Flag
### 5. UCAxTXBUF (eUSCI_Ax Transmit Buffer)
Sendepuffer für zu übertragende Daten:
- Hier werden die 8 Bit Daten geschrieben, die über SIMO gesendet werden sollen
- Schreibzugriff auf dieses Register startet eine Übertragung
- Nach dem Schreiben wird das UCTXIFG-Flag gelöscht
### 6. UCAxIE (eUSCI_Ax Interrupt Enable)
Interrupt-Freigaberegister mit zwei relevanten Bits für SPI:
- UCTXIE: Aktiviert den Sende-Interrupt (wird ausgelöst, wenn der Tx-Puffer leer ist)
- UCRXIE: Aktiviert den Empfangs-Interrupt (wird ausgelöst, wenn neue Daten empfangen wurden)
### 7. UCAxIFG (eUSCI_Ax Interrupt Flag)
Interrupt-Flagregister, das den Status der Interrupts anzeigt:
- UCTXIFG: Sendeinterrupt-Flag (gesetzt, wenn der Tx-Puffer leer ist)
- UCRXIFG: Empfangsinterrupt-Flag (gesetzt, wenn neue Daten im Rx-Puffer verfügbar sind)
### 8. UCAxIV (eUSCI_Ax Interrupt Vector)
Interruptvektor-Register, das den Grund für einen Interrupt angibt:
- Enthält Codes, die anzeigen, ob der Interrupt durch TXIFG oder RXIFG ausgelöst wurde
- Wird in der Interrupt-Service-Routine verwendet, um den Interrupt-Grund zu bestimmen

## Initialisierungsschritte

Die empfohlene Reihenfolge der Schritte laut MSP430-Benutzerhandbuch zur Einrichtung der SPI-Peripherie ist:

1. Setzen des UCSWRST-Bits im UCAxCTLW0-Konfigurationsregister, um die eUSCI_Ax-Peripherie in einen Software-Reset zu versetzen
2. Initialisierung aller eUSCI_Ax-Konfigurationsregister
3. Konfiguration der Ports
4. Löschen von UCSWRST, um die eUSCI_Ax-Peripherie aus dem Reset-Zustand zu nehmen
5. Aktivieren von Interrupts (optional) im UCAxIE-Konfigurationsregister (UCRXIE oder UCTXIE)

![[Pasted image 20250504163156.png]]
![[Pasted image 20250504163304.png]]
![[Pasted image 20250504163316.png]]
![[Pasted image 20250504163326.png]]
# Datenempfang als SPI-Master
## Grundkonzept des Datenempfangs im Master-Modus

Wenn ein Gerät als SPI-Master konfiguriert ist und Daten über SOMI (Slave Out, Master In) empfängt, erzeugt der Master trotzdem die SCLK-Pulse, um die Daten aus dem Slave herauszuschieben und in den Master einzulesen. Diese Synchronisation ist ein zentrales Merkmal der SPI-Kommunikation.
## Empfangsprozess
Der Datenempfangsprozess verläuft wie folgt:
1. Die Daten werden durch ein Rx-Schieberegister empfangen
2. Nachdem alle Bits eingeschoben wurden, wird das Datenbyte in den RX-Puffer (UCAxRXBUF) verschoben
3. Das Rx-System verfolgt die eingehenden Daten und setzt das RXIFG-Flag im UCAxIFG-Register, wenn neue Daten im Puffer eingetroffen sind
4. Interrupts können durch das RXIFG ausgelöst werden, indem das RXIE-Bit im UCAxIE-Register aktiviert wird

## Erzeugung von Clock-Pulsen

Da der Master das SCLK-Signal generiert, muss er die notwendigen Taktimpulse an den Slave senden, damit der Slave seine Daten zurück in das Rx-Schieberegister des Masters schieben kann. Dies wird erreicht, indem ein Dummy-Byte (mit beliebigem Wert) in das Tx-Register des Masters geschrieben wird, um das System zu zwingen, acht SCLK-Pulse zu erzeugen.

## Praktisches Beispiel

In dem beschriebenen Beispiel wird der MSP430FR2355 LaunchPad™ verwendet, wobei der SIMO-Pin von eUSCI_A0 mit dem SOMI-Pin von eUSCI_A0 verbunden wird. Dies ermöglicht es, ein Byte Daten auf SIMO zu senden und zu beobachten, wie es acht Taktzyklen später im Rx-Puffer ankommt.

Obwohl dieses Beispiel etwas vereinfacht ist, veranschaulicht es, wie ein Master Daten von einem Slave anfordert, indem er in den Tx-Puffer schreibt und dann auf einen RXIFG-Interrupt wartet, der anzeigt, dass Daten im Rx-Puffer verfügbar sind.

## Testaufbau mit Push-Buttons

In diesem Design werden die Drucktastenschalter S1 und S2 verwendet, um verschiedene Datenbytes (0x10 und 0x66) vom Tx zum Rx zu senden:

- Wenn der Rx 0x10 empfängt, schaltet er LED1 um
- Wenn der Rx 0x66 empfängt, schaltet er LED2 um


# SPI-Slave-Betrieb auf dem MSP430FR2355

## Senden von Daten als SPI-Slave

Wenn ein Gerät als SPI-Slave arbeitet, muss es so konfiguriert werden, dass es mit den Systemeinstellungen des Masters übereinstimmt. Zu diesen Einstellungen gehören:

- Drei-Pin- vs. Vier-Pin-Modus
- STE-Polarität
- LSB vs. MSB zuerst
- 8-Bit vs. 7-Bit Datenrahmen
- Taktpolarität
- Taktphase

Das Gerät muss außerdem mit der UCMST-Einstellung in den Slave-Modus versetzt werden. Die Taktquelle und Bitrate müssen nicht konfiguriert werden, da der SCLK vom Master gesendet wird. Wenn der Mikrocontroller UCMST = 0 erkennt, weiß er, dass er den empfangenen SCLK verwenden soll, anstatt seinen eigenen Taktgenerator zu nutzen.

Das Senden als SPI-Slave besteht darin, Daten in den Tx-Puffer zu legen und dann zu warten, bis der Master acht SCLK-Impulse sendet, um die Daten herauszuschieben. Sobald Daten in den Tx-Puffer gelegt wurden, kann der Slave das TXFLG überwachen, um zu sehen, wann die Daten vollständig herausgeschoben wurden. Da der Slave den SCLK nicht steuert, weiß er nicht, wann die Daten herausgeschoben werden. Daher wird empfohlen, einen TXFLG-Interrupt zu verwenden, um anzuzeigen, dass die Daten übertragen wurden.

## Empfangen von Daten als SPI-Slave
Wenn ein Gerät als SPI-Slave konfiguriert ist, besteht das Empfangen von Daten darin, passiv zu warten, bis Daten in den Rx-Puffer geschoben wurden. Sobald ein vollständiger Datenrahmen eingetroffen ist, wird das RXFLG-Flag gesetzt. Als Slave ist dies die einzige Methode, die existiert, um anzuzeigen, dass Daten eingetroffen sind. Daher ist die Verwendung eines RXFLG-Interrupts, um den Empfang von Daten anzuzeigen, die effizienteste Möglichkeit, den SPI-Empfänger zu konfigurieren.



## Inter-integrated Circuit (I2C) Bus

- eine serielle Schnittstelle, die mit einer Zwei-Draht-Verbindung implementiert wird und mehrere Master sowie mehrere Slaves unterstützen kann.
- Ein I²C-Bus enthält eine Taktleitung (SCL = serieller Takt) und eine Datenleitung (SDA = serielle Daten).
- Eine I²C-Verbindung arbeitet immer im Halbduplex-Modus, was bedeutet, dass alle Geräte die Datenleitung gemeinsam nutzen, wobei jeweils nur ein Gerät zu einem bestimmten Zeitpunkt sendet.
- ![[Pasted image 20250520013242.png]]
- I2C Open-Drain Output Treiber: Erklärung:
	- Der I²C-Bus verwendet ein "Open-Drain" Ausgangskonzept, das auf einem NMOS-Transistor (n-type Metal Oxide Semiconductor Field Effect Transistor) basiert. Dieser Transistor funktioniert als spannungsgesteuerter Schalter mit folgenden Eigenschaften:
		- NMOS als Schalter:
			- Wenn die Gate-Spannung (Steueranschluss) auf VCC liegt: Transistor schaltet EIN
			- Wenn die Gate-Spannung auf GND (Masse) liegt: Transistor schaltet AUS
			- Im EIN-Zustand: Leitungspfad zwischen Source und Drain (Schalter geschlossen)
			- Im AUS-Zustand: Kein Leitungspfad zwischen Source und Drain (Schalter offen)
	- Aufbau und Funktion
		- In der Open-Drain Konfiguration:
			- Der Drain-Anschluss des NMOS wird mit der Signalleitung verbunden
			- Der Source-Anschluss wird mit GND (Masse) verbunden
		- Mit dieser Anordnung kann der Ausgang:
			- Die Signalleitung auf logisch LOW ziehen (durch Kurzschließen mit GND)
			- Die Signalleitung aber NICHT aktiv auf logisch HIGH ziehen
	- Pull-up Widerstand als Lösung
		- Um die Leitung auf HIGH zu bringen, wird ein Pull-up Widerstand verwendet:
			- Der Widerstand verbindet die Signalleitung mit VCC (Versorgungsspannung)
			- Wenn der NMOS-Transistor AUS ist, zieht der Pull-up Widerstand die Leitung auf HIGH
			- Wenn der NMOS-Transistor EIN ist, wird die Leitung auf LOW gezogen (der Pfad zur Masse hat einen geringeren Widerstand als der Pull-up Widerstand)
	- Vorteile für den I²C-Bus
		- Diese Konfiguration ermöglicht, dass mehrere Geräte dieselbe Signalleitung teilen können, ohne Konflikte zu erzeugen:
			- Jedes Gerät kann die Leitung nur auf LOW ziehen, aber nicht aktiv auf HIGH
			- Wenn ein Gerät LOW und ein anderes HIGH signalisieren möchte, gewinnt immer LOW (Wired-AND Logik)
			- Diese Anordnung verhindert Kurzschlüsse und Beschädigungen, die entstehen würden, wenn Geräte direkt gegeneinander arbeiten würden
## I²C Master-Slave-Konzept:
- Der I²C-Bus verwendet das Konzept von Mastern und Slaves für die Kommunikation. Der Master ist das Gerät, das die Kommunikation initiiert und den Takt kontrolliert. Ein I²C-Bus unterstützt auch mehrere Master. Jeder Slave auf dem Bus hat eine eindeutige und vorbestimmte Adresse, die als Slave-Adresse bezeichnet wird. Diese Adresse wird vom Master verwendet, um anzuzeigen, mit welchem Slave er kommunizieren möchte. Einige I²C-Geräte haben eine fest einprogrammierte Slave-Adresse, die nicht geändert werden kann. Andere Geräte stellen möglicherweise einen Teil einer fest einprogrammierten Slave-Adresse bereit und erlauben dem Benutzer, Pull-up- oder Pull-down-Widerstände an Pins anzuschließen, um die restlichen Bits der Slave-Adresse festzulegen. Wenn der Bus im Ruhezustand ist, werden sowohl SDA als auch SCL durch die Pull-up-Widerstände auf HIGH gehalten, und kein I²C-Gerät versucht zu kommunizieren. Wenn Geräte den Bus steuern, gilt er als beschäftigt (busy).
- I²C-Informationen werden in Nachrichten übertragen. Eine typische I²C-Nachricht beginnt mit einer START-Bedingung (S) und endet mit einer STOPP-Bedingung (P). Ein Master leitet eine neue Nachricht ein, indem er eine START-Bedingung (S) erzeugt, wobei SDA auf LOW gezogen wird, während SCL noch HIGH ist. Dies signalisiert jedem Gerät auf dem Bus, dass ein Master mit der Kommunikation beginnen möchte und sie sich bereit machen sollten. Sobald die START-Bedingung erzeugt wurde, wird SCL auf LOW gezogen und beginnt zu pulsen, um den Takt für die Nachricht bereitzustellen. Der Master ist für das Pulsen des Taktes verantwortlich. Der Master beendet eine Nachricht durch Erzeugen einer STOPP-Bedingung. Eine STOPP-Bedingung tritt auf, wenn es einen LOW-zu-HIGH-Übergang auf SDA gibt, während SCL HIGH ist. Sobald SDA auf HIGH geht, bleibt auch SCL HIGH, was anzeigt, dass der Bus wieder im Ruhezustand ist.
- Innerhalb einer Nachricht sind die Daten in Frames und Steuer-/Statussignale unterteilt. Jeder Taktimpuls innerhalb der I²C-Nachricht wird mit Perioden nummeriert. Der erste Taktimpuls nach Initiierung einer Nachricht wird als "Periode 1" bezeichnet. Der zweite Taktimpuls wird als "Periode 2" bezeichnet, und so weiter. Sowohl der Master als auch die Slaves zählen die Anzahl der Perioden, die seit dem Start der Nachricht aufgetreten sind, um zu wissen, wann bestimmte Frames und Signale auf dem Bus vorhanden sein sollten. Dies ist entscheidend, damit jedes Gerät weiß, wann es innerhalb der Nachricht kommunizieren darf. Dies verhindert, dass mehrere Geräte die SDA-Leitung zum falschen Zeitpunkt herunterziehen und eine Überstromsituation verursachen.
- **Nachrichtenstruktur im Detail**
	- Nachdem der Master die START-Bedingung erzeugt hat, sendet er zunächst die Slave-Adresse, mit der er kommunizieren möchte. I²C-Slave-Adressen können entweder 7 Bit (Standard) oder 10 Bit sein. Auf die Slave-Adresse folgt das Lese-/Schreibsignal, das angibt, welche Art von Transaktion in der Nachricht angefordert wird. Die START-Bedingung, die Slave-Adresse und das Lese-/Schreibsignal umfassen die Perioden 1-8.
	- Periode 9 der Nachricht ist für das Slave-Acknowledge (ACK) oder No-Acknowledge (NACK) Signal reserviert. Nachdem der Master die Slave-Adresse und das Lese-/Schreibsignal gesendet hat, überprüft jeder Slave auf dem Bus, ob er adressiert wird. Wenn ein Slave mit der angegebenen Slave-Adresse existiert, sendet er ein ACK-Signal zurück an den Master, indem er SDA auf LOW zieht. Wenn der Master das ACK-Signal sieht, weiß er, dass ein Slave mit der angegebenen Adresse existiert und fährt mit der Nachricht fort.
	- Wenn kein Gerät auf dem Bus mit der angegebenen Slave-Adresse existiert, wird kein Gerät SDA herunterziehen. Dies führt dazu, dass Periode 9 auf HIGH bleibt und als NACK interpretiert wird. Ein NACK in Periode 9 teilt dem Master mit, dass kein Slave mit der angegebenen Adresse existiert. Der Master erzeugt dann eine STOPP-Bedingung und beendet die Nachricht.
- **Datenübertragungsphase**
	- Nach einer erfolgreichen ACK-Bestätigung vom Slave werden die Daten dann 8 Bit auf einmal gesendet, beginnend mit dem MSB (Most Significant Bit).Nach dem Senden jedes Bytes sendet das empfangende Gerät ein ACK-Signal, das anzeigt, dass es die Daten erfolgreich empfangen hat.
	- Wenn der Master an einen Slave schreibt, sendet der Master die 8 Bits Daten und der Slave erzeugt das ACK/NACK-Signal.
	- Wenn der Master von einem Slave liest, sendet der Slave die 8 Bits Daten und der Master erzeugt das ACK/NACK-Signal.
	- Nachdem die Daten gesendet und bestätigt wurden, kann der Master die Nachricht beenden, indem er die STOPP-Bedingung erzeugt.
- ![[Pasted image 20250520015908.png]]
- ![[Pasted image 20250520061923.png]]
- Multiple bytes of data
- ![[Pasted image 20250520062009.png]]
- ![[Pasted image 20250520062249.png]]
- ![[Pasted image 20250520062514.png]]
- ![[Pasted image 20250520062849.png]]
- In situations where the slave contains multiple registers, the master can also write a block of data. This is handled by the slave by automatically incrementing its register address after each byte of data is written. The master still sends the slave address, the write signal, and the starting register address. The next byte of data that is sent goes into the first register address location. The slave then increments its register address. The next byte written by the master goes into the next register address. The slave will continue to increment its register address until it sees the STOP condition generated by the master. This allows the master to write a block of data to the registers within the slave while only providing the starting address of the register array.
- ![[Pasted image 20250520063155.png]]
- ![[Pasted image 20250520063232.png]]


## I2C Master Operationen
- ![[Pasted image 20250520064242.png]]
- eUSCI_B Register im I2C-Modus
	- - **UCBxCTLW0** (eUSCI_B Kontrollwort 0) – hat unterschiedliche Bitfelder im I2C-Modus
	- **UCBxCTLW1** (eUSCI_B Kontrollwort 1) – hat unterschiedliche Bitfelder im I2C-Modus
	- **UCBxBRW** (eUSCI_B Bitraten-Kontrollwort) – gleiche Funktion wie im SPI-Modus
	- **UCBxSTATW** (eUSCI_B Status) – hat unterschiedliche Bitfelder im I2C-Modus
	- **UCBxTBCNT** (eUSCI_B Bytezähler-Schwellwert)
	- **UCBxRXBUF** (eUSCI_B Empfangspuffer) – gleiche Funktion wie im SPI-Modus
	- **UCBxTXBUF** (eUSCI_B Sendepuffer) – gleiche Funktion wie im SPI-Modus
	- **UCBxI2COA0** (eUSCI_B I2C eigene Adresse 0)
	- **UCBxI2COA1** (eUSCI_B I2C eigene Adresse 1)
	- **UCBxI2COA2** (eUSCI_B I2C eigene Adresse 2)
	- **UCBxI2COA3** (eUSCI_B I2C eigene Adresse 3)
	- **UCBxADDRX** (eUSCI_B empfangene Adresse)
	- **UCBxADDMASK** (eUSCI_B Adressmaske)
	- **UCBxI2CSA** (eUSCI_B I2C Slave-Adresse)
	- **UCBxIE** (eUSCI_B Interrupt-Freigabe) – hat unterschiedliche Bitfelder im I2C-Modus
	- **UCBxIFG** (eUSCI_B Interrupt-Flag) – hat unterschiedliche Bitfelder im I2C-Modus
	- **UCBxIV** (eUSCI_B Interrupt-Vektor) – hat unterschiedliche Bitfelder im I2C-Modus
- **Writing Data as an I2C Master**
	- ### Initialisierung des I2C-Peripheriegeräts (Übersetzung und Erklärung)
		- Der erste Schritt bei der Einrichtung des I2C-Peripheriegeräts besteht darin, das System in einen Software-Reset zu versetzen, um zu vermeiden, dass während der Einrichtung fehlerhafte Daten übertragen werden. Dies geschieht durch Setzen des UCSWRST-Bits im eUSCI_Bx-Kontrollwort 0 (UCBxCTLW0)-Register. Nach einem Reset ist UCSWRST = 1, sodass sich eUSCI_Bx standardmäßig im Software-Reset befindet; es ist jedoch gute Praxis, dieses Bit explizit zu setzen, um sicherzustellen, dass das System deaktiviert ist.
		- ![[Pasted image 20250520064925.png]]
	-  **UCBxCTLW1-Register und automatische STOP-Bedingungsgenerierung**
		- Es gibt zusätzliche Konfigurationsbits für die Einrichtung eines grundlegenden I2C-Master-Transmitters im UCBxCTLW1-Register. Die am häufigsten verwendete Einstellung ist die automatische STOP-Bedingungsgenerierung (UCASTPx). Wenn UCASTPx = 10 ist, wird der Master automatisch die STOP-Bedingung generieren, sobald die gewünschte Anzahl von Datenbytes gesendet oder empfangen wurde.
		- ![[Pasted image 20250520065900.png]]
	-  **UCBxI2CSA (Slave-Adresse)**
		- Enthält die Adresse des Slave-Geräts, mit dem kommuniziert werden soll.
		- Wird im Master-Modus verwendet, um anzugeben, welchen Slave man adressieren möchte.
		- ![[Pasted image 20250520070438.png]]
	- **UCBxTBCNT (Bytezähler-Schwellwert)**
		- Definiert die Anzahl der Bytes, die automatisch übertragen/empfangen werden sollen.
		- Wird in Verbindung mit dem automatischen Stopp-Bedingungsmodus verwendet.
		- ![[Pasted image 20250520070457.png]]
	- **UCBxIE (Interrupt-Freigabe)**
		- Bestimmt, welche Ereignisse Interrupts auslösen können:
			- ![[Pasted image 20250520070544.png]]
	- **UCBxIFG (Interrupt-Flags)**
		- Zeigt an, welche Ereignisse aufgetreten sind und möglicherweise einen Interrupt ausgelöst haben:
			- ![[Pasted image 20250520070623.png]]
	- **UCBxIV (Interrupt-Vektor)**
		- Dieses Register enthält einen Vektorwert, der die höchste Priorität des ausstehenden Interrupts angibt.
		- Es wird in Interrupt-Serviceroutinen verwendet, um schnell die Ursache des Interrupts zu bestimmen.
		- Durch Lesen dieses Registers wird automatisch das Flag mit der höchsten Priorität gelöscht.
		- ![[Pasted image 20250520070723.png]]
- ![[Pasted image 20250520070757.png]]
- ![[Pasted image 20250520070938.png]]
- ![[Pasted image 20250520071045.png]]
## Reading Data as an I2C Master
- Beim Lesen von einem Slave folgen wir vielen der Initialisierungsschritte wie beim Senden. Wir konfigurieren weiterhin die Geschwindigkeit von SCL mit UCB0BRW, versetzen das Peripheriegerät mit UCMODEx in den I2C-Modus und machen es mit UCMST zu einem Master. Wir legen weiterhin die Slave-Adresse, mit der kommuniziert werden soll, in UCB0I2CA fest und geben die Anzahl der Bytes an, die vor einer automatischen STOPP-Bedingung übertragen werden sollen, mit UC0TBCNT. Der einzige Unterschied während der eUSCI_B0-Initialisierung für das Lesen besteht darin, das Peripheriegerät mit UCTR = 0 in den Empfangsmodus zu versetzen. Beim Lesen wird das UCRXIFG0-Flag gesetzt, wenn der Slave ein Datenbyte zurücksendet und es im Rx-Puffer ankommt. Dieses Flag löst einen eUSCI_B0-Interrupt aus. Innerhalb der eUSCI_B0-Serviceroutine speichern wir einfach den Rx-Pufferwert in einer Variable. Im Lesemodus erzeugt der Master nach dem letzten Byte in der Übertragung ein NACK-Signal, wie durch den Wert in UC0TBCNT vorgegeben. Betrachten wir ein Programm, das kontinuierlich ein Datenbyte von einem Slave mit der Slave-Adresse 0x68 liest. In diesem Programm werden wir kontinuierlich eine START-Bedingung erzeugen, indem wir UCTXSTT innerhalb der Hauptschleife setzen. Wir werden eine Rx-Interrupt-Serviceroutine verwenden, um den im Rx-Puffer empfangenen Wert zu lesen.
- ![[Pasted image 20250520071432.png]]
- ![[Pasted image 20250520071459.png]]
- ![[Pasted image 20250520071825.png]]
- Betrachten wir nun ein Beispiel für das Lesen von einer spezifischen Registeradresse innerhalb des Slave-Geräts. Zur Erinnerung: Dies wird durch das Senden von zwei Nachrichten erreicht; die erste ist eine Schreibnachricht, die die Registeradresse im Datenframe bereitstellt; die zweite ist eine Lesenachricht, die die Daten aus der angegebenen Registeradresse vom Slave zum Master überträgt. Es gibt verschiedene Möglichkeiten, dieses Design umzusetzen. Das vorgestellte Beispiel erzeugt die Start-Bedingungen für die beiden Nachrichten in der Haupt-while()-Schleife und überlässt dann der eUSCI_B0-Interrupt-Serviceroutine das Senden der Registeradresse während der Schreibnachricht und das Empfangen der Daten während der Lesenachricht. Bei diesem Ansatz muss zwischen den beiden Start-Bedingungen eine Funktionalität vorhanden sein, die wartet, bis die vorherige Nachricht abgeschlossen ist, bevor die nächste Nachricht gesendet werden kann. Dies wird durch Abfragen des STOP-Flags (UCSTPIFG) im UCB0IFG-Register erreicht. Dieses Flag wird gesetzt, sobald das Stopp-Bit für eine vollständige Nachricht erzeugt wurde.
## I2C Slave Operation
- Wenn ein MCU als I2C-Master fungiert, kann der MSP430FR2355 auch als I2C-Slave konfiguriert werden. Dies ermöglicht anderen I2C-Mastern, einige der Fähigkeiten des MCU zu nutzen, wie seine Timer, seinen ADC oder andere Peripheriegeräte. Die Konfiguration des MSP430FR2355 als Slave erfolgt durch Setzen von UCMODx = 11, um das Peripheriegerät in den I2C-Modus zu versetzen, und UCMST = 0, um es als Slave zu konfigurieren. Im Slave-Modus erzeugt der MCU kein SCL, daher ist keine Konfiguration von UCSSELx oder UCBRx erforderlich. Der MCU wird zunächst mit UCTR = 0 in den Empfangsmodus versetzt, um die I2C-Slave-Adresse zu empfangen, die der Master an alle Slaves sendet. Der MSP430FR2355 unterstützt bis zu vier separate und benutzerprogrammierbare Slave-Adressen. Jede dieser Slave-Adressen enthält unabhängige Interrupt-Flags für sowohl Tx als auch Rx. Die Slave-Adresswerte werden während der Initialisierung vom Benutzer in den eUSCI_Bx I2C Own Address n (UCBxI2COAn)-Registern gespeichert. Die vier spezifischen Registernamen im MSP430FR2355 sind UCBxI2CA3, UCBxI2CA2, UCBxI2CA1 und UCBxI2CA0. Jedes dieser Register enthält ein Own Address Enable (UCOAEN)-Bit an Position 10, das gesetzt sein muss, wenn das Slave-Adressregister aktiv sein soll. Das UCBxI2CA0-Register ist einzigartig, da seine 15. Position das General Call Response Enable (ECGEN) für das gesamte Slave-System des MCU ist. Die 15. Positionen in den anderen drei I2C-eigenen Adressregistern sind reserviert.
- ![[Pasted image 20250520072613.png]]
- ### General Call-Funktionalität
- Das ECGEN-Bit im UCBxI2CA0-Register ermöglicht dem Slave, auf General Call-Adressen (0x00) zu reagieren. Dies ist nützlich für:
	- Broadcast-Befehle an alle Geräte am Bus
	- Systemweite Reset- oder Konfigurationsbefehle
	- Synchronisierung mehrerer Slaves
- Im Slave-Modus wird, wenn die vom Master gesendete I2C-Slave-Adresse mit einem der Werte in einem aktivierten UCBxI2COAn-Register übereinstimmt, automatisch ein ACK gesendet und das UCSTTIFG-Flag gesetzt. Ob der MCU senden oder empfangen soll, wird automatisch durch Setzen des entsprechenden UCTXIFG- oder UCRXIFG-Flags im Slave konfiguriert (d.h. es ist nicht notwendig, UCTR manuell zu konfigurieren). Der Benutzer muss einfach nur innerhalb der eUSCI_B-Serviceroutine, abhängig von der Art der angeforderten Datenübertragung, den Tx- oder Rx-Puffer lesen oder beschreiben. Für eine Slave-Übertragung werden Daten in den Tx-Puffer gelegt und automatisch herausgeschoben. Der Master sendet ein ACK zurück, wenn er ein weiteres Byte empfangen möchte. Dieses ACK löst einen weiteren Sende-Interrupt aus, damit der MCU mehr Daten senden kann. Wenn der Master keine Daten mehr empfangen möchte, sendet er ein NACK gefolgt von der STOP-Bedingung, um die Nachricht zu beenden. Für einen Slave-Empfang schiebt der Master Daten in das Rx-Schieberegister. Nach Abschluss werden die Daten in den Rx-Puffer übertragen und das UCRXIFG wird gesetzt, was anzeigt, dass die Daten bereit sind, in eine interne Variable übertragen zu werden. Der Slave sendet dann ein ACK-Signal zurück an den Master.