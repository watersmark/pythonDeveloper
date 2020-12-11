def to_jaden_case(string):
    stringResult = ""

    countMass = 1
    countSplit = len(string.split(" "))

    for elem in string.split(" "):
        stringResult += elem[0].upper() + elem[1:]
        stringResult += "" if (countMass == countSplit) else " "
        countMass += 1
    return stringResult

print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
