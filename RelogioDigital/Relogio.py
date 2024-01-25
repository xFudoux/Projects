import tkinter
from tkinter import *
from datetime import datetime
import locale

#Importando fonte externas para dentro
from tkextrafont import Font        #Obs:tem que estar dentro da janela

#Cores#
preto = '#3d3d3d'
branco = '#fcfafa'
verde = '#3a992f'
vermelho = '#b00911'
marrom = '#6e2a19'
azul = '#022e75'

fundo = preto
cor_letra = branco

#CONFIGURAÇÕES DA JANELA
janela = Tk ()
Font(file='digital-7.ttf')           #Fonte importado via tkextrafont
janela.title('Relógio')     #NOME
janela.geometry('320x150')  #TAMANHO
janela.resizable(width=False,height=False)          #NAO PERMITE ALTERAR O TAMANHO DA JANELA
janela.configure(bg=preto)
#---------------------------------------------------------------------------------------------------------------

#Hora/Data
def relogio():
    locale.setlocale(locale.LC_TIME,'pt_BR')       #setar saida dia/mes para portugues
    tempo = datetime.now()
    hora = tempo.strftime('%H:%M:%S')
    dia_semana = tempo.strftime('%A').title()
    dia = tempo.strftime('%d/%m/%Y')
    mes = tempo.strftime('%B').title()
    ano = tempo.strftime('%Y')

    l1.configure(text=hora)
    l1.after(200,relogio)
    l2.configure(text=f'{dia_semana}     {dia}')

l1 = Label(janela,text='',font='digital-7 80',bg=fundo,fg=cor_letra)
l1.grid(row=0,column=0,sticky=NW,padx=5)

l2 = Label(janela,text='',font='digital-7 21',bg=fundo,fg=verde)
l2.grid(row=1,column=0,sticky=NW,padx=5)


relogio()
janela.mainloop()
