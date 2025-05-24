import customtkinter

app = customtkinter.CTk(fg_color = "#E2E2E2")

WIDTH = 860
HEIGHT = 800

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

screen_x = screen_width // 2 - WIDTH // 2
screen_y = screen_height // 2 - HEIGHT // 2

app.geometry(f"{WIDTH}x{HEIGHT}+{screen_x}+{screen_y}")
app.update()

app.resizable(False, False)