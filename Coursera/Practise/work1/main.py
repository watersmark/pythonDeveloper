
# сделаем обход и будем выбирать два числа
# либо равных, либо больших
# заведём две переменные для иттерации
def productFib(prod):

    firstDigit = 0
    secondDigit = 1

    while True:
        if firstDigit * secondDigit < prod:
            firstDigit, secondDigit = secondDigit, firstDigit + secondDigit
            continue
        if firstDigit * secondDigit == prod:
            return [firstDigit, secondDigit, True]
        else:
            return [firstDigit, secondDigit, False]


print(productFib(714))
print(productFib(800))