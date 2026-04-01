import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def enviar():
    nome= entrada_nome.get()
    idade= entrada_idade.get()
    escolaridade= combo_escolaridade.get()
    area= area.get()
    

    mensagem  = f"Nome: {nome}\n Idade:{idade}\n Ecolaridade:{escolaridade}\n Area:{area}"
    messagebox.showinfo("Dados Informados",mensagem)

janela = tk.Tk()
janela.title("Formulario de cadastro")

label_dados = tk.Label(janela,text= "Dados pessoais")
label_dados.pack()

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Nome da Janela
tela = tk.Tk()
tela.title("Formulário de Cadastro")
tela.minsize(300, 300)
tela.maxsize(600, 600)
tela.geometry("500x500")

# Subtitulo
sub_titulo = ttk.Label(tela, text="Dados Pessoais", font=("Times New Roman", 10, "bold"))
sub_titulo.grid(row=0, column=2)

vazio = ttk.Label(tela, text="")
vazio.grid(row=1, column=2)

# Entrada do nome
msg_nome = ttk.Label(tela, text="Insira seu Nome: ", font=("Times New Roman", 10))
msg_nome.grid(row=2, column=1)

entrada_nome = tk.Entry(tela, width=30)
entrada_nome.grid(row=2, column=2)

vazio = ttk.Label(tela, text="")
vazio.grid(row=3, column=4)

# Entrada da Idade
msg_idade = ttk.Label(tela, text="Insira sua Idade: ", font=("Times New Roman", 10))
msg_idade.grid(row=4, column=1)

entrada_idade = tk.Entry(tela, width=30)
entrada_idade.grid(row=4, column=2)

vazio = ttk.Label(tela, text="")
vazio.grid(row=5, column=6)

# Subtitulo dados Profissionais
sub_titulo_profissional = ttk.Label(tela, text="Dados Profissionais", font=("Times New Roman", 10, "bold"))
sub_titulo_profissional.grid(row=6, column=2)

vazio = ttk.Label(tela, text="")
vazio.grid(row=7, column=8)

# Escolaridade
escolaridade = ttk.Label(tela, text="Selecione sua escolaridade: ", font=("Times New Roman", 10))
escolaridade.grid(row=8, column=1)

combo_escolaridade = ttk.Combobox(
    tela,
    width=28,
    values=[
        "Ensino Médio Incompleto",
        "Ensino Médio Cursado",
        "Ensino Médio Completo",
    ]
)
combo_escolaridade.grid(row=8, column=2)

vazio = ttk.Label(tela, text="")
vazio.grid(row=9, column=10)

# Área de Atuação
area = tk.IntVar()

tk.Label(tela, text="Selecione sua Área de Atuação: ", font=("Times New Roman", 10, "bold")).grid(row=10, column=2)
tk.Radiobutton(tela, text="Técnico em Informática", font=("Times New Roman", 10), value=1, variable=area).grid(row=11, column=2)
tk.Radiobutton(tela, text="Técnico em Enfermagem", font=("Times New Roman", 10), value=2, variable=area).grid(row=12, column=2)
tk.Radiobutton(tela, text="Técnico em Segurança do Trabalho", font=("Times New Roman", 10), value=3, variable=area).grid(row=13, column=2)
tk.Radiobutton(tela, text="Técnico em Estética", font=("Times New Roman", 10), value=4, variable=area).grid(row=14, column=2)

vazio = ttk.Label(tela, text="")
vazio.grid(row=15, column=16)

# Função de Enviar
def enviar():
    nome = entrada_nome.get()
    idade = entrada_idade.get()
    info_escola = combo_escolaridade.get()

    # Descobrir área selecionada
    if area.get() == 1:
        area_atuacao = "Técnico em Informática"
    elif area.get() == 2:
        area_atuacao = "Técnico em Enfermagem"
    elif area.get() == 3:
        area_atuacao = "Técnico em Segurança do Trabalho"
    elif area.get() == 4:
        area_atuacao = "Técnico em Estética"
    # Mostrar no MessageBox
    messagebox.showinfo(
        "Dados do Formulário",f"Nome: {nome}\nIdade: {idade}\nEscolaridade: {info_escola}\nArea de Atuação: {area_atuacao}"
    )

# Botão de Enviar
tk.Button(tela, text="Enviar Formulário", command=enviar).grid(row=16, column=2)

tela.mainloop()

