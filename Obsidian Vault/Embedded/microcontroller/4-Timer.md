## Funktionsweise von Timern im Detail
![[Pasted image 20250326115259.png]]
- Ein Timer ist im Wesentlichen ein digitaler Zähler, der bei jeder steigenden Flanke eines Taktsignals (clk) inkrementiert wird. Bei den MSP430 Mikrocontrollern handelt es sich typischerweise um 16-Bit Timer, was bedeutet, dass sie Werte von 0 bis 65535 (0xFFFF in Hexadezimal) zählen können.
- **Taktquelle**
	- Die Timer können verschiedene Taktquellen nutzen:
		- SMCLK (Subsystem Master Clock) - typischerweise mit 1 MHz
		- ACLK (Auxiliary Clock) - typischerweise mit 32.768 kHz
		- INCLK (External Clock) - externer Takt über einen Pin
		- TBxCLK (Timer-spezifischer externer Takt)
	- Die Auswahl der Taktquelle erfolgt über das Timer Control Register (TBxCTL) im TBSSEL-Feld mit Bits 8-9.
- **Taktteiler (Prescaler)**
	- Der Timer verfügt über einen Prescaler, der den Eingangstakt teilen kann. Dies ermöglicht längere Zeitintervalle mit dem gleichen 16-Bit Zähler. Die Taktteiler-Optionen sind:
		- ID = 00: Teilen durch 1 (keine Teilung)
		- ID = 01: Teilen durch 2
		- ID = 10: Teilen durch 4
		- ID = 11: Teilen durch 8
	- **IDEX-Bits** im Timer Expansion Register (Bits 0-2):
		- 000: Teilen durch 1
		- 001: Teilen durch 2
		- 010: Teilen durch 3
		- 011: Teilen durch 4
		- 100: Teilen durch 5
		- 101: Teilen durch 6
		- 110: Teilen durch 7
		- 111: Teilen durch 8
	- Die effektive Teilung ergibt sich aus der Multiplikation beider Werte: Gesamtteilung = ID × IDEX
- ## Praktisches Beispiel
	- Nehmen wir an, wir haben einen MSP430-Mikrocontroller mit einem SMCLK (Subsystem Master Clock) von 1 MHz als Taktquelle für den Timer. Wir möchten den Timer so einstellen, dass er jede Sekunde einen Interrupt auslöst.
- ### Schritt 1: Berechnung des benötigten Teilungsfaktors
	Ohne Taktteiler würde der Timer bei jedem Takt (1 µs bei 1 MHz) um 1 inkrementiert werden:
	- Ein 16-Bit Timer (max. Wert 65535) würde nach ca. 65,5 ms überlaufen
	- Für 1 Sekunde benötigen wir aber eine Million Takte
- ### Schritt 2: Auswahl der Taktteiler-Einstellungen
	Wir könnten folgende Konfiguration wählen:
	- ID = 10 (Teilen durch 4)
	- IDEX = 111 (Teilen durch 8)
	- Gesamtteilung = 4 × 8 = 32
- ### Schritt 3: Berechnung des finalen Timer-Werts
	Mit dieser Teilung wird der Timer für jeden 32. Takt inkrementiert.
	- Neue Timer-Frequenz = 1 MHz ÷ 32 = 31,25 kHz
	- Für 1 Sekunde benötigen wir: 31.250 Timer-Inkremente
