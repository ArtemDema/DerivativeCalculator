r"""
Обработка действий плюса и минуса
"""

def sun_and_minus_calculating(function: list, sum, minus):
    if function != None:
        for part in function:
            if "x" in part:
                return function

    for i in range(5):
        for part in function:
            index = function.index(part)
            if "+" in part:
                if len(part) == 1:
                    list_sum = []
                    if index - 2 >= 0:
                        if function[index - 2] == "-":
                            list_sum.append(function[index - 2])
                    list_sum.append(function[index - 1])
                    result = sum(function[index - 1], function[index + 1])
                    if result != None:
                        del function[index + 1]
                        del function[index - 1]
                        del function[index - 1]
                        function.insert(index - 1, str(result))

            if "-" in part:
                if len(part) == 1:
                    if index != 0:
                        list_minus = []
                        if index - 2 >= 0:
                            if function[index - 2] == "-":
                                list_minus.append(function[index - 2])
                        list_minus.append(function[index - 1])
                        result = minus(list_minus, function[index + 1])
                        del function[index - 1]
                        del function[index - 1]
                        del function[index - 1]
                        function.insert(index - 1, str(result))
                    else:
                        function[index] = f"{function[index]}{function[index + 1]}"
                        del function[index + 1]

    return function