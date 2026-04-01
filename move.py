import tkinter as tk

janela = tk.Tk()
janela.geometry("400x400")
janela.title("Mover elementos")

frame_formulario = tk.Frame(janela, bg='blue')
frame_formulario.place(x=15)


texto = tk.Label(text="Nome")
texto.place(x=20, y=100)

entrada_nome= tk.Entry(janela)

janela.mainloop()