- Wir stellen also den Timer im Up-Modus ein und setzen den Vergleichswert (TBxCL0) auf 31250.
```
void configureTimer() {
    // Taktteiler auf ID=10 (÷4) und IDEX=111 (÷8) einstellen, Up-Modus
    TB0CTL = TBSSEL_2 | ID_2 | MC_1;  // TBSSEL_2: SMCLK als Quelle, ID_2: ÷4, MC_1: Up-Modus
    TB0EX0 = TBIDEX_7;                // TBIDEX_7: ÷8
    
    // Setze den Vergleichswert für 1 Sekunde
    TB0CCR0 = 31250 - 1;              // -1 weil der Timer von 0 zählt
    
    // Interrupt aktivieren
    TB0CCTL0 = CCIE;                  // Compare mode, interrupt enabled
}

// Interrupt-Service-Routine
#pragma vector=TIMER0_B0_VECTOR
__interrupt void TIMER0_B0_ISR(void) {
    // Code, der jede Sekunde ausgeführt werden soll
    P1OUT ^= BIT0;                    // LED an P1.0 umschalten
}
```
- Durch die Verwendung des Taktteilers haben wir erreicht, dass der Timer nicht so schnell zählt und damit längere Zeitintervalle (hier: 1 Sekunde) präzise messen kann, ohne den 16-Bit-Bereich zu überschreiten.
- **Binary Counter**
	- Der Binary Counter (Binärzähler) ist das Herzstück eines Timers:
		- Er ist ein digitaler Zähler, der bei jedem Taktimpuls (nach der Prescaler-Teilung) inkrementiert wird
		- Bei den MSP430-Timern handelt es sich um 16-Bit Counter, die Werte von 0 bis 65535 (0xFFFF) speichern können
		- Der aktuelle Zählerstand wird im Timer-Register (TAxR für Timer_A oder TBxR für Timer_B) gespeichert
		- Der Counter kann je nach Modus bis zu einem bestimmten Wert zählen und dann zurückgesetzt werden oder kontinuierlich durchlaufen
- **Compare Register**
	- Die Compare Register ermöglichen es, Aktionen auszulösen, wenn der Binary Counter bestimmte Werte erreicht:
		- Jeder Timer hat ein oder mehrere Compare Register (TAxCCRn für Timer_A oder TBxCCRn für Timer_B)
		- Das Compare Register 0 (TAxCCR0/TBxCCR0) hat eine besondere Bedeutung, da es im Up-Modus den maximalen Zählwert definiert
		- Der Mikrocontroller vergleicht kontinuierlich den Wert des Binary Counters mit den Werten in den Compare Registern
		- Wenn ein Match (Übereinstimmung) auftritt, kann ein Flag gesetzt werden (CCIFG - Capture/Compare Interrupt Flag)
		- Diese Flags können Interrupts auslösen oder per Polling abgefragt werden
```
TB0CCR0 = 50000;  // Timer zählt bis 50000 im Up-Modus
TB0CCTL0 |= CCIE; // Aktiviere Interrupt wenn TB0R == TB0CCR0
```
- **Overflow**
	- Der Overflow (Überlauf) ist ein spezieller Zustand des Binary Counters:
		- Ein Overflow tritt auf, wenn der Counter seinen maximalen Wert überschreitet und wieder bei 0 beginnt
		- Im Continuous Mode passiert dies, wenn der Zähler von 0xFFFF auf 0 wechselt
		- Im Up Mode passiert dies, wenn der Zähler den Wert im Compare Register 0 erreicht und auf 0 zurückgesetzt wird
		- Im Up/Down Mode gibt es keinen klassischen Overflow, sondern der Zähler wechselt bei Erreichen des Maximalwerts die Richtung
	- Beim Auftreten eines Overflows wird das TBIFG/TAIFG Flag (Timer_B/Timer_A Interrupt Flag) im Timer Control Register gesetzt. Dieses Flag kann:
		- Einen Interrupt auslösen, wenn der entsprechende Interrupt-Enable Bit (TBIE/TAIE) gesetzt ist
		- Per Software abgefragt werden (Polling)
```
	if (TB0CTL & TBIFG) {    // Überprüfe, ob ein Overflow aufgetreten ist
    P1OUT ^= BIT0;       // LED umschalten
    TB0CTL &= ~TBIFG;    // Flag zurücksetzen
}
```

## Zusammenspiel der Komponenten

