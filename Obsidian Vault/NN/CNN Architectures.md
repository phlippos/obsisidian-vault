Typische CNN-Architekturen stapeln mehrere Faltungsschichten (jede in der Regel gefolgt von einer ReLU-Schicht), dann eine Pooling-Schicht, dann wieder einige Faltungsschichten (+ReLU), dann eine weitere Pooling-Schicht und so weiter. Das Bild wird im Verlauf des Netzwerks immer kleiner, aber es wird auch typischerweise tiefer und tiefer (d. h. mit mehr Merkmalskarten), dank der Faltungsschichten.


!!!Ein häufiger Fehler ist die Verwendung zu großer Faltungskerne. Beispielsweise sollte man anstelle einer Faltungsschicht mit einem 5×5-Kern zwei Schichten mit 3×3-Kernen stapeln: Dies wird weniger Parameter verwenden, weniger Berechnungen erfordern und in der Regel besser funktionieren.

Die Anzahl der Filter nimmt zu, während wir uns in einem CNN zur Ausgabeschicht hocharbeiten (zunächst 64, dann 128, dann 256). Es ist sinnvoll, dass sie zunimmt, da die Anzahl der Low-Level-Features oft ziemlich niedrig ist (z.B. kleine Kreise, horizontale Linien), aber es gibt viele verschiedene Möglichkeiten, sie zu höherwertigen Features zu kombinieren. Es ist eine gängige Praxis, die Anzahl der Filter nach jeder Pooling-Schicht zu verdoppeln: Da eine Pooling-Schicht jede räumliche Dimension um den Faktor 2 verringert, können wir die Anzahl der Merkmalskarten in der nächsten Schicht verdoppeln, ohne Angst vor einer Explosion der Anzahl der Parameter, des Speicherverbrauchs oder der Rechenlast haben zu müssen.


LeNet-5
1. **Eingabeschicht**: Die Eingabebilder im MNIST-Datensatz haben eine Größe von 32x32 Pixeln, aber LeNet-5 verwendet eine 28x28-Eingabeschicht, da die Ränder der 32x32-Bilder keine Informationen enthalten.
    
2. **Convolutional Layer C1**: Diese Schicht verwendet 6 Filter mit einer Größe von 5x5 und einer Stride von 1. Jeder Filter wird auf das Eingangsbild angewendet, um 6 Merkmalskarten zu erzeugen.
    
3. **Pooling Layer S2**: Dies ist eine durchschnittliche Poolingschicht mit einer Größe von 2x2 und einer Stride von 2, die die Größe der Merkmalskarten halbiert.
    
4. **Convolutional Layer C3**: Diese Schicht verwendet 16 Filter mit einer Größe von 5x5 und einer Stride von 1, um 16 Merkmalskarten zu erzeugen.
    
5. **Pooling Layer S4**: Ähnlich wie S2 ist dies eine durchschnittliche Poolingschicht mit einer Größe von 2x2 und einer Stride von 2.
    
6. **Fully Connected Layer C5**: Dies ist ein vollständig verbundener Layer mit 120 Neuronen, der die Merkmale aus S4 aufnimmt.
    
7. **Fully Connected Layer F6**: Ein weiterer vollständig verbundener Layer mit 84 Neuronen.
    
8. **Ausgabeschicht**: Die Ausgabeschicht hat 10 Neuronen (eins für jede Ziffer von 0 bis 9) und verwendet in der Regel eine Softmax-Aktivierungsfunktion für die Klassifikation.

-   Die durchschnittlichen Pooling-Schichten sind etwas komplexer als üblich: Jedes Neuron berechnet den Mittelwert seiner Eingaben, multipliziert das Ergebnis dann mit einem erlernbaren Koeffizienten (einer pro Merkmalskarte) und fügt einen erlernbaren Bias-Term hinzu (wieder einer pro Merkmalskarte). Abschließend wird die Aktivierungsfunktion angewendet. Diese Art von Pooling kann nützlich sein, um die Flexibilität des Modells zu erhöhen und ihm zu ermöglichen, komplexere Muster zu lernen. . Diese Art von Pooling kann auch dazu beitragen, Overfitting zu reduzieren, da das Modell in der Lage ist, relevante Informationen zu verstärken und irrelevante Informationen zu unterdrücken.
- - Gegeben sei der 2x2-Bereich der Eingangskarte mit den Werten:
    `[1, 2] [3, 4]`
