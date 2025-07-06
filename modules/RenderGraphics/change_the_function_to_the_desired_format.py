r"""
Изменение функции в нудный формат для построения графика
"""
import re

def change_function(expr: str):
    expr = expr.replace('^', '**')
    expr = re.sub(r'√\(?([a-zA-Z0-9\+\-\*/\^\.]+)\)?', r'np.sqrt(\1)', expr)
    expr = re.sub(r'\bsin\(', 'np.sin(', expr)
    expr = re.sub(r'\bcos\(', 'np.cos(', expr)
    expr = re.sub(r'log\(([^()]+)\)\(([^()]+)\)', r'(np.log(\2)/np.log(\1))', expr)
    expr = re.sub(r'\bln\(', 'np.log(', expr)

    return expr