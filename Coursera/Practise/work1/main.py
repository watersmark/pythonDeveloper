# возьмём два указателя
# будем передвигать их по алгоритму ниже для перетаскивания  элементов
def move_zeros(array):
    first_cursor = 0  # main
    second_cursor = 0  # support

    for elem in array:
        if elem != 0 or isinstance(elem, bool):
            array[first_cursor], array[second_cursor] = array[second_cursor], array[first_cursor]
            first_cursor += 1
            second_cursor += 1
        else:
            first_cursor += 1

    return array


print(move_zeros([False, 1, 0, 1, 2, 0, 1, 3, "a"]))
