# для чтения из файла, так же применяются
# команды readline и readlines
# readline считывает строку до символа ереноса строки
# readlines считывает все строки в массив строк

file = open('test.txt', 'r')
for elem in file.readlines():
    print(elem)

file.close()

# для удобной работы с файлами используем
with open('test.txt', 'r') as f:
    for line in f:  # считываем файл построчно можно было указать f.readlines()
        print(line)
