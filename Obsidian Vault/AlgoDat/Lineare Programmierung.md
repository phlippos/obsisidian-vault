>Vereinfacht ausgedrückt ist es die Methode herauszufinden, wie man etwas am besten macht. Bei begrenzten Ressourcen müssen Sie die Ressourcen optimal nutzen und das bestmögliche Ergebnis in Bezug auf ein bestimmtes Ziel erzielen, z. B. geringste Kosten, höchste Marge oder kürzeste Zeit.
>
>Die Situation, die eine Suche nach den besten Werten der Variablen erfordert, die bestimmten Einschränkungen unterliegen, ist die Verwendung linearer Programmierprobleme. Diese Situationen können mit den üblichen Berechnungs- und numerischen Techniken nicht bewältigt werden.
>**Komponenten der linearen Programmierung**
>	- **Entscheidungsvariablen** : Variablen, die Sie bestimmen möchten, um die optimale Lösung ze erreichen
>	- **Zielfunktion** : Mathematische Gleichung, die das Ziel darstellt, das Sie erreichen möchten
>	- **Einschränkungen** : Einschränkungen oder Restriktionen, denen Ihre Entscheidungsvariablen folgen müssen
>	- **Nicht-Negativitätsbeschränkungen:** In einigen realen Szenarien können Entscheidungsvariablen nicht negativ sein
>**Zusätzliche Merkmale der linearen Programmierung**
>	- **Endlichkeit:*** Die Anzahl der Entscheidungsvariablen und Einschränkungen in einem LP-Problem ist endlich.
>	- **Linearität:*** Die Zielfunktion und alle Einschränkungen müssen lineare Funktionen der Entscheidungsvariablen sein ****.**** Das bedeutet, dass der Grad der Variablen eins sein sollte.
>**Wie löst man lineare Programmierprobleme?**
****Schritt 1:**** Markieren Sie die Entscheidungsvariablen im Problem.
****Schritt 2:**** Erstellen Sie die Zielfunktion des Problems und prüfen Sie, ob die Funktion minimiert oder maximiert werden muss.
****Schritt 3:**** Notieren Sie alle Randbedingungen der linearen Probleme.
****Schritt 4:**** Stellen Sie sicher, dass die Entscheidungsvariablen nicht negative Einschränkungen aufweisen.
****Schritt 5:**** Lösen Sie nun das lineare Programmierproblem mit einer beliebigen Methode. Im Allgemeinen verwenden wir entweder die Simplex- oder die grafische Methode.

### **Lineare Programmiermethoden**
1. Simplex-Methode
2. grafische Methode

#### 1. Simplex-Methode
* Bei dieser Methode wiederholen wir eine bestimmte Bedingung mehrmals, bis eine optimale Lösung erreicht ist.
****Schritt 1:**** Formulieren Sie die linearen Programmierprobleme basierend auf den gegebenen Einschränkungen.

****Schritt 2:**** Wandeln Sie alle gegebenen Ungleichungen in Gleichungen oder Gleichheiten der linearen Programmierprobleme um, indem Sie bei Bedarf die Slack-Variable zu jeder Ungleichung hinzufügen.

****Schritt 3:**** Erstellen Sie die anfängliche Simplex-Tabelle. Indem Sie jede Einschränkungsgleichung in einer Zeile darstellen und die Zielfunktion in die untere Zeile schreiben. Die so erhaltene Tabelle wird Simplex-Tabelle genannt.

****Schritt 4:**** Identifizieren Sie den größten negativen Eintrag in der unteren Zeile. Die Spalte des Elements mit dem höchsten negativen Eintrag wird als Pivot-Spalte bezeichnet

****Schritt 5:**** Teilen Sie die Einträge der Spalte ganz rechts durch die Einträge der jeweiligen Pivot-Spalte, mit Ausnahme der Einträge der untersten Zeile. Jetzt wird die Zeile mit den wenigsten Einträgen als Pivotzeile bezeichnet. Das Pivot-Element ergibt sich aus dem Schnittpunkt der Pivot-Zeile und der Pivot-Spalte.

****Schritt 6:**** Setzen Sie mithilfe der Matrixoperation und mithilfe des Pivot-Elements alle Einträge in der Pivot-Spalte auf Null.

****Schritt 7:**** Überprüfen Sie die unterste Zeile auf nicht negative Einträge. Wenn in der unteren Zeile keine negativen Einträge vorhanden sind, beenden Sie den Vorgang, andernfalls starten Sie den Vorgang erneut ab Schritt 4.

****Schritt 8:**** Die so erhaltene endgültige Simplex-Tabelle liefert die Lösung unseres Problems.

- Maximale #Pivots in der Praxis meistens 2(m+n)
- Keine Regel für die Auswahl der Pivots garantiert polynomielle Laufzeit
- Die meisten Regeln führen zu exponentieller Laufzeit (worst-case)
- Endlossschleife (Ausartung/Degeneracy) möglich, wenn man zwischen
  denselben Extrempunkten hin- und herspringt.
- Die Auswahlregel von Blend (Blend’s rule) garantiert endliche Anzahl von Pivotelementen.
Blend’s rule: wähle immer das erste Element mit positivem Koeffizienten im
Zielfunktion.
  (CPLEX, COINIOR, mosek, AMPL, AIMMS, ...)

### ** Graphische Darstellung**
Die grafische Methode ist eine andere Methode als die Simplex-Methode, die zur Lösung linearer Programmierprobleme verwendet wird. Wie der Name schon sagt, verwendet diese Methode Graphen, um die gegebenen linearen Programmierprobleme zu lösen. Dies ist die beste Methode zur Lösung linearer Programmierprobleme und erfordert weniger Aufwand als die Simplex-Methode. 

Mit dieser Methode zeichnen wir alle Ungleichungen auf, die in den gegebenen linearen Programmierproblemen Einschränkungen unterliegen. Sobald alle Ungleichungen des gegebenen LPP im XY-Graphen aufgetragen sind, ergibt der gemeinsame Bereich aller Ungleichungen die optimale Lösung. Alle Eckpunkte des zulässigen Bereichs werden berechnet und der Wert der Zielfunktion an allen diesen Punkten wird berechnet. Durch den Vergleich dieser Werte erhalten wir die optimale Lösung des LPP.
![[Pasted image 20240503230131.png]]
![[Pasted image 20240503230259.png]]