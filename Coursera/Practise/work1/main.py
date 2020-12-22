# rec func to check mass
def same_structure_as(original, other):
    try:
      

        if len(original) != len(other):
            return False
        temp_res = True

        # делаем рекурсивные шаги
        for index in range(len(original)):

            if type(original[index]) == type(other[index]) or (issubclass(type(original[index]), (int, str)) and issubclass(type(other[index]), (int, str))):
                if isinstance(original[index], list):
                    temp_res = same_structure_as(original[index], other[index])

                    # если из функции вернулся None
                    if temp_res == None:
                        temp_res = True
                else:
                    if index == len(original) - 1:
                        return True
            else:
                return False

            # выходим из функции
            if not temp_res:
                return False

        return True
    except:
        return False


print(same_structure_as([1,'[',']'], ['[',']',1]))

