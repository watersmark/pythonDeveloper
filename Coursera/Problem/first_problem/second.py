# подсчитать сколько каждой цифры в данном файле
import collections

result_map = {}
mass_string = None

with open("E:\Download\Yandex\pi.txt", "r") as file:
    mass_string = file.read()

mass_string = mass_string[3:]

for elem in mass_string:
    if elem in result_map:
        result_map[elem] += 1
    else:
        result_map[elem] = 1

result_map = collections.OrderedDict(sorted(result_map.items()))
print(result_map)
