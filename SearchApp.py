import tkinter as tk
from tkinter import ttk
from tkinter import *
import webbrowser

app = tk.Tk()
app.title("Поиск")
app.configure(background='#ececec')

app_name = ttk.Label(app, text='Поисковое приложение', font='Arial 24 bold')
app_name.grid(row=0, column=1)

search_label = ttk.Label(app, text='Поиск')
search_label.grid(row=1, column=0)

text_field = ttk.Entry(app, width=50)
text_field.grid(row=1, column=1)

search_engine = StringVar()
search_engine.set("bing")

def search():
    if text_field.get().strip() != "":
        if search_engine.get() == 'google':
            webbrowser.open('https://www.google.com/search?q=' + text_field.get())
        elif search_engine.get() == 'bing':
            webbrowser.open('https://www.bing.com/search?q=' + text_field.get())

def searchBtn():
    search()

def enterBtn(event):
    search()


btn_search = ttk.Button(app, text='Найти', width=10, command=search)
btn_search.grid(row=1, column=2)
text_field.bind('<Return>', enterBtn)

radio_google = ttk.Radiobutton(app, text='Google', value='google', variable=search_engine)
radio_google.grid(row=2, column=1, sticky=W)
radio_bing = ttk.Radiobutton(app, text='Bing', value='bing', variable=search_engine)
radio_bing.grid(row=2, column=1, sticky=E)

app.wm_attributes('-topmost', True)

text_field.focus()

app.mainloop()
