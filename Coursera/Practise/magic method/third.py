# рассмотрим методы для работы с атрибутами объекта
# атрибут __getattribute__(self, item) вызывается самым первым при обращении к
# атрибуту объекта
# метод __getattr__(self, item) будет вызван если атрибут не найден
# если его не переопределить будет выброшена ошибка
# аттрибут __setattr__(self, key, value) переопределяет создание аттрибута
# для удаления аттрибута спользуем __getattr__
# для вызова объекта, как функции используем __call__(self, *args, **kwargs)


# все аттрибуты можно создать используя внутри метода их object.__setattr__(self, key, value)
# object__getattr__ не существует и вызывается через object.__getattribute__


class Researcher(object):

    def __init__(self, name):
        self.name = name

    def __getattr__(self, item):
        return "Nothing found"

    def __getattribute__(self, item):
        print(f"Looking for {item}")
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        object.__setattr__(self, key, value)

    def __delattr__(self, name):
        value = object.__getattribute__(self, name)
        print(value)
        object.__delattr__(self, name)

    def __call__(self, *args, **kwargs):
        print(*args)

# getattr
first_search = Researcher("Tolan")
print(first_search.name)
print(first_search.age)

# setattr
first_search.color = 'red'
print(first_search.color)

# delattr
del first_search.color

# __call__
first_search(1, 3)

