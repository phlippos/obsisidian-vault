![[Pasted image 20250309203052.png]]
### Input Register (PxIN)
- Das Input Register (PxIN) ist eines der wichtigsten Konfigurationsregister für die I/O-Ports des MSP430-Mikrocontrollers. Es dient zum Lesen des Zustands der Eingangspins.
- Eigenschaften des PxIN Registers:
	-  **Funktionsweise**: Liest den aktuellen elektrischen Zustand der Pins
	- **Bit = 0**: Der entsprechende Pin ist auf niedrigem Pegel (LOW/0V)
	- **Bit = 1**: Der entsprechende Pin ist auf hohem Pegel (HIGH/VCC)
	- **Typ**: Read-only (R) - kann nur gelesen, nicht beschrieben werden
	- **Reset-Wert**: Undefiniert (abhängig vom Zustand der Pins beim Reset)
- Anwendungsbeispiel:
	- if (P1IN & 0x02) // button (P1.1, low active) not pressed?
	- Diese Abfrage prüft, ob der Taster an Pin P1.1 **nicht** gedrückt ist:
		- `0x02` entspricht binär `00000010`, testet also Bit 1 (P1.1)
		- Die Tasterverbindung ist "low active" - wenn der Taster gedrückt wird, wird der Pin auf LOW gezogen
		- Wenn P1.1 = 1 (HIGH), ist der Taster nicht gedrückt
		- Wenn P1.1 = 0 (LOW), ist der Taster gedrückt
```
		// Wenn Taster (low active) gedrückt ist 
		if (!(P1IN & 0x02)) {
		 // Taster ist gedrückt, führe Aktion aus 
		}
		// Alternativ: Wenn Taster (high active) gedrückt ist 
		if (P1IN & 0x02) { 
		// Taster ist gedrückt, führe Aktion aus
		}
```
```
// Prüfen, ob sowohl P1.0 als auch P1.2 HIGH sind
if ((P1IN & 0x05) == 0x05) {
    // Beide Pins sind HIGH
}
```
- Was repräsentieren die Werte?
	- `P1IN` ist das Eingangsregister für Port 1 des MSP430. Es enthält den aktuellen Zustand aller 8 Pins dieses Ports.
	- `0x02` ist eine hexadezimale Konstante, die in binärer Form `00000010` entspricht.
- Die bitweise UND-Operation (&)
	- Beim bitweisen UND werden nur die Bits im Ergebnis auf 1 gesetzt, die in beiden Operanden 1 sind.
	- Alle anderen Bits werden auf 0 gesetzt.
- Was passiert beim Ausführen?
	- ![[Pasted image 20250309204318.png]]
- Das Ergebnis
	-  Das Resultat ist nur dann ungleich Null (also wahr in einer if-Abfrage), wenn P1.1 auf HIGH ist (Bit = 1)
	- Wenn P1.1 auf LOW ist (Bit = 0), wird das Resultat Null sein
	- //
		- ![[Pasted image 20250309204415.png]]
		- ![[Pasted image 20250309204422.png]]
	- Diese Operation wird typischerweise verwendet, um den Zustand eines bestimmten Pins zu überprüfen, ohne die anderen Pins zu berücksichtigen. In diesem Fall wird überprüft, ob der Pin P1.1 (der zweite Pin von Port 1) HIGH ist, also ob der Taster nicht gedrückt ist.
	- #### low active
		- Bei einem Low-Active-Gerät oder -Signal:
			- Der **aktive** Zustand wird durch ein **logisches LOW** (0, GND, 0V) repräsentiert
			- Der **inaktive** Zustand wird durch ein **logisches HIGH** (1, VCC, 3.3V/5V) repräsentiert
		- Ein Low-Active-Taster ist so verdrahtet, dass er im nicht gedrückten Zustand auf HIGH gezogen wird (durch einen Pull-up-Widerstand) und beim Drücken mit GND verbunden wird, was den Pin auf LOW zieht.
			- ![[Pasted image 20250309204628.png]]
			- ![[Pasted image 20250309204654.png]]
	- #### high active
		- Bei einem High-Active-Gerät oder -Signal:
			- Der **aktive** Zustand wird durch ein **logisches HIGH** (1, VCC, 3.3V/5V) repräsentiert
			- Der **inaktive** Zustand wird durch ein **logisches LOW** (0, GND, 0V) repräsentiert
		- Ein High-Active-Taster ist so verdrahtet, dass er im nicht gedrückten Zustand auf LOW gezogen wird (durch einen Pull-down-Widerstand) und beim Drücken mit VCC verbunden wird, was den Pin auf HIGH zieht.
			- ![[Pasted image 20250309204806.png]]
			- ![[Pasted image 20250309204813.png]]
	- Warum verwendet man Low-Active oder High-Active?
		- Low-Active-Vorteile:
			- Bessere Rauschimmunität in vielen Umgebungen
			- Einfachere Implementierung mit Pull-up-Widerständen
			- Standard für viele Mikrocontroller-Interrupt-Eingänge
		- High-Active-Vorteile:
			- Intuitiver zu verstehen (HIGH = AN)
			- Direkter Vergleich mit Versorgungsspannung
			- In manchen Schaltungen einfacher zu implementieren

