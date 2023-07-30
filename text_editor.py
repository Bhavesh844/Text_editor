import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

# Define global variables
current_file = None

# Functions for menu commands
def new_file():
    global current_file
    text.delete(1.0, tk.END)
    current_file = None

def open_file():
    global current_file
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, "r") as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())
            current_file = file_path

def save_file():
    global current_file
    if current_file:
        with open(current_file, "w") as file:
            file.write(text.get(1.0, tk.END))
    else:
        save_file_as()

def save_file_as():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))
        global current_file
        current_file = file_path

def cut():
    text.event_generate("<<Cut>>")

def copy():
    text.event_generate("<<Copy>>")

def paste():
    text.event_generate("<<Paste>>")

def undo():
    text.event_generate("<<Undo>>")

def redo():
    text.event_generate("<<Redo>>")

def select_all():
    text.tag_add("sel", 1.0, tk.END)

def about():
    messagebox.showinfo("About", "Bhavesh Text Editor\nCreated with Python and Tkinter. @Bhavesh_Kumar ")

def exit_app():
    if messagebox.askyesno("Exit", "Do you want to exit?"):
        app.destroy()

def search_text():
    search_query = simpledialog.askstring("Search", "Enter text to search:")
    if search_query:
        start_pos = "1.0"
        while True:
            start_pos = text.search(search_query, start_pos, stopindex=tk.END)
            if not start_pos:
                break
            end_pos = f"{start_pos}+{len(search_query)}c"
            text.tag_add("search", start_pos, end_pos)
            start_pos = end_pos

def clear_search():
    text.tag_remove("search", 1.0, tk.END)

def wrap_text():
    text.config(wrap=tk.WORD if wrap_var.get() == 1 else tk.NONE)

def change_font_size():
    font_size = simpledialog.askinteger("Font Size", "Enter font size:", initialvalue=12)
    if font_size:
        font_name = text['font'].split()[0]
        text['font'] = (font_name, font_size)

# Create the main application window
app = tk.Tk()
app.title("Bhavesh Text Editor")
app.geometry("850x650")

# Create the text widget
text = tk.Text(app, wrap=tk.WORD)
text.pack(expand=True, fill=tk.BOTH)

# Create the menu bar
menu_bar = tk.Menu(app)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_file_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=undo)
edit_menu.add_command(label="Redo", command=redo)
edit_menu.add_separator()
edit_menu.add_command(label="Select All", command=select_all)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

search_menu = tk.Menu(menu_bar, tearoff=0)
search_menu.add_command(label="Search", command=search_text)
search_menu.add_command(label="Clear Search", command=clear_search)
menu_bar.add_cascade(label="Search", menu=search_menu)

options_menu = tk.Menu(menu_bar, tearoff=0)
wrap_var = tk.IntVar(value=1)
options_menu.add_checkbutton(label="Wrap Text", variable=wrap_var, command=wrap_text)
options_menu.add_command(label="Change Font Size", command=change_font_size)
menu_bar.add_cascade(label="Options", menu=options_menu)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=about)
menu_bar.add_cascade(label="Help", menu=help_menu)

app.config(menu=menu_bar)

app.mainloop()
