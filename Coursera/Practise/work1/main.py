def unique_in_order(iterable):
    massSet = []

    for index in range(len(iterable)):
        if index == 0:
            massSet.append(iterable[index])
        else:
            massSet.append(iterable[index]) if iterable[index - 1] != iterable[index] else None

    return massSet

print(unique_in_order('AAAABBBCCDAABBB'))