Die zwei Hauptschwierigkeiten , mit denen RNNs konfrontiert sind : 
- Instabile Gradienten, die durch verschiedene Techniken wie rekurrentes Dropout und rekurrente Layer-Normalisierung gemildert werden können
- A very limited short-term memory, das durch den Einsatz von LSTM- und GRU- Zellen erweitert werden kann
Jedes rekurrente Neuron hat zwei Gewichtssätze: einen für die Eingaben x(t) und einen anderen für die Ausgaben des vorherigen Zeitschritts y(t−1). Nennen wir diese Gewichtungsvektoren wx​ und wy​. Wenn wir die gesamte rekurrente Schicht anstelle nur eines rekurrenten Neurons betrachten, können wir alle Gewichtungsvektoren in zwei Gewichtungsmatrizen Wx​ und Wy platzieren. Der Ausgabevektor der gesamten rekurrenten Schicht kann dann ungefähr so berechnet werden, wie man es erwarten würde.
![[Pasted image 20240614135759.png]] Beachten Sie, dass viele Forscher in RNNs lieber die hyperbolische Tangens (tanh) Aktivierungsfunktion anstelle der ReLU Aktivierungsfunktion verwenden.

### Memory Cell
- ![[Pasted image 20240614140857.png]]
- ![[Pasted image 20240614140912.png]]

### Input Output Sequences
- Ein RNN kann gleichzeitig eine Sequenz von Eingaben verarbeiten und eine Sequenz von Ausgaben erzeugen. Dieser Typ von Sequenz-zu-Sequenz-Netzwerk ist nützlich zur Vorhersage von Zeitreihen wie Aktienkursen: Man gibt ihm die Preise der letzten N Tage ein, und es muss die um einen Tag in die Zukunft verschobenen Preise ausgeben (d. h. von vor N - 1 Tagen bis morgen).
- Alternativ könnte man dem Netzwerk eine Sequenz von Eingaben zuführen und alle Ausgaben außer der letzten ignorieren. Mit anderen Worten, dies ist ein Sequenz-zu-Vektor-Netzwerk. Zum Beispiel könnte man dem Netzwerk eine Sequenz von Wörtern, die einer Filmkritik entsprechen, zuführen, und das Netzwerk würde einen Sentiment-Score ausgeben (z. B. von –1 [hassen] bis +1 [lieben]).
- Umgekehrt könnte man dem Netzwerk denselben Eingangsvektor immer wieder bei jedem Zeitschritt zuführen und es eine Sequenz ausgeben lassen . Dies ist ein Vektor-zu-Sequenz-Netzwerk. Zum Beispiel könnte die Eingabe ein Bild (oder die Ausgabe eines CNN) sein, und die Ausgabe könnte eine Bildbeschreibung sein.
- Zuletzt könnte man ein Sequenz-zu-Vektor-Netzwerk, genannt Encoder, gefolgt von einem Vektor-zu-Sequenz-Netzwerk, genannt Decoder, verwenden . Dies könnte beispielsweise für die Übersetzung eines Satzes von einer Sprache in eine andere verwendet werden. Man würde dem Netzwerk einen Satz in einer Sprache zuführen, der Encoder würde diesen Satz in eine einzelne Vektor-Darstellung umwandeln, und dann würde der Decoder diesen Vektor in einen Satz in einer anderen Sprache dekodieren. Dieses zweistufige Modell, genannt Encoder-Decoder, funktioniert viel besser als der Versuch, mit einem einzigen Sequenz-zu-Sequenz-RNN (wie dem oben links dargestellten) direkt zu übersetzen: Die letzten Wörter eines Satzes können die ersten Wörter der Übersetzung beeinflussen, daher muss man warten, bis man den gesamten Satz gesehen hat, bevor man ihn übersetzt.

