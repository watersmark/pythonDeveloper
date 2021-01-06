# можно переопределить сложение объектов
# для этого используем метод __add__(self, other)


class Integer(object):

    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return self.number + other.number


first = Integer(5)
second = Integer(6)
print(first + second)
