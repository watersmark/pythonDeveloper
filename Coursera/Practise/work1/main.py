# python коллекции

# рассмотрим список и его методы
# данными способами можно инициализировать list
empty_list = []
empty_list = list()
user_list = [1, ['name', True], 23.45]

# срез списка (последний элемент
# не входит в список
# при получени среза получается новый объект
print(user_list[1:2])

# добавление и расширение списков
tempList = ["new", "list"]
user_list.extend(tempList)  # расширение
print(user_list)

tempList.append(5)  # добавление
print(tempList)

tempList += 'a'  # ущё один способ добавления

# метод для форматирования списков join
print(", ".join([str(elem) for elem in tempList]))

# сортировка в list
# list.sort сортирует исходный список возвращвет None
# sorted(list) возвращает отсортированную копию списка
tempSort = [1, 3, 2, 0, 8, 6]

print(sorted(tempSort, reverse=True))  # вернулась копия

tempSort.sort(reverse=True)  # обратный порядок сортировки
print(tempSort)
