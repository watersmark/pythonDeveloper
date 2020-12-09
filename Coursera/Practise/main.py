# форматирование строк

# передаём placeholder
str = "{} не лгут, а лгут {}".format('Цифры', "люди")
print(str)

# передам именованный placeholder
# неименованные аргументы указать уже нельзя
problem = "задач"
str = "{num} Кб должно хватить для {problem}".format(
    num = 640, problem=problem)
print(str)

# f-строки
subj = "optimize"
auth = 'Knuth'

print(f"Преждевременная {subj} - плохо. Автор {auth}")


# вывод чисел с модификаторами
num = 2 / 3
print(f"{num:.3f}")
print("{num:.3f}".format(num=num))