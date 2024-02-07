from tkinter import *
import tkinter.messagebox

def listaCompras():
    janela_lista_compras = Tk()
    janela_lista_compras.title("Lista De Compras")
    janela_lista_compras.geometry("400x300")

    frame_lista_compras = Frame(janela_lista_compras)
    frame_lista_compras.pack()

    listbox_lista_compras = Listbox(frame_lista_compras, height=8, width=50)
    listbox_lista_compras.pack(side=LEFT, padx=10, pady=5)

    scrollbar_lista_compras = Scrollbar(frame_lista_compras)
    scrollbar_lista_compras.pack(side=RIGHT, fill=Y)
    listbox_lista_compras.config(yscrollcommand=scrollbar_lista_compras.set)
    scrollbar_lista_compras.config(command=listbox_lista_compras.yview)

    entrada_lista_compras = Entry(janela_lista_compras, width=50)
    entrada_lista_compras.pack(padx=10, pady=5)

    botao_lista_compras = Button(janela_lista_compras, text="Adicionar Produto", width=20, command=lambda: adicionar(entrada_lista_compras, listbox_lista_compras))
    botao_lista_compras.pack(padx=10, pady=5)

    botao_lista_compras = Button(janela_lista_compras, text="Deletar Produto", width=20, command=deletar)
    botao_lista_compras.pack(padx=10, pady=5)

    janela_lista_compras.mainloop()

def adicionar(entrada, listbox):
    produto = entrada.get()
    if produto != "" and produto != " ":
        listbox.insert(END, produto)
        entrada.delete(0, END)
    else:
        tkinter.messagebox.showwarning(title="Erro!", message="Escreva um produto na barra de entrada")

def deletar(listbox):
    try:
        index_compras = listbox.curselection()[0]
        listbox.delete(index_compras)
    except:
        tkinter.messagebox.showwarning(title="Erro!", message="Selecione um produto com seu cursor")

def salvar():
    return

def carregar():
    return