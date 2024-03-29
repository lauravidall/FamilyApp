from tkinter import *
import tkinter.messagebox

def pessoas():
    janela_pessoas = Tk()
    janela_pessoas.title("Pessoas Da Família")
    janela_pessoas.geometry("400x300")

    frame_pessoas = Frame(janela_pessoas)
    frame_pessoas.pack()

    listbox_pessoas = Listbox(frame_pessoas, height=8, width=50)
    listbox_pessoas.pack(side=LEFT, padx=10, pady=5)

    scrollbar_pessoas = Scrollbar(frame_pessoas)
    scrollbar_pessoas.pack(side=RIGHT, fill=Y)
    listbox_pessoas.config(yscrollcommand=scrollbar_pessoas.set)
    scrollbar_pessoas.config(command=listbox_pessoas.yview)

    entrada_pessoas = Entry(janela_pessoas, width=50)
    entrada_pessoas.pack(padx=10, pady=5)

    botao_pessoas = Button(janela_pessoas, text="Adicionar Membro", width=20, command=lambda: adicionar(entrada_pessoas, listbox_pessoas))
    botao_pessoas.pack(padx=10, pady=5)

    botao_pessoas = Button(janela_pessoas, text="Deletar Membro", width=20, command=lambda: deletar(listbox_pessoas))
    botao_pessoas.pack(padx=10, pady=5)

    leitura_txt(listbox_pessoas)

    janela_pessoas.mainloop()

def adicionar(entrada, listbox):
    pessoa = entrada.get()
    if pessoa != "" and pessoa != " ":
        item = f"{pessoa}\n"
        with open("pessoas.txt", 'a', encoding="utf-8") as file:
            file.write(item)
        listbox.insert(END, item)
        entrada.delete(0, END)
    else:
        tkinter.messagebox.showwarning(title="Erro!", message="Escreva um nome na barra de entrada")

# def deletar(listbox):
#     try:
#         index_pessoa = listbox.curselection()[0]
#         listbox.delete(index_pessoa)
#     except:
#         tkinter.messagebox.showwarning(title="Erro!", message="Selecione um nome com seu cursor")

def deletar(listbox):
    try:
        index_pessoas = listbox.curselection()[0]
        item_selecionado = listbox.get(index_pessoas) + "\n"
        listbox.delete(index_pessoas)

        with open("pessoas.txt", 'r', encoding="utf-8") as file:
            linhas = file.readlines()
        
        with open("pessoas.txt", 'w', encoding="utf-8") as file:
            for linha in linhas:
                if linha != item_selecionado:
                    file.write(linha)

    except IndexError:
        tkinter.messagebox.showwarning(title="Erro!", message="Selecione uma pessoa com o cursor.")
        
def leitura_txt(listbox):
    try:
        with open("pessoas.txt", 'r', encoding="utf-8") as file:
            linhas = file.readlines()
            for linha in linhas:
                listbox.insert(END, linha.strip())
    except FileNotFoundError:
        pass