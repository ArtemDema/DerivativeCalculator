import customtkinter
from .main_Frames import equation_frame

class Equation(customtkinter.CTkLabel):
    def __init__(self, master: any, text: str):
        super().__init__(master = master, text = text, font = ("Roboto Slab", 28), text_color = "#000000")

    def add_text(self, add_simvol):
        self.configure(text = self._text + add_simvol)
    
    def delete_text(self):
        self.configure(text = self._text[:-1])
    
    def confirm_text(self):
        pass
    

equation = Equation(master = equation_frame, text = "1")
equation.place(x = 5, y = 10)