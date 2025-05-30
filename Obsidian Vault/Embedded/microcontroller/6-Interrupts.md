## **Was ist ein Interrupt?**

Ein **Interrupt** ist ein Mechanismus zur Unterbrechung des laufenden Programms:
- **Unterbricht** das laufende Programm an beliebiger Stelle
- Wird durch ein **vorher definiertes Ereignis** ausgelöst
- Nach Auslösen wird die zugehörige **Interrupt-Funktion (ISR)** ausgeführt
- Nach Funktionsausführung kehrt das System zur ursprünglichen Programmstelle zurück
- **Alternative zu Polling**: Effizienter als ständiges Abfragen von Zuständen

## **Interrupt-Typen**
Es gibt **drei Haupttypen** von Interrupts:
### **2.1 System Reset**
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
### **2.2 Nicht maskierbare Interrupts (NMI)**
- Werden **nicht** durch das General Interrupt Enable (GIE) Bit maskiert
- Unterteilt in:
    - **System NMI (SNMI)**:
        - Fehlerhafte Versorgungsspannung
        - Zugriff auf leeren Speicher
        - JTAG Mailbox Events
    - **User NMI (UNMI)**:
        - Flanke am NMI Pin
        - Fehlerhafter Oszillator-Takt
        - Zugriffsverletzung im Flash Memory
# JTAG Mailbox Events
## **Was ist JTAG?**
**JTAG** steht für **"Joint Test Action Group"** und ist ein internationaler Standard (IEEE 1149.1) für:

- **Testen** von integrierten Schaltkreisen
- **Debuggen** von Mikrocontrollern
- **Programmieren** von Flash-Speicher
- **Boundary Scan Testing**

## **JTAG Mailbox Konzept**

Die **JTAG Mailbox** ist ein Kommunikationsmechanismus zwischen:

- **Debug-Host** (Computer mit Debugger/Programmer)
- **Target-Mikrocontroller** (MSP430)

### **Funktionsweise**

```
Debug-Host  ←→  JTAG Interface  ←→  MSP430 Mailbox  ←→  CPU
```

## **JTAG Mailbox Events (JMB Events)**

**JTAG Mailbox Events** sind spezielle Ereignisse, die auftreten, wenn:

### **1. Datenübertragung stattfindet**

- **Host → Target**: Debugger sendet Daten an Mikrocontroller
- **Target → Host**: Mikrocontroller sendet Daten an Debugger

### **2. Mailbox-Status sich ändert**

- **Mailbox voll**: Neue Daten können nicht empfangen werden
- **Mailbox leer**: Bereit für neue Daten
- **Überlauffehler**: Daten gehen verloren

### **3. Debug-Operationen ausgeführt werden**

- **Breakpoint erreicht**
- **Einzelschritt-Ausführung**
- **Memory-Read/Write-Operationen**

## **Warum sind JMB Events System NMI?**

JMB Events werden als **System NMI (nicht maskierbare Interrupts)** klassifiziert, weil:

### **Kritische Debug-Funktionalität**

- Debug-Operationen dürfen **nicht durch normale Interrupts blockiert** werden
- **Höchste Priorität** für Debug-Kommunikation erforderlich

### **Systemintegrität**

- **Fehlerhafte Debug-Kommunikation** könnte System beschädigen
- **Sofortige Behandlung** von Mailbox-Fehlern notwendig

### **Real-Time Debugging**

- **Unterbrechungsfreie Debug-Sessions** ermöglichen
- **Konsistente Datenübertragung** zwischen Host und Target

## **Praktische Auswirkungen**

### **Für Entwickler**

c

```c
// JMB Events können nicht maskiert werden
__disable_interrupt();  // Hat KEINEN Einfluss auf JMB Events
```

### **Debug-Session Beispiel**

1. **Debugger setzt Breakpoint** → JMB Event
2. **CPU erreicht Breakpoint** → System stoppt
3. **Debugger liest Register** → JMB Event
4. **Entwickler inspiziert Variablen** → Weitere JMB Events
5. **Continue-Befehl** → JMB Event

