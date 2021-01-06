# рассмотри ещё два метода это
# __hash__(self)  и __eq__(self, other)
# первый метод переопределяет hash у объекта
# второй метод переопределяет операцию сравнения объектов


class User(object):

    def __new__(cls, name):
        return super().__new__(cls)

    def __init__(self, name):
        self.name = name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name


first_user = User('Kolan')
second_user = User('Kolan')

print(first_user == second_user)
print(hash(first_user) == hash(second_user))