## **1. Grundlagen der A/D-Wandlung**

### **1.1 Vom analogen zum digitalen Signal**

Der **Analog-Digitalwandler (ADC)** wandelt kontinuierliche analoge Signale in diskrete digitale Werte um. Die Abbildung zeigt:
![[Pasted image 20250530130937.png]]
- **Blaue Kurve**: Kontinuierliches analoges Signal (Sinuswelle)
- **Rote Punkte**: Diskrete Abtastpunkte (Samples)
- **Rote Treppenfunktion**: Quantisiertes digitales Signal

### **1.2 Wichtige Kenngrößen bei der A/D-Wandlung**

#### **Sampling-Rate**

- **Definition**: Anzahl der Abtastungen pro Sekunde
- **Nyquist-Prinzip**: Sampling-Frequenz muss mindestens **2× die höchste Signalfrequenz** betragen
- **Formel**: fs ≥ 2 × fsignal

![[Pasted image 20250530131112.png]]![[Pasted image 20250530131411.png]]
#### **Quantisierung**
- **Definition**: Aufteilung des analogen Wertebereichs in diskrete Stufen
- **Auflösung**: Anzahl der Bits bestimmt die Anzahl der Quantisierungsstufen
- **12-Bit ADC**: 2¹² = 4096 Stufen (0-4095)
#### **Referenzspannung**
- **Definition**: Bestimmt den Messbereich des ADCs
- **Bedeutung**: Legt fest, welche analoge Spannung dem maximalen Digitalwert entspricht
- ![[Pasted image 20250530132348.png]]
## **4. Praktisches Beispiel: Temperatursensor**

### **4.1 Programmstruktur**

#### **Initialisierung**

c

```c
#include <msp430.h>

// Kalibrierungswerte für Temperatursensor
#define CALADC12_15V_30C  *((unsigned int *)0x1A1A)  // 30°C
#define CALADC12_15V_85C  *((unsigned int *)0x1A1C)  // 85°C

unsigned int temp;
volatile float temperatureDegC;
volatile float temperatureDegF;
```

#### **Register-Konfiguration**
![[Pasted image 20250530132931.png]]
![[Pasted image 20250530132935.png]]
![[Pasted image 20250530133002.png]]
![[Pasted image 20250530132542.png]]
# ADC Control Register 0 (ADCCTL0) - Detaillierte Erklärung

## **Registerübersicht**

Das **ADCCTL0** ist das Haupt-Kontrollregister für den ADC des MSP430. Es ist ein 16-Bit Register, das verschiedene Aspekte der ADC-Operation steuert.

## **Bit-für-Bit Erklärung**

### **Bits 15-12: Reserved**

- **Zweck**: Reserviert für zukünftige Nutzung
- **Wert**: Immer 0
- **Hinweis**: Sollten nicht verändert werden

---

### **Bits 11-8: ADCSHT (ADC Sample-and-Hold Time)**

- **Zweck**: Bestimmt die **Sample-Zeit** des ADCs
- **Wichtigkeit**: Kritisch für genaue Messungen

#### **Sample-Zeit Konfiguration:**

c

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

#### **Praktische Bedeutung:**

- **Kurze Sample-Zeit**: Schnellere Wandlung, aber möglicherweise ungenau bei hochohmigen Quellen
- **Lange Sample-Zeit**: Langsamere Wandlung, aber genauer bei hochohmigen Quellen

#### **Beispiel-Code:**

c

```c
ADC12CTL0 |= ADC12SHT0_8;  // 8 ADCCLK Cycles Sample-Zeit
```

---

### **Bit 7: ADCMSC (ADC Multiple Sample and Conversion)**

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

#### **Beispiel-Code:**

c

```c
// Single-Shot Modus
ADC12CTL0 &= ~ADC12MSC;

// Continuous Modus  
ADC12CTL0 |= ADC12MSC;
```

---

### **Bits 6-5: Reserved**

- **Zweck**: Reserviert
- **Wert**: Immer 0

---

### **Bit 4: ADCON (ADC On)**

- **Zweck**: **Power-Control** für den ADC-Kern

#### **Funktionen:**

- **ADCON = 0**: ADC ist **ausgeschaltet** (Stromsparmodus)
- **ADCON = 1**: ADC ist **eingeschaltet** und betriebsbereit

