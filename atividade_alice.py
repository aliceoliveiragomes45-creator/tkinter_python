import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


# Função para enviar os dados
def enviar():
    nome = entry_nome.get()
    idade = entry_idade.get()
    escolaridade = combo_escolaridade.get()
    area = var_area.get()

    mensagem = f"Nome: {nome}\nIdade: {idade}\nEscolaridade: {escolaridade}\nÁrea: {area}"
    messagebox.showinfo("Dados Informados", mensagem)

# Criando janela
janela = tk.Tk()
janela.title("Formulário de Cadastro")

# ===== Dados Pessoais =====
label_dados = tk.Label(janela, text="Dados Pessoais")
label_dados.pack()

tk.Label(janela, text="Nome:").pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()

tk.Label(janela, text="Idade:").pack()
entry_idade = tk.Entry(janela)
entry_idade.pack()

# ===== Dados Profissionais =====
label_prof = tk.Label(janela, text="Dados Profissionais")
label_prof.pack()

tk.Label(janela, text="Escolaridade:").pack()
combo_escolaridade = ttk.Combobox(janela)
combo_escolaridade['values'] = ("Ensino Fundamental", "Ensino Médio", "Ensho Superior")
combo_escolaridade.pack()

tk.Label(janela, text="Área de Atuação:").pack()

var_area = tk.StringVar()

tk.Radiobutton(janela, text="TI", variable=var_area, value="TI").pack()
tk.Radiobutton(janela, text="Administração", variable=var_area, value="Administração").pack()
tk.Radiobutton(janela, text="Saúde", variable=var_area, value="Saúde").pack()

# ===== Botão =====
botao = tk.Button(janela, text="Enviar", command=enviar)
botao.pack()

# Rodar janela
janela.mainloop()

