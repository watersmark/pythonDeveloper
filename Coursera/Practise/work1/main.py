def alphabet_position(text):
    text = text.lower()

    massAlphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                    's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    return " ".join([str(massAlphabet.index(elem) + 1) for elem in text if elem in massAlphabet])


print(alphabet_position("The sunset sets at twelve o' clock."))