#### **Wichtige Hinweise:**

- ADC muss eingeschaltet sein, bevor Wandlungen möglich sind
- Nach dem Einschalten kurze Stabilisierungszeit abwarten

#### **Beispiel-Code:**

c

```c
ADC12CTL0 |= ADC12ON;      // ADC einschalten
__delay_cycles(100);       // Stabilisierungszeit
```

---

### **Bits 3-2: Reserved**

- **Zweck**: Reserviert
- **Wert**: Immer 0

---

### **Bit 1: ADCENC (ADC Enable Conversion)**

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

#### **Beispiel-Code:**

c

```c
// Konfiguration
ADC12CTL0 &= ~ADC12ENC;    // Disable für Konfiguration
ADC12CTL1 = ADC12SHP;      // Konfiguration ändern
ADC12CTL0 |= ADC12ENC;     // Enable für Betrieb
```

---

### **Bit 0: ADCSC (ADC Start Conversion)**

- **Zweck**: **Startet** eine ADC-Wandlung

#### **Funktionen:**

- **ADCSC = 0**: Keine Wandlung
- **ADCSC = 1**: **Startet Wandlung** (wird automatisch gelöscht nach Start)

#### **Verhalten:**

- Bit wird **automatisch gelöscht** nach Wandlungsstart
- Muss für jede neue Wandlung gesetzt werden (außer im Continuous-Modus)

#### **Beispiel-Code:**

c

```c
ADC12CTL0 |= ADC12SC;      // Wandlung starten
```

---

## **Typische Konfigurationssequenz**

c

```c
// 1. ADC ausschalten für Konfiguration
ADC12CTL0 &= ~ADC12ENC;

// 2. ADC konfigurieren
ADC12CTL0 = ADC12SHT0_8 +    // 8 ADCCLK Sample-Zeit
            ADC12ON;         // ADC einschalten

// 3. Andere Register konfigurieren
ADC12CTL1 = ADC12SHP;        // Sample-Timer
ADC12MCTL0 = ADC12INCH_10;   // Kanal A10

// 4. Stabilisierungszeit
__delay_cycles(100);

// 5. Wandlungen aktivieren  
ADC12CTL0 |= ADC12ENC;

// 6. Erste Wandlung starten
ADC12CTL0 |= ADC12SC;
```

## **Praktische Anwendungsbeispiele**

### **Einzelmessung (Single-Shot):**

c

```c
ADC12CTL0 = ADC12SHT0_8 + ADC12ON;  // Sample-Zeit + ADC an
ADC12CTL0 |= ADC12ENC;              // Enable
ADC12CTL0 |= ADC12SC;               // Start Conversion
```

### **Kontinuierliche Messung:**

c

```c
ADC12CTL0 = ADC12SHT0_8 + ADC12MSC + ADC12ON;  // Continuous Modus
ADC12CTL0 |= ADC12ENC;                          // Enable  
ADC12CTL0 |= ADC12SC;                           // Start (läuft kontinuierlich)
```

### **Hochohmige Quelle:**

c

```c
ADC12CTL0 = ADC12SHT0_12 + ADC12ON;  // Längere Sample-Zeit für hochohmige Quellen
```

## **Häufige Fehler und Lösungen**

### **Problem: Konfiguration funktioniert nicht**

c

```c
// ❌ Falsch - ADCENC ist gesetzt
ADC12CTL0 |= ADC12ENC;
ADC12CTL1 = ADC12SHP;  // Fehler! Konfiguration nicht möglich

// ✅ Richtig - ADCENC zuerst löschen
ADC12CTL0 &= ~ADC12ENC;  // Disable für Konfiguration
ADC12CTL1 = ADC12SHP;    // Konfiguration möglich
ADC12CTL0 |= ADC12ENC;   // Wieder aktivieren
```

### **Problem: Ungenaue Messungen**

c

```c
// ❌ Zu kurze Sample-Zeit
ADC12CTL0 = ADC12SHT0_0 + ADC12ON;  // Nur 4 ADCCLK Cycles

// ✅ Angemessene Sample-Zeit
ADC12CTL0 = ADC12SHT0_8 + ADC12ON;  // 8 ADCCLK Cycles (Standard)
```