## **MSP430-spezifische Details**

### **Mailbox Register**

- **JMBIIN**: Eingehende Daten vom Host
- **JMBIOUT**: Ausgehende Daten zum Host
- **JMBCLR**: Mailbox löschen

### **Ereignisse die JMB Events auslösen**

- **JTAG-Datenregister wird geschrieben**
- **Mailbox-Overflow tritt auf**
- **Debug-Halt wird angefordert**
- **Flash-Programmierung über JTAG**

## **Zusammenfassung**

**JTAG Mailbox Events** sind spezielle Hardware-Ereignisse, die bei der Debug-Kommunikation zwischen Entwicklungsumgebung und Mikrocontroller auftreten. Sie werden als nicht maskierbare System-Interrupts behandelt, um eine zuverlässige und unterbrechungsfreie Debug-Funktionalität zu gewährleisten.

**Wichtig für Entwickler**: Diese Events laufen im Hintergrund ab und sind normalerweise transparent für die Anwendungssoftware, außer bei speziellen Debug-Anwendungen oder Low-Level-Systemprogrammierung.

### **2.3 Maskierbare Interrupts**

- Werden durch das **GIE Bit** global aktiviert/deaktiviert (`__enable_interrupt()`)
- Können **zusätzlich einzeln** maskiert werden
- Werden durch **interruptfähige Peripherie** ausgelöst
- Beispiele: Port-Interrupts, Timer-Interrupts

## **3. Interrupt-Prioritäten**

- Bei **mehreren gleichzeitigen Interrupts** muss die Reihenfolge geregelt sein
- Prioritäten sind oft **im System festgelegt**, können aber teilweise gewählt werden
- **Höchste Priorität**: System Reset (Priorität 63)
- **Niedrigste Priorität**: Reservierte Interrupts (Priorität 0)

## **4. Interrupt-Ablauf**
Der Interrupt-Prozess läuft in folgenden Schritten ab:
1. **Aktuellen Befehl beenden**
2. **Kontext sichern**: Programmzähler (PC) und Statusregister (SR) auf Stack
3. **SR löschen** (automatisch durch MCU)
4. **ISR-Adresse laden** und Interrupt Service Routine ausführen
5. **Kontext wiederherstellen**: SR und PC vom Stack holen
6. **Zur ursprünglichen Stelle zurückkehren**

## **Interruptvektoren**
- **Adressen der ISRs** werden in Interruptvektoren abgelegt
- **Interrupt-Vektor-Tabelle** liegt außerhalb des Programmspeichers
- Spezifikation in C mit: `#pragma vector=<VECTOR_LABEL>`
- Jeder Interrupt hat eine **feste Adresse** in der Vektor-Tabelle
- ![[Pasted image 20250530121032.png]]![[Pasted image 20250530121153.png]]
- ![[Pasted image 20250530121329.png]]
- ![[Pasted image 20250530121342.png]]![[Pasted image 20250530121351.png]]

## **6. Port-Interrupts am MSP430FR2355**

### **Interruptfähige Ports**

- Nur **Port 1 und Port 2** sind interruptfähig
![[Pasted image 20250530121520.png]]
### **Wichtige Register für Port 1**

- **P1IV (Interrupt Vector Register)**: Identifiziert die Interrupt-Quelle
- **P1IES (Interrupt Edge Select)**: Konfiguriert Flankenart
    - 0b = Low-to-High Transition
    - 1b = High-to-Low Transition
    - ![[Pasted image 20250530121607.png]]
- **P1IE (Interrupt Enable)**: Aktiviert/deaktiviert Port-Interrupts
	- ![[Pasted image 20250530121620.png]]
- **P1IFG (Interrupt Flag)**: Zeigt pendende Interrupts an
	- ![[Pasted image 20250530121634.png]]

## **7. Praktische Anwendung: Tastendruck erkennen**

### **Funktionsweise**

