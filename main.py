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

def zip(): # compacta os arquivos
    global arquivos_encontrados
    filetypes = [('Arquivos', '*.zip')]
    destiny = filedialog.asksaveasfilename(defaultextension=".zip", initialfile="Arquivos", filetypes=filetypes)
    with zipfile.ZipFile(destiny, 'w') as zip_file:
        for file in arquivos_encontrados:
            zip_file.write(file, os.path.basename(file))

def select(): # Seleciona o direório de busca
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
frame.geometry("240x240")
frame.title("SearchFile")
frame.resizable(False, False)

label_searchFile = ctk.CTkLabel(master=frame,text="SearchFile", width=180, height=30)
label_searchFile.configure(justify="center", font=("arial", 18))
label_searchFile.place(x=30, y=5)

button_select = ctk.CTkButton(master=frame, text= "Diretório origem", width=180, height=30, command=select, fg_color="dark grey", text_color="black", hover_color="gray")
button_select.configure(font=("arial", 14))
button_select.place(x=30, y=50)

entry_select = ctk.CTkEntry(master=frame, width=180, height=30)
entry_select.configure(justify="center", font=("arial", 14))
entry_select.place(x=30, y=90)

label_code = ctk.CTkLabel(master=frame,text="Insira a palavra chave:", width=180, height=30, text_color="white")
label_code.configure(justify="center", font=("arial", 16))
label_code.place(x=30, y=125)

entry_searchFile = ctk.CTkEntry(master=frame, width=180, height=30)
entry_searchFile.place(x=30, y=160)
entry_searchFile.configure(justify="center", font=("arial", 14))

button_execute = ctk.CTkButton(master=frame, text="Executar", width=180, height=30, command=execute, fg_color="dark grey", text_color="black", hover_color="gray")
button_execute.configure(font=("arial", 14))
button_execute.place(x=30, y=200)

frame.mainloop()
