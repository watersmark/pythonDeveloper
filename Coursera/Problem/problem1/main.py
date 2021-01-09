from functools import reduce

def variance(numbers):
    # считаем среднее
    # mean = reduce(lambda x, y: x + y, numbers) / len(numbers)
    mean = 0
    for elem in numbers:
        mean += elem
    mean = mean / len(numbers)

    # считаем дисперсию
    dispers = 0
    for elem in numbers:
        dispers += (elem - mean) ** 2

    return dispers / len(numbers)



a = [1.5, 2.5, 4, 2, 1, 1]
print(variance(a) == 1.0833333333333333)


"""
[1, 2, 2, 3]
"""