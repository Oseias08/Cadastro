# -*- coding: utf-8 -*-
import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Cadastro de Membros")
janela.configure(background="#dde")

frame = tk.Frame(janela)
frame.pack()
frame.configure(background="#dde")

# Salvando dados pessoais
user_info_frame = tk.LabelFrame(frame, text="Dados Pessoais", background="#dde", foreground="#009")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

# Criando os nomes das entradas 

nome_label= tk.Label(user_info_frame, text="Nome Completo", background="#dde", foreground="#009", width=20, anchor=tk.W)
nome_label.grid(row=0, column=0, sticky=tk.W)
sobrenome_label=tk.Label(user_info_frame, text="Apelido", background="#dde", foreground="#009")
sobrenome_label.grid(row=0, column=1, sticky=tk.W)
nascimento_label=tk.Label(user_info_frame, text="Data de Nascimento", background="#dde", foreground="#009")
nascimento_label.grid(row=0, column=2, sticky=tk.W)
civil_label=tk.Label(user_info_frame, text="Estado Civil", background="#dde", foreground="#009", width=10, anchor=tk.W)
civil_label.grid(row=6, column=0, sticky=tk.NW)
telefone_label = tk.Label(user_info_frame, text="Telefone", background="#dde", foreground="#009")
telefone_label.grid(row=2, column=2, sticky=tk.W)
sexo_label=tk.Label(user_info_frame, text="Sexo", background="#dde", foreground="#009")
sexo_label.grid(row=6, column=0, sticky=tk.N)
endereco_label=tk.Label(user_info_frame, text="Endereço", background="#dde", foreground="#009")
endereco_label.grid(row=2, column=0, sticky=tk.W)
cep_label=tk.Label(user_info_frame, text="CEP", background="#dde", foreground="#009", width=20, anchor=tk.W)
cep_label.grid(row=2, column=1, sticky=tk.W)
email_label= tk.Label(user_info_frame, text="E-mail", background="#dde", foreground="#009", width=20, anchor=tk.W)
email_label.grid(row=4, column=0, sticky=tk.W)


# Criando as caixas de entrada 

nome_entry=tk.Entry(user_info_frame, width=100)
sobrenome_entry=tk.Entry(user_info_frame)
nascimento_entry=tk.Entry(user_info_frame)
email_entry=tk.Entry(user_info_frame, width=100)
telefone_entry=tk.Entry(user_info_frame)
sexo_combobox=ttk.Combobox(user_info_frame, value=[" ", "Masculino", "Feminino"], width=9)
endereco_entry=tk.Entry(user_info_frame, width=100)
cep_entry=tk.Entry(user_info_frame)
civil_combobox=ttk.Combobox(user_info_frame, value=[" ","Casado(a)","Solteiro(a)","Viúvo(a)","Divorciado(a)"], width=13)
nome_entry.grid(row=1, column=0)
sobrenome_entry.grid(row=1, column=1, sticky=tk.W)
nascimento_entry.grid(row=1, column=2, sticky=tk.W)
telefone_entry.grid(row=3, column=2)
endereco_entry.grid(row=3, column=0, sticky=tk.W)
cep_entry.grid(row=3, column=1, sticky=tk.W)
email_entry.grid(row=5, column=0, sticky=tk.W)
civil_combobox.grid(row=7, column=0, columnspan=1, sticky=tk.W)
sexo_combobox.grid(row=7, column=0, columnspan=1, sticky=tk.S)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=5, pady=2.5)










janela.mainloop()