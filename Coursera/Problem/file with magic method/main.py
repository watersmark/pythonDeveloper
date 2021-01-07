import os
import tempfile


class File:
    index = 1

    def __init__(self, path_to_file):

        if not os.path.exists(path_to_file):
            file = open(path_to_file, 'a+')

        self.path = path_to_file
        self.bool = False
        self.index = 0

    # чтение из файла
    def read(self):
        if os.path.exists(self.path):
            with open(self.path, 'r') as file:
                return file.read()

        return ''

    # запись в файл
    def write(self, info):
        with open(self.path, 'w') as file:
            file.write(info)

    # перегруженные методы
    def __add__(self, other):
        new_file = File(os.path.join(tempfile.gettempdir(), f"{File.index}.txt"))
        File.index += 1

        # считаем информацию из файлов
        result_str = ""
        result_str += (self.read() + other.read())
        # запишем информацию в файл
        new_file.write(result_str)

        return new_file

    def __str__(self):
        return self.path

    def __iter__(self):
        return self

    def __next__(self):
        temp = self.read().strip().split("\n")

        if self.index < len(temp):
            temp_index = self.index
            self.index += 1
            return (str(temp[temp_index]) + '\n')
        else:
            self.index = 0
            raise StopIteration





if __name__ == "__main__":
    path_to_file = 'some_filename'

    file_obj_1 = File(path_to_file + '_1')
    file_obj_2 = File(path_to_file + '_2')
    file_obj_1.write('line 1\n')

    file_obj_2.write('line 2\n')

    new_file_obj = file_obj_1 + file_obj_2

    print(isinstance(new_file_obj, File))
    print(new_file_obj)

    for line in new_file_obj:
        print(ascii(line))













