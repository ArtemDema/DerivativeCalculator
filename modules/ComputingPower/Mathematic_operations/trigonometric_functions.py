r"""
Синус, косинус, тангeнс и котангенс
"""

import math

def trigonometric_functions(function: list, type, minus, sum, multiplication):
    for i in range(len(function)):
            function[i] = function[i].replace("(", "").replace(")", "")

    for i in range(len(function)):
            function[i] = function[i].replace("sin", "").replace("cos", "")

    for i in range(len(function)):
            function[i] = function[i].replace("tg", "")

    for part in function:
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
        
        if "*" in part:
            index_f = function.index(part)
            result_f = multiplication(function[index_f - 1], function[index_f + 1])
            del function[index_f - 1]
            del function[index_f - 1]
            del function[index_f - 1]
            function.insert(index_f - 1, result_f)

    if type == "sin":
        return math.sin(int(function[0]))
    if type == "cos":
        return math.cos(int(function[0]))
    if type == "tg":
        return math.tan(int(function[0]))
    if type == "ctg":
        return math.tan(int(function[0]))