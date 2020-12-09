# ввод и вывод строк
#nameUser = input()
#print(nameUser)

# байтовые строки
# Русские символы не поддерживает
example_str = b"hello"
print(example_str, type(example_str))

for elem in example_str:
    print(elem, end=" ")
print()

# метод encode для строки
# поддерживает Русские символы
# каждый символ кодируется двумя буквами
example_str = "привет"

example_str = example_str.encode()
print(example_str)

# метод decode
example_str = example_str.decode()
print(example_str)