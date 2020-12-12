def duplicate_encode(word):
    word = word.lower()
    mapItem = dict()
    resString = ""

    for elem in word:
        if elem not in mapItem:
            mapItem[elem] = 1
        else:
            mapItem[elem] = mapItem[elem] + 1

    for elem in word:
        resString += ")" if mapItem[elem] > 1 else "("

    return resString

print(duplicate_encode("(( @"))