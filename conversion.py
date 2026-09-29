DECLARE myDecimal AS REAL
DECLARE myInteger AS INTEGER

SET myDecimal TO 99.23
SET myInteger TO INTEGER(myDecimal)

OUTPUT myInteger

DECLARE myInteger AS INTEGER
DECLARE myFloat AS REAL

SET myInteger TO 23
SET myFloat TO REAL(myInteger)

OUTPUT myFloat

DECLARE myNumber AS INTEGER
DECLARE myString AS STRING

SET myNumber TO 150
SET myString TO STRING(myNumber)

OUTPUT myString

DECLARE string1 AS STRING
DECLARE number1 AS INTEGER

SET string1 TO  "100"
SET number1 TO INTEGER(string1)

OUTPUT number1
