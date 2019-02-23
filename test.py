import tkinter as tk
from tkinter import ttk
import webbrowser

app = tk.Tk()
app.title("Поиск")

search_label = ttk.Label(app, text='Search')
search_label.grid(row=0, column=0)

text_field = ttk.Entry(app, width=50)
text_field.grid(row=0, column=1)

app.mainloop()