Das Zusammenspiel dieser drei Komponenten ermöglicht vielfältige Timer-Funktionen:
1. Der **Binary Counter** zählt die Taktimpulse und hält die verstrichene Zeit fest
2. Die **Compare Register** vergleichen kontinuierlich ihren Wert mit dem Counter-Wert und lösen Aktionen aus, wenn eine Übereinstimmung gefunden wird
3. Der **Overflow** gibt an, wann der Counter einen kompletten Zyklus durchlaufen hat
Diese Funktionen werden für verschiedene Anwendungen genutzt:
- Präzise Zeitsteuerung
- Pulsweitenmodulation (PWM) für Motorsteuerung, LED-Dimmung, etc.
- Periodische Interrupt-Generierung
- Zeitmessung zwischen Ereignissen
- Implementierung von Kommunikationsprotokollen

## Timer_B
- **Grundstruktur des Timer_B**
	- Der Timer_B ist ein erweitertes Timer-Modul im MSP430F5529 Mikrocontroller und bietet mehr Funktionalität als der grundlegende Timer_A.  besteht das Timer_B-System des MSP430F5529 aus vier unabhängigen Timern:
		- **TB0**: Timer_B0 mit drei Capture/Compare-Registern (Timer0_B3)
		- **TB1**: Timer_B1 mit drei Capture/Compare-Registern (Timer1_B3)
		- **TB2**: Timer_B2 mit drei Capture/Compare-Registern (Timer2_B3)
		- **TB3**: Timer_B3 mit sieben Capture/Compare-Registern (Timer3_B7)
