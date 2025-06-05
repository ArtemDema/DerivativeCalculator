r"""
Корень
"""
import math


def radical(function: list, minus, sum, multiplication):
    for i in range(len(function)):
        function[i] = function[i].replace("(", "").replace(")", "")

    for part in function:
        if "*" in part:
            index_f = function.index(part)
            result_f = multiplication(function[index_f - 1], function[index_f + 1])
            del function[index_f - 1]
            del function[index_f - 1]
            del function[index_f - 1]
            function.insert(index_f - 1, result_f)

        if "+" in part:
            index_f = function.index(part)
            result_f = sum(function[index_f - 1], function[index_f + 1])
            del function[index_f - 1]
            del function[index_f - 1]
            del function[index_f - 1]
            function.insert(index_f - 1, result_f)
    
        if "-" in part:
            index_f = function.index(part)
            result_f = minus(function[index_f - 1], function[index_f + 1])
            del function[index_f - 1]
            del function[index_f - 1]
            del function[index_f - 1]
            function.insert(index_f - 1, result_f)
    
    return math.sqrt(int(function[0]))