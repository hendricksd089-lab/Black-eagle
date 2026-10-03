int("The sky is blue")
str_manip = "The sky is blue"
print(len(str_manip)) #15
last_letter = str_manip[-1]
str_manip = str_manip.replace(last_letter, "@") 
print(str_manip)
last_letter = str_manip[-1]
str_manip = str_manip.replace(last_letter, "@")
print(str_manip)
print(str_manip[-1:-4:-1])
DECLARE str_manip AS STRING
SET str_manip TO "The sky is blue"

OUTPUT LENGTH(str_manip)

SET last_letter TO LAST CHARACTER OF str_manip
REPLACE all occurrences of last_letter IN str_manip WITH "@"
OUTPUT str_manip

SET last_letter TO LAST CHARACTER OF str_manip

OUTPUT REVERSE(FIRST 3 CHARACTERS OF str_manip)  // or:last 3 characters backwards