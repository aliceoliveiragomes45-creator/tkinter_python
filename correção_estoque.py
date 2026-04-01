import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import os 
from datetime import datetime

DB_FILE = "Estoque_db.sqlite3"

# FUNÇÃO DE SEGURANÇA (Simulação)
# Em um sistema real, use hashlib (sha256) e salt
def hash_senha(senha):
    return senha

# JANELA DE LOGIN
class JanelaLogin:
    def __init__(self, janela):

        self.janela = janela
        self.janela.geometry("420x320")
        self.janela.title("LOGIN")
        self.janela.resizable(False, False)
        self.janela.eval('tk::PlaceWindow . center')
        
        # CRIAÇÃO DO FRAME 
        frame_principal = ttk.Frame(self.janela, padding="30 40")
        frame_principal.pack(fill="both", expand=True)
        
        # LABEL E ENTRADA DE DADOS DE TELA DE LOGIN
        ttk.Label(frame_principal, text="Login Controle de Estoque", font=("Arial", 14, "bold"))\
             .grid(row=0, column=0, columnspan=2, pady=(0, 25), sticky='ew')
        
        ttk.Label(frame_principal, text="USUÁRIO").grid(row=1, column=0, sticky='e', pady=8)
        self.usuario_var = tk.StringVar(value="admin")
        entrada_usuario = ttk.Entry(frame_principal, textvariable=self.usuario_var, width=25)
        entrada_usuario.grid(row=1, column=1, pady=8, sticky='w')
  
        ttk.Label(frame_principal, text="SENHA").grid(row=2, column=0, sticky='e', pady=8)
        self.senha_var = tk.StringVar()
        self.entrada_senha = ttk.Entry(frame_principal, textvariable=self.senha_var, width=25, show="*")
        self.entrada_senha.grid(row=2, column=1, pady=8, sticky='w')
        
        # BOTÕES
        btn_frame = ttk.Frame(frame_principal) # Corrigido nome (frane -> frame)
        btn_frame.grid(row=4, column=0, columnspan=2, pady=8, sticky='ew')
        ttk.Button(btn_frame, text='ENTRAR', command=self.verificar_login).pack(side='left')
        ttk.Button(btn_frame, text='SAIR', command=self.janela.quit).pack(side='left', padx=10)
        
        # LOGAR COM ENTER 
        self.entrada_senha.bind("<Return>", lambda event: self.verificar_login())
        
        style = ttk.Style()
        style.configure('Accent.TButton', font=('Arial', 10, 'bold'))
        self.entrada_senha.focus()

    def verificar_login(self):
        usuario = self.usuario_var.get().strip()
        senha = self.senha_var.get().strip()
    
        # Credenciais hardcoded (apenas para teste)
        if usuario == "admin" and senha == "8520789":
            messagebox.showinfo("Bem Vindo", f"Login Realizado com Sucesso!\nOlá, {usuario}")
            self.janela.destroy()
            abrir_sistema_estoque()
        else:
            messagebox.showerror("Erro de Login", "Usuário ou Senha Incorreto")
            self.senha_var.set("")
            self.entrada_senha.focus()