- **Interrupt für P1.1 aktivieren**
- **Fallende Flanke konfigurieren** (Tastendruck)
- Bei Tastendruck wird Interrupt ausgelöst
- ![[Pasted image 20250530121742.png]]
- ### **Problem: Taster-Prellen**

Mechanische Taster erzeugen beim Betätigen mehrere ungewollte Flanken ("Bounce"):

- **Idealisiertes Signal**: Sauberer Übergang zwischen HIGH und LOW
- **Reales Signal**: Mehrfache Übergänge durch mechanisches Prellen
- ![[Pasted image 20250530121919.png]]
- ### **Lösungsansätze für Entprellen**
1. **Schaltungstechnisch**: RC-Glied als Tiefpass
    - Schwierig bei vorhandener Platine
2. <mark style="background: #FFB86CA6;">**Softwareseitig**</mark>:
    - Nach Flankenerkennung "Prellzeit" abwarten
    - Interrupts temporär deaktivieren
    - Timer-basierte Entprellung
# Detaillierte Analyse: Taster-Prellen und Entprellung

## **1. Das Problem: Mechanisches Prellen im Detail**

### **Physikalische Ursachen**

```
Mechanische Kontakte beim Schalten:
┌─────────────────────────────────────┐
│  Beweglicher Kontakt                │
│     │                               │
│     ▼                               │
│  ╔══════╗    ┌─────┐                │
│  ║      ║    │ Feste │               │
│  ║ Feder║    │Kontakte│              │
│  ║      ║    └─────┘                │
│  ╚══════╝                           │
└─────────────────────────────────────┘
```

**Beim Tastendrück passiert:**

1. **Erster Kontakt**: Kontakte berühren sich kurz
2. **Aufprall und Rückfederung**: Mechanische Energie lässt Kontakte "hüpfen"
3. **Mehrfache Berührungen**: 5-50ms lang unregelmäßige Kontakte
4. **Stabilisierung**: Endgültiger, stabiler Kontakt
### **Zeitverhalten beim Prellen**

```
Idealisiertes Signal:
VCC ────┐
        │
        │
        └──────── GND

Reales Signal mit Prellen:
VCC ────┐ ┌┐ ┌┐┌┐  ┌────
        │ ││ ││││  │
        └─┘└─┘└┘└──┘
        ↑           ↑
    Erste      Stabile
   Berührung   Verbindung
   
Prellzeit: 5-50ms (typisch 10-20ms)
```

## **2. Hardware-Lösungen im Detail**

### **2.1 RC-Tiefpass (Klassische Lösung)**

#### **Grundschaltung:**

```
VCC ──┬── R ──┬──○ Taster ○──┬── GND
      │       │              │
      │       C              │
      │       │              │
      └───────┴──────────────┘
              │
              ├── zum µC-Pin
```

#### **Dimensionierung:**

- **Widerstand R**: 1kΩ - 10kΩ (typisch 4,7kΩ)
- **Kondensator C**: 10nF - 100nF (typisch 47nF)
- **Zeitkonstante τ = R × C**

#### **Berechnung der Zeitkonstante:**

```
R = 4,7kΩ, C = 47nF
τ = 4.700Ω × 47×10⁻⁹F = 220,9µs

Nach 5τ ≈ 1,1ms ist Signal zu 99% stabil
```

#### **Signalverlauf mit RC-Glied:**

```
Ohne RC-Glied:           Mit RC-Glied:
VCC ────┐ ┌┐ ┌┐          VCC ────┐
        │ ││ ││                 │ ╱
        └─┘└─┘└──                └╱────
        Prellen                 Smooth
```

### **2.2 Schmitt-Trigger-Buffer**

#### **Schaltung:**

```
Taster ── RC-Glied ── 74HC14 ── zum µC
                    (Schmitt-Trigger)
```

#### **Vorteile:**

- **Definierte Schaltschwellen** (z.B. 1,6V/0,9V bei 3,3V)
- **Hysterese** verhindert Oszillation
- **Digitaler Ausgang** unabhängig von Eingangssteilheit

