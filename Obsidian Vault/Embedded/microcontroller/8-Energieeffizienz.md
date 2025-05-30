## 1. Warum ist Low-Power wichtig?

### Hauptgründe für energieeffiziente Systeme:

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

### Praktisches Beispiel:

Ein Temperatursensor, der alle 10 Minuten misst:

- **Ohne Low-Power**: Batterie hält 1 Monat
- **Mit Low-Power**: Batterie hält 5-10 Jahre
## 2. Ursachen für Verlustleistung in CMOS-Devices

### Statische Verlustleistung

**Definition**: Verlustleistung, die auch bei inaktiven Transistoren auftritt

**Hauptursachen**:

- **Sub-threshold current**: Schwacher Strom auch bei "ausgeschalteten" Transistoren
- **Gate leakage**: Leckstrom durch das Gate-Oxid
- **Drain junction leakage**: Leckstrom an den pn-Übergängen

**Formel**: P_statisch = U × I_leck

**Technologie-Einfluss**:

- Je kleiner die Strukturgrößen (nm-Prozess), desto größer die Leckströme
- 65nm vs. 28nm: Leckströme können um Faktor 10 steigen

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

### Praktisches Beispiel:

```
Systemvergleich:
- Standard: V_dd = 3.3V, f = 16MHz → P_dyn = 100mW
- Optimiert: V_dd = 1.8V, f = 8MHz → P_dyn = 26mW (74% Einsparung!)
```

## 3. Taktnetzwerk (Unified Clock System - UCS)

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

### Praktische Konfiguration:

c

```c
// Beispiel: Energieoptimierte Konfiguration
ACLK  ← XT1CLK (32kHz, externer Quarz)
MCLK  ← DCOCLK (1MHz nur bei Bedarf)
SMCLK ← REFOCLK (32kHz für langsame Peripherie)
```

## 4. Low-Power Modes des MSP430F5529

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

**Beispiel-Code**:

c

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

**Praktisches Beispiel**:

c

```c
// Aufwachen alle 8 Sekunden durch Watchdog
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

## 5. Praktische Anwendungsbeispiele

### Beispiel 1: Temperatursensor mit Display

c

```c
void main(void) {
    // Initialisierung...
    
    while(1) {
        // Alle 10 Sekunden messen
        measure_temperature();
        update_display();
        
        // 10s in LPM3 schlafen
        start_timer_10s();
        __bis_SR_register(LPM3_bits + GIE);
        
        // Nach Timer-Interrupt hier weiter
    }
}

// Energiebilanz:
// - Aktiv: 1s @ 300μA = 0.083μAh
// - Sleep: 9s @ 0.9μA = 0.0025μAh
// - Ø Verbrauch: 0.086μAh → 10 Jahre Batterielaufzeit!
```

### Beispiel 2: Datenlogger

c

```c
void main(void) {
    while(1) {
        // ADC konfigurieren
        setup_adc();
        
        // In LPM0: ADC arbeitet selbstständig
        __bis_SR_register(LPM0_bits + GIE);
        
        // Nach ADC-Interrupt: Daten speichern
        save_to_flash();
        
        // Lange Pause in LPM3
        __bis_SR_register(LPM3_bits + GIE);
    }
}
```

### Beispiel 3: Energieoptimierung durch Spannungsreduktion

```
Szenario: 8MHz Taktfrequenz

Option 1: V_cc = 3.3V
- Aktiv: 200μA
- LPM3: 1.2μA

Option 2: V_cc = 2.2V  
- Aktiv: 135μA (32% weniger!)
- LPM3: 0.7μA (42% weniger!)

Bei 1% Duty Cycle:
- Option 1: 200μA×0.01 + 1.2μA×0.99 = 3.19μA
- Option 2: 135μA×0.01 + 0.7μA×0.99 = 2.04μA
→ 36% Energieeinsparung!
```


## 6. Design-Strategien für Low-Power

### Hardware-Design:

1. **Spannungsreduktion**: Niedrigste noch funktionale Spannung wählen
2. **Taktoptimierung**: Nur so schnell wie nötig
3. **Peripherie-Management**: Unbenutzte Module abschalten
4. **Pull-up/Pull-down**: Schwimmende Eingänge vermeiden

### Software-Design:

1. **Interrupt-driven Design**: CPU nur bei Bedarf aktiv
2. **Effiziente Algorithmen**: Weniger Taktzyklen
3. **Power Management**: Systematisches Ein-/Ausschalten
4. **Watchdog nutzen**: Für periodische Aufgaben

### Messungen und Optimierung:

```
Typische Stromwerte MSP430F5529:
- Active Mode @ 1MHz:    ~200μA
- LPM0:                  ~50μA  
- LPM3:                  ~0.9μA
- LPM4.5:               ~0.1μA

Faktor 2000 zwischen aktiv und tiefster Schlaf!
```

Die Kunst liegt darin, das System so wenig wie möglich aktiv zu halten und trotzdem alle Anforderungen zu erfüllen.