- ## Hardware-Architektur
	- Die Hardware-Architektur des Timer_B umfasst mehrere Schlüsselkomponenten:
		- Clock-Quellen und Clock-Multiplex (MUX):
			- Der Timer_B kann aus verschiedenen Taktquellen gespeist werden:
				- **TBxCLK** (00): Externer Takt über einen Pin
				- **ACLK** (01): Auxiliary Clock (typischerweise 32.768 kHz)
				- **SMCLK** (10): Subsystem Master Clock (typischerweise 1 MHz)
				- **INCLK** (11): Externer Takt durch einen anderen Pin
			- Die Auswahl erfolgt über das TBSSEL-Feld (Bits 8-9) im TBxCTL-Register.
		- ### Prescaler (Taktteiler)
			Der TimerB verfügt über ein zweistufiges Prescaler-System:
			1. **Erste Stufe (ID-Feld)**:
			    - ID = 00: Teilen durch 1
			    - ID = 01: Teilen durch 2
			    - ID = 10: Teilen durch 4
			    - ID = 11: Teilen durch 8
			2. **Zweite Stufe (IDEX-Feld im TBxEX0-Register)**:
			    - IDEX = 000: Teilen durch 1
			    - IDEX = 001: Teilen durch 2
			    - IDEX = 010: Teilen durch 3
			    - IDEX = 011: Teilen durch 4
			    - IDEX = 100: Teilen durch 5
			    - IDEX = 101: Teilen durch 6
			    - IDEX = 110: Teilen durch 7
			    - IDEX = 111: Teilen durch 8
			- Die effektive Teilung ist das Produkt beider Werte (ID × IDEX), was Teilungsfaktoren von 1 bis 64 ermöglicht.
		- **16-Bit Binary Counter**
			- Der Kernzähler des Timer_B ist ein 16-Bit-Zähler, der folgende Eigenschaften hat:
				-  Zählt von 0 bis 65535 (0xFFFF)
				- Der aktuelle Zählerstand wird im TBxR-Register gespeichert
				- Kann durch das TBCLR-Bit im TBxCTL-Register zurückgesetzt werden
				- Arbeitet in verschiedenen Modi (Stop, Up, Continuous, Up/Down)
		- **Capture/Compare-Register**
			- Jeder Timer_B hat mehrere Capture/Compare-Register (TBxCCRn):
				- TBxCCR0 hat eine besondere Bedeutung und definiert oft den Maximalwert im Up-Modus
				- Die Register können für zwei Hauptfunktionen verwendet werden:
					1. **Capture-Modus**: Speichert den aktuellen Zählerstand bei einem externen Ereignis
					2. **Compare-Modus**: Vergleicht kontinuierlich den Zählerstand mit einem festen Wert
		- Timer Overflow Tracking
			- Diese Einheit überwacht Überläufe des Timers und setzt entsprechende Flags:
				- Das TBIFG-Flag wird gesetzt, wenn ein Überlauf auftritt
				- Das TBIE-Bit kann aktiviert werden, um bei Überlauf einen Interrupt auszulösen
		- ## Betriebsmodi des Timer_B
			- Der Timer_B kann in vier verschiedenen Modi betrieben werden, die durch das MC-Feld (Bits 4-5) im TBxCTL-Register konfiguriert werden:
				### 1. Stop-Modus (MC = 00)
				- Der Timer ist angehalten
				- Nützlich zur Energieeinsparung, wenn der Timer nicht benötigt wird
				### 2. Up-Modus (MC = 01)
				- Der Timer zählt von 0 bis zum Wert in TBxCCR0
				- Bei Erreichen von TBxCCR0 wird das CCIFG-Flag in TBxCCR0 gesetzt
				- Der Zähler wird auf 0 zurückgesetzt und das TBIFG-Flag gesetzt
				- Ideal für regelmäßige Zeitintervalle und PWM-Erzeugung
				### 3. Continuous-Modus (MC = 10)
				- Der Timer zählt kontinuierlich von 0 bis 0xFFFF
				- Bei Überlauf (Wechsel von 0xFFFF zu 0) wird das TBIFG-Flag gesetzt
				- Nützlich für Zeitmessungen und unregelmäßige Ereignisse
				### 4. Up/Down-Modus (MC = 11)
				- Der Timer zählt von 0 bis zum Wert in TBxCCR0 und dann wieder zurück auf 0
				- Das CCIFG-Flag wird vor Erreichen des Maximalwerts gesetzt
				- Das TBIFG-Flag wird vor Erreichen von 0 gesetzt
				- Besonders geeignet für symmetrische PWM-Signale
		- ## Timer_B Control Register (TBxCTL)
			Das TBxCTL-Register ist das Hauptkonfigurationsregister für den Timer_B und enthält folgende wichtige Felder:
			- **TBCLGRP** (Bits 14-13): Timer_B Compare Latch Groupings
			- **CNTL** (Bits 12-11): Counter Length, bestimmt die Länge des Zählers (8, 10, 12 oder 16 Bit)
			- **TBSSEL** (Bits 9-8): Timer_B Clock Source Select (TBCLK, ACLK, SMCLK, INCLK)
			- **ID** (Bits 7-6): Input Divider (Taktteiler: /1, /2, /4, /8)
			- **MC** (Bits 5-4): Mode Control (Stop, Up, Continuous, Up/Down)
			- **TBCLR** (Bit 2): Timer_B Clear, setzt den Zähler zurück
			- **TBIE** (Bit 1): Timer_B Interrupt Enable
			- **TBIFG** (Bit 0): Timer_B Interrupt Flag
		- ## Timer_B Expansion Register 0 (TBxEX0)
			Das TBxEX0-Register bietet zusätzliche Konfigurationsmöglichkeiten, insbesondere für den erweiterten Taktteiler:
			- **IDEX** (Bits 2-0): Input Divider Expansion (zusätzlicher Taktteiler: /1 bis /8)
```
//Präzise Zeitsteuerung
TB0CTL = TBSSEL_2 | ID_3 | MC_1;  // SMCLK, /8, Up-Modus
TB0EX0 = TBIDEX_7;               // Zusätzlich /8 = Gesamt /64
TB0CCR0 = 15625 - 1;             // 1 MHz / 64 = 15625 Takte für 1 Sekunde
TB0CCTL0 = CCIE;                 // Compare-Interrupt aktivieren
```
```
//PWM-Generierung
TB0CTL = TBSSEL_2 | MC_1;       // SMCLK, Up-Modus
TB0CCR0 = 1000 - 1;             // PWM-Periode
TB0CCR1 = 500;                  // 50% Duty Cycle
TB0CCTL1 = OUTMOD_7;            // Reset/Set Ausgangsmodus
```
![[Pasted image 20250326123446.png]]
![[Pasted image 20250326123651.png]]![[Pasted image 20250326123942.png]]
![[Pasted image 20250326124323.png]]
![[Pasted image 20250326124335.png]]![[Pasted image 20250326124356.png]]
![[Pasted image 20250326125620.png]]
1. **Timer Clock**: Das Taktsignal, das den Timer antreibt
2. **Timer**: Der aktuelle Zustand des Timers, der zwischen verschiedenen Werten wechselt:
    - TBCL0-1 (kurz vor dem Maximalwert)
    - TBCL0 (Maximalwert)
    - 0h (Null)
    - 1h (fortschreitender Zählerstand)
