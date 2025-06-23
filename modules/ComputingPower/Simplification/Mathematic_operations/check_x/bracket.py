r"""
Проверка, и проведение действий в скобочках c X
"""
from .degree import degree_x
from .division import division_x
from .logarithm import logarithm_x
from .radical import radical_x
from .trigonometric_functions import trigonometric_functions_x
from ...cut_function import cut_function

def bracket_calculating_x(function: list):
    result_degree = None
    result_trigonometric = None
    result_radical = None
    result_division = None
    result_logarithm = None
    
    function[0] = function[0][1:]
    function[0] = function[0][:-1]
    function = cut_function(function)

    if len(function) == 1:
        return None
    if function[0] == "-" and len(function) == 2:
        return None

    for part in function:
        if "^" in part:
            index = function.index(part)
            if len(part) == 1:
                list_degree = [function[index + 1]]
                index_degree = index
                result_degree = degree_x(function[index - 1], list_degree)
    if result_degree != None:
        del function[result_degree + 1]
        del function[result_degree]
        for i in range(len(result_degree)):
            function.insert(index_degree + i, result_degree[i])

    list_trigonometric_c = {}
    for part in function:
        if "sin" in part or "cos" in part or "tg" in part:
            index = function.index(part)
            if function[index] == "sin" or function[index] == "cos": len_t = 3
            else: len_t = 2
            if len(part) == len_t:
                list_trigonometric = [function[index + 1]]
                index_trigonometric = index
                result_trigonometric = trigonometric_functions_x(list_trigonometric, f"{function[index]}")
                list_trigonometric_c[f"{index_trigonometric}"] = result_trigonometric
    if len(list_trigonometric_c) != 0:
        for idx in sorted(list_trigonometric_c.keys(), key=int, reverse=True):
            index = int(idx)
            values = list_trigonometric_c[idx]
            del function[index + 1]
            del function[index]
            for v in reversed(values):
                function.insert(index, v)

    for part in function:
        if "√" in part:
            index = function.index(part)
            if len(part) == 1:
                list_radical = [function[index + 1]]
                index_radical = index
                result_radical = radical_x(list_radical)
    if result_radical != None:
        del function[index_radical + 1]
        del function[index_radical]
        for i in range(len(result_radical)):
            function.insert(index_radical + i, result_radical[i])

    for part in function:
        if "/" in part:
            index = function.index(part)
            if len(part) == 1:
                next_part = str(function[index + 1])
                if len(next_part) == 3:
                    list_division_f = [function[index - 1]]
                    list_division_s = [function[index + 1]]
                    index_division = index
                    result_division = division_x(list_division_f, list_division_s)
    if result_division != None:
        del function[index_division + 1]
        del function[index_division]
        del function[index_division - 1]
        for i in range(len(result_division)):
            function.insert(index_division - 1 + i, result_division[i])

    for part in function:
        if "log" in part or "ln" in part:
            index = function.index(part)
            if f"{function[index]}" == "log":
                if len(part) == 3:
                    list_logarithm_f = [function[index + 1]]
                    list_logarithm_s = [function[index + 2]]
                    index_logarithm = index
                    result_logarithm = logarithm_x(list_logarithm_f, list_logarithm_s, "log")
            else:
                if len(part) == 2:
                    list_logarithm_f = [function[index + 1]]
                    index_logarithm = index
                    result_logarithm = logarithm_x(list_logarithm_f, None, "lg")
    if result_logarithm != None:
        del function[index_logarithm + 1]
        del function[index_logarithm]
        for i in range(len(result_logarithm)):
            function.insert(index_logarithm + i, result_logarithm[i])

    for part in function:
        if "(" in part:
            list_bracket = [function[index]]
            result_bracket = bracket_calculating_x(list_bracket)
            if result_bracket != None:
                index_bracket = index
    if result_bracket != None:
        del function[index_bracket]
        for i in range(len(result_bracket)):
            function.insert(index_bracket + 1 + i, result_bracket[i])
    
    return function