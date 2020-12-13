# множества являются хешируемыми

# инициализация множеств
oddSet = set()
evenSet = set()

# добавление элемента множества
oddSet.add(3)
oddSet.add("3")
print(oddSet)

# удаление элемента множества
oddSet.remove(3)
print(oddSet)

# чтобы сделать множество неизменяемым
# в данное множество сы не можем добавлятьи удалять элементы
frozen = frozenset(['Anna', "Rana"])

# frozen.add(3) так не получится сделать