3. **Set TBxCTL TBIFG**: Zeigt, wann das Timer_B Interrupt Flag gesetzt wird
    - Das blaue Oval markiert, wann das TBIFG-Flag gesetzt wird (beim Überlauf von TBxCL0 auf 0)
4. **Set TBxCCR0 CCIFG**: Zeigt, wann das Capture/Compare Interrupt Flag gesetzt wird
    - Das gelbe Oval markiert, wann das CCIFG-Flag gesetzt wird (beim Erreichen von TBxCL0)
Die roten und blauen Linien mit Pfeilen verdeutlichen den Zusammenhang zwischen:
- Dem Erreichen des Maximalwerts im oberen Diagramm und dem Setzen des CCIFG-Flags (rote Linie)
- Dem Überlauf/Zurücksetzen auf 0 und dem Setzen des TBIFG-Flags (blaue Linie)
![[Pasted image 20250326130005.png]]
![[Pasted image 20250326130529.png]]## CCIFG (Capture/Compare Interrupt Flag):

- Das CCIFG Flag (in TBxCCRn) wird **vor** dem Erreichen des Maximalwerts gesetzt
- In der Abbildung ist dies mit einem roten Kreis markiert, wo das "Set TBxCCR0 CCIFG" Signal ansteigt
- Zeitlich passiert dies beim Hochzählen, kurz bevor der Timer seinen Maximalwert (TBxCL0/TBxCCR0) erreicht
- Dies unterscheidet sich vom Up-Modus, wo das CCIFG genau beim Erreichen des Maximalwerts gesetzt wird
## TBIFG (Timer_B Interrupt Flag):
- Das TBIFG Flag (in TBxCTL) wird **vor** dem Erreichen der 0 gesetzt
- In der Abbildung ist dies mit einem blauen Kreis markiert, wo das "Set TBxCTL TBIFG" Signal ansteigt
- Zeitlich passiert dies beim Herunterzählen, kurz bevor der Timer wieder auf 0 zurückgeht
- Dies erfolgt während der Abwärtszählphase des Timers
<mark style="background: #FFB86CA6;">Der Up/Down Mode bietet also zwei präzise definierte Zeitpunkte für Interrupt-Generierung</mark>:
1. Kurz vor dem Erreichen des Maximalwerts (CCIFG)
2. Kurz vor dem Erreichen von 0 (TBIFG)

![[Pasted image 20250326130932.png]]
![[Pasted image 20250326131132.png]]
## Timer_A
- Timer_A ist ein 16-bit Timer/Counter, der in praktisch allen MSP430-Mikrocontrollern vorhanden ist. Er bietet im Vergleich zu anderen Timer-Modulen wie Timer_B eine feste Timerlänge von 16 Bit und verfügt typischerweise über bis zu 7 Capture/Compare-Register.
- ## Betriebsmodi
	- Timer_A unterstützt vier Hauptbetriebsmodi, die im TAxCTL Register (Timer_A Control Register) konfiguriert werden:
		1. **Stop-Modus (MC = 00)**: Der Timer ist angehalten.
		2. **Up-Modus (MC = 01)**: Der Timer zählt wiederholt von 0 bis zum Wert in TAxCCR0.
		3. **Continuous-Modus (MC = 10)**: Der Timer zählt kontinuierlich von 0 bis 0xFFFF und beginnt dann wieder bei 0.
		4. **Up/Down-Modus (MC = 11)**: Der Timer zählt von 0 bis zum Wert in TAxCCR0 und dann wieder zurück auf 0.
