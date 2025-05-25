import customtkinter
from ..window import app

# popup_window = None

def pop_up_w():
    # global popup_window
    # if popup_window == None:
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

    button = customtkinter.CTkButton(popup_window, width = 90, height = 45, text="Confirm", command = popup_window.destroy)
    button.place(x = 55, y = 140)