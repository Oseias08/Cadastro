import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Cadastro de Membros")

frame = tk.Frame(janela)
frame.pack()

# Salvando dados pessoais
user_info_frame = tk.LabelFrame(frame, text="Dados Pessoais")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

# Criando os nomes das entradas 

nome_label= tk.Label(user_info_frame, text="Nome Completo")
nome_label.grid(row=0, column=0)
sobrenome_label=tk.Label(user_info_frame, text="Apelido")
sobrenome_label.grid(row=0, column=1)
nascimento_label=tk.Label(user_info_frame, text="Data de Nascimento")
nascimento_label.grid(row=0, column=2)
civil_label=tk.Label(user_info_frame, text="Estado Civil")
civil_label.grid(row=2, column=0)

# Criando as caixas de entrada 

nome_entry=tk.Entry(user_info_frame)
sobrenome_entry=tk.Entry(user_info_frame)
nascimento_entry=tk.Entry(user_info_frame)
civil_combobox=ttk.Combobox(user_info_frame, value=[" ","Casado(a)","Solteiro(a)","Viúvo(a)","Divorciado(a)"])
nome_entry.grid(row=1, column=0)
sobrenome_entry.grid(row=1, column=1)
nascimento_entry.grid(row=1, column=2)
civil_combobox.grid(row=3, column=0)


for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)










janela.mainloop()