- ![[Pasted image 20250326133724.png]]
- ![[Pasted image 20250326133757.png]]
- ![[Pasted image 20250326133829.png]]
- ## Timer_A Register
	- Die wichtigsten Register zur Steuerung von Timer_A sind:
		1. **TAxCTL (Timer_A Control Register)**: Steuert die Taktquelle, den Taktteiler, den Betriebsmodus und die Interrupts.
		2. **TAxR (Timer_A Register)**: Enthält den aktuellen Zählwert des Timers.
		3. **TAxCCRn (Capture/Compare Register n)**: Wird für Capture- oder Compare-Operationen verwendet.
		4. **TAxCCTLn (Capture/Compare Control Register n)**: Steuert die Capture/Compare-Funktionen.
		5. **TAxEX0 (Timer_A Expansion Register 0)**: Bietet zusätzliche Taktteiler-Optionen.
	- Die wichtigsten Felder des TACTL-Registers sind:
		1. **TASSEL (Bits 9-8)**: Timer_A-Taktquellenauswahl
		    - 00b = TACLK (externe Taktquelle)
		    - 01b = ACLK (Hilfstakt, typ
		    - ischerweise 32,768 kHz)
		    - 10b = SMCLK (Submain-Takt, typisch 1 MHz)
		    - 11b = INCLK (externe Taktquelle)
		2. **ID (Bits 7-6)**: Eingangstaktteiler
		    - 00b = Teilen durch 1
		    - 01b = Teilen durch 2
		    - 10b = Teilen durch 4
		    - 11b = Teilen durch 8
		3. **MC (Bits 5-4)**: Mode Control - bestimmt den Betriebsmodus des Timers
		    - 00b = Stop-Modus (Timer angehalten)
		    - 01b = Up-Modus (Timer zählt von 0 bis TACCR0)
		    - 10b = Continuous-Modus (Timer zählt von 0 bis 0xFFFF)
		    - 11b = Up/Down-Modus (Timer zählt von 0 bis TACCR0 und zurück zu 0)
		4. **TACLR (Bit 2)**: Timer_A Clear - Setzt den Timer zurück
		    - Das Setzen dieses Bits löscht TAR, die Taktteiler-Logik und die Zählrichtung
		    - Wird automatisch zurückgesetzt und immer als 0 gelesen
		5. **TAIE (Bit 1)**: Timer_A Interrupt Enable
		    - 0 = Interrupt deaktiviert
		    - 1 = Interrupt aktiviert
		6. **TAIFG (Bit 0)**: Timer_A Interrupt Flag
		    - 0 = Kein Interrupt anstehend
		    - 1 = Interrupt anstehend
	- ![[Pasted image 20250326134047.png]]
	- ![[Pasted image 20250326134207.png]]
	- ![[Pasted image 20250326134229.png]]

## Unterschiede zwischen Timer_A, Timer_B und Timer_D im MSP430
## Hauptunterschiede
### Timer_A
- In fast allen MSP430-Controllern vorhanden
- 16-bit Timer/Counter
- Bis zu 7 Capture/Compare-Register
- Feste Timerlänge (immer 16-bit)
- Grundlegende Timer-Funktionalität
### Timer_B
- Nicht in allen MSP430-Controllern verfügbar
- 16-bit Timer/Counter
- Mehrere unabhängige Timer (TB0, TB1, TB2, TB3)
- Variable Anzahl an Capture/Compare-Registern pro Timer
    - TB0, TB1, TB2: je 3 Register (Timer0_B3, Timer1_B3, Timer2_B3)
    - TB3: 7 Register (Timer3_B7)
- Aktueller Timerstand in TBxR
- Maximale Länge ebenfalls 16 bit
### Timer_D
- Nur in wenigen spezialisierten MSP430-Modellen verfügbar
- 16-bit Timer mit mehreren Capture/Compare-Registern
- Bietet zusätzliche Funktionen:
    - High-Resolution Mode
    - Externe Steuerungsmöglichkeiten
    - Synchronisierung mit anderen Timern
