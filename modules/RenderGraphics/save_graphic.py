r"""
Сохранение графика
"""
import customtkinter

def save_graph():
    from .render_graphic import fig
    file_path = customtkinter.filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG файлы", "*.png")],
        title="Save griphic as..."
    )
    if file_path:
        if fig != None:
            fig.savefig(file_path)