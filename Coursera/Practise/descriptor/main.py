# рассмотрим работу дескрипторов
# атрибуты всегда пишутся без self
# иначе нам вернётся расположение объекта в памяти
# так же есть метод __sots__, который определяет
# атрибуты только экземпляра класса, для атрибутов класса это не работает


class ImportantValue(object):
    __slots__ = ['amount']

    def __init__(self, money=0):
        print('init')
        self.amount = money

    def __get__(self, obj, obj_type):
        return self.amount

    def __set__(self, obj, value):
        self.amount = value * 10


class UserMoney(object):
    __slots__ = ['tt', 'money_people']

    moneys = ImportantValue()

    def __getattr__(self, item):
        print('no attr')

    def __getattribute__(self, item):
        print("attr get now")
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        print('set attr')
        object.__setattr__(self, key, value)


user_first = UserMoney()
print(user_first.moneys)

user_first.moneys = 20
print(user_first.moneys)

del UserMoney.moneys
print(user_first.moneys)