### Direction Register (PxDIR)
- Das PxDIR-Register (Port x Direction Register) ist ein grundlegendes Konfigurationsregister für die GPIO-Pins (General Purpose Input/Output) des Mikrocontrollers. Es bestimmt die Datenrichtung jedes einzelnen Pins eines Ports.
- Eigenschaften:
	- Bitbreite: 8 Bit (0-7)
	- Zugriffstyp: RW (Read/Write - Lesen/Schreiben)
	- Standardzustand nach Reset: 0h (alle Bits auf 0 gesetzt)
	- Adressierung: Für jeden Port gibt es ein eigenes DIR-Register (P1DIR, P2DIR, usw.)
- Funktionsweise:
	- Bit = 0: Der entsprechende Pin wird als Eingang (Input) konfiguriert
		- Der Pin kann nun externe Signale einlesen
		- Die interne Ausgangsstufe ist deaktiviert
		- Der Zustand kann über das PxIN-Register gelesen werden
	- Bit = 1: Der entsprechende Pin wird als Ausgang (Output) konfiguriert
		- Der Pin kann nun Signale ausgeben
		- Der Ausgangswert wird über das PxOUT-Register gesteuert
		- Der interne Pullup/Pulldown-Widerstand hat keine Auswirkung mehr
- Bei der MSP430-Familie ist zu beachten, dass nach einem Reset alle Pins standardmäßig als Eingänge konfiguriert sind (alle PxDIR-Bits = 0). Dies ist eine Sicherheitsmaßnahme, um Kurzschlüsse oder unbeabsichtigte Signalausgaben beim Systemstart zu vermeiden.
- Die Konfiguration der GPIO-Pins erfolgt typischerweise in der Initialisierungsphase des Programms, bevor die eigentliche Hauptschleife (main loop) beginnt.
```
Einzelne Pins konfigurieren
P1DIR |= 0x01;      // Konfiguriert P1.0 als Ausgang
P1DIR |= 0x03;      // Konfiguriert P1.0 und P1.1 als Ausgänge (0x03 = 0b00000011)
P2DIR |= 0x80;      // Konfiguriert P2.7 als Ausgang (0x80 = 0b10000000)
P3DIR &= ~0x20;     // Konfiguriert P3.5 als Eingang (setzt Bit 5 auf 0)
```
```
Mehrere Pins gleichzeitig konfigurieren
P1DIR = 0xFF;       // Alle Pins von Port 1 als Ausgänge konfigurieren (0xFF = 0b11111111)
P2DIR = 0x00;       // Alle Pins von Port 2 als Eingänge konfigurieren
P3DIR = 0xF0;       // P3.4-P3.7 als Ausgänge, P3.0-P3.3 als Eingänge (0xF0 = 0b11110000)
```
```
Bitmasken verwenden
#define LED_ROT     BIT0    // BIT0 entspricht 0x01 oder 0b00000001
#define LED_GRUEN   BIT1    // BIT1 entspricht 0x02 oder 0b00000010
#define TASTER      BIT3    // BIT3 entspricht 0x08 oder 0b00001000

P1DIR |= (LED_ROT | LED_GRUEN);   // Konfiguriert LEDs als Ausgänge
P1DIR &= ~TASTER;                 // Konfiguriert Taster als Eingang
```


### Output Register (PxOUT)
- Das PxOUT-Register hat eine doppelte Funktion, abhängig davon, ob die entsprechenden Pins als Ausgänge oder Eingänge konfiguriert sind:
- Bei Ausgängen (Output-Modus):
	-  Bit = 0: Der Ausgang wird auf logisch Low gesetzt (0V)
	- Bit = 1: Der Ausgang wird auf logisch High gesetzt (VCC, typischerweise 3,3V oder 1,8V)
