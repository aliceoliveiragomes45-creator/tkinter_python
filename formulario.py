import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

janela = tk.Tk()
janela.title("Formulário")
janela.geometry("300x300")

def enviar():
    nome= entrada_nome.get()
    estado=combo_estado.get()
    sexo= opc.get()
    
    sexo_texto ="Masculino" if sexo ==1  else "Feminino"

    msg = f"Nome: {nome}\n Estado:{estado}\n Sexo:{sexo}"
    messagebox.showinfo("Dados enviados",msg)

tk.Label(janela, text="Formulário de Cadastro", font=("Arial", 14)).grid(column=1, pady=20)

#entrada de texto
tk.Label(janela, text="Nome:", font=("Arial")).grid(row=1, column=0)
entrada_nome= tk.Entry(janela, font=("Arial"))
entrada_nome.grid(row=1, column=1)
#RADIOBUTTON
opc = tk.IntVar()

tk.Label(janela, text="Sexo:", font=("Arial")).grid(row=3, column=0)
tk.Radiobutton(janela, text="Masculino", font=("Arial"), value=1, variable=opc)\
.grid(row=3, column=1)
tk.Radiobutton(janela, text="Feminino", font=("Arial"), value=2, variable=opc)\
.grid(row=4, column=1)

#COMBOBOX
tk.Label(janela, text="Estado").grid(row=5, column=0)
combo_estado = ttk.Combobox(janela, values=["MG", "SP", "RJ", "RN", "BA"])
combo_estado.grid(row=5, column=1)

#BOTAO
tk.Button(janela, text= "Enviar").grid(row=7, column=1,pady=20)


janela.mainloop()
