def is_isogram(string):
    myMap = dict()

    for elem in string:
        if myMap.get(elem[0].upper()) == None:
            myMap[elem.upper()] = 1
        else:
            return False

    return True

print(is_isogram("Dermatoglyphics"))
print(is_isogram("moOse"))