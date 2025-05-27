import customtkinter, PIL, os
from .equation import equation
from ..window import app
from ..ComputingPower import start_power

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
        self.popup_window_exist = False
        self.popup_window_example_exist = False
        self.equal_C = 0
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
                return
            elif self.image_name == "Enter":
                self.pop_up_w()
                return
            else:
                equation.confirm_text()
                return

        if self._text == "Example":
            self.example_button()
            return
        equation.add_text(self._text)

    def close(self, popup_window, entry):
        self.equal_C = entry.get()
        popup_window.destroy()
        self.popup_window_exist = False
        start_power(equation, self)
    
    def close_example(self, popup_window):
        popup_window.destroy()
        self.popup_window_example_exist = False
    
    def pop_up_w(self):
        if self.popup_window_exist == False:
            popup_window = customtkinter.CTkToplevel(app)

            WIDTH = 200
            HEIGHT = 200

            screen_width = app.winfo_screenwidth()
            screen_height = app.winfo_screenheight()

            screen_x = screen_width // 2 - WIDTH // 2
            screen_y = screen_height // 2 - HEIGHT // 2

            popup_window.geometry(f"{WIDTH}x{HEIGHT}+{screen_x}+{screen_y}")
            popup_window.attributes("-topmost", True)

            label = customtkinter.CTkLabel(master = popup_window, text="Enter what will be equal to C", font = ("Roboto Slab", 14))
            label.pack(pady=20)

            entry = customtkinter.CTkEntry(master = popup_window, width = 130, height = 50,placeholder_text = "  Enter only number")
            entry.place(x = 35, y = 55)

            button = customtkinter.CTkButton(popup_window, width = 90, height = 45, text="Confirm", command = lambda: self.close(popup_window, entry))
            button.place(x = 55, y = 140)
            self.popup_window_exist = True
            popup_window.protocol("WM_DELETE_WINDOW", lambda: self.close(popup_window, entry))
        
    def example_button(self):
        if self.popup_window_example_exist == False:
            popup_window_example = customtkinter.CTkToplevel(app)

            WIDTH = 500
            HEIGHT = 500

            screen_width = app.winfo_screenwidth()
            screen_height = app.winfo_screenheight()

            screen_x = screen_width // 2 - WIDTH // 2
            screen_y = screen_height // 2 - HEIGHT // 2

            popup_window_example.geometry(f"{WIDTH}x{HEIGHT}+{screen_x}+{screen_y}")
            popup_window_example.attributes("-topmost", True)

            scrol_frame = customtkinter.CTkScrollableFrame(master = popup_window_example, width = 500, height = 450)
            scrol_frame.place(x = 0, y = 50)

            label = customtkinter.CTkLabel(master = popup_window_example, text="How to fill in the input field", font = ("Roboto Slab", 14))
            label.pack(padx= 10, pady = 10)

            list_examples = ["sin, cos, tg and ctg:","sin(45), cos(60)", "we write in brackets","+ and -:", "10+66, 3*√25 -10",
                             "after √ space","*", "2*tg(85), 50*(√25)^(3), |-7|*8^(2)","where in mathematics there is multiplication (which we do not write), here we must write it",
                             "^", "2^(5)*8", "in brackets all following symbols will be counted in powers",
                             "/", "1/2, 4*3^(3)/3√25 *sin(10)", "after the fraction always put a space",
                             "|", "|-45|+5","After the module, you don't have to put a space","log and lg",
                             "log(3)(3), lg(10), log(8)(1/3)", "first log in brackets is the base, the second bracket is the argument", 
                             "√", "√100 *2", "after √ space (if there is no space, the symbols will be considered under the root)"]

            for i in range(8):
                text1 = customtkinter.CTkLabel(master = scrol_frame, font = ("Roboto Slab", 28), text_color = "#FFFFFF",
                                            text = list_examples[0])
                text1.pack(padx = 10, pady = 20)
                del list_examples[0]

                text2 = customtkinter.CTkLabel(master = scrol_frame, font = ("Roboto Slab", 14), text_color = "#FFFFFF",
                                            text = list_examples[0])
                text2.pack(padx = 10, pady = 20)
                del list_examples[0]

                text3 = customtkinter.CTkLabel(master = scrol_frame, font = ("Roboto Slab", 12), text_color = "#FFFFFF",
                                            text = list_examples[0])
                text3.pack(padx = 10, pady = 20)
                del list_examples[0]
                #-------------------------------------------------------
                text1 = customtkinter.CTkLabel(master = scrol_frame, font = ("Roboto Slab", 28), text_color = "#FFFFFF",
                                            text = "---------------------------------------")
                text1.pack(pady = 10)
                #-------------------------------------------------------
            self.popup_window_example_exist = True
            popup_window_example.protocol("WM_DELETE_WINDOW", lambda: self.close_example(popup_window_example))