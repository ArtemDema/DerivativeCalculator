from .main_Frames import button_frame, graphic_frame
from .class_button import Button

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
button5 = Button(master = button_frame, x = 433, y = 10, text = " ", fg_color = "#D9D9D9", hover_color = "#ACACAC")
button5 = Button(master = button_frame, x = 433, y = 70, text = ".", fg_color = "#D9D9D9", hover_color = "#ACACAC")

for i in range(3):
    button6 = Button(master = button_frame, x = 543, y = 10 + (60 * i), text = list_text_button[0], fg_color = "#D9D9D9",
                    hover_color = "#ACACAC")
    del list_text_button[0]

button7 = Button(master = button_frame, x = 543, y = 190, text = "", fg_color = "#E06363", hover_color = "#AA2C2C", 
                image = "Delete")

for i in range(4):
    button8 = Button(master = button_frame, x = 649, y = 10 + (60 * i), text = list_text_button[0], fg_color = "#D9D9D9",
                    hover_color = "#ACACAC")
    del list_text_button[0]

for i in range(3):
    button9 = Button(master = button_frame, x = 755, y = 10 + (60 * i), text = list_text_button[0], fg_color = "#D9D9D9",
                    hover_color = "#ACACAC")
    del list_text_button[0]

button10 = Button(master = button_frame, x = 755, y = 190, text = "", fg_color = "#65E08A",
                    hover_color = "#3FD56C", image = "Enter")

button11 = Button(master = graphic_frame, x = 760, y = 450, text = "", fg_color = "#D9D9D9",
                    hover_color = "#ACACAC", image = "Download")

button12 = Button(master = graphic_frame, x = 0, y = 450, text = "Example", fg_color = "#D9D9D9",
                    hover_color = "#ACACAC")