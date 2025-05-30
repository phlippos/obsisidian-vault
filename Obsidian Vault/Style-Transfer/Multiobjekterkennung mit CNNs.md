
## Sliding window
- Der Sliding Window Ansatz ist eine der grundlegenden Methoden zur Objekterkennung mit Convolutional Neural Networks (CNNs). Bei diesem Verfahren wird ein Fenster fester Größe systematisch über das Eingabebild geschoben und für jede Position eine Klassifikation durchgeführt.
- ## Funktionsweise
	1. Ein Klassifikations-CNN wird trainiert, um einzelne Objekte zu erkennen
	2. Während der Inferenz wird dieses CNN mit einem Fenster fester Größe über das gesamte Bild geschoben
	3. Für jede Position wird eine Vorhersage getroffen, ob ein Objekt vorhanden ist und welcher Klasse es angehört
	4. Durch Zusammenführen überlappender Detektionen mittels Non-Maximum Suppression (NMS) werden finale Ergebnisse erzielt
- ## Vor- und Nachteile
	- **Vorteile:**
		- Konzeptionell einfach zu verstehen und implementieren
		- Kann mit jedem Klassifikations-CNN verwendet werden
		- Ermöglicht die Erkennung mehrerer Objekte im Bild
	- **Nachteile:**
		- <mark style="background: #FFB86CA6;">Hoher Rechenaufwand durch redundante Berechnungen</mark>
		- <mark style="background: #FFB86CA6;">Schwierigkeiten bei der Erkennung von Objekten unterschiedlicher Größe </mark>(erfordert mehrere Skalierungen)
		- Weniger effizient als moderne End-to-End-Ansätze wie YOLO, SSD oder Faster R-CNN
- ## Verbesserungen und Alternativen
- Moderne Objekterkennungssysteme haben den einfachen Sliding Window Ansatz weitgehend ersetzt durch:
	- **Region-based CNNs (R-CNN, Fast R-CNN, Faster R-CNN)**: Verwendung von Region Proposals statt erschöpfender Suche
	- **Single-Shot-Detektoren (SSD, YOLO)**: End-to-End-Netzwerke, die Objektlokalisierung und Klassifikation in einem Durchlauf erledigen
	- **Feature Pyramid Networks (FPN)**: Verbesserte Objekterkennung über verschiedene Skalierungen
Wir haben die grundlegenden Konzepte der Objekterkennung behandelt und aus erster Hand erfahren, dass insbesondere die Multiobjekterkennung eine deutlich komplexere Aufgabe darstellt als z.B. die Bildklassifikation. Die Anforderung, alle im Bild vorhandenen Objekte zu klassifizieren und auch deren Position und Ausdehnung im Bild zu bestimmen, führt zu einer Reihe von Herausforderungen.

Zum einen müssen Modelle in der Lage sein, mit einer variablen Anzahl von Objekten in einem Bild umzugehen. Zum anderen müssen sie Objekte unterschiedlicher Größe, Form und Perspektive erkennen können. Darüber hinaus kann es zu Überlappungen zwischen Objekten kommen, was die Erkennung zusätzlich erschwert.

Diese Anforderungen erfordern komplexere Lösungsansätze in allen Phasen des Gesamtprozesses, von der Datenaufbereitung über das Training und die Inferenz bis hin zur Auswertung.