- Die durchschnittliche Poolingschicht berechnet den Durchschnitt dieser Werte: (1+2+3+4)/4 = 2.5
- Das Neuron multipliziert den Durchschnitt mit seinem Koeffizienten, z.B. 1.2, und addiert den Bias, z.B. 0.5: 2.5 * 1.2 + 0.5 = 3.5
- Schließlich wird die Aktivierungsfunktion auf das Ergebnis angewendet, z.B. ReLU: ReLU(3.5) = 3.5

- In LeNet-5 ist dies jedoch nicht der Fall. Stattdessen sind die meisten Neuronen in den Merkmalskarten der C3-Schicht nur mit drei oder vier der Merkmalskarten der S2-Schicht verbunden. Dies bedeutet, dass jedes Neuron in der C3-Schicht nur auf eine Teilmenge der Informationen aus der S2-Schicht zugreifen kann, was zu einer Art lokaler Verarbeitung führt.Diese Art der Verbindung kann dazu beitragen, die Anzahl der Parameter im Netzwerk zu reduzieren, da weniger Verbindungen zwischen den Schichten erforderlich sind. Außerdem kann es dazu beitragen, bestimmte Merkmale in den Daten hervorzuheben, indem es den Neuronen ermöglicht, sich auf spezifische Teile des Eingaberaums zu konzentrieren.

## **AlexNet**:
1. **Eingabeschicht**: Die Eingabebilder haben eine Größe von 224x224 Pixeln (im Gegensatz zu den kleineren Bildern in früheren Arbeiten).
    
2. **Convolutional Layer 1 (Conv1)**: Diese Schicht besteht aus 96 Filtern der Größe 11x11, die mit einem Stride von 4 angewendet werden. Es folgt eine ReLU-Aktivierungsfunktion und eine Max-Pooling-Schicht mit einer Größe von 3x3 und einem Stride von 2.
    
3. **Convolutional Layer 2 (Conv2)**: Diese Schicht besteht aus 256 Filtern der Größe 5x5. Es folgt wieder eine ReLU-Aktivierung und eine Max-Pooling-Schicht mit der gleichen Größe wie vorher.
    
4. **Convolutional Layer 3 (Conv3)**: Diese Schicht besteht aus 384 Filtern der Größe 3x3.
    
5. **Convolutional Layer 4 (Conv4)**: Diese Schicht besteht aus 384 Filtern der Größe 3x3.
    
6. **Convolutional Layer 5 (Conv5)**: Diese Schicht besteht aus 256 Filtern der Größe 3x3. Es folgt eine ReLU-Aktivierung und eine Max-Pooling-Schicht.
    
7. **Vollständig verbundene Schicht 1 (FC6)**: Dies ist ein vollständig verbundener Layer mit 4096 Neuronen.
    
8. **Vollständig verbundene Schicht 2 (FC7)**: Ein weiterer vollständig verbundener Layer mit 4096 Neuronen.
    
9. **Ausgabeschicht**: Die Ausgabeschicht hat 1000 Neuronen (entsprechend den 1000 Klassen des ImageNet-Datensatzes) und verwendet in der Regel eine Softmax-Aktivierungsfunktion für die Klassifikation.
- Local Response Normalization : 
	- Die lokale Reaktionsnormalisierung (LRN) ist eine Technik, die oft in CNN-Architekturen verwendet wird, um die Aktivierung von Neuronen zu regulieren.
	- Die LRN wird typischerweise nach einer Convolutional Layer und einer Aktivierungsfunktion wie der ReLU angewendet. Sie funktioniert, indem sie die Aktivierungen jedes Neurons in Bezug auf seine Nachbarn normalisiert. Dies geschieht durch die Berechnung des Quotienten zwischen der Aktivierung des Neurons und einer summierten Maßzahl der Aktivierungen seiner benachbarten Neuronen.
	- ![[Pasted image 20240513200500.png]]
	- ![[Pasted image 20240513200530.png]]
