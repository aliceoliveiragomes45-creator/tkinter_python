import tkinter as tk

janela_main = tk.Tk()

janela_main.title("minha janela")
janela_main.configure(background= "pink")
janela_main.minsize(200,200)
janela_main.maxsize(500,500)
janela_main.geometry("300x300")

#OBJETO EM JANELA
tk.Label(janela_main,
         text= "Hello world",
         bg= "ligth pink",
         font=("Arial", 16, "bold")
         ).pack(expand=True)
#IMAGENS
imagem = tk.PhotoImage(file="barbie.png")
tk.Label(janela_main, image=imagem). pack()
