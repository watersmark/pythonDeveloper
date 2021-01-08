# метаклассы нужны для создания других классов
# общим метаклассом является type
# он реализован замыканием на уровне C
# если один класс является общим для потомков, то потомки
# будут создаваться по тому же образцу(Meta), что и их родитель


class Meta(type):

    def __new__(cls, name, bases, attrs):
        print(f'Create new {name}')
        return super().__new__(cls, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        print(f"Creating {name}")

        if not hasattr(cls, 'registry'):
            cls.registry = {}
        else:
            cls.registry[name.lower()] = cls

        super().__init__(name, bases, attrs)

class Base(metaclass=Meta): pass

class A(Base): pass

class B(Base): pass