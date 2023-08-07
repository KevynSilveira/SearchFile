import os
import zipfile
import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog

def buscar_arquivos_por_termo():
    termo = entry_searchFile.get()
    diretorio = entry_select.get()

    arquivos_encontrados = []
    for nome_arquivo in os.listdir(diretorio):
        if termo.lower() in nome_arquivo.lower():
            arquivos_encontrados.append(os.path.join(diretorio, nome_arquivo))
    return arquivos_encontrados

def zipar_arquivos(arquivos, destino):
    with zipfile.ZipFile(destino, 'w') as zip_file:
        for arquivo in arquivos:
            zip_file.write(arquivo, os.path.basename(arquivo))

def selecionar_pasta_busca():
    diretorio = filedialog.askdirectory()
    entry_select.delete(0, tk.END)
    entry_select.insert(0, diretorio)

def selecionar_pasta_destino():
    destino_zip = filedialog.asksaveasfilename(defaultextension=".zip")
    entry_destiny.delete(0, tk.END)
    entry_destiny.insert(0, destino_zip)


frame = ctk.CTk()
frame.geometry("200x300")
frame.title("Busca arquivos")
frame.resizable(False, False)

button_select = ctk.CTkButton(master=frame, text= "Diretório origem", width=150, height=30, command=selecionar_pasta_busca)
button_select.place(x=25, y=10)

entry_select = ctk.CTkEntry(master=frame, width=150, height=30)
entry_select.place(x=25, y=50)

button_destiny = ctk.CTkButton(master=frame, text= "Diretório destino", width=150, height=30, command=selecionar_pasta_destino)
button_destiny.place(x=25, y=90)

entry_destiny = ctk.CTkEntry(master=frame, width=150, height=30)
entry_destiny.place(x=25, y=130)

label_searchFile = ctk.CTkLabel(master=frame,text="Código", width=150, height=30)
label_searchFile.place(x=25, y=160)

entry_searchFile = ctk.CTkEntry(master=frame, width=150, height=30)
entry_searchFile.place(x=25, y=190)

button_execute = ctk.CTkButton(master=frame, text= "Executar", width=150, height=30)
button_execute.place(x=25, y=260)

frame.mainloop()


