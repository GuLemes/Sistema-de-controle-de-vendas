import tkinter as tk
from tkinter import messagebox, simpledialog

# Estrutura de dados para armazenar os produtos
produtos = {}

def adicionar_produto():
    nome = simpledialog.askstring("Adicionar Produto", "Digite o nome do produto:")
    if nome:
        preco = simpledialog.askfloat("Adicionar Produto", "Digite o preço do produto:")
        quantidade = simpledialog.askinteger("Adicionar Produto", "Digite a quantidade em estoque:")
        produtos[nome] = {"preço": preco, "quantidade": quantidade}
        messagebox.showinfo("Informação", f"Produto {nome} adicionado com sucesso!")

def atualizar_produto():
    nome = simpledialog.askstring("Atualizar Produto", "Digite o nome do produto a ser atualizado:")
    if nome and nome in produtos:
        preco = simpledialog.askfloat("Atualizar Produto", "Digite o novo preço do produto:")
        quantidade = simpledialog.askinteger("Atualizar Produto", "Digite a nova quantidade em estoque:")
        produtos[nome]["preço"] = preco
        produtos[nome]["quantidade"] = quantidade
        messagebox.showinfo("Informação", f"Produto {nome} atualizado com sucesso!")
    else:
        messagebox.showwarning("Aviso", f"Produto {nome} não encontrado no estoque.")

def visualizar_estoque():
    if produtos:
        estoque_str = "\n".join([f"Nome: {nome}, Preço: {dados['preço']}, Quantidade: {dados['quantidade']}" for nome, dados in produtos.items()])
        messagebox.showinfo("Estoque", estoque_str)
    else:
        messagebox.showinfo("Estoque", "Estoque vazio.")

def sair():
    root.destroy()

# Configuração da janela principal
root = tk.Tk()
root.title("Sistema de Gerenciamento de Vendas")

# Botões do menu
btn_adicionar = tk.Button(root, text="Adicionar Produto", command=adicionar_produto)
btn_adicionar.pack(pady=10)

btn_atualizar = tk.Button(root, text="Atualizar Produto", command=atualizar_produto)
btn_atualizar.pack(pady=10)

btn_visualizar = tk.Button(root, text="Visualizar Estoque", command=visualizar_estoque)
btn_visualizar.pack(pady=10)

btn_sair = tk.Button(root, text="Sair", command=sair)
btn_sair.pack(pady=10)

# Iniciar o loop principal da interface
root.mainloop()
