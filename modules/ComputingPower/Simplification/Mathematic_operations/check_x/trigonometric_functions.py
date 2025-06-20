r"""
Синус, косинус, тангeнс и котангенс c X
"""


def trigonimetric_functions_calculating(index, list, type, minus, sum, multiplication, division, division_calculating, radical, radical_calculating, degree, degree_calculating, logarithm, log_calculating, ln_calculating, bracket_calculating, module_calculating):
    list_trigonometric = []
    column = 0
    final = False 
    while final == False:
        if ")" in list[index + 1]:
            list_trigonometric.append(list[index + 1])
            del list[index + 1]
            column -= 1
            if column == 0: final = True
        elif "(" in list[index + 1]:
            list_trigonometric.append(list[index + 1])
            del list[index + 1]
            column += 1
        else:
            list_trigonometric.append(list[index + 1])
            del list[index + 1]
    
    list_trigonometric = [''.join(list_trigonometric)]

    result_f = trigonometric_functions(list_trigonometric, type, minus, sum, multiplication, division, division_calculating, radical, radical_calculating, degree, degree_calculating, logarithm, log_calculating, ln_calculating, bracket_calculating, module_calculating)

    del list[index]
    list.insert(index, str(result_f))
    
    return list