Das ADCCTL0 Register ist zentral für die ADC-Operation und erfordert sorgfältige Konfiguration für optimale Ergebnisse.


![[Pasted image 20250530132615.png]]
# ADC Control Register 1 (ADCCTL1) - Detaillierte Erklärung

## **Registerübersicht**

Das **ADCCTL1** ist das zweite Kontrollregister für den ADC des MSP430. Es steuert hauptsächlich **Timing, Taktquellen und Wandlungsmodi** des ADCs.

## **Bit-für-Bit Erklärung**

### **Bits 15-12: Reserved**

- **Zweck**: Reserviert für zukünftige Nutzung
- **Wert**: Immer 0
- **Hinweis**: Nicht verändern

---

### **Bits 11-10: ADCSHSx (ADC Sample-and-Hold Source Select)**

- **Zweck**: Wählt die **Trigger-Quelle** für Sample-and-Hold

#### **Trigger-Quellen:**

c

```c
ADCSHS_0 = 00b = ADCSC Bit (Software-Trigger)
ADCSHS_1 = 01b = Timer Trigger 0 (hardware-spezifisch)
ADCSHS_2 = 10b = Timer Trigger 1 (hardware-spezifisch)  
ADCSHS_3 = 11b = Timer Trigger 2 (hardware-spezifisch)
```

#### **Praktische Anwendung:**

- **ADCSHS_0**: **Manuelle Steuerung** über Software
- **ADCSHS_1-3**: **Automatische Trigger** durch Timer-Events

#### **Beispiel-Code:**

c

```c
// Software-Trigger (Standard)
ADC12CTL1 |= ADC12SHS_0;

// Timer-basierter Trigger
ADC12CTL1 |= ADC12SHS_1;  // Timer Trigger 0
```

---

### **Bit 9: ADCSHP (ADC Sample-and-Hold Pulse-mode)**

- **Zweck**: Steuert das **Sample-Timing**

#### **Modi:**

- **ADCSHP = 0**:
    - **Level-triggered Sampling**
    - Sample-Signal muss **konstant hoch** bleiben während Sample-Zeit
    - Für externe Trigger-Signale
- **ADCSHP = 1**:
    - **Pulse-triggered Sampling**
    - **Interner Sample-Timer** wird verwendet
    - **Standard-Modus** für die meisten Anwendungen

#### **Beispiel-Code:**

c

```c
ADC12CTL1 |= ADC12SHP;  // Pulse-Modus (empfohlen)
```

---

### **Bit 8: ADCISSH (ADC Invert Signal Sample-and-Hold)**

- **Zweck**: **Invertiert** das Sample-and-Hold Signal

#### **Funktionen:**

- **ADCISSH = 0**: Sample-Input **nicht invertiert** (Standard)
- **ADCISSH = 1**: Sample-Input **invertiert**

#### **Anwendung:**

- Normalerweise auf 0 belassen
- Nur für spezielle Hardware-Konfigurationen erforderlich

---

### **Bits 7-5: ADCDIVx (ADC Clock Divider)**

- **Zweck**: **Teilt den ADC-Takt** um die Wandlungsgeschwindigkeit zu steuern

#### **Teilerverhältnisse:**

c

```c
ADCDIV_0 = 000b = Divide by 1 (kein Teiler)
ADCDIV_1 = 001b = Divide by 2  
ADCDIV_2 = 010b = Divide by 3
ADCDIV_3 = 011b = Divide by 4
ADCDIV_4 = 100b = Divide by 5
ADCDIV_5 = 101b = Divide by 6
ADCDIV_6 = 110b = Divide by 7
ADCDIV_7 = 111b = Divide by 8
```

#### **Praktische Bedeutung:**

- **Niedriger Teiler**: Schnellere Wandlung, höherer Stromverbrauch
- **Hoher Teiler**: Langsamere Wandlung, niedrigerer Stromverbrauch

#### **Berechnung der ADC-Frequenz:**

c

```c
fADC = fSource / (Divider + 1)

// Beispiel: SMCLK = 1MHz, ADCDIV_3 (Divide by 4)
fADC = 1MHz / 4 = 250kHz
```

#### **Beispiel-Code:**

c

```c
ADC12CTL1 |= ADC12DIV_2;  // Teiler = 3, fADC = fSource/3
```

---

