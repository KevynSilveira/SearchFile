import os
import zipfile
import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog
from tkinter import messagebox

arquivos_encontrados = []#Lista de arquivos

def search(): # Busca os arquivos por código
    code = entry_searchFile.get()
    directory = entry_select.get()
    global arquivos_encontrados
    for file in os.listdir(directory):
        if code.lower() in file.lower():
            arquivos_encontrados.append(os.path.join(directory, file))
    return arquivos_encontrados

def zip():
    global arquivos_encontrados
    filetypes = [('Arquivos', '*.zip')]
    destiny = filedialog.asksaveasfilename(defaultextension=".zip", initialfile="Arquivos", filetypes=filetypes)
    with zipfile.ZipFile(destiny, 'w') as zip_file:
        for file in arquivos_encontrados:
            zip_file.write(file, os.path.basename(file))

def select():
    diretorio = filedialog.askdirectory()
    entry_select.delete(0, tk.END)
    entry_select.insert(0, diretorio)

def execute():
    try:
        path = entry_select.get()
        searchfile = entry_searchFile.get()
        if(path!="" and searchfile!= ""):
            search()
            zip()
        else:
            messagebox.showerror("ATENÇÃO", "Preenca todos os campos")
    except Exception as e:
        messagebox.showerror("ATENÇÃO", f"Ocorreu um erro: {e}")

frame = ctk.CTk()
frame.geometry("200x200")
frame.title("Busca arquivos")
frame.resizable(False, False)

button_select = ctk.CTkButton(master=frame, text= "Diretório origem", width=150, height=30, command=select)
button_select.place(x=25, y=10)

entry_select = ctk.CTkEntry(master=frame, width=150, height=30)
entry_select.place(x=25, y=50)

label_searchFile = ctk.CTkLabel(master=frame,text="Código", width=150, height=30)
label_searchFile.place(x=25, y=90)

entry_searchFile = ctk.CTkEntry(master=frame, width=150, height=30)
entry_searchFile.place(x=25, y=120)
entry_searchFile.configure(justify="center")

button_execute = ctk.CTkButton(master=frame, text= "Executar", width=150, height=30, command=execute)
button_execute.place(x=25, y=160)

frame.mainloop()