### Training RNNs
- ![[Pasted image 20240614170728.png]]
### Forecasting a time Series
- Angenommen, Sie untersuchen die Anzahl der aktiven Benutzer pro Stunde auf Ihrer Website, die tägliche Temperatur in Ihrer Stadt oder die finanzielle Gesundheit Ihres Unternehmens, die vierteljährlich mit mehreren Metriken gemessen wird. In all diesen Fällen sind die Daten eine Sequenz von einem oder mehreren Werten pro Zeitschritt. Dies wird als Zeitreihe bezeichnet. In den ersten beiden Beispielen gibt es pro Zeitschritt einen einzelnen Wert, sodass es sich um **univariate Zeitreihen** handelt, während im finanziellen Beispiel mehrere Werte pro Zeitschritt vorliegen (z. B. der Umsatz des Unternehmens, Schulden usw.), sodass es sich um **multivariate Zeitreihen** handelt. Eine typische Aufgabe besteht darin, zukünftige Werte vorherzusagen, was als **Prognose** bezeichnet wird. Eine weitere häufige Aufgabe besteht darin, Lücken zu füllen: fehlende Werte aus der Vergangenheit vorherzusagen (oder vielmehr „postdict“). Dies wird als **Imputation** bezeichnet.
### Baseline metrics
- es ist oft eine gute Idee, einige Basismetriken zu haben. Andernfalls könnten wir am Ende denken, dass unser Modell großartig funktioniert, obwohl es in Wirklichkeit schlechter abschneidet als grundlegende Modelle. Ein einfachster Ansatz besteht beispielsweise darin, den letzten Wert in jeder Serie vorherzusagen. Dies wird als naive Vorhersage bezeichnet und ist manchmal überraschend schwer zu übertreffen.
- ![[Pasted image 20240614173711.png]]
- Ein weiterer einfacher Ansatz besteht darin, ein vollständig verbundenes Netzwerk (Fully Connected Network) zu verwenden. Da dieses eine flache Liste von Merkmalen für jede Eingabe erwartet, müssen wir eine Flatten-Schicht hinzufügen.

### Implementing a Simple RNN
- ![[Pasted image 20240614174124.png]]
- Wir müssen die Länge der Eingabesequenzen nicht angeben (im Gegensatz zum vorherigen Modell), da ein rekurrentes neuronales Netzwerk eine beliebige Anzahl von Zeitschritten verarbeiten kann (deshalb setzen wir die erste Eingabedimension auf None).
- Standardmäßig verwendet die SimpleRNN-Schicht die hyperbolische Tangens (tanh) Aktivierungsfunktion.
- ![[Pasted image 20240614174402.png]]
- ![[Pasted image 20240614174513.png]]
- Für jedes rekurrente Neuron in einem einfachen RNN gibt es nur einen Parameter pro Eingabe- und pro versteckte Zustandsdimension (in einem einfachen RNN ist das einfach die Anzahl der rekurrenten Neuronen in der Schicht), plus einen Bias-Term. In diesem einfachen RNN sind das insgesamt nur drei Parameter.
- Beachten Sie, dass die letzte Schicht nicht ideal ist: Sie muss eine einzelne Einheit haben, da wir eine univariate Zeitreihe vorhersagen möchten, und dies bedeutet, dass wir einen einzelnen Ausgabewert pro Zeitschritt haben müssen. Das Problem dabei ist, dass der versteckte Zustand nur eine einzelne Zahl ist. Das ist wirklich nicht viel und wahrscheinlich nicht besonders nützlich. Vermutlich wird das RNN hauptsächlich die versteckten Zustände der anderen rekurrenten Schichten verwenden, um alle benötigten Informationen von Zeitschritt zu Zeitschritt zu übertragen, und es wird den versteckten Zustand der letzten Schicht nicht sehr stark nutzen. Zudem muss die SimpleRNN-Schicht standardmäßig die tanh-Aktivierungsfunktion verwenden, sodass die vorhergesagten Werte im Bereich von -1 bis 1 liegen müssen. Aber was, wenn Sie eine andere Aktivierungsfunktion verwenden möchten? Aus beiden Gründen könnte es vorzuziehen sein, die Ausgabeschicht durch eine Dense-Schicht zu ersetzen: Dies würde etwas schneller laufen, die Genauigkeit wäre ungefähr gleich und es würde uns erlauben, jede beliebige Ausgabekativierungsfunktion zu wählen.