### **Bits 4-3: ADCSSELx (ADC Clock Source Select)**

- **Zweck**: Wählt die **Taktquelle** für den ADC

#### **Taktquellen:**

c

```c
ADCSSEL_0 = 00b = MODCLK (interne Hochgeschwindigkeits-Taktquelle)
ADCSSEL_1 = 01b = ACLK (Auxiliary Clock)
ADCSSEL_2 = 10b = MCLK (Master Clock)  
ADCSSEL_3 = 11b = SMCLK (Sub-Master Clock)
```

#### **Eigenschaften der Taktquellen:**

- **MODCLK**: Interner, spezieller ADC-Takt (~5MHz)
- **ACLK**: Meist 32kHz, sehr niedrig
- **MCLK**: Haupt-CPU-Takt
- **SMCLK**: Sub-Master-Takt (oft gleich MCLK)

#### **Beispiel-Code:**

c

```c
ADC12CTL1 |= ADC12SSEL_2;  // MCLK als Taktquelle
```

---

### **Bits 2-1: ADCCONSEQx (ADC Conversion Sequence Mode)**

- **Zweck**: Bestimmt den **Wandlungsmodus** des ADCs

#### **Wandlungsmodi:**

c

```c
ADCCONSEQ_0 = 00b = Single-channel, single-conversion
ADCCONSEQ_1 = 01b = Sequence-of-channels  
ADCCONSEQ_2 = 10b = Repeat-single-channel
ADCCONSEQ_3 = 11b = Repeat-sequence-of-channels
```

#### **Detaillierte Beschreibung:**

**ADCCONSEQ_0 - Single-channel, single-conversion:**

- Eine Wandlung, ein Kanal
- Nach Wandlung stoppt ADC
- Für gelegentliche Messungen

**ADCCONSEQ_1 - Sequence-of-channels:**

- Mehrere Kanäle nacheinander
- Jeder Kanal einmal
- Für Multi-Sensor Systeme

**ADCCONSEQ_2 - Repeat-single-channel:**

- Ein Kanal, kontinuierlich
- Automatische Wiederholung
- Für kontinuierliche Überwachung

**ADCCONSEQ_3 - Repeat-sequence-of-channels:**

- Mehrere Kanäle, kontinuierlich
- Sequenz wiederholt sich automatisch
- Für kontinuierliche Multi-Sensor Überwachung

#### **Beispiel-Code:**

c

```c
// Kontinuierliche Einzelkanal-Messung
ADC12CTL1 |= ADC12CONSEQ_2;

// Sequenz mehrerer Kanäle
ADC12CTL1 |= ADC12CONSEQ_1;
```

---

### **Bit 0: ADCBUSY (ADC Busy)**

- **Zweck**: **Status-Flag** - zeigt an, ob ADC gerade arbeitet
- **Typ**: **Read-Only** (nur lesbar)

#### **Status:**

- **ADCBUSY = 0**: ADC ist **inaktiv**
- **ADCBUSY = 1**: ADC führt gerade eine **Wandlung durch**

#### **Anwendung:**

c

```c
// Warten bis Wandlung abgeschlossen
while(ADC12CTL1 & ADC12BUSY);

// Oder in Bedingung prüfen
if(!(ADC12CTL1 & ADC12BUSY)) {
    // ADC ist bereit für neue Wandlung
    ADC12CTL0 |= ADC12SC;
}
```

---

## **Typische Konfigurationsbeispiele**

### **Standard-Konfiguration (Einzelmessung):**

c

```c
ADC12CTL1 = ADC12SHP +          // Pulse-Mode
            ADC12SSEL_2 +       // MCLK als Taktquelle
            ADC12DIV_0 +        // Kein Taktteiler
            ADC12CONSEQ_0;      // Single-channel, single-conversion
```

### **Kontinuierliche Messung:**

c

```c
ADC12CTL1 = ADC12SHP +          // Pulse-Mode
            ADC12SSEL_2 +       // MCLK
            ADC12DIV_2 +        // Teiler = 3 (langsamerer Takt)
            ADC12CONSEQ_2;      // Repeat-single-channel
```

### **Multi-Channel Sequenz:**

c

```c
ADC12CTL1 = ADC12SHP +          // Pulse-Mode
            ADC12SSEL_3 +       // SMCLK
            ADC12DIV_1 +        // Teiler = 2
            ADC12CONSEQ_1;      // Sequence-of-channels
```

