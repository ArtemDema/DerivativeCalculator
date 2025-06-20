r"""
Деление c X
"""


def division_calculating(index, list, type, minus, sum,
            multiplication, degree, degree_calculating, radical, radical_calculating, 
            logarithm, log_calculating, ln_calculating, trigonometric_functions, trigonimetric_functions_calculating, bracket_calculating, module_calculating):
    list_division_f = []
    list_division_s = []
    index_division = 1
    stop = False
    while stop == False:
        if "(" in list[index - index_division]:
            stop = True
        else:
            index_division += 1

    for i in range(index_division):
        list_division_f.append(list[index - index_division])
        index_division -= 1

    column = 0
    final = False 
    while final == False:
        if ")" in list[index + 1]:
            list_division_s.append(list[index + 1])
            del list[index + 1]
            column -= 1
            if column == 0: final = True
        elif "(" in list[index + 1]:
            list_division_s.append(list[index + 1])
            del list[index + 1]
            column += 1
        else:
            list_division_s.append(list[index + 1])
            del list[index + 1]

    list_division_f = [''.join(list_division_f)]
    list_division_s = [''.join(list_division_s)]

    result_f = division(list_division_f, list_division_s, minus, sum,
            multiplication, degree, degree_calculating, radical, radical_calculating, 
            logarithm, log_calculating, ln_calculating, trigonometric_functions, trigonimetric_functions_calculating, bracket_calculating, module_calculating)
    
    stop = False
    index_division = 1
    while stop == False:
        if "(" in list[index - index_division]:
            del list[index - index_division]
            list[index - index_division] = str(result_f)
            stop = True
        else: 
            del list[index - index_division]
            index_division += 1
            
    return list