class EstoqueApp:
    def __init__(self, janela_main):
        self.janela_main = janela_main
        self.janela_main.title("Controle de Estoque")
        self.janela_main.geometry("950x650")
        self.janela_main.minsize(800, 600)

        self.conn = sqlite3.connect(DB_FILE)
        self.criar_tabelas()
        self.criar_interface()

        style = ttk.Style()
        # Corrigido: rowheigth -> rowheight
        style.configure("Treeview.Heading", rowheight=26, font=('Arial', 10))
        style.configure("Treeview", rowheight=26, font=('Arial', 10))

    def criar_tabelas(self):
        # Corrigido: self.corn -> self.conn
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtos(
              id TEXT PRIMARY KEY,
              nome TEXT NOT NULL,
              quantidade INTEGER NOT NULL, -- Corrigido: INTERGER -> INTEGER
              preco  REAL NOT NULL         -- Corrigido: preço -> preco (evitar acentos no DB)
           )
        ''')
        self.conn.commit()
    
    def criar_interface(self):
        # BOTÕES DE INTERAÇÃO
        frame_botoes = ttk.Frame(self.janela_main, padding="10")
        frame_botoes.pack(fill="x")

        botoes = [
            ("Novo Produto", self.novo_produto),
            ("Editar Produto", self.editar_produto),
            ("Excluir Produto", self.excluir_produto),
            ("Entrada", self.entrada_estoque), # Nome deve bater com o método
            ("Saída", self.saida_estoque),     # Nome deve bater com o método
            ("Atualizar", self.atualizar_tabela),
            ("SAIR", self.sair),
        ]
        for texto, cmd in botoes:
            ttk.Button(frame_botoes, text=texto, command=cmd).pack(side="left", padx=5)
        
        # TABELA
        frame_tabela = ttk.Frame(self.janela_main, padding="10")
        frame_tabela.pack(fill="both", expand=True)

        colunas = ("id", "nome", "quantidade", "preco")
        self.tree = ttk.Treeview(frame_tabela, columns=colunas, show="headings", selectmode="browse")

        self.tree.heading("id", text="Código")
        self.tree.heading("nome", text="Nome do Produto")
        self.tree.heading("quantidade", text="Quantidade")
        self.tree.heading("preco", text="Preço R$")
       
        self.tree.column("id", width=50, anchor="center")
        self.tree.column("nome", width=150)
        self.tree.column("quantidade", width=100, anchor="center")
        self.tree.column("preco", width=100, anchor="e")

        scrollbar = ttk.Scrollbar(frame_tabela, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.status_var = tk.StringVar(value="Pronto")
        ttk.Label(self.janela_main, textvariable=self.status_var, relief="sunken", anchor="w")\
           .pack(side="bottom", fill="x", ipady=5)
        
        self.atualizar_tabela()
        
    def atualizar_tabela(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, nome, quantidade, preco FROM produtos ORDER BY id")
        for row in cursor.fetchall():
            self.tree.insert("", "end", values=(row[0], row[1], row[2], f"{row[3]:.2f}"))
        cursor.execute("SELECT COUNT(*) FROM produtos")
        total = cursor.fetchone()[0]
        self.status_var.set(f"Total de produtos: {total} | Banco: {DB_FILE}")

    def get_produto_selecionado(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("ATENÇÃO", "Selecione um produto na tabela!")
            return None
        id = self.tree.item(sel[0])["values"] [0]
        cursor = self.conn.cursor()
        cursor.execute("SELECT nome, quantidade, preco FROM produtos WHERE id=?", (id,))
        row = cursor.fetchone()
        return (id, {"nome": row[0], "quantidade": row[1], "preco": row[2]}) if row else None
    
    def novo_produto(self):
        janela_add = tk.Toplevel(self.janela_main)
        janela_add.title("Adicionar Produto")
        janela_add.geometry("450x350")
        janela_add.transient(self.janela_main)
        janela_add.grab_set()

        ttk.Label(janela_add, text="ID (Código):").pack(pady=(20, 5))
        entrada_id = ttk.Entry(janela_add, width=25)
        entrada_id.pack()

        ttk.Label(janela_add, text="Nome:").pack(pady=(10, 5))
        entrada_nome = ttk.Entry(janela_add, width=25)
        entrada_nome.pack()

        ttk.Label(janela_add, text="Quantidade:").pack(pady=(10, 5))
        entrada_quantidade = ttk.Entry(janela_add, width=25)
        entrada_quantidade.pack()

        ttk.Label(janela_add, text="Preço UND (use ponto ou vírgula):").pack(pady=(10, 5))
        entrada_preco = ttk.Entry(janela_add, width=25)
        entrada_preco.pack()
        def salvar():
            id_val = entrada_id.get().strip().upper()
            nome = entrada_nome.get().strip()
            try:
                qtd = int(entrada_quantidade.get())
                if qtd < 0: raise ValueError("Negativo")
                preco_str = entrada_preco.get().replace(',', '.')
                preco = float(preco_str)
                if preco < 0: raise ValueError("Negativo")
            except ValueError:
                messagebox.showerror("ERRO", "Valores Inválidos! (Qtd int >= 0, Preço float >= 0)")
                return
            
            if not id_val or not nome:
               messagebox.showwarning("Atenção", "Código e Nome são obrigatórios")
               return
               
            try:
                cursor = self.conn.cursor()
                cursor.execute("INSERT INTO produtos(id, nome, quantidade, preco) VALUES(?,?,?,?)",
                               (id_val, nome, qtd, preco))
                self.conn.commit()
                self.atualizar_tabela()
                janela_add.destroy()
                messagebox.showinfo("Sucesso!", f"Produto {nome} cadastrado!")
            except sqlite3.IntegrityError:
                messagebox.showerror("Erro", "Este ID já existe!")

        ttk.Button(janela_add, text="Salvar", command=salvar).pack(pady=25)
   
        
    def editar_produto(self):
        item = self.get_produto_selecionado()
        if not item:
            return
        id, dados = item
        
        janela_edit = tk.Toplevel(self.janela_main) 
        janela_edit.title("Editar Produto")
        janela_edit.geometry("450x350")
        janela_edit.transient(self.janela_main)
        janela_edit.grab_set()
        
        ttk.Label(janela_edit, text=f"ID: {id}").pack(pady=10)

        ttk.Label(janela_edit, text="Nome: ").pack()
        entrada_nome = ttk.Entry(janela_edit, width=50)
        entrada_nome.insert(0, dados["nome"])
        entrada_nome.pack(pady=5)

        ttk.Label(janela_edit, text="Quantidade: ").pack()
        entrada_quantidade = ttk.Entry(janela_edit, width=20)
        entrada_quantidade.insert(0, dados["quantidade"])
        entrada_quantidade.pack(pady=5)

        ttk.Label(janela_edit, text="Preço R$: ").pack()
        entrada_preco = ttk.Entry(janela_edit, width=20)
        entrada_preco.insert(0, dados["preco"])
        entrada_preco.pack(pady=5)

        def salvar():
            try:
                nome = entrada_nome.get().strip()
                qnt = int(entrada_quantidade.get())
                preco = float(entrada_preco.get().replace(",", "."))
                
                if not nome or qnt < 0 or preco < 0:
                    messagebox.showerror("Erro", "Dados inválidos.")
                    return

                cursor = self.conn.cursor()
                cursor.execute("UPDATE produtos SET nome=?, quantidade=?, preco=? WHERE id=?",
                               (nome, qnt, preco, id))
                self.conn.commit()
                self.atualizar_tabela()
                janela_edit.destroy()
                messagebox.showinfo("Sucesso!", "Produto Atualizado")
            except Exception as e:
                messagebox.showerror("Erro!", f"Verifique os Valores. {e}")

    
        ttk.Button(janela_edit, text="Salvar Alterações", command=salvar).pack(pady=25)

    def excluir_produto(self):
        item = self.get_produto_selecionado()
        if not item:
            return
        id, dados = item
        if messagebox.askyesno("Confirmação", f"Excluir {dados["nome"]}({id})"):
                cursor = self.conn.cursor()
                cursor.execute("DELETE FROM produtos WHERE id=?", (id))
                self.conn.commit()
                self.atualizar_tabela()
                messagebox.showinfo("Sucesso", "Produto excluído.")
    def movimentar_estoque(self, tipo):
        item = self.get_produto_selecionado()
        if not item:
            return
        id, dados = item
        titulo= "Entrada" if tipo == "entrada" else "Saída"
        qnt_str = simpledialog.asktring(titulo, f"Quantidade a{tipo} em {dados['nome']}?", parent= self.janela_main)
        if not qnt_str:
            return
        try:
            qtd = int(qnt_str)
            if qtd <=0:
                raise ValueError
        
            cursor = self.conn.cursor()
            if tipo == "entrada":
                cursor.execute("UPDATE produtos SET quantidade = quantidade + ? WHERE id=?", (qtd, id))
            else:
                cursor.execute('SELECT quantidade FROM produtos WHERE id=?' ,(id,))
                atual = cursor.fetchone()[0]
                if qtd > atual:
                    messagebox.showerror("Eroo", f"Estoque insuficiente! Diposnivel: {atual}")
                cursor.execute('UPDATE produtos SET quantidade = quantidade  - ? WHERE id=?', (qtd, id))
            self.conn.commit()
            self.atualizar_tabela()
            messagebox.showerror('Sucesso!', f"Movimentação de {qtd} unidades realizar!")
        except:
            messagebox.showerror("Erro", "Informe um número inteiro Positivo") 

    def entrada_estoque(self):
       self.movimentar_estoque("entrada")

    def saida_estoque(self):
       self.movimentar_estoque("saida")

    def sair(self): self.janela_main.quit()
        

def abrir_sistema_estoque():
    janela_main = tk.Tk()
    app = EstoqueApp(janela_main)
    janela_main.mainloop()

if __name__ == "__main__":
    janela = tk.Tk()
    # Ocultar a janela principal inicial para não piscar antes do login
    janela.withdraw() 
    app = JanelaLogin(janela)
    janela.mainloop()