### **Timer-getriggerte Messung:**

c

```c
ADC12CTL1 = ADC12SHS_1 +        // Timer Trigger 0
            ADC12SHP +          // Pulse-Mode
            ADC12SSEL_2 +       // MCLK
            ADC12CONSEQ_2;      // Repeat-single-channel
```

## **Optimierung für verschiedene Anwendungen**

### **Niedrigster Stromverbrauch:**

c

```c
ADC12CTL1 = ADC12SHP +          // Pulse-Mode
            ADC12SSEL_1 +       // ACLK (32kHz)
            ADC12DIV_7 +        // Maximaler Teiler
            ADC12CONSEQ_0;      // Single-conversion
```

### **Höchste Geschwindigkeit:**

c

```c
ADC12CTL1 = ADC12SHP +          // Pulse-Mode
            ADC12SSEL_0 +       // MODCLK (~5MHz)
            ADC12DIV_0 +        // Kein Teiler
            ADC12CONSEQ_2;      // Kontinuierlich
```

### **Ausgewogene Performance:**

c

```c
ADC12CTL1 = ADC12SHP +          // Pulse-Mode
            ADC12SSEL_2 +       // MCLK
            ADC12DIV_1 +        // Teiler = 2
            ADC12CONSEQ_0;      // Single-conversion
```

## **Häufige Fehlerquellen**

### **Problem: ADC zu schnell/ungenau**

c

```c
// ❌ Zu schneller Takt
ADC12CTL1 = ADC12SSEL_0 + ADC12DIV_0;  // MODCLK ohne Teiler

// ✅ Angemessener Takt  
ADC12CTL1 = ADC12SSEL_2 + ADC12DIV_2;  // MCLK mit Teiler
```

### **Problem: Kontinuierliche Messung stoppt**

c

```c
// ❌ Falscher Modus
ADC12CTL1 |= ADC12CONSEQ_0;  // Single-conversion

// ✅ Richtiger Modus
ADC12CTL1 |= ADC12CONSEQ_2;  // Repeat-single-channel
```

Das ADCCTL1 Register ist entscheidend für die **Timing-Konfiguration** und den **Betriebsmodus** des ADCs und muss sorgfältig an die Anwendungsanforderungen angepasst werden.
![[Pasted image 20250530132622.png]]![[Pasted image 20250530133030.png]]
# ADC Conversion Memory Control (ADCMCTL0) Register - Detaillierte Erklärung

## **Registerübersicht**

Das **ADCMCTL0** Register konfiguriert die **Wandlungsparameter** für den ersten Speicherplatz (MEM0) des ADCs. Jeder Speicherplatz (MEM0-MEM15) hat sein eigenes MCTLx Register.

## **Bit-für-Bit Erklärung**

### **Bits 15-7: Reserved**

- **Zweck**: Reserviert für zukünftige Nutzung
- **Wert**: Immer 0
- **Hinweis**: Nicht verändern

---

### **Bits 6-4: ADCSREFx (ADC Reference Voltage Select)**

- **Zweck**: Wählt die **Referenzspannungsquelle** für diese Wandlung

#### **Referenzspannungsoptionen:**

c

```c
ADCSREF_0 = 000b = VR+ = AVCC, VR- = AVSS
ADCSREF_1 = 001b = VR+ = VREF, VR- = AVSS  
ADCSREF_2 = 010b = VR+ = VEREF+ buffered, VR- = AVSS
ADCSREF_3 = 011b = VR+ = VEREF+ buffered, VR- = AVSS
ADCSREF_4 = 100b = VR+ = AVCC, VR- = VREF-
ADCSREF_5 = 101b = VR+ = VREF, VR- = VREF-
ADCSREF_6 = 110b = VR+ = VEREF+ buffered, VR- = VREF-
ADCSREF_7 = 111b = VR+ = VEREF+, VR- = VREF-
```

#### **Praktische Bedeutung:**

**ADCSREF_0 (Standard):**

- **VR+ = AVCC** (meist 3,3V oder 5V)
- **VR- = AVSS** (0V/GND)
- **Messbereich**: 0V bis Versorgungsspannung
- **Für**: Allgemeine Spannungsmessungen

