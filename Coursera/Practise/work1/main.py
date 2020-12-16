# пройдёмся по всему массиву
# и найдём локальные максимумы и минимумы
def pick_peaks(arr):

    pos_mass = []
    peaks_mass = []

    pos_cursor = 0
    doing_step = 0
    is_plato = False
    minus_count = 0
    different_count = 0

    for index in range(len(arr) - 1):
        doing_step += 1

        if arr[index] <= arr[index + 1]:

            if arr[index] == arr[index + 1]:
                minus_count += 1
                is_plato = True
            else:
                is_plato = False
                different_count += 1
        else:
            different_count += 1

            if doing_step > 1 and different_count > 1:

                if is_plato:
                    pos_mass.append(index - minus_count)
                    peaks_mass.append(arr[index])
                else:
                    pos_mass.append(index)
                    peaks_mass.append(arr[index])

            minus_count = 0
            doing_step = 0
            is_plato = False
            different_count = 0

    return {"pos" : pos_mass, "peaks" : peaks_mass}

result = pick_peaks([2,1,3,2,2,2,2,1])
print(result["pos"])
print(result["peaks"])