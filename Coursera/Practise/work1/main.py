# словари dict()

# словари хэшируются получаем значения за константное время
empty_dict = {}
empty_dict = dict()

# если обратиться к словарю по ключу
# которого не существует, то будет ошибка
# для этого используем метод get
testMap = dict([[1, 2], ['a', 3], ['a', 4]])
print(testMap.get(7, 'not found'))

# в словарь можно добавлять и удалаять элементы
testMap['test'] = 32 # удаление элемента
print(testMap)

del testMap['a']  # удаление элмента
print(testMap)

# удаляем элемент и возвращаем его значение
print(testMap.pop(1))


# для иттерации по словарю
testMap = dict([['a', 11], ['b', 12], [32, 'ds']])

for elem in testMap.items():
    print(elem[1])