**ADCSREF_1 (Interne Referenz):**

- **VR+ = VREF** (1,5V, 2,0V oder 2,5V)
- **VR- = AVSS** (0V/GND)
- **Messbereich**: 0V bis Referenzspannung
- **Für**: Präzise Messungen, unabhängig von Versorgungsspannung

#### **Beispiel-Code:**

c

```c
// Versorgungsspannung als Referenz
ADC12MCTL0 = ADC12SREF_0 + ADC12INCH_1;

// Interne 1,5V Referenz
ADC12MCTL0 = ADC12SREF_1 + ADC12INCH_1;
```

---

### **Bits 3-0: ADCINCHx (ADC Input Channel Select)**

- **Zweck**: Wählt den **Eingangskanal** für diese Wandlung

#### **Verfügbare Kanäle:**

c

```c
ADCINCH_0  = 0000b = A0/VEREF+ (P1.0)
ADCINCH_1  = 0001b = A1 (P1.1)  
ADCINCH_2  = 0010b = A2/VEREF- (P1.2)
ADCINCH_3  = 0011b = A3 (P1.3)
ADCINCH_4  = 0100b = A4 (P1.4)
ADCINCH_5  = 0101b = A5 (P1.5)
ADCINCH_6  = 0110b = A6 (P1.6)
ADCINCH_7  = 0111b = A7 (P1.7)
ADCINCH_8  = 1000b = A8 (P5.0)
ADCINCH_9  = 1001b = A9 (P5.1)
ADCINCH_10 = 1010b = A10 (P5.2) - Temperatursensor
ADCINCH_11 = 1011b = A11 (P5.3)
ADCINCH_12 = 1100b = A12 (on-chip temperature sensor)
ADCINCH_13 = 1101b = A13 (internal reference voltage)
ADCINCH_14 = 1110b = A14 (DVSS)
ADCINCH_15 = 1111b = A15 (DVCC)
```

#### **Spezielle interne Kanäle:**

**A10/A12 - Temperatursensor:**

- **Zweck**: Interne Temperaturmessung
- **Typ**: Integrierter Silizium-Temperatursensor
- **Kalibrierung**: Werkskalibriert bei 30°C und 85°C

**A13 - Interne Referenzspannung:**

- **Zweck**: Überwachung der internen Referenz
- **Nutzen**: Kalibrierung und Selbsttest

**A14 - DVSS (Digital Ground):**

- **Zweck**: Offset-Kalibrierung
- **Sollwert**: Nahe 0V

**A15 - DVCC (Digital Supply):**

- **Zweck**: Versorgungsspannungsüberwachung
- **Nutzen**: Battery-Monitoring

---

## **Praktische Konfigurationsbeispiele**

### **Externe Spannung messen (Standard):**

c

```c
// Kanal A1 mit Versorgungsspannung als Referenz
ADC12MCTL0 = ADC12SREF_0 + ADC12INCH_1;

// Berechnung: Vin = (ADC_Wert/4095) × AVCC
```

### **Präzise Spannungsmessung:**

c

```c
// Kanal A2 mit interner 1,5V Referenz
ADC12MCTL0 = ADC12SREF_1 + ADC12INCH_2;

// Berechnung: Vin = (ADC_Wert/4095) × 1,5V
```

### **Temperaturmessung:**

c

```c
// Interner Temperatursensor
ADC12MCTL0 = ADC12SREF_1 + ADC12INCH_10;

// Kalibrierung mit Werks-Kalibrierdaten erforderlich
```

### **Batteriespannungsüberwachung:**

c

```c
// DVCC-Überwachung mit interner Referenz
ADC12MCTL0 = ADC12SREF_1 + ADC12INCH_15;

// DVCC = (ADC_Wert/4095) × 1,5V × 2  // Spannungsteiler beachten
```

### **Offset-Kalibrierung:**

c

```c
// DVSS messen für Nullpunkt-Kalibrierung
ADC12MCTL0 = ADC12SREF_1 + ADC12INCH_14;

// Sollwert: nahe 0
```

---

## **Multi-Channel Sequenz-Konfiguration**

### **Sequenzielle Kanalmessung:**

c

