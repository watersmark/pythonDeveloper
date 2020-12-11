def friend(x):

    massFriends = []
    for elem in x:
        massFriends.append(elem) if (len(elem) == 4) else None

    return massFriends

print(friend(["Ryan", "Kieran", "Mark"]))