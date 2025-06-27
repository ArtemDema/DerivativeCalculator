r"""
Не главная, но все важная вычислительная обработка
"""

from .check_x import *

def checks_X(equation: list):
    result_degree = None
    result_trigonometric = None
    result_radical = None
    result_division = None
    result_logarithm = None
    result_bracket = None     

    list_degree_c = {}
    for part in equation:
        if "^" in part:
            index = equation.index(part)
            if len(part) == 1:
                list_degree = [equation[index + 1]]
                index_degree = index
                result_degree = degree_x(equation[index - 1], list_degree)
                del equation[index + 1]
                list_degree_c[f"{index_degree - 1}"] = result_degree
    if len(list_degree_c) != 0:
        for idx in sorted(list_degree_c.keys(), reverse=True):
            index = int(idx)
            values = list_degree_c[idx]
            del equation[index - 1]
            del equation[index - 1]
            for part in reversed(values):
                equation.insert(index, part)

    list_radical_c = {}
    for part in equation:
        if "√" in part:
            index = equation.index(part)
            if len(part) == 1:
                list_radical = [equation[index + 1]]
                index_radical = index
                result_radical = radical_x(list_radical)
                list_radical_c[f"{index_radical}"] = result_radical
    if len(list_radical_c) != 0:
        for idx in sorted(list_radical_c.keys(), reverse=True):
            index = int(idx)
            values = list_radical_c[idx]
            del equation[index + 1]
            del equation[index]
            for part in reversed(values):
                equation.insert(index, part)

    list_logarithm_c = {}
    for part in equation:
        if "log" in part or "ln" in part:
            index = equation.index(part)
            if f"{equation[index]}" == "log":
                if len(part) == 3:
                    list_logarithm_f = [equation[index + 1]]
                    list_logarithm_s = [equation[index + 2]]
                    index_logarithm = index
                    del equation[index + 2]
                    result_logarithm = logarithm_x(list_logarithm_f, list_logarithm_s, "log")
                    list_logarithm_c[f"{index_logarithm}"] = result_logarithm
            else:
                if len(part) == 2:
                    list_logarithm_f = [equation[index + 1]]
                    index_logarithm = index
                    result_logarithm = logarithm_x(list_logarithm_f, None, "ln")
                    list_logarithm_c[f"{index_logarithm}"] = result_logarithm
    if len(list_logarithm_c) != 0:
        for idx in sorted(list_logarithm_c.keys(), reverse=True):
            index = int(idx)
            values = list_logarithm_c[idx]
            del equation[index + 1]
            del equation[index]
            for part in reversed(values):
                equation.insert(index, part)

    list_trigonometric_c = {}
    for part in equation:
        if "sin" in part or "cos" in part or "tg" in part:
            index = equation.index(part)
            if equation[index] == "sin" or equation[index] == "cos": len_t = 3
            else: len_t = 2
            if len(part) == len_t:
                list_trigonometric = [equation[index + 1]]
                index_trigonometric = index
                result_trigonometric = trigonometric_functions_x(list_trigonometric, f"{equation[index]}")
                list_trigonometric_c[f"{index_trigonometric}"] = result_trigonometric
    if len(list_trigonometric_c) != 0:
        for idx in sorted(list_trigonometric_c.keys(), reverse=True):
            index = int(idx)
            values = list_trigonometric_c[idx]
            del equation[index + 1]
            del equation[index]
            for part in reversed(values):
                equation.insert(index, part)

    list_division_c = {}
    for part in equation:
        if "/" in part:
            index = equation.index(part)
            if len(part) == 1:
                next_part = str(equation[index + 1])
                if len(next_part) == 3:
                    index_division = index
                    list_division_f = [equation[index - 1]]
                    list_division_s = [equation[index + 1]]
                    result_division = division_x(list_division_f, list_division_s)
                    list_division_c[f"{index_division - 1}"] = result_division
    if len(list_division_c) != 0:
        for idx in sorted(list_division_c.keys(), reverse=True):
            index = int(idx)
            values = list_division_c[idx]
            del equation[index + 2]
            del equation[index + 1]
            del equation[index]
            
            for part in reversed(values):
                equation.insert(index, part)

    list_bracket_c = {}
    for part in equation:
        if "(" in part:
            index = equation.index(part)
            left_ok = index == 0 or equation[index - 1] not in ["/", "^"]
            right_ok = index == len(equation) - 1 or equation[index + 1] not in ["/", "^"]
            if left_ok and right_ok:
                list_bracket = [equation[index]]
                result_bracket = bracket_calculating_x(list_bracket)
                if result_bracket != None:
                    index_bracket = index
                    list_bracket_c[f"{index_bracket}"] = result_bracket
    if len(list_bracket_c) != 0:
        for idx in sorted(list_bracket_c.keys(), reverse=True):
            index = int(idx)
            values = list_bracket_c[idx]
            del equation[index]
            for part in reversed(values):
                equation.insert(index, part)

    for part in equation:
        if part == "-":
            index = equation.index(part)
            if equation[index + 1] == "-":
                del equation[index + 1]
                equation[index] = "+"
    return equation