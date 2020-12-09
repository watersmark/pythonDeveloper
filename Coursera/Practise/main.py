# методы строк
quote = "покажите мне код"

# метод нахождения колличества букв в строке
print(quote.count('о'))

# сделать первую букву большой
print(quote.capitalize())

# позволяет проверить является ли строка числом
tempStr = '2017'
print(tempStr.isdigit())

# оператор in позволяет проверить содержится ли
# подстрока в строке
tempStr = 'Hello'
print('lo' in tempStr)

# преобразования строк
num_string = str(999.01)
print(num_string, type(num_string))

# иттерация по строке
for elem in num_string:
    print(elem, end="")

