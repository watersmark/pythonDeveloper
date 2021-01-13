# найти самую длинную последовательность одинаковых цифр

str = None
with open("E:\Download\Yandex\\pi.txt", "r") as file:
    str = file.read()[3:]

print(str)
counts = 6
count_now = 0


for index in range(len(str)):
    if str[index] == '9':
        count_now += 1

        if count_now == 6:
            print(index - (6 - 2))
    else:
        count_now = 0


# max_count = 0
# elem = None
#
# new_count = 0
# elem_now = None
#
# for index in range(len(str)):
#     if index == 0:
#
#         elem_now = str[index]
#         elem = str[index]
#         new_count = 1
#
#         continue
#
#     if str[index] == elem_now:
#         new_count += 1
#     else:
#         if max_count < new_count:
#             max_count = new_count
#             elem = elem_now
#
#         elem_now = str[index]
#         new_count = 1
#
# if max_count < new_count:
#     max_count = new_count
#     elem = elem_now
#
# print(f"Elem is {elem};", f"Count elem is {max_count}")
#
