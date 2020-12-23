def summary_res(map_str):
    another_add = (1, 5)

    result_sum = 0

    for key in map_str:
        if key != 1:
            if key in another_add: result_sum += key * (map_str[key] // 3) * 100 + 50 * (map_str[key] - (map_str[key] // 3) * 3)
            else: result_sum += key * (map_str[key] // 3) * 100
        else:
            result_sum += (map_str[key] // 3) * 1000 + 100 * (map_str[key] - (map_str[key] // 3) * 3)

    return result_sum


def score(dice):
    map_str = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6 : 0}

    for digit in dice:
        map_str[digit] += 1

    return summary_res(map_str)


print(score([2, 4, 4, 5, 4]))

