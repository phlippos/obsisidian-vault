1. 
	C0-Test : 
	- Der C0-Test zielt darauf ab, jede Anweisung im Code mindestens einmal auszuführen. Das bedeutet, dass jede Zeile des Codes mindestens einmal getestet werden muss.
	C1-Test:
	- Um eine vollständige Zweigüberdeckung zu erreichen, müssen wir sicherstellen, dass jede Verzweigung sowohl für den `true`- als auch für den `false`-Fall getestet wird. Das bedeutet, dass wir jede Bedingung im Code sowohl wahr als auch falsch testen müssen.
	C2-Test
	- Ein C2-Test zielt darauf ab, alle möglichen Pfade durch den Code abzudecken. Das bedeutet, dass jede mögliche Kombination von Verzweigungen im Code getestet wird.
	Unterschiede :
	- C0: Fokus auf einzelne Anweisungen, unabhängig von den Bedingungen.
	- C1: Fokus auf alle Bedingungen und deren mögliche Ausgänge.
	- C2: Fokus auf alle möglichen Pfade durch den Code, inklusive aller Kombinationen von Bedingungen und Schleifen.
2. 
	- C2 ist Sehr aufwendig, da alle möglichen Pfade durch den Code getestet werden müssen, was zu einer exponentiellen Zunahme der Testfälle führen kann, insbesondere bei komplexem Code mit vielen Verzweigungen und Schleifen.
3. 
	- C2a : alle möglichen Pfade werden durchlaufen.  Schwierigkeiten: unmöglich bei Schleifen.
	- C2b : Schleifen werden nach speziellen Regeln durchlaufen.  Schwierigkeiten : aufwendig
	- C2c : Schleifen werden genau n-mal durchlaufen.  Schwierigkeiten : aufwendig