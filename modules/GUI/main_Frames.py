import customtkinter
from ..window import app

button_frame = customtkinter.CTkFrame(master = app, width = 860, height = 250, fg_color = "#C2C2C2")
button_frame.place(x = 0, y = 550)
button_frame.pack_propagate(False)

equation_frame = customtkinter.CTkFrame(master = app, width = 860, height = 50, fg_color = "#C5DCE4")
equation_frame.place(x = 0, y = 500)
equation_frame.pack_propagate(False)

graphic_frame = customtkinter.CTkFrame(master = app, width = 860, height = 500, fg_color = "#E2E2E2")
graphic_frame.place(x = 0, y = 0)
graphic_frame.pack_propagate(False)