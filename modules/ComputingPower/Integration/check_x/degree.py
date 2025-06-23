r"""
Степень c X
"""

def degree_x(function_f, function_s):
    list_operations = ["^","/","√","|","*","+","(",")","+","-",]
    final = False
    while final == False:
        number = 0
        for i in range(len(list_operations)):
            for part in function_s:
                if f"{list_operations[i]}" in part:
                    if len(part) > 1:
                        number += 1
                        index_f = function_s.index(part)
                        del function_s[index_f]
                        split_f= part.split(f"{list_operations[i]}", 1)
                        split_f.insert(1, f"{list_operations[i]}")
                        if split_f[0] == "": 
                            del split_f[0]
                        if len(split_f) == 3:
                            if split_f[2] == "": 
                                del split_f[2]
                        for i in range(len(split_f)):
                            function_s.insert(index_f + i, split_f[i])
        if number == 0: final = True
    
    del (function_s[0])
    del (function_s[-1])
    if function_f == "x":
        result = [f"(x^({float(function_s) + 1}))", "/", f"({float(function_s) + 1})"]
    else:
        result = [f"{float(function_s)}","^","(x)","/","(ln",f"({float(function_f)}))"]
    return result