- Besonders geeignet für präzise Timing-Anwendungen und PWM-Erzeugung

## Wann welchen Timer verwenden?
- **Timer_A**: Für einfache Timing-Aufgaben, Verzögerungen, grundlegende PWM.
- **Timer_B**: Wenn mehrere unabhängige Timer benötigt werden oder mehr Capture/Compare-Register als bei Timer_A verfügbar sind.
- **Timer_D**: Für Anwendungen, die hochpräzises Timing erfordern, wie präzise Motorsteuerung, Digital-zu-Analog-Umwandlung oder wenn eine Synchronisation mit anderen Timern notwendig ist.



## Watchdog Timer 
Seine Hauptaufgabe ist es, das System bei Fehlfunktionen oder Software-Hängern automatisch zurückzusetzen.
## Grundlegende Funktionsweise
Der Watchdog Timer ist im Grunde ein Zähler, der kontinuierlich hochzählt. Wenn dieser Zähler seinen maximalen Wert erreicht und überläuft, löst er einen Systemreset aus (PUC - Power-Up Clear). Im normalen Betrieb muss die Software den Watchdog regelmäßig zurücksetzen ("füttern"), bevor er überläuft, um anzuzeigen, dass das System ordnungsgemäß funktioniert.

## Watchdog Control Register (WDTCTL)
Das Watchdog Control Register (WDTCTL) ist ein 16-bit Register, das zur Konfiguration und Steuerung des Watchdog Timers verwendet wird. Seine Struktur ist wie folgt:
![[Pasted image 20250326135210.png]]
**WDTPW (Bits 15-8)**: Watchdog-Passwort. Dieses Feld muss mit dem Wert 0x5A beschrieben werden, bevor andere Bits im Register geändert werden können. Jeder andere Wert führt zu einem sofortigen PUC (Power-Up Clear/Reset).

**WDTHOLD (Bit 7)**: Stoppt den Watchdog Timer, wenn auf 1 gesetzt.
- 0: Watchdog Timer läuft
- 1: Watchdog Timer ist angehalten

**WDTSSEL (Bits 6-5)**: Auswahl der Taktquelle für den Watchdog Timer.
- 00: SMCLK (typisch 1 MHz)
- 01: ACLK (typisch 32.768 kHz)
- 10: VLOCLK (Very Low Frequency Oscillator)
- 11: X_CLK (externer Takt)

**WDTTMSEL (Bit 4)**: Auswahl des Betriebsmodus.
- 0: Watchdog-Modus (Reset bei Überlauf)
- 1: Interval-Timer-Modus (Interrupt bei Überlauf)

**WDTCNTCL (Bit 3)**: Zurücksetzen des Zählers.
- Das Setzen dieses Bits auf 1 setzt den Zähler auf 0 zurück
- Das Bit wird automatisch zurückgesetzt

**WDTIS (Bits 2-0)**: Auswahl des Zeitintervalls für den Watchdog Timer. Die Intervalle variieren je nach MSP430-Modell, typischerweise:

- 000: Watchdog-Takt / 32768 (ca. 1s bei 32.768 kHz)
- 001: Watchdog-Takt / 8192 (ca. 250ms bei 32.768 kHz)
- 010: Watchdog-Takt / 512 (ca. 16ms bei 32.768 kHz)
- 011: Watchdog-Takt / 64 (ca. 2ms bei 32.768 kHz)
- 100: Watchdog-Takt / 1 (1s bei 1 MHz SMCLK)
- 101: Watchdog-Takt / 256 (250ms bei 1 MHz)
- 110: Watchdog-Takt / 16384 (16ms bei 1 MHz)
- 111: Watchdog-Takt / 1048576 (ca. 1ms bei 1 MHz)
```
WDTCTL = WDTPW | WDTHOLD; // Passwort (0x5A) und HOLD-Bit setzen
```

