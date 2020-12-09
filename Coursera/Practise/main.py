# рассмотрим работу со строками как их задавать
# и так же как их экранировать

# Сырые строки обозначаются r
# и убирают экранирование символов, оставляя их как
# просто символы в строке
example_str = r"C:\\work\\"
print(example_str)

# строки можно переносить
# для этого используем обратный слеш
str2 = "this text is this text " \
       "this text is this text" \
       "this text is this text"
print(str2)

# для написания большого блока кода

str3 = """
        this text is this text 
        this text is this text
        this text is this text
"""
print(str3)

# строки можно объединять
# строки неизменяемые при сложении двух строк
# создаётся новый объект в памяти
# это можно узнать по адресу в памяти
str4 = "str4"
print(id(str4))
str4 += 'a'
print(id(str4))

# срезы строк
# [start:stop:step]
# срез может идти справа налево или
# слева направо главное помнить что он начнётся с элемента
# start, по умолчанию шаг 1, если указать только шаг -1
# то массив перевернётся

example_str = "Курс по Python на Coursera"

print(example_str[9:])
print(example_str[9:15])
print(example_str[-8:-2])
print(example_str[::-1])


