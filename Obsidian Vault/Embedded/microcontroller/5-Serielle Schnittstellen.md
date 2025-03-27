

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
			-  **Ruhezustand**: Im Ruhezustand (keine Übertragung) liegt die Leitung auf High-Pegel (logisch 1).
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