### **2.3 Hardware-Debouncer ICs**

#### **Spezielle ICs:**

- **MAX6816-MAX6818**: 8-Pin-Debouncer
- **MC14490**: 16-Pin Hex-Debouncer
- **74HC164**: Schieberegister-basiert

## **3. Software-Lösungen im Detail**

### **3.1 Einfache Delay-Methode**

#### **Grundprinzip:**

c

```c
#include <msp430.h>

volatile unsigned char button_pressed = 0;

// Port 1 Interrupt Service Routine
#pragma vector=PORT1_VECTOR
__interrupt void Port_1_ISR(void)
{
    // Debounce-Delay (blockierend - nicht optimal!)
    __delay_cycles(160000);  // ~10ms bei 16MHz
    
    // Prüfe ob Taster noch gedrückt
    if (!(P1IN & BIT1)) {
        button_pressed = 1;
    }
    
    P1IFG &= ~BIT1;  // Clear interrupt flag
}

void init_button(void)
{
    P1DIR &= ~BIT1;        // P1.1 als Input
    P1REN |= BIT1;         // Pull-up aktivieren
    P1OUT |= BIT1;         // Pull-up setzen
    P1IES |= BIT1;         // Fallende Flanke
    P1IE |= BIT1;          // Interrupt aktivieren
    P1IFG &= ~BIT1;        // Flag löschen
}
```

#### **Nachteile:**

- **Blockiert CPU** während Delay
- **Ungenaue Zeitgebung**
- **Nicht echtzeitfähig**

### **3.2 State-Machine-basierte Entprellung**

#### **Zustandsautomat:**

```
IDLE ──(Press)──> DEBOUNCE ──(Timer)──> PRESSED
  ↑                   │                     │
  │                   │                     │
  └──(Release)←── WAIT_RELEASE ←─(Release)──┘
```

#### **Implementation:**

c

```c
#include <msp430.h>

typedef enum {
    BTN_IDLE,
    BTN_DEBOUNCE,
    BTN_PRESSED,
    BTN_WAIT_RELEASE
} button_state_t;

volatile button_state_t btn_state = BTN_IDLE;
volatile unsigned int debounce_timer = 0;
volatile unsigned char button_event = 0;

#define DEBOUNCE_TIME 20  // 20ms

// Timer A0 ISR (1ms Tick)
#pragma vector=TIMER0_A0_VECTOR
__interrupt void Timer_A0_ISR(void)
{
    // Button State Machine
    switch(btn_state) {
        case BTN_IDLE:
            if (!(P1IN & BIT1)) {  // Taster gedrückt
                btn_state = BTN_DEBOUNCE;
                debounce_timer = DEBOUNCE_TIME;
            }
            break;
            
        case BTN_DEBOUNCE:
            if (debounce_timer > 0) {
                debounce_timer--;
            } else {
                if (!(P1IN & BIT1)) {  // Immer noch gedrückt
                    btn_state = BTN_PRESSED;
                    button_event = 1;  // Event setzen
                } else {
                    btn_state = BTN_IDLE;  // Falsche Erkennung
                }
            }
            break;
            
        case BTN_PRESSED:
            if (P1IN & BIT1) {  // Taster losgelassen
                btn_state = BTN_WAIT_RELEASE;
                debounce_timer = DEBOUNCE_TIME;
            }
            break;
            
        case BTN_WAIT_RELEASE:
            if (debounce_timer > 0) {
                debounce_timer--;
            } else {
                if (P1IN & BIT1) {  // Immer noch losgelassen
                    btn_state = BTN_IDLE;
                } else {
                    btn_state = BTN_PRESSED;  // Immer noch gedrückt
                }
            }
            break;
    }
}

void init_timer_1ms(void)
{
    // Timer A0 für 1ms Interrupt
    TA0CCTL0 = CCIE;                    // Enable interrupt
    TA0CCR0 = 16000 - 1;               // 1ms bei 16MHz
    TA0CTL = TASSEL_2 + MC_1;          // SMCLK, Up mode
}
```

