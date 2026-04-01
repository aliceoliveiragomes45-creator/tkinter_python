import tkinter as  tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
#Tela de Cadastro
tela = tk.Tk()
tela.title("Formulário de Cadastro")
tela.minsize(400,400)
tela.geometry("50x600")


#Inclusão do Nome
nome = ttk.Label(tela,text="Insira seu Nome:")
nome.place(x=20, y=35)
entrada_nome = tk.Entry(tela)
entrada_nome.place(x=20, y=60)
#Inclusão do Sobrenome
sobrenome = ttk.Label(tela,text="Insira seu Sobrenome:")
sobrenome.place(x=20, y=85)
entrada_sobrenome = tk.Entry(tela)
entrada_sobrenome.place(x=20, y=110)

#Inclusão da Data de Nascimento
data_nasc = ttk.Label(tela,text="Insira sua data de nascimento:")
data_nasc.place(x=20, y=135)
entrada_nasc = tk.Entry(tela)
entrada_nasc.place(x=20, y=160)

#Inclusão de CPF
cpf = ttk.Label(tela,text="Insira seu CPF:")
cpf.place(x=20, y=185)
entrada_cpf = tk.Entry(tela)
entrada_cpf.place(x=20, y=210)

#Inclusão de CEP
cep = ttk.Label(tela,text="Insira seu CEP:")
cep.place(x=20, y=235)
entrada_cep = tk.Entry(tela)
entrada_cep.place(x=20, y=260)

#ENTRADA DE SEXO
label_entrada = ttk.Label(tela,text="Sexo:")
label_entrada.place(x=20, y=285)
opcao = tk.IntVar()
opc_1 = tk.Radiobutton(tela, text="Masculino", variable=opcao, value=1)
opc_2 = tk.Radiobutton(tela, text="Feminino", variable=opcao, value=2)
opc_3 = tk.Radiobutton(tela, text="Outro", variable=opcao, value=3)
opc_1.place(x=20, y=310)
opc_2.place(x=20, y=335)
opc_3.place(x=20, y=360)

#Inclusão de Estado
estado = ttk.Label(tela, text="Selecione o estado correspondente ao CEP:")
estado.place(x=20, y=385)
estado_entrada = ttk.Combobox(tela, values=["MG", "RJ", "RS", "RN", "CE"])
estado_entrada.place(x=20, y= 410)

#Inclusão de Cidade
cidade = ttk.Label(tela,text="Informe sua Cidade:")
cidade.place(x=20, y=435)
entrada_cidade = tk.Entry(tela)
entrada_cidade.place(x=20, y=460)

#BOTÃO
def clicar():
    nome = entrada_nome.get()
    sobrenome = entrada_sobrenome.get()
    nasc = entrada_nasc.get()
    cpf = entrada_cpf.get()
    cep = entrada_cep.get()
    estado = estado_entrada.get()
    if opcao.get() == 1:
        sexo = "Masculino"
    elif opcao.get() == 2:
        sexo = "Feminino"
    elif opcao.get() == 3:
        sexo = "Outro"
    cidade = entrada_cidade.get()
    messagebox.showinfo("Mensagem: ",f"Nome: {nome}, Sobrenome: {sobrenome}, Nascido em: {nasc}, CPF: {cpf}, CEP: {cep}, Sexo: {sexo}, Estado: {estado}, Cidade: {cidade}.")
btn = tk.Button(tela, text="Enviar formulário", command=clicar)
btn.place(x=20, y=485)
tela.mainloop()
