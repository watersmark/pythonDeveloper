# функции

# аргументы по умолчанию
def function_greet(name='unknown'):
    print(name)


function_greet()

# аргументы по умолчанию для каждой функции
# интерпретатор записывает в особые переменные
# поэтому изменяемы типы данных лучше не использовать, как значения по
# умолчанию, так как они могут быть дозаписаны

def append_one(arg=[]):
    arg.append(1)
    return arg

print(append_one())
print(append_one())

# надо было сделать тип по умолчанию, как None
def function(iterable=None):
    iterable = iterable or []
    return iterable

print(function())


# в python функции могут принимать неограниченное
# кол-во аргументов
# чтобы задать произвольнео число аргументов
# используем звёздочку в функции
# чтобы развернуть произвольное число аргументов
# так же используем звёздочку
# при разименовании словаря мы получаем озиционые аргументы
# и можем передать их в *args
def printer(*args):

    print(args) # кортеж
    print(*args) # отдельные элементы

printer(1, 3, 4, 5)


def print_arg(**args):
    print(args) # словарь ключ-значение

    for elem in args.items():   # получили отдельные значения
        print("{key}, {value}".format(key=elem[0], value=elem[1]))

print_arg(a=10, b=12)








