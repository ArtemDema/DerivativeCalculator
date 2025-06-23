r"""
Проверка, и проведение действий в скобочках c X
"""
from .degree import degree_x
from .division import division_x
from .logarithm import logarithm_x
from .radical import radical_x
from .trigonometric_functions import trigonometric_functions_x
from ...Simplification import cut_function

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
        return
    if function[0] == "-" and len(function) == 2:
        return None
    
    list_degree_c = {}
    for part in function:
        if "^" in part:
            index = function.index(part)
            if len(part) == 1:
                list_degree = [function[index + 1]]
                index_degree = index
                result_degree = degree_x(list_degree, f"{function[index]}")
                list_degree_c[f"{index_degree}"] = result_degree
    if len(list_degree_c) != 0:
        for idx in sorted(list_degree_c.keys(), reverse=True):
            index = int(idx)
            values = list_degree_c[idx]
            del function[index + 1]
            del function[index]
            for v in reversed(values):
                function.insert(index, v)

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
        for idx in sorted(list_trigonometric_c.keys(), reverse=True):
            index = int(idx)
            values = list_trigonometric_c[idx]
            del function[index + 1]
            del function[index]
            for v in reversed(values):
                function.insert(index, v)

    list_radical_c = {}
    for part in function:
        if "√" in part:
            index = function.index(part)
            if len(part) == 1:
                list_radical = [function[index + 1]]
                index_radical = index
                result_radical = radical_x(list_radical)
                list_radical_c[f"{index_radical}"] = result_radical
    if len(list_radical_c) != 0:
        for idx in sorted(list_radical_c.keys(), reverse=True):
            index = int(idx)
            values = list_radical_c[idx]
            del function[index + 1]
            del function[index]
            for v in reversed(values):
                function.insert(index, v)

    list_division_c = {}
    for part in function:
        if "/" in part:
            index = function.index(part)
            if len(part) == 1:
                next_part = str(function[index + 1])
                if len(next_part) == 3:
                    index_division = index
                    list_division_f = [function[index - 1]]
                    list_division_s = [function[index + 1]]
                    result_division = division_x(list_division_f, list_division_s)
                    list_division_c[f"{index_division - 1}"] = result_division
    if len(list_division_c) != 0:
        for idx in sorted(list_division_c.keys(), reverse=True):
            index = int(idx)
            values = list_division_c[idx]
            del function[index + 2]
            del function[index + 1]
            del function[index]
            
            for part in reversed(values):
                function.insert(index, part)

    list_logarithm_c = {}
    for part in function:
        if "log" in part or "ln" in part:
            index = function.index(part)
            if f"{function[index]}" == "log":
                if len(part) == 3:
                    list_logarithm_f = [function[index + 1]]
                    list_logarithm_s = [function[index + 2]]
                    index_logarithm = index
                    result_logarithm = logarithm_x(list_logarithm_f, list_logarithm_s, "log")
                    list_logarithm_c[f"{index_logarithm}"] = result_logarithm
            else:
                if len(part) == 2:
                    list_logarithm_f = [function[index + 1]]
                    index_logarithm = index
                    result_logarithm = logarithm_x(list_logarithm_f, None, "ln")
                    list_logarithm_c[f"{index_logarithm}"] = result_logarithm
    if len(list_logarithm_c) != 0:
        for idx in sorted(list_logarithm_c.keys(), reverse=True):
            index = int(idx)
            values = list_logarithm_c[idx]
            del function[index + 1]
            del function[index]
            for v in reversed(values):
                function.insert(index, v)

    list_bracket_c = {}
    for part in function:
        if "(" in part:
            list_bracket = [function[index]]
            result_bracket = bracket_calculating_x(list_bracket)
            if result_bracket != None:
                index_bracket = index
                list_bracket_c[f"{index_bracket}"] = result_bracket
    if len(list_bracket_c) != 0:
        for idx in sorted(list_bracket_c.keys(), reverse=True):
            index = int(idx)
            values = list_bracket_c[idx]
            del function[index]
            for v in reversed(values):
                function.insert(index, v)
    
    return function