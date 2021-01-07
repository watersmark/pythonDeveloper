# в данном модуле рассмотрим создание контекстных менеджеров
# для их создания задаём магические методы enter и exit
# классы контекстных менеджеров задаются с маленькой буквы


class my_context_manager(object):

    def __init__(self, filename, mode):
        self.file = open(filename, mode)

    def __enter__(self):
        return self.file

    def __exit__(self, *args):
        self.file.close()

with my_context_manager('text.txt', 'w') as file:
    file.write('good day')
