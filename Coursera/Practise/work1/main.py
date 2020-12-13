# чтобы словарь мог помнить порядок вхождения элементов

from  collections import  OrderedDict

ordered = OrderedDict()
for number in range(10):
    ordered[number] = str(number)

for key in ordered.keys():
    print(key)