# рассмотрим магические методы
# первый метод это метод __new__(cls)

# в данном примере мы переопределяем возвращаемую ссылку на класс ещё до его инициализации
# и реализуем паттерн Singleton
# метод init отработает после метода new


class Singleton:
    instance = None

    def __new__(cls, name):

        print("init cls start")

        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, name):
        print("init start")
        self.name = name

    def get_name(self):
        return self.name

a = Singleton("Tolan")
print(a.get_name())

b = Singleton("Kolan")
print(b.get_name())
print(a.get_name())

print(a is b)
