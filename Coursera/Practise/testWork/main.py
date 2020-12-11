import sys

digit_string = sys.argv[1]

sumDigits = 0
for elem in digit_string:
    sumDigits += int(elem)

print(sumDigits)