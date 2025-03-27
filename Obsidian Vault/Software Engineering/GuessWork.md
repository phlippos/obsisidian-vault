1.  die Methode add(T) kann nicht richtig funktioniert. z.B. das Duplikat wird nicht richtig behandelt.
	1. Erwartung : wenn ein schon in Set existierendes Element zu Set hinzugefügt wird, dann muss die Größe von Set unverändert bleiben.
2. die Methode remove(T) kann für ein Element verwendet werden, das nicht in Set vorkommt.
	1. Erwartung : wenn das der Fall ist, soll die Methode eine unerwartete Ausnahme werfen.
3. die Methode contains(T) kann ein Element nehmen, dessen Art nicht gleich mit der erwarteten Art ist.
	1. Erwartung : Werfen unexpected type error.
4. unexpected type error kann für alle Methode generiert werden, die auf ein bestimmtes Objekt als Input warten.