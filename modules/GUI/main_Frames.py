r"""
Создание главных фреймов для приложения
"""

import customtkinter
from ..window import app

graphic_frame = customtkinter.CTkFrame(master = app, width = 860, height = 500, fg_color = "#FFFFFF", corner_radius = 0)
graphic_frame.place(x = 0, y = 0)
graphic_frame.pack_propagate(False)

button_frame = customtkinter.CTkFrame(master = app, width = 860, height = 250, fg_color = "#665588", corner_radius = 0)
button_frame.place(x = 0, y = 550)
button_frame.pack_propagate(False)

equation_frame = customtkinter.CTkFrame(master = app, width = 860, height = 50, fg_color = "#4A396D", corner_radius = 0, border_width = 2,
                    border_color = "#000000")
equation_frame.place(x = 0, y = 500)
equation_frame.pack_propagate(False)