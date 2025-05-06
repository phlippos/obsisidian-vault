

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