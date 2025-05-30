
## Umwandlung von CNN zu FCN
- Bei der Umwandlung eines CNN mit Dense-Schichten in ein FCN werden die vollständig verbundenen Schichten durch 1×1 Konvolutionen ersetzt:
	- Eine Dense-Schicht mit 4096 Neuronen entspricht einer 1×1 Konvolution mit 4096 Filtern
	- Die abschließende Klassifikationsschicht wird zu einer 1×1 Konvolution mit N Filtern (N = Anzahl der Klassen)
- Vorteile für die Objekterkennung
	- **Effiziente Fenstererkennung**: Anstatt ein Fenster explizit über das Bild zu schieben und jedes Mal das CNN auszuwerten, verarbeitet ein FCN das gesamte Bild in einem Durchgang. Die Ausgabe ist eine "Heatmap", die Erkennungswahrscheinlichkeiten für jede Position anzeigt.
	- **Wiederverwendung von Berechnungen**: FCNs nutzen gemeinsame Merkmale für überlappende Regionen, was den Rechenaufwand erheblich reduziert. Dies macht die implizite Sliding Window Implementierung um Größenordnungen effizienter.
	- **Flexibilität bei Eingabegrößen**: Wie Sie richtig erwähnt haben, können FCNs Bilder beliebiger Größe verarbeiten - ein enormer Vorteil gegenüber CNNs mit festen Eingabegrößen.
- FCNs in modernen Objektdetektoren
	- FCNs bilden die Grundlage vieler moderner Objekterkennungssysteme:
		- **SSD (Single Shot Detector)**: Nutzt ein FCN-Backbone und führt Vorhersagen auf mehreren Feature Maps unterschiedlicher Auflösung durch
		- **YOLO (You Only Look Once)**: Implementiert einen FCN-basierten Ansatz für End-to-End-Objekterkennung
		- **Feature Pyramid Networks**: Erweitern FCNs durch hierarchische Verbindungen zwischen Feature Maps verschiedener Auflösungen
	- 