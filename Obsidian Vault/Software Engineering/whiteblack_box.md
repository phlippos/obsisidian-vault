Kriterien
- 1A   weight <= 0.0  (ungültige Äquivalenzklasse)
- 1B   weight > 0.0 (gültige Äquivalenzklasse)
- 2A   weight  == 100.0 (gültige Äquivalenzklasse)
- 2B   weight >100.0 and weight <= 101.0 (gültige Äquivalenzklasse)
- 2C   weight > 101.0 and weight < 105.0 (ungültige Äquivalenzklasse)
- 2D   weight >= 105.0 and weight <= 175.0 (ungültige Äquivalenzklasse)
- 2E   weight > 175.0 (ungültige Äquivalenzklasse)

| Eingabe | Ausgabe          | Kriterium |     |
| ------- | ---------------- | --------- | --- |
| -1.0    | undefined        | 1A        |     |
| 100.0   | "perfect"        | 1B,2A     |     |
| 100.5   | "perfect"        | 1B,2B     |     |
| 102.0   | "manual check"   | 1B,2C     |     |
| 110.0   | "reject"         | 1B,2D     |     |
| 180.0   | "stop and check" | 1B,2E     |     |
|         |                  |           |     |
|         |                  |           |     |
|         |                  |           |     |
|         |                  |           |     |
3.
- Der Ansatz testet auf Softwarefehler, indem er die Eingabewerte an den Grenzen der zulässigen Bereiche überprüft.
- 0.0
- 100.0
- 101.0
- 101.1
- 105.0
- 175.0
- 175.1