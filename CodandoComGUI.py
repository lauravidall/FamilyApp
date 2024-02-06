'''' Passo a passo:
1- Importar o tkinter
2- Colocar todo o código que você quer que rode quando uma pessoa apertar algum botão, dentro de uma função
3- Criar e modificar a sua janela com o tkinter'''

import os
os.system('clear')

from tkinter import *
#Tk() --> utilizado para abrir código em uma janela a parte

def pegarcotacoes():

    Dol = 4.98
    Eur = 5.79

    texto = f"""
    Dolar: {Dol}
    Euro: {Eur}"""

    textodascotacoes["text"] = texto

janela = Tk() #abre a janela e depois fecha ela
janela.title("Cotações Atuais")
janela.geometry("300x300") #voce dita o tamanho da sua janela

#Label --> texto dentro da janela. 1-Onde vai ser exibido, qual janela? 
textodeorientacao = Label(janela, text="Clique no botão para ver as cotações")
#Grid --> Onde o texto da label vai ser posicionado e voce bota o padx e o pady para posicionar melhor o texto na sua janela
textodeorientacao.grid(column=0, row=0, padx=10, pady=10)

#Button --> método pra criar um botão  
botao = Button(janela, text="Buscar cotação do Dolar e do Euro", command=pegarcotacoes) #Não botar o parenteses pos funcao
botao.grid(column=0, row=1, padx=10, pady=10)

textodascotacoes = Label(janela, text="")
textodascotacoes.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop() #deixa a janela aberta pra sempre (vai ser sempre a ultima coisa do código)