```c
// MEM0: Kanal A0
ADC12MCTL0 = ADC12SREF_0 + ADC12INCH_0;

// MEM1: Kanal A1  
ADC12MCTL1 = ADC12SREF_0 + ADC12INCH_1;

// MEM2: Temperatursensor
ADC12MCTL2 = ADC12SREF_1 + ADC12INCH_10;

// MEM3: Versorgungsspannung (Ende der Sequenz)
ADC12MCTL3 = ADC12SREF_1 + ADC12INCH_15 + ADC12EOS;
```

### **Verschiedene Referenzen pro Kanal:**

c

```c
// Hochpräzise Messung mit interner Referenz
ADC12MCTL0 = ADC12SREF_1 + ADC12INCH_0;  // 1,5V Referenz

// Vollbereich-Messung mit Versorgungsspannung
ADC12MCTL1 = ADC12SREF_0 + ADC12INCH_1;  // AVCC Referenz

// Differentielle Messung  
ADC12MCTL2 = ADC12SREF_5 + ADC12INCH_2;  // VREF+ und VREF-
```

---

## **Spannungsberechnung für verschiedene Referenzen**

### **Mit Versorgungsspannung (ADCSREF_0):**

c

```c
float voltage = (float)adc_value * AVCC / 4095.0f;

// Beispiel: AVCC = 3,3V, ADC = 2048
// voltage = 2048 * 3,3V / 4095 = 1,65V
```

### **Mit interner 1,5V Referenz (ADCSREF_1):**

c

```c
float voltage = (float)adc_value * 1.5f / 4095.0f;

// Beispiel: ADC = 2730 
// voltage = 2730 * 1,5V / 4095 = 1,0V
```

### **Temperatursensor-Berechnung:**

c

```c
// Mit Kalibrierdaten bei 30°C und 85°C
float temp = ((float)adc_value - CAL_30C) * 55.0f / 
             (CAL_85C - CAL_30C) + 30.0f;
```

---

## **Optimierung für verschiedene Anwendungen**

### **Maximale Präzision:**

c

```c
ADC12MCTL0 = ADC12SREF_1 + ADC12INCH_0;  // Interne Referenz
// + längere Sample-Zeit in ADCCTL0
// + mehrfache Messungen und Mittelwert
```

### **Maximaler Messbereich:**

c

```c
ADC12MCTL0 = ADC12SREF_0 + ADC12INCH_0;  // Versorgungsspannung
// Messbereich: 0V bis AVCC
```

### **Differentielle Messung:**

c

```c
ADC12MCTL0 = ADC12SREF_7 + ADC12INCH_0;  // VEREF+ und VREF-
// Für kleine Signale mit großem Offset
```

---

## **Häufige Anwendungsfehler**

### **Problem: Falscher Messbereich**

c

```c
// ❌ Falsch: 5V Signal mit 1,5V Referenz
ADC12MCTL0 = ADC12SREF_1 + ADC12INCH_0;  // Überlauf!

// ✅ Richtig: 5V Signal mit Versorgungsreferenz
ADC12MCTL0 = ADC12SREF_0 + ADC12INCH_0;  // Vollbereich
```

### **Problem: Temperatursensor ohne Referenz**

c

```c
// ❌ Falsch: Temperatursensor mit variabler Referenz
ADC12MCTL0 = ADC12SREF_0 + ADC12INCH_10;

// ✅ Richtig: Temperatursensor mit fester Referenz  
ADC12MCTL0 = ADC12SREF_1 + ADC12INCH_10;
```

### **Problem: Ungeeignete Kanalwahl**

c

```c
// ❌ Falsch: Nicht verfügbarer Kanal
ADC12MCTL0 = ADC12SREF_0 + ADC12INCH_16;  // Existiert nicht!

// ✅ Richtig: Verfügbarer Kanal verwenden
ADC12MCTL0 = ADC12SREF_0 + ADC12INCH_1;   // A1 verfügbar
```

Das ADCMCTL0 Register ist entscheidend für die **Kanal- und Referenzauswahl** und muss präzise auf die jeweilige Messaufgabe abgestimmt werden.

![[Pasted image 20250530133037.png]]![[Pasted image 20250530133043.png]]![[Pasted image 20250530133049.png]]![[Pasted image 20250530133140.png]]![[Pasted image 20250530133304.png]]
![[Pasted image 20250530133314.png]]