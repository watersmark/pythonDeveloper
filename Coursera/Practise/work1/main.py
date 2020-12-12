def filter_list(l):
    return [elem for elem in l if isinstance(elem, int)]

print(filter_list([1,2,'a','b']))

