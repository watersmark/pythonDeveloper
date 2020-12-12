def digital_root(n):

    if len(str(n)) == 1:
        return int(n)

    return digital_root(str(sum([int(elem) for elem in str(n)])))

print(digital_root(132189))

# string = "942"
# digit = sum([int(elem) for elem in string])
#
# print(digit)
#

