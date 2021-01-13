def snail(snail_map):
    # массив для хранения результата
    result_str = []

    # проход по строкам
    row = len(snail_map[0])
    # проход по столбцам
    col = len(snail_map[0]) - 1

    # позиция массива
    x_pos = 0
    y_pos = -1

    for index in range(2 * (len(snail_map[0]) - 1) + 1):
        # идём вправо общий
        if index % 4 == 0:
            if index == 0:
                for steps in range(row):
                    result_str.append(snail_map[x_pos][y_pos + 1])
                    y_pos += 1
            else:
                for _ in range(row):
                    result_str.append(snail_map[x_pos][y_pos + 1])
                    y_pos += 1
            row -= 1

        # идём вниз
        if index % 4 == 1:
            for _ in range(col):
                result_str.append(snail_map[x_pos + 1][y_pos])
                x_pos += 1
            col -= 1
        # идём влево

        if index % 4 == 2:
            for _ in range(row):
                result_str.append(snail_map[x_pos][y_pos - 1])
                y_pos -= 1
            # y_pos += 1
            row -= 1

        # идём вверх
        if index % 4 == 3:
            for _ in range(col):
                result_str.append(snail_map[x_pos - 1][y_pos])
                x_pos -= 1
            col -= 1

    return result_str

# вводим сколько будет строк
count = int(input())
snail_map = []

# вводим строки
for _ in range(count):
    snail_map.append(input().split(" "))

print(snail(snail_map))
