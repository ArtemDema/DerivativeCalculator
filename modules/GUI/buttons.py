import customtkinter, PIL, os
from .main_Frames import button_frame, graphic_frame

class Button(customtkinter.CTkButton):
    def __init__(self, master: any, x: int, y: int, text: str, fg_color: str, hover_color: str, image: str = None):
        super().__init__(master = master, hover_color = hover_color, text = text, fg_color = fg_color)
        self.x = x
        self.y = y 

        self.button = customtkinter.CTkButton(
            master = self.master,
            width = 100,
            height = 50,
            text = self._text,
            fg_color = self._fg_color,
            text_color = "#FFFFFF",
            font = ("Roboto Slab", 28),
            corner_radius = 0,
            hover_color = self._hover_color,
            image = self.image_load(image)
        )
        self.button.place(x = self.x, y = self.y)

    def image_load(self, image_name):
        if image_name != None:
            image_path = os.path.abspath(os.path.join(__file__+ f'/../../../static/images/{image_name}.png'))
            image = PIL.Image.open(image_path)
            return customtkinter.CTkImage(
                light_image = image,
                size = (30, 30)
            )
        return None




list_text_button = ["sin x","cos x","tg x","x^n","√x","ctg x","+","*","log","-","/","ln","1","4","7","2","5","8","0","3","6","9"]
#-------------------------------------------------------------------
for i in range(3):
    button = Button(master = button_frame, x = 10, y = 10 + (60 * i), text = list_text_button[0], fg_color = "#D9D9D9",
                    hover_color = "#ACACAC")
    del list_text_button[0]

for i in range(3):
    button = Button(master = button_frame, x = 120, y = 10 + (60 * i), text = list_text_button[0], fg_color = "#D9D9D9",
                    hover_color = "#ACACAC")
    del list_text_button[0]
#-------------------------------------------------------------------

for i in range(3):
    button = Button(master = button_frame, x = 270, y = 10 + (60 * i), text = list_text_button[0], fg_color = "#D9D9D9",
                    hover_color = "#ACACAC")
    del list_text_button[0]

for i in range(3):
    button = Button(master = button_frame, x = 380, y = 10 + (60 * i), text = list_text_button[0], fg_color = "#D9D9D9",
                    hover_color = "#ACACAC")
    del list_text_button[0]
#-------------------------------------------------------------------

for i in range(3):
    button = Button(master = button_frame, x = 530, y = 10 + (60 * i), text = list_text_button[0], fg_color = "#D9D9D9",
                    hover_color = "#ACACAC")
    del list_text_button[0]

button = Button(master = button_frame, x = 530, y = 190, text = "", fg_color = "#E06363", hover_color = "#AA2C2C", 
                image = "Delete")

for i in range(4):
    button = Button(master = button_frame, x = 640, y = 10 + (60 * i), text = list_text_button[0], fg_color = "#D9D9D9",
                    hover_color = "#ACACAC")
    del list_text_button[0]

for i in range(3):
    button = Button(master = button_frame, x = 750, y = 10 + (60 * i), text = list_text_button[0], fg_color = "#D9D9D9",
                    hover_color = "#ACACAC")
    del list_text_button[0]

button = Button(master = button_frame, x = 750, y = 190, text = "", fg_color = "#65E08A",
                    hover_color = "#3FD56C", image = "Enter")

button = Button(master = graphic_frame, x = 760, y = 450, text = "", fg_color = "#D9D9D9",
                    hover_color = "#ACACAC", image = "Download")