- Die LRN bewirkt eine normierte Hemmung, bei der stärkere Aktivierungen stärker unterdrückt werden als schwächere. Dies kann dazu beitragen, die Varianz in den Aktivierungen zu verringern und die Robustheit des Modells zu verbessern. Es wird jedoch zunehmend weniger verwendet, da Batch-Normalisierung und andere Techniken in vielen Fällen effektiver sind.
- Wenn ein Neuron in einer bestimmten Merkmalskarte sehr aktiviert ist, führt dies zu einer großen Norm im Nenner des Normalisierungsterms. Dies hat zur Folge, dass die Aktivierung der benachbarten Neuronen in anderen Merkmalskarten an derselben Position durch den Normalisierungsterm reduziert wird, da der Nenner der Division größer wird.
- Diese Art der gegenseitigen Hemmung zwischen den Merkmalskarten kann dazu beitragen, die Konkurrenz zwischen den Merkmalen zu verstärken und die Unterscheidungsfähigkeit des Netzwerks zu verbessern. Indem die am stärksten aktivierten Neuronen die Aktivierung benachbarter Neuronen dämpfen, werden die Merkmalskarten angeregt, verschiedene Aspekte der Daten zu erfassen und zu repräsentieren.

## GoogLeNet
- Inception Modules: 
	- ![[Pasted image 20240513211016.png]]
	- Diese Module sind darauf ausgelegt, die räumliche und rechnerische Effizienz zu verbessern, indem sie parallele Konvolutionen in verschiedenen Größen durchführen und die Ergebnisse kombinieren.
	- Ein Inception-Modul besteht aus mehreren parallelen Faltungspfaden, die gleichzeitig auf die Eingangsdaten angewendet werden. Diese Pfade umfassen typischerweise 1x1-, 3x3- und 5x5-Konvolutionen sowie einen Max-Pooling-Pfad. Die Ausgabe jedes Pfades wird dann kanalweise konkateniert, um eine einzige Ausgabe zu erzeugen. Dies ermöglicht dem Netzwerk, Merkmale auf verschiedenen Skalen und Abstraktionsebenen zu erfassen und zu kombinieren.
	- Vorteile:

1. **Multiskalen-Feature-Extraktion**: Durch die gleichzeitige Anwendung von Faltungen unterschiedlicher Größe kann das Netzwerk Merkmale auf verschiedenen Skalen erfassen, was zu einer verbesserten Repräsentation der Daten führt.
    
2. **Dimensionalitätsreduktion**: 1x1-Konvolutionen in jedem Pfad dienen dazu, die Anzahl der Feature-Maps zu reduzieren, was die Rechenkomplexität verringert und die Effizienz des Modells verbessert.
    
3. **Diversität der Merkmale**: Die parallelen Pfade ermöglichen dem Netzwerk, verschiedene Arten von Merkmalen zu erfassen, was zu einer breiteren Abdeckung und einer besseren Generalisierung führt.
* Warum wird 1x1 Kernel verwendet. Es gibt 3 Gründe :
	1. Obwohl sie keine räumlichen Muster erfassen können, können sie Muster entlang der Tiefendimension erfassen.
	2. Sie sind so konfiguriert, dass sie weniger Feature-Maps ausgeben als ihre Eingaben, so dass sie als Engpass-Schichten dienen, d. h. sie reduzieren die Dimensionalität. Dies reduziert die Rechenkosten und die Anzahl der Parameter, beschleunigt das Training und verbessert die Generalisierung.
	3.  Jedes Paar von Faltungsschichten ([1 × 1, 3 × 3] und [1 × 1, 5 × 5]) wirkt wie eine einzelne leistungsstarke Faltungsschicht, die komplexere Muster erfassen kann. Anstatt einen einfachen linearen Klassifikator über das Bild zu ziehen, zieht dieses Paar von Faltungsschichten ein zweischichtiges neuronales Netzwerk über das Bild
-  man kann sich das gesamte Inception-Modul als eine Faltungsschicht auf Steroiden vorstellen, die in der Lage ist, Merkmalskarten auszugeben, die komplexe Muster auf verschiedenen Ebenen erfassen.
- !!!!!!!!!!! haben Sie sechs weitere Hyperparameter, die Sie für jede hinzugefügte Inception-Ebene anpassen müssen.
- ![[Pasted image 20240513213514.png]]


