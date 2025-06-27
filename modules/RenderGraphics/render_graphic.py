r"""
Отрисовка графика 
"""
import matplotlib
import matplotlib.pyplot
import numpy as np
from ..ComputingPower import start_power
from .change_the_function_to_the_desired_format import change_function

fig, ax = matplotlib.pyplot.subplots()
canvas = None

def render_and_simplification(equation, button9, graphic_frame):
    global canvas 

    start_equation = equation._text
    equal_C = button9.equal_C
    function = start_power(start_equation)
    function = "".join(function)
    function = change_function(function)
    function += f"+{str(equal_C)}"

    x = np.linspace(-10, 10, 2000)
    y = eval(function)
    ax.clear()
    ax.plot(x, y)
    ax.set_title("График функции")
    ax.grid(True)

    if canvas:
        canvas.get_tk_widget().destroy()

    canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=graphic_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)