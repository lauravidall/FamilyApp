from tkinter import *
import tkinter.messagebox

def eventos():
    janela_eventos = Tk()
    janela_eventos.title("Eventos Da Família")
    janela_eventos.geometry("400x300")

    frame_eventos = Frame(janela_eventos)
    frame_eventos.pack()

    listbox_eventos = Listbox(frame_eventos, height=8, width=50)
    listbox_eventos.pack(side=LEFT, padx=10, pady=5)

    scrollbar_eventos = Scrollbar(frame_eventos)
    scrollbar_eventos.pack(side=RIGHT, fill=Y)
    listbox_eventos.config(yscrollcommand=scrollbar_eventos.set)
    scrollbar_eventos.config(command=listbox_eventos.yview)

    entrada_eventos = Entry(janela_eventos, width=50)
    entrada_eventos.pack(padx=10, pady=5)

    botao_eventos = Button(janela_eventos, text="Adicionar Evento", width=20, command=lambda: adicionar(entrada_eventos, listbox_eventos))
    botao_eventos.pack(padx=10, pady=5)

    botao_eventos = Button(janela_eventos, text="Deletar Evento", width=20, command=lambda: deletar(listbox_eventos))
    botao_eventos.pack(padx=10, pady=5)

    leitura_txt(listbox_eventos)

    janela_eventos.mainloop()

def adicionar(entrada, listbox):
    evento = entrada.get()
    if evento != "" and evento != " ":
        item = f"{evento}\n"
        with open("eventos.txt", 'a', encoding="utf-8") as file:
            file.write(item)
        listbox.insert(END, item)
        entrada.delete(0, END)
    else:
        tkinter.messagebox.showwarning(title="Erro!", message="Escreva um evento na barra de entrada")

# def deletar(listbox):
#     try:
#         index_eventos = listbox.curselection()[0]
#         listbox.delete(index_eventos)
#     except:
#         tkinter.messagebox.showwarning(title="Erro!", message="Selecione um evento com seu cursor")
        
def deletar(listbox):
    try:
        index_eventos = listbox.curselection()[0]
        item_selecionado = listbox.get(index_eventos) + "\n"
        listbox.delete(index_eventos)

        with open("eventos.txt", 'r', encoding="utf-8") as file:
            linhas = file.readlines()
        
        with open("eventos.txt", 'w', encoding="utf-8") as file:
            for linha in linhas:
                if linha != item_selecionado:
                    file.write(linha)

    except IndexError:
        tkinter.messagebox.showwarning(title="Erro!", message="Selecione um evento com o cursor.")
        
def leitura_txt(listbox):
    try:
        with open("eventos.txt", 'r', encoding="utf-8") as file:
            linhas = file.readlines()
            for linha in linhas:
                listbox.insert(END, linha.strip())
    except FileNotFoundError:
        pass