- Bei Eingängen (Input-Modus) mit aktivierten Pull-up/Pull-down Widerständen:
	- Bit = 0: Der interne Pull-down-Widerstand wird aktiviert (Pin wird zu GND gezogen)
	- Bit = 1: Der interne Pull-up-Widerstand wird aktiviert (Pin wird zu VCC gezogen)
- Die technischen Eigenschaften des Registers:
	- Bitbreite: 8 Bit (0-7)
	- Zugriffstyp: RW (Read/Write - Lesen/Schreiben)
	- Standardzustand nach Reset: Undefiniert
- Es ist wichtig zu beachten, dass für die korrekte Funktion der Pull-up/Pull-down-Widerstände:
	- Der entsprechende Pin als Eingang konfiguriert sein muss (PxDIR = 0)
	- Das entsprechende Bit im PxREN-Register (Resistor Enable) auf 1 gesetzt sein muss
	- Dieser Mechanismus ist besonders nützlich für Taster, Schalter und andere Eingabegeräte, um einen definierten Signalpegel auch bei offenem Kontakt sicherzustellen.
```
LEDs steuern
// Einzelne LEDs ein- und ausschalten
P1OUT |= BIT0;                // LED an P1.0 einschalten (High)
P1OUT &= ~BIT1;               // LED an P1.1 ausschalten (Low)
P1OUT ^= BIT2;                // LED an P1.2 umschalten (Toggle)

// Mehrere LEDs gleichzeitig steuern
#define LED_MASK (BIT0 | BIT1 | BIT2)
P1OUT |= LED_MASK;            // Alle LEDs einschalten
P1OUT &= ~LED_MASK;           // Alle LEDs ausschalten
```
```
Pull-up/Pull-down-Widerstände für Eingänge
// Taster mit Pull-up-Widerstand
P1DIR &= ~BIT3;               // P1.3 als Eingang konfigurieren
P1REN |= BIT3;                // Widerstand für P1.3 aktivieren
P1OUT |= BIT3;                // Pull-up für P1.3 auswählen

// Taster mit Pull-down-Widerstand
P2DIR &= ~BIT4;               // P2.4 als Eingang konfigurieren
P2REN |= BIT4;                // Widerstand für P2.4 aktivieren
P2OUT &= ~BIT4;               // Pull-down für P2.4 auswählen
```
```
Binäre Zahlen ausgeben

void outputBinary(uint8_t value) {
    P1OUT &= 0xF0;            // Untere 4 Bits löschen
    P1OUT |= (value & 0x0F);  // Neue Werte für untere 4 Bits setzen
}

// Verwendung:
outputBinary(5);              // Setzt P1.0 und P1.2 auf High (binär 0101)
outputBinary(10);             // Setzt P1.1 und P1.3 auf High (binär 1010)
```
```
Bit-Manipulation mit Makros
// Nützliche Makros für Bit-Manipulation
#define SET_BIT(PORT, BIT)    ((PORT) |= (BIT))
#define CLEAR_BIT(PORT, BIT)  ((PORT) &= ~(BIT))
#define TOGGLE_BIT(PORT, BIT) ((PORT) ^= (BIT))
#define GET_BIT(PORT, BIT)    ((PORT) & (BIT))

// Verwendung:
SET_BIT(P1OUT, BIT0);         // P1.0 auf High setzen
CLEAR_BIT(P2OUT, BIT1);       // P2.1 auf Low setzen
TOGGLE_BIT(P3OUT, BIT2);      // P3.2 umschalten
if(GET_BIT(P1IN, BIT3))       // Prüfen, ob P1.3 High ist
```

### Pullup or Pulldown Resistor Enable Register (PxREN)
- Das PxREN-Register steuert die Aktivierung der internen Pull-up- oder Pull-down-Widerstände für jeden Pin eines Ports:
	- **Bit = 0:** Der interne Pull-up/Pull-down-Widerstand für den entsprechenden Pin ist deaktiviert
	- **Bit = 1:** Der interne Pull-up/Pull-down-Widerstand für den entsprechenden Pin ist aktiviert
- Wichtige Eigenschaften des Registers:
	- Bitbreite: 8 Bit (0-7)
	- Zugriffstyp: RW (Read/Write - Lesen/Schreiben)
	- Standardzustand nach Reset: 0h (alle Widerstände deaktiviert)
- Zu beachten ist:
	- Das PxREN-Register aktiviert lediglich die Widerstände
	- Die Auswahl zwischen Pull-up und Pull-down erfolgt über das entsprechende Bit im PxOUT-Register:
		- Wenn PxOUT-Bit = 0: Pull-down-Widerstand wird ausgewählt
		- Wenn PxOUT-Bit = 1: Pull-up-Widerstand wird ausgewählt
	- Der betreffende Pin muss als Eingang konfiguriert sein (PxDIR-Bit = 0)
