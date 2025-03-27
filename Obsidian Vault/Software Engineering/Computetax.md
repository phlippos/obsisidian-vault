Kriterium 1A : income <= 10.000
Kriterium 1B : 10.001 <= income && income <= 20.000
Kriterium 1C : 20.001 <= income && income <= 30.000
Kriterium 1D : income >= 30.001


| ID  | Eingabe        | Ausgabe | Kriterium |
| --- | -------------- | ------- | --------- |
| TF1 | income =10000  | 0       | 1A        |
| TF3 | income = 20000 | 1000    | 1B        |
| TF3 | income = 20001 | 1002    | 1C        |
| TF4 | income = 30000 | 3000    | 1D        |
| TF5 | income = 30001 | 3003    | 1E        |
|     |                |         |           |