## ResNet
- Der Schlüssel zum Training eines solchen tiefen Netzwerk zu trainieren, ist die Verwendung von Skip-Verbindungen (auch Shortcut-Verbindungen genannt): Das Signal, das in eine Schicht eingespeist wird, wird auch dem Ausgang einer Schicht hinzugefügt, die sich etwas weiter oben im Stapel befindet.
- Beim Training eines neuronalen Netzes besteht das Ziel darin, dass es eine Zielfunktion h(x) modelliert. Wenn man die Eingabe x zur Ausgabe des Netzes hinzufügt (d. h. man fügt eine Sprungverbindung hinzu), dann wird das Netz gezwungen, f(x) = h(x) - x zu modellieren, anstatt h(x). Dies wird Residuales Lernen genannt
- ![[Pasted image 20240513233709.png]]
- Wenn Sie ein normales neuronales Netz initialisieren, liegen seine Gewichte nahe bei Null, so dass das Netz nur Werte nahe bei Null ausgibt. Wenn Sie eine Skip-Verbindung hinzufügen, gibt das resultierende Netz nur eine Kopie seiner Eingaben aus; mit anderen Worten, es modelliert zunächst die Identitätsfunktion. Wenn die Zielfunktion ziemlich nahe an der Identitätsfunktion liegt (was oft der Fall ist), wird das Training dadurch erheblich beschleunigt.
- Wenn Sie außerdem viele Sprungverbindungen hinzufügen, kann das Netz Fortschritte machen, auch wenn mehrere Schichten noch nicht mit dem Lernen begonnen haben. Dank der Skip-Verbindungen kann sich das Signal problemlos über das gesamte Netz ausbreiten. 
- ![[Pasted image 20240513234036.png]]
- ![[Pasted image 20240513234146.png]]
- die Anzahl der Merkmalskarten wird alle paar Residualeinheiten verdoppelt, während gleichzeitig gleichzeitig mit der Halbierung ihrer Höhe und Breite (unter Verwendung einer Faltungsschicht mit Stride 2). In diesem Fall können die Eingänge nicht direkt zu den Ausgängen der Residualeinheit hinzugefügt werden, da sie nicht die gleiche Form haben. Um dieses Problem zu lösen, werden die Eingaben durch eine 1 × 1 Faltungsschicht mit Stride 2 und der richtigen Anzahl von Ausgabe-Merkmalskarten geleitet.
- ![[Pasted image 20240513234458.png]]
## Xception
- Die Xception-Architektur basiert auf der Idee, dass die räumliche und die kanalweise Dimension in einem separaten Schritt behandelt werden sollten. Im Wesentlichen verwendet Xception sogenannte "Depthwise Separable Convolutions", um diese beiden Schritte zu trennen.
- 1. **Depthwise Separable Convolutions**: In einer herkömmlichen Faltung werden Höhe, Breite und Tiefe gleichzeitig behandelt. In Xception werden jedoch zuerst sogenannte "Depthwise Convolutions" durchgeführt, bei denen jede Eingabe-Feature-Map separat gefaltet wird, und dann wird eine "Pointwise Convolution" durchgeführt, bei der eine 1x1-Convolution auf die Ausgabe der Depthwise Convolutions angewendet wird, um die Dimensionalität zu erhöhen oder zu verringern.
- 2. **Reduzierte Anzahl von Parametern**: Durch die Verwendung von Depthwise Separable Convolutions werden weniger Parameter benötigt, was die Trainingszeit verkürzt und Overfitting reduziert.

- Angenommen, es liegen Eingabedaten der Größe **Df x Df x M** vor, wobei Df x Df die Bildgröße und M die Anzahl der Kanäle (3 für ein RGB-Bild) ist. Angenommen, es gibt N Filter/Kernel der Größe **Dk x Dk x M** . Wenn eine normale Faltungsoperation durchgeführt wird, beträgt die Ausgabegröße **Dp x Dp x N** .
- ![[Pasted image 20240514002929.png]]
- Die Anzahl der Multiplikationen in einer Faltungsoperation = Größe des Filters = Dk x Dk x M
- Die Gesamtzahl der Multiplikationen beträgt N x Dp x Dp x (Multiplikationen pro Faltung).
- **Gesamtzahl der Multiplikationen = N x Dp^2 x Dk^2 x M**
- **TIEFENWEISE KONVOLUTION**
	- Bei **_der Tiefenoperation_** wird die Faltung jeweils auf einen **einzelnen Kanal** angewendet, im Gegensatz zu Standard-CNNs, bei denen sie für alle M Kanäle durchgeführt wird. Hier haben die Filter/Kernel also die Größe **Dk x Dk x 1** . Vorausgesetzt, dass die Eingabedaten M Kanäle enthalten, sind M solcher Filter erforderlich. Die Ausgabe hat die Größe **Dp x Dp x** M.
	- Eine einzelne Faltungsoperation erfordert Dk x Dk Multiplikationen.
	- Da die Filter um Dp x Dp-Zeiten über alle M-Kanäle verschoben werden, Die Gesamtzahl der Multiplikationen ist gleich M x Dp x Dp x Dk x Dk
	- **Gesamtzahl der Multiplikationen = M x Dk^2 x Dp^2**