### Forecasting Several Time Steps Ahead
- Bisher haben wir nur den Wert zum nächsten Zeitschritt vorhergesagt, aber wir könnten genauso gut den Wert mehrere Schritte im Voraus vorhersagen, indem wir die Zielwerte entsprechend ändern (z. B. um 10 Schritte im Voraus zu prognostizieren, ändern Sie einfach die Zielwerte so, dass sie den Wert 10 Schritte im Voraus anstelle von 1 Schritt im Voraus angeben).
- Aber was, wenn wir die nächsten 10 Werte vorhersagen möchten? 
- Die erste Option besteht darin, das bereits trainierte Modell zu verwenden, um den nächsten Wert vorherzusagen, diesen Wert zu den Eingaben hinzuzufügen (so zu tun, als ob dieser vorhergesagte Wert tatsächlich aufgetreten wäre), und das Modell erneut zu verwenden, um den folgenden Wert vorherzusagen, und so weiter.
- Wenn wir Vorhersagen mit einem rekurrenten neuronalen Netzwerk (RNN) machen, ist die Genauigkeit bei der Vorhersage des nächsten Wertes in der Regel höher als bei der Vorhersage weiter entfernter Werte. Das liegt daran, dass sich die Fehler bei jeder Vorhersage akkumulieren können.
- Beispiel: Vorhersage für die nächsten 10 Schritte
1. **Schrittweise Vorhersage:**
    - Wir trainieren ein Modell, das den nächsten Wert vorhersagt.
    - Um 10 Schritte in die Zukunft zu schauen, nehmen wir die erste Vorhersage und verwenden diese, um die nächste Vorhersage zu machen, und so weiter.
2. **Genauigkeit:**
    - Die Vorhersage des nächsten Wertes ist normalerweise genau.
    - Wenn wir die Vorhersage für die nächsten 10 Schritte testen, wird der mittlere quadratische Fehler (MSE) etwa 0,029 sein. Das bedeutet, dass die Fehler sich summieren und die Genauigkeit abnimmt.

- Vergleich mit einfachen Methoden
1. **Naive Methode:**
    - Wir nehmen an, dass die Zeitreihe für die nächsten 10 Schritte konstant bleibt.
    - Diese Methode hat einen hohen Fehler (MSE von etwa 0,223).
2. **Einfaches lineares Modell:**
	- Ein lineares Modell versucht, die nächsten Werte anhand einer einfachen Linie vorherzusagen.
	- Diese Methode hat einen MSE von etwa 0,0188, was viel besser ist als die naive Methode und auch besser als unser RNN.
- Die schrittweise Vorhersage mit einem RNN kann nützlich sein, aber die Fehler summieren sich, was die Genauigkeit bei längeren Vorhersagen verringert.
- Für einfache Aufgaben oder kurze Vorhersagen kann ein RNN gut funktionieren, aber für komplexere Aufgaben oder längere Vorhersagen sind manchmal einfachere Modelle wie lineare Modelle besser und schneller zu trainieren.


- Die zweite Option besteht darin, ein RNN zu trainieren, das alle nächsten 10 Werte auf einmal vorhersagt. Wir können immer noch ein Sequenz-zu-Vektor-Modell verwenden, aber es wird 10 Werte statt 1 ausgeben.
- **Vorghehen**
	- Das RNN wird so modifiziert, dass es eine Ausgabe von 10 Werten anstelle von nur einem einzigen Wert liefert.
	- Das bedeutet, dass wir die letzte Schicht des RNNs so anpassen, dass sie 10 Ausgabeneinheiten hat.
- **Training**
	- Das Modell wird darauf trainiert, für jeden Zeitschritt die nächsten 10 Werte der Zeitreihe vorherzusagen.
	- Dies erfordert, dass die Zielwerte (Targets) entsprechend geändert werden, sodass sie die nächsten 10 Werte der Zeitreihe enthalten.
