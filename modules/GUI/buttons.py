import customtkinter, PIL, os
from .main_Frames import button_frame, graphic_frame
from .equation import equation
from .pop_up_window import pop_up_w

class Button(customtkinter.CTkButton):
    def __init__(self, master: any, x: int, y: int, text: str, fg_color: str, hover_color: str, image: str = None):
        self.image_name = None
        customtkinter.CTkButton.__init__(
                    self = self,
                    master = master,
                    width = 100,
                    height = 50,
                    text = text,
                    fg_color = fg_color,
                    text_color = "#FFFFFF",
                    font = ("Roboto Slab", 28),
                    corner_radius = 0,
                    hover_color = hover_color,
                    image = self.image_load(image),
                    command = self.add_text_b
        )
        self.x = x
        self.y = y
        self.place(x = self.x, y = self.y)

    def image_load(self, image_name):
        if image_name != None:
            self.image_name = image_name
            image_path = os.path.abspath(os.path.join(__file__+ f'/../../../static/images/{image_name}.png'))
            image = PIL.Image.open(image_path)
            return customtkinter.CTkImage(
                light_image = image,
                size = (30, 30)
            )
        return None
    
    def add_text_b(self):
        if self.image_name != None:
            if self.image_name == "Delete":
                equation.delete_text()
            elif self.image_name == "Enter":
                pop_up_w()
            else:
                equation.confirm_text()

        equation.add_text(self._text)



list_text_button = ["sin","cos","tg","|","^","√",
                    "ctg","x","+","*","log","(","-","/","ln",
                    ")","1","4","7","2","5","8","0","3","6","9"]

#-------------------------------------------------------------------
for i in range(4):
    button1 = Button(master = button_frame, x = 5, y = 10 + (60 * i), text = list_text_button[0], fg_color = "#D9D9D9",
                    hover_color = "#ACACAC")
    del list_text_button[0]

for i in range(4):
    button2 = Button(master = button_frame, x = 111, y = 10 + (60 * i), text = list_text_button[0], fg_color = "#D9D9D9",
                    hover_color = "#ACACAC")
    del list_text_button[0]
#-------------------------------------------------------------------

for i in range(4):
    button3 = Button(master = button_frame, x = 217, y = 10 + (60 * i), text = list_text_button[0], fg_color = "#D9D9D9",
                    hover_color = "#ACACAC")
    del list_text_button[0]

for i in range(4):
    button4 = Button(master = button_frame, x = 323, y = 10 + (60 * i), text = list_text_button[0], fg_color = "#D9D9D9",
                    hover_color = "#ACACAC")
    del list_text_button[0]
#-------------------------------------------------------------------

for i in range(3):
    button5 = Button(master = button_frame, x = 543, y = 10 + (60 * i), text = list_text_button[0], fg_color = "#D9D9D9",
                    hover_color = "#ACACAC")
    del list_text_button[0]

button6 = Button(master = button_frame, x = 543, y = 190, text = "", fg_color = "#E06363", hover_color = "#AA2C2C", 
                image = "Delete")

for i in range(4):
    button7 = Button(master = button_frame, x = 649, y = 10 + (60 * i), text = list_text_button[0], fg_color = "#D9D9D9",
                    hover_color = "#ACACAC")
    del list_text_button[0]

for i in range(3):
    button8 = Button(master = button_frame, x = 755, y = 10 + (60 * i), text = list_text_button[0], fg_color = "#D9D9D9",
                    hover_color = "#ACACAC")
    del list_text_button[0]

button9 = Button(master = button_frame, x = 755, y = 190, text = "", fg_color = "#65E08A",
                    hover_color = "#3FD56C", image = "Enter")

button10 = Button(master = graphic_frame, x = 760, y = 450, text = "", fg_color = "#D9D9D9",
                    hover_color = "#ACACAC", image = "Download")