def find_outlier(integers):
    isOdd = 0
    isEven = 0

    for elem in integers[0:4]:
        if elem % 2 == 0:
            isEven += 1
        else:
            isOdd += 1

    boolIsOdd = False
    if isOdd > isEven:
        boolIsOdd = True

    for elem in integers:
        if boolIsOdd:
            if elem % 2 == 0:
                return elem
        else:
            if elem % 2 != 0:
                return elem


print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))