- Diese Funktionalität ist besonders nützlich für:
	- Tasteneingang ohne externe Widerstände
	- Vermeidung von schwebenden Eingängen bei unverbundenen Pins
	- Definition eines Standardzustands für Eingänge (z.B. Taster normalerweise auf High)
	- Reduzierung der externen Bauelemente

### Welches Problem kann bei unbenutzten I/Os entstehen?
- Bei unbenutzten I/Os (Input/Output-Pins) können verschiedene Probleme auftreten, insbesondere bei Mikrocontrollern wie dem MSP430:
	- **Schwebende Eingänge (Floating Inputs)**: Wenn ein Pin als Eingang konfiguriert ist, aber nicht angeschlossen wird, kann sein Zustand undefiniert sein. Dies führt zu:
		- Zufälligen Zustandswechseln
		- Erhöhtem Stromverbrauch durch ungewollte Schaltvorgänge in der Eingangsstufe
		- Möglichen Fehlinterpretationen bei Interrupts oder Abfragen
	- **Erhöhter Stromverbrauch**: Schwebende Eingänge können durch ständiges Umschalten zwischen High und Low die CMOS-Eingangsstufen in einen linearen Betriebsbereich bringen, was den Stromverbrauch deutlich erhöht.
	- **Elektromagnetische Störungen (EMI)**: Unbenutzte Pins können als Antennen wirken und elektromagnetische Störungen einfangen, die sich auf andere Schaltungsteile auswirken können.
	- **Unbeabsichtigte Ausgangszustände**: Wenn ein unbenutzter Pin versehentlich als Ausgang konfiguriert ist, kann er einen ungewollten Signalpegel ausgeben, der bei Kurzschluss zu erhöhtem Stromverbrauch oder sogar zur Beschädigung führen kann.
	- **Leistungsaufnahme im Schlafmodus**: In Low-Power-Anwendungen können schwebende Eingänge den Stromverbrauch im Schlafmodus erhöhen, was die Batterielebensdauer verkürzt.

### Delay
- die Verwendung eines Software-Delays in Form einer leeren for-Schleife und enthält eine Warnung des Compilers. Eine wichtige Frage wird gestellt: "Warum soll man die Delay-Funktion nicht als Software-Delay ausführen?"
- Die im Code gezeigte Methode (`for(i=10000; i>0; i--);`) ist eine sogenannte "busy-waiting" Delay-Implementierung. Es gibt mehrere Gründe, warum diese Methode problematisch ist und vermieden werden sollte:
	- **Ineffiziente Energienutzung**: Während der Schleife läuft der Prozessor mit voller Leistung, führt jedoch keine nützlichen Operationen aus. Dies ist besonders bei batteriebetriebenen Geräten wie MSP430-Anwendungen problematisch.
	- **Ungenauigkeit**: Die Verzögerungsdauer hängt von:
		- Taktfrequenz des Prozessors
		- Optimierungsstufe des Compilers
		- Möglichen Interrupts während der Ausführung ab und kann zwischen verschiedenen Compilierungen oder Betriebsbedingungen variieren.
	- **Blockierung anderer Aufgaben**: Während der Prozessor in der Delay-Schleife ist, kann er keine anderen Aufgaben ausführen. Dies verschwendet Rechenzeit und macht es unmöglich, auf Ereignisse zu reagieren.
	- **Portabilitätsprobleme**: Bei Änderungen der CPU-Geschwindigkeit müsste der Delay-Wert angepasst werden.
	- **Ineffizientes Multitasking**: Es ist nicht möglich, während des Delays andere Funktionen auszuführen.
- Der Compiler erkennt dieses Muster und gibt eine Warnung aus, dass stattdessen ein Timer-Modul verwendet werden sollte.
- Bessere Alternativen sind:
	- Verwendung von Timer-Hardware (`Timer_A` oder `Timer_B` im MSP430)
	- Verwendung der `__delay_cycles()`-Funktion für kurze, präzise Verzögerungen
	- Implementierung eines Low-Power-Modus mit Timer-Wakeups
	- Ereignisgesteuerte Programmierung statt zeitgesteuerter Verzögerungen
- Diese Alternativen sind energieeffizienter, genauer und ermöglichen es dem Prozessor, während Wartezeiten andere Aufgaben zu erledigen oder in den Energiesparmodus zu wechseln.
