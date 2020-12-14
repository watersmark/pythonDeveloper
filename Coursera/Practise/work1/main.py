# функции

# функции могут быть аннотированны
# передаваемые значения могут несоответствовать типам
# типы нужны для понимания программистом или IDE
def add(x: int, y: int) -> int:
    print(x + y)

def mult(x: [], y: {}) -> None:
    print(x)


# в Python все значения передаются по ссылке
def multMass(firstTuple: (), secondMass: []) -> None:
    firstTuple = secondMass

# first = (1, )
# multMass(first, 3)
# print(first)


# в python есть именованные аргументы
def say(greeting: str, name: str) -> None:
    print("{greet} {name} !".format(greet=greeting, name=name))

say(name='Topa',greeting="Opa")
