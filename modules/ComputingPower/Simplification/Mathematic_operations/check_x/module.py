r"""
Модуль c X
"""


def module_calculating(index, list, minus, sum, 
           multiplication, division, division_calculating, 
           radical, radical_calculating, degree_calculating, degree, logarithm, log_calculating, ln_calculating, trigonometric_functions, trigonimetric_functions_calculating, bracket_calculating):
    
    list_module = []
    final = False 
    list_module.append(list[index])
    while final == False:
        if "|" in list[index + 1]:
            list_module.append(list[index + 1])
            del list[index + 1]
            final = True
        else:
            list_module.append(list[index + 1])
            del list[index + 1]
    
    list_module = [''.join(list_module)]

    result_f = module(list_module, minus, sum, 
           multiplication, division, division_calculating, 
           radical, radical_calculating, degree_calculating, degree, logarithm, log_calculating, ln_calculating, trigonometric_functions, trigonimetric_functions_calculating, bracket_calculating)

    del list[index]
    list.insert(index - 1, str(result_f))

    return list