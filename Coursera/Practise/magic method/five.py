# для переопределения взятия по индексу и добавления по индексу используем
# getitem и setitem
# позволяет работать с объектом, как со списком


class MyList(object):

    def __init__(self, original_list=None):
        self.container = original_list or []

    def __getitem__(self, index):
        return self.container[index - 1]

    def __setitem__(self, index, value):
        self.container[index - 1] = value

    def __str__(self):
        print(self.container)


numbers = MyList([1, 3, 4, 5])
print(numbers[2])