- **Punktweise Faltung**
	- Bei **_der punktweisen Operation_** wird eine **1×1-Faltungsoperation** auf die M Kanäle angewendet. Die Filtergröße für diesen Vorgang beträgt also **1 x 1 x M** . Angenommen, wir verwenden N solcher Filter, beträgt die Ausgabegröße **Dp x Dp x N** .
	- ![[Pasted image 20240514003457.png]]
	- Eine einzelne Faltungsoperation erfordert 1 x M Multiplikationen.
	- die Gesamtzahl der Multiplikationen ist gleich M x Dp x Dp x (Anzahl der Filter)
	- **Gesamtzahl der Multiplikationen = M x Dp^2 x N**
- **Gesamtmultiplikationen = Tiefenkonv. Multiplikationen + Punktweise Konv. Multiplikationen**
	- **Gesamtmultiplikationen = M * Dk^2 * Dp^2 + M * Dp^2 * N = M * Dp^2 * (Dk^2 + n)**
	- **Gesamtzahl der Multiplikationen = M x Dp^2 x (Dk^2 + N)**
	- 

| Art                  | Komplexität           |
| -------------------- | --------------------- |
| Standard CNN         | N x Dp^2 x Dg^2 x M   |
| In der Tiefe teilbar | M x Dp^2 x (Dk^2 + N) |
## SeNet
- Die Steigerung ergibt sich aus der Tatsache, dass ein SENet ein kleines neuronales Netz hinzufügt, genannt SE-Block, zu jeder Einheit der ursprünglichen Architektur hinzufügt
- ![[Pasted image 20240514004920.png]]
- Ein SE-Block analysiert die Ausgabe des Geräts, an das er angeschlossen ist, und konzentriert sich ausschließlich auf die der Tiefendimension (er sucht nicht nach räumlichen Mustern), und er lernt, welche Merkmale in der Regel zusammen am aktivsten sind.  Anhand dieser Informationen werden dann die Merkmalskarten neu kalibriert. 
- Ein SE-Block kann zum Beispiel lernen, dass Münder, Nasen und Augen auf Bildern normalerweise zusammen erscheinen: Wenn man einen Mund und eine Nase sieht, sollte man erwarten, auch Augen zu sehen, aber nur eine geringe Aktivierung in der Augenmerkkarte, so wird die Augenmerkskarte verstärkt.  (genauer gesagt, wird es irrelevante Feature-Maps reduzieren Karten)
- ![[Pasted image 20240514005304.png]]
- ![[Pasted image 20240514005323.png]]
- Wenn die Eingabe beispielsweise 256 Merkmalskarten enthält, gibt sie 256 Zahlen aus, die den Gesamtgrad der Reaktion für jeden Filter darstellen. Die nächste Schicht ist wo der "Squeeze" stattfindet: <mark style="background: #FFF3A3A6;">Diese Schicht hat deutlich weniger als 256 Neuronen - in der Regel 16 Mal weniger als die Anzahl der Merkmalskarten (z. B. 16 Neuronen), so dass die 256 Zahlen werden zu einem kleinen Vektor komprimiert </mark>.
- Dieser Engpass-Schritt zwingt den SE-Block dazu, eine allgemeine Darstellung  der Merkmalskombinationen zu lernen.
- Schließlich nimmt die Ausgabeschicht die Einbettung und gibt einen Rekalibrierungsvektor aus, der eine Zahl pro Merkmalskarte enthält (z.B. 256), Die Merkmalskarten werden dann mit diesem Rekalibrierungsvektor multipliziert, so dass irrelevante Merkmale (mit einem niedrigen Rekalibrierungswert) verkleinert werden, während relevante Merkmale (mit einem Rekalibrierungswert nahe 1) in Ruhe gelassen werden.