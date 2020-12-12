def spin_words(sentence):
    resString = ""

    countElem = 1
    for elem in sentence.split(" "):
        resString += elem if len(elem) < 5 else elem[::-1]
        resString += " " if countElem != len(sentence.split(" ")) else ""
        countElem += 1
    return resString

print(spin_words("Welcome"))