### **3.3 Interrupt-basierte Entprellung mit Timer**

#### **Elegante Lösung:**

c

```c
#include <msp430.h>

volatile unsigned char btn_debounce_active = 0;
volatile unsigned char button_pressed = 0;

// Port 1 Interrupt
#pragma vector=PORT1_VECTOR
__interrupt void Port_1_ISR(void)
{
    if (!btn_debounce_active) {
        // Debounce-Timer starten
        btn_debounce_active = 1;
        TA1CCR0 = 320;  // 20ms bei 16kHz Timer
        TA1CTL = TASSEL_1 + MC_1 + TACLR;  // ACLK, Up mode
        
        // Port-Interrupt temporär deaktivieren
        P1IE &= ~BIT1;
    }
    
    P1IFG &= ~BIT1;  // Clear flag
}

// Timer A1 Interrupt (Debounce-Timer)
#pragma vector=TIMER1_A0_VECTOR
__interrupt void Timer_A1_ISR(void)
{
    // Timer stoppen
    TA1CTL = 0;
    btn_debounce_active = 0;
    
    // Taster-Status prüfen
    if (!(P1IN & BIT1)) {
        button_pressed = 1;  // Gültiger Tastendruck
    }
    
    // Port-Interrupt wieder aktivieren
    P1IE |= BIT1;
    P1IFG &= ~BIT1;  // Eventuell gesetzte Flags löschen
}
```

### **3.4 Polling-basierte Entprellung**

#### **Für einfache Anwendungen:**

c

```c
unsigned char debounce_button(void)
{
    static unsigned char btn_history = 0xFF;  // Button history
    
    // Shift history und neuen Wert hinzufügen
    btn_history = (btn_history << 1) | ((P1IN & BIT1) ? 1 : 0);
    
    // Button als gedrückt erkennen wenn letzte 8 Samples LOW
    if (btn_history == 0x00) {
        return 1;  // Button definitiv gedrückt
    }
    
    // Button als losgelassen erkennen wenn letzte 8 Samples HIGH  
    if (btn_history == 0xFF) {
        return 0;  // Button definitiv losgelassen
    }
    
    return 2;  // Unbestimmter Zustand (Prellen)
}

// Hauptschleife
int main(void)
{
    static unsigned char last_btn_state = 0;
    unsigned char current_btn_state;
    
    while(1) {
        current_btn_state = debounce_button();
        
        if (current_btn_state != 2) {  // Gültiger Zustand
            if (current_btn_state && !last_btn_state) {
                // Steigende Flanke erkannt
                handle_button_press();
            }
            last_btn_state = current_btn_state;
        }
        
        __delay_cycles(16000);  // 1ms Delay bei 16MHz
    }
}
```

## **6. Praktische Tipps**

### **Timing-Werte:**

- **Prellzeit**: 5-50ms (typisch 10-20ms)
- **Debounce-Zeit**: 20-50ms (sicher)
- **Abtastrate**: 1-5ms (für Software-Polling)

### **Häufige Fehler:**

1. **Zu kurze Debounce-Zeit** → Prellen nicht vollständig unterdrückt
2. **Blocking Delays** → System nicht reaktionsfähig
3. **Interrupt-Flags nicht löschen** → Endlosschleife
4. **Pull-up/Pull-down vergessen** → Floating inputs

Die **Timer-basierte Lösung mit State Machine** ist meist der beste Kompromiss zwischen Effizienz, Zuverlässigkeit und Ressourcenverbrauch.

![[Pasted image 20250530123625.png]]

## **8. Timer-Interrupts**

**Anwendungen**:

- **Zeitmessung**
- **PWM-Erzeugung**
- **Taster-Entprellung**

**Vorteile gegenüber Polling**:

- Elegantere Lösung als Polling der Interrupt-Flags
- Ereignisgesteuerte Programmierung möglich