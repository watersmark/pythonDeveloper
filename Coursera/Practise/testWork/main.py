import sys

digit_string = sys.argv[1]

for index in range(1, int(digit_string) + 1):
    print("{empty}{symbol}".format(empty=(int(digit_string) - index) * " ", symbol=index * "#"))