- Vorteile
	- Indem das RNN alle 10 nächsten Werte gleichzeitig vorhersagt, werden die Fehler nicht über mehrere Vorhersageschritte akkumuliert.
	- Dies kann die Genauigkeit der Vorhersagen verbessern, da das Modell direkt lernt, mehrere Werte gleichzeitig vorherzusagen.
- ![[Pasted image 20240614222020.png]]


- **Sequenz to Sequenz**
	- Wir können dieses Sequenz-zu-Vektor-RNN in ein Sequenz-zu-Sequenz-RNN umwandeln. Der Vorteil dieser Technik besteht darin, dass der Verlust (Loss) einen Term für die Ausgabe des RNN bei jedem einzelnen Zeitschritt enthält, nicht nur für die Ausgabe beim letzten Zeitschritt. 
	- Dies bedeutet, dass es viel mehr Fehlergradienten gibt, die durch das Modell fließen, und diese müssen nicht nur durch die Zeit fließen; sie fließen auch von der Ausgabe jedes Zeitschritts. Dies stabilisiert und beschleunigt das Training.
	- Um dies klarzustellen:
		- Bei Zeitschritt 0 wird das Modell einen Vektor ausgeben, der die Vorhersagen für die Zeitschritte 1 bis 10 enthält.
		- - Bei Zeitschritt 1 wird das Modell die Zeitschritte 2 bis 11 vorhersagen, und so weiter.
	- Jedes Ziel (Target) muss daher eine Sequenz mit der gleichen Länge wie die Eingabesequenz sein und an jedem Schritt einen 10-dimensionalen Vektor enthalten.
	-  !!! **Überschneidung zwischen Eingaben und Zielwerten:** In einem Sequenz-zu-Sequenz-RNN werden die Zielwerte so definiert, dass sie zukünftige Werte enthalten, die auch in den Eingabesequenzen vorkommen. Das bedeutet, dass YtrainY_{\text{train}}Ytrain​ Werte enthält, die bereits in XtrainX_{\text{train}}Xtrain​ enthalten sind, aber zeitlich versetzt.
	- **Keine Vorhersage in die Zukunft:** Das Modell ist so konstruiert, dass es nur auf vergangene Werte zugreifen kann, um zukünftige Vorhersagen zu treffen. Bei jedem Zeitschritt kennt das Modell nur die Werte der vergangenen Zeitschritte. Dadurch bleibt das Modell kausal und kann keine Informationen aus der Zukunft verwenden, um gegenwärtige Entscheidungen zu treffen.
	- **Kausales Modell:** Ein kausales Modell bezieht sich auf ein Modell, das nur auf vergangene und gegenwärtige Informationen zugreifen kann, aber nicht auf zukünftige. Das ist wichtig, um realistische Vorhersagen zu treffen, da in realen Szenarien zukünftige Informationen nicht verfügbar sind.
- TimeDistributed sorgt dafür, dass jedes Zeitschritt die Vorhersagen für die nächsten `forecast_steps` ausgibt.
- ![[Pasted image 20240614223424.png]]



### Handling long Sequences
- Um ein RNN auf langen Sequenzen zu trainieren, müssen wir es über viele Zeitschritte laufen lassen, wodurch das entrollte RNN zu einem sehr tiefen Netzwerk wird. Genau wie jedes tiefe neuronale Netzwerk kann es unter dem Problem der instabilen Gradienten leiden: Das Training kann sehr lange dauern oder instabil sein. Darüber hinaus wird ein RNN beim Verarbeiten einer langen Sequenz nach und nach die ersten Eingaben in der Sequenz vergessen.

