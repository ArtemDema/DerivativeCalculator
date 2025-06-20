r"""
Логарифм c X
"""


def log_calculating(index, list, type, minus, sum, 
              multiplication, division, division_calculating, radical, radical_calculating, 
              degree, degree_calculating, trigonometric_functions, trigonimetric_functions_calculating, bracket_calculating, module_calculating):
    list_logarithm_f = []
    list_logarithm_s = []
    stop = False
    column = 0
    while stop == False:
        if ")" in list[index + 1]:
            list_logarithm_f.append(list[index + 1])
            del list[index + 1]
            column -= 1
            if column == 0: stop = True
        elif "(" in list[index + 1]:
            list_logarithm_f.append(list[index + 1])
            del list[index + 1]
            column += 1
        else:
            list_logarithm_f.append(list[index + 1])
            del list[index + 1]
    
    stop = False
    column = 0
    while stop == False:
        if ")" in list[index + 1]:
            list_logarithm_s.append(list[index + 1])
            del list[index + 1]
            column -= 1
            if column == 0: stop = True
        elif "(" in list[index + 1]:
            list_logarithm_s.append(list[index + 1])
            del list[index + 1]
            column += 1
        else:
            list_logarithm_s.append(list[index + 1])
            del list[index + 1]

    result_f = logarithm(list_logarithm_f, list_logarithm_s, "log", minus, sum, 
              multiplication, division, division_calculating, radical, radical_calculating, 
              degree, degree_calculating, trigonometric_functions, trigonimetric_functions_calculating, bracket_calculating, module_calculating)
    del list[index]
    list.insert(index, str(result_f))

    return list

def ln_calculating(index, list, type, minus, sum, 
              multiplication, division, division_calculating, radical, radical_calculating, 
              degree, degree_calculating, trigonometric_functions, trigonimetric_functions_calculating, bracket_calculating, module_calculating):
    list_logarithm_f = []
    column = 0
    final = False 
    while final == False:
        if ")" in list[index + 1]:
            list_logarithm_f.append(list[index + 1])
            del list[index + 1]
            column -= 1
            if column == 0: final = True
        elif "(" in list[index + 1]:
            list_logarithm_f.append(list[index + 1])
            del list[index + 1]
            column += 1
        else:
            list_logarithm_f.append(list[index + 1])
            del list[index + 1]
    
    list_logarithm_f = [''.join(list_logarithm_f)]

    result_f = logarithm(list_logarithm_f, None, "ln", minus, sum, 
              multiplication, division, division_calculating, radical, radical_calculating, 
              degree, degree_calculating, trigonometric_functions, trigonimetric_functions_calculating, bracket_calculating, module_calculating)

    del list[index]
    list.insert(index, str(result_f))

    return list