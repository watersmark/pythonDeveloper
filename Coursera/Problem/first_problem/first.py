
# найти 12

str = None
with open("E:\Download\Yandex\pi.txt", "r") as file:
    str = file.read()

str = str[3:]
req_mass = "12"
count = 0
pos_mass = []

for index in range(len(str)):
    if str[index] == req_mass[count]:
        count += 1

        if count == len(req_mass):
            pos_mass.append(index - (len(req_mass) - 1))
            count = 0
    else:
        count = 0

print(pos_mass, len(pos_mass), sep="\n")