### Fighting the unstable Gradients Problem
- Viele der Tricks, die wir bei tiefen Netzen verwendet haben, um das Problem der instabilen Gradienten zu lindern, können auch bei RNNs verwendet werden: gute Parameterinitialisierung, schnellere Optimierer, Dropout und so weiter. 
- Allerdings können nicht-sättigende Aktivierungsfunktionen (z. B. ReLU) hier möglicherweise nicht so hilfreich sein; tatsächlich können sie dazu führen, dass das RNN während des Trainings noch instabiler wird.
- Warum?
- Angenommen, der Gradient Descent-Algorithmus aktualisiert die Gewichte so, dass die Ausgaben beim ersten Zeitschritt leicht erhöht werden. Da dieselben Gewichte bei jedem Zeitschritt verwendet werden, können auch die Ausgaben beim zweiten Zeitschritt leicht erhöht werden, und beim dritten und so weiter, bis die Ausgaben explodieren—und eine nicht-sättigende Aktivierungsfunktion verhindert das nicht.
- **Problem:** Bei jedem Zeitschritt werden dieselben Gewichte verwendet. Wenn eine Gewichtsaktualisierung die Ausgabe in einem frühen Zeitschritt leicht erhöht, werden alle nachfolgenden Ausgaben ebenfalls leicht erhöht. Diese kleinen Erhöhungen summieren sich über viele Zeitschritte.
- **Explodierende Ausgaben:** Im Laufe der Zeit können diese kumulativen Erhöhungen dazu führen, dass die Ausgaben explodieren (sehr große Werte annehmen).
- **Problem:** Da ReLU keine obere Schranke hat, kann es nicht verhindern, dass die Ausgaben explodieren, wenn die Gradientenaktualisierungen die Gewichte erhöhen.
- Lösungsmöglichkeiten:
	- perbolische Tangens (tanh) oder Sigmoid-Aktivierungsfunktionen, die die Ausgaben auf einen bestimmten Bereich begrenzen (tanh: [-1, 1], Sigmoid: [0, 1]).
		- **Vorteil:** Diese Funktionen verhindern, dass die Ausgaben unendlich groß werden, da sie eine Sättigungsebene haben.
	- Gradient Clipping
- Batch Normalization und RNNs
	- Bei RNNs kann Batch Normalization jedoch nicht so effizient eingesetzt werden.
	- Zwischen Zeitstufen nicht effizient
		- **Problem:** BN kann nicht effektiv zwischen den Zeitstufen eines RNNs verwendet werden, da die gleichen BN-Parameter für unterschiedliche Zeitstufen verwendet werden müssen. Dies bedeutet, dass die BN-Schicht die gleiche Skalierung und Verschiebung auf unterschiedliche Eingaben und versteckte Zustände anwendet, unabhängig von deren tatsächlichen Werten.
		- **Konsequenz:** Dies führt oft zu suboptimalen Ergebnissen.
	- Zwischen rekurrenten Schichten
		- **Effizienter Ansatz:** BN kann zwischen rekurrenten Schichten (vertikal in einer RNN-Architektur) angewendet werden. Dies bedeutet, dass BN auf die Eingaben der rekurrenten Schicht angewendet wird, bevor diese Schicht verarbeitet wird.
		- **Vorteil:** Laut einer Studie von César Laurent et al. (2015) ist BN leicht vorteilhaft, wenn es auf die Eingaben und nicht auf die versteckten Zustände angewendet wird. Es ist also besser als nichts, wenn es zwischen rekurrenten Schichten angewendet wird, aber nicht innerhalb der rekurrenten Schichten (horizontal).
-  Layer Normalization in RNNs
	- Normalisierung über die Merkmalsdimension:
		- **Batch Normalization:** Normalisiert über die Batch-Dimension.
		- **Layer Normalization:** Normalisiert über die Merkmalsdimension, also innerhalb jedes Zeitschritts für jede Instanz unabhängig.
	- Berechnung der Statistiken
		- **Batch Normalization:** Benötigt exponentiell gleitende Mittelwerte, um die Statistiken der Merkmale über alle Instanzen im Trainingssatz zu schätzen.
		- **Layer Normalization:** Berechnet die erforderlichen Statistiken bei jedem Zeitschritt für jede Instanz auf die gleiche Weise während des Trainings und der Testphase. Es müssen keine gleitenden Mittelwerte verwendet werden.
	- Verwendung in RNNs
		- **Layer Normalization:** Wird typischerweise direkt nach der linearen Kombination der Eingaben und der versteckten Zustände in RNNs verwendet.