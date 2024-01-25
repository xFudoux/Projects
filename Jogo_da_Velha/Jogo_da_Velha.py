import tkinter
from tkinter import ttk
from tkinter import *


#cores

# cores ---------------------------------------
branco = "#FFFFFF"  # branca / white
preto = "#333333"  # preta pesado / dark black
laranja = "#fcc058"  # laranja / orange
azul = "#38576b"  # valor / value
azul_claro = "#3297a8"   # azul / blue
amarelo = "#fff873"   # amarela / yellow
vermelho = "#e85151"   # vermelha / red
branco_acizentado ="#fcfbf7"
fundo = "#3b3b3b" # preta / black

#Janela

janela = Tk()
janela.title('Jogo Da Velha')
janela.geometry('260x370')
janela.resizable(0,0)
janela.configure(bg=fundo)

#Dividindo a Janela

tela_cima = Frame(janela,width=240,height=100,bg=preto,relief='raised')
tela_cima.grid(row=0,column=0,sticky='Nw',padx=10,pady=10)

tela_baixo = Frame(janela,width=240,height=300,bg=fundo,relief='flat')
tela_baixo.grid(row=1,column=0,sticky='Nw')


#Configurando TELA_CIMA

jogador_X = Label(tela_cima,text='X',height=1,relief='flat',anchor='center',font='Ivy 40 bold',bg=preto,fg=vermelho)
jogador_X.place(x=25,y=10)
jogador_X = Label(tela_cima,text='Jogador 1',height=1,relief='flat',anchor='center',font=('Ivy 7 bold'),bg=preto,fg=branco)
jogador_X.place(x=17,y=70)
jogador_X_pontos = Label(tela_cima,text='0',height=1,relief='flat',anchor='center',font='Ivy 30 bold',bg=preto,fg=branco)
jogador_X_pontos.place(x=80,y=20)

separador = Label(tela_cima,text=':',height=1,relief='flat',anchor='center',font='Ivy 20 bold',bg=preto,fg=branco)
separador.place(x=110,y=25)

jogador_O = Label(tela_cima,text='O',height=1,relief='flat',anchor='center',font='Ivy 42 bold',bg=preto,fg=azul_claro)
jogador_O.place(x=170,y=8)
jogador_O = Label(tela_cima,text='Jogador 2',height=1,relief='flat',anchor='center',font=('Ivy 7 bold'),bg=preto,fg=branco)
jogador_O.place(x=165,y=70)
jogador_O_pontos = Label(tela_cima,text='0',height=1,relief='flat',anchor='center',font='Ivy 30 bold',bg=preto,fg=branco)
jogador_O_pontos.place(x=130,y=20)


#Criando funções do jogo

jogador_1 = 'X'
jogador_2 = 'O'

ponto_X = 0
ponto_O = 0

#Lista que representa as linhasXColunas
'''           1 | 2 | 3
            A   |   |
            ----|---|----
            B   |   |
            ----|---|----
            C   |   |
            ----|---|----
'''
LxC = [['A1','A2','A3'],['B1','B2','B3'],['C1','C2,','C3']]

jogando = 'X'
joga = ''
contador = 0
contador_de_rodadas = 0


#Função para iniciar o jogo

def iniciar_jogo():
    botao_play.destroy()
    def controlar_movimento(interacao):
        global jogando
        global contador
        global jogar
        #Verifica o valor recebido com a lista
        if interacao == ('A1'):

            #verificando se aquela posição esta vazia
            if A_1['text'] == '':

                #Verifica quem esta jogando,para definir a cor
                if jogando == 'X':
                    cor=vermelho
                if jogando == 'O':
                    cor=azul_claro

                #Definindo a cor que vai aparecer no botão de acordo com quem esta jogando
                A_1['fg'] = cor
                A_1['text'] = jogando
                LxC[0][0] = jogando

                # verificando quem jogou, para trocar o jogador
                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                #aumentando o n° do contador
                contador+=1
        if interacao == ('A2'):

            #verificando se aquela posição esta vazia
            if A_2['text'] == '':

                #Verifica quem esta jogando,para definir a cor
                if jogando == 'X':
                    cor=vermelho
                if jogando == 'O':
                    cor=azul_claro

                #Definindo a cor que vai aparecer no botão de acordo com quem esta jogando
                A_2['fg'] = cor
                A_2['text'] = jogando
                LxC[0][1] = jogando

                # verificando quem jogou, para trocar o jogador
                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                #aumentando o n° do contador
                contador+=1
        if interacao == ('A3'):

            #verificando se aquela posição esta vazia
            if A_3['text'] == '':

                #Verifica quem esta jogando,para definir a cor
                if jogando == 'X':
                    cor=vermelho
                if jogando == 'O':
                    cor=azul_claro

                #Definindo a cor que vai aparecer no botão de acordo com quem esta jogando
                A_3['fg'] = cor
                A_3['text'] = jogando
                LxC[0][2] = jogando

                # verificando quem jogou, para trocar o jogador
                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                #aumentando o n° do contador
                contador+=1
        if interacao == ('B1'):

            #verificando se aquela posição esta vazia
            if B_1['text'] == '':

                #Verifica quem esta jogando,para definir a cor
                if jogando == 'X':
                    cor=vermelho
                if jogando == 'O':
                    cor=azul_claro

                #Definindo a cor que vai aparecer no botão de acordo com quem esta jogando
                B_1['fg'] = cor
                B_1['text'] = jogando
                LxC[1][0] = jogando

                # verificando quem jogou, para trocar o jogador
                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                #aumentando o n° do contador
                contador+=1
        if interacao == ('B2'):

            #verificando se aquela posição esta vazia
            if B_2['text'] == '':

                #Verifica quem esta jogando,para definir a cor
                if jogando == 'X':
                    cor=vermelho
                if jogando == 'O':
                    cor=azul_claro

                #Definindo a cor que vai aparecer no botão de acordo com quem esta jogando
                B_2['fg'] = cor
                B_2['text'] = jogando
                LxC[1][1] = jogando

                # verificando quem jogou, para trocar o jogador
                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                #aumentando o n° do contador
                contador+=1
        if interacao == ('B3'):

            #verificando se aquela posição esta vazia
            if B_3['text'] == '':

                #Verifica quem esta jogando,para definir a cor
                if jogando == 'X':
                    cor=vermelho
                if jogando == 'O':
                    cor=azul_claro

                #Definindo a cor que vai aparecer no botão de acordo com quem esta jogando
                B_3['fg'] = cor
                B_3['text'] = jogando
                LxC[1][2] = jogando

                # verificando quem jogou, para trocar o jogador
                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                #aumentando o n° do contador
                contador+=1
        if interacao == ('C1'):

            #verificando se aquela posição esta vazia
            if C_1['text'] == '':

                #Verifica quem esta jogando,para definir a cor
                if jogando == 'X':
                    cor=vermelho
                if jogando == 'O':
                    cor=azul_claro

                #Definindo a cor que vai aparecer no botão de acordo com quem esta jogando
                C_1['fg'] = cor
                C_1['text'] = jogando
                LxC[2][0] = jogando

                # verificando quem jogou, para trocar o jogador
                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                #aumentando o n° do contador
                contador+=1
        if interacao == ('C2'):

            #verificando se aquela posição esta vazia
            if C_2['text'] == '':

                #Verifica quem esta jogando,para definir a cor
                if jogando == 'X':
                    cor=vermelho
                if jogando == 'O':
                    cor=azul_claro

                #Definindo a cor que vai aparecer no botão de acordo com quem esta jogando
                C_2['fg'] = cor
                C_2['text'] = jogando
                LxC[2][1] = jogando

                # verificando quem jogou, para trocar o jogador
                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                #aumentando o n° do contador
                contador+=1
        if interacao == ('C3'):

            #verificando se aquela posição esta vazia
            if C_3['text'] == '':

                #Verifica quem esta jogando,para definir a cor
                if jogando == 'X':
                    cor=vermelho
                if jogando == 'O':
                    cor=azul_claro

                #Definindo a cor que vai aparecer no botão de acordo com quem esta jogando
                C_3['fg'] = cor
                C_3['text'] = jogando
                LxC[2][2] = jogando

                # verificando quem jogou, para trocar o jogador
                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                #aumentando o n° do contador
                contador+=1
                
        #Apos o contador ser >= 5,encerra o jogo e verifica o vencedor
        if contador >= 5:
            #linhas
            if LxC[0][0] == LxC[0][1] == LxC[0][2] != '':
                vencedor(jogando)
            elif LxC[1][0] == LxC[1][1] == LxC[1][2] != '':
                vencedor(jogando)
            elif LxC[2][0] == LxC[2][1] == LxC[2][2] != '':
                vencedor(jogando)
            #colunas
            if LxC[0][0] == LxC[1][0] == LxC[2][0] != '':
                vencedor(jogando)
            elif LxC[0][1] == LxC[1][1] == LxC[2][1] != '':
                vencedor(jogando)
            elif LxC[0][2] == LxC[1][2] == LxC[2][2] != '':
                vencedor(jogando)
            #diagonais
            if LxC[0][0] == LxC[1][1] == LxC[2][2] != '':
                vencedor(jogando)
            elif LxC[0][2] == LxC[1][1] == LxC[2][0] != '':
                vencedor(jogando)
            #Empate
            if contador >= 9:
                vencedor('Deu Empate')


    def vencedor(vencedor):
        global jogando
        global ponto_X
        global ponto_O
        global LxC
        global contador_de_rodadas
        global contador

        #Desabilitando os botoes
        A_1['state'] = 'disable'
        A_2['state'] = 'disable'
        A_3['state'] = 'disable'
        B_1['state'] = 'disable'
        B_2['state'] = 'disable'
        B_3['state'] = 'disable'
        C_1['state'] = 'disable'
        C_2['state'] = 'disable'
        C_3['state'] = 'disable'

        jogador_vencedor = Label(tela_baixo,text='',width=17,relief='flat',anchor='center',font='Ivy 13 bold',bg=fundo,fg=laranja)
        jogador_vencedor.place(x=40,y=227)

        if vencedor == 'X':
            ponto_O +=1
            jogador_vencedor['text'] = 'Jogador O Venceu'
            jogador_O_pontos['text'] = ponto_O
        if vencedor == 'O':
            ponto_X +=1
            jogador_vencedor['text'] = 'Jogador X Venceu'
            jogador_X_pontos['text'] = ponto_X
        if vencedor == 'Deu Empate':
            jogador_vencedor['text'] = 'Empatou'

       #Zera as informações
        def recomeçar():
            global contador
            # Apagar os textos dos botoes
            A_1['text'] = ''
            A_2['text'] = ''
            A_3['text'] = ''
            B_1['text'] = ''
            B_2['text'] = ''
            B_3['text'] = ''
            C_1['text'] = ''
            C_2['text'] = ''
            C_3['text'] = ''

            #Voltando o estado dos botões ao normal
            A_1['state'] = 'normal'
            A_2['state'] = 'normal'
            A_3['state'] = 'normal'
            B_1['state'] = 'normal'
            B_2['state'] = 'normal'
            B_3['state'] = 'normal'
            C_1['state'] = 'normal'
            C_2['state'] = 'normal'
            C_3['state'] = 'normal'

            #reiniciando a tabela
            LxC = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3'], ['C1', 'C2,', 'C3']]

            jogador_vencedor['text'] = ''
            botao_play.destroy()

        #Botao para jogar proxima rodada
        botao_play = Button(tela_baixo, command=recomeçar, text='Proxima Rodada', height=1, font='Ivy 12 bold',overrelief=RIDGE, bg=fundo, fg=branco_acizentado)
        botao_play.place(x=54, y=195)

        def fim_de_jogo():
            botao_play.destroy()
            jogador_vencedor.destroy()

            fim_da_rodada()
        if contador_de_rodadas >=5:
            fim_de_jogo()
        else:
            contador_de_rodadas +=1
            LxC = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3'], ['C1', 'C2,', 'C3']]
            contador = 0

    def fim_da_rodada():
        global LxC
        global contador
        global contador_de_rodadas
        global ponto_X
        global ponto_O

        if ponto_X > ponto_O:
            vitoria = Label(tela_baixo,text='Jogador X Venceu',width=17,relief='flat',bg=fundo,font='Ivy 13 bold',fg=amarelo,anchor='center')
            vitoria.place(x=45,y=10)
        elif ponto_O > ponto_O:
            vitoria = Label(tela_baixo, text='Jogador O Venceu', width=17, relief='flat', bg=fundo, font='Ivy 13 bold',fg=amarelo,anchor='center')
            vitoria.place(x=45, y=10)
        else:
            vitoria = Label(tela_baixo, text='Empatou', width=17, relief='flat', bg=fundo, font='Ivy 13 bold',fg=amarelo,anchor='center')
            vitoria.place(x=45, y=10)

        #Zerando as informações
        LxC = [['A1','A2','A3'],['B1','B2','B3'],['C1','C2,','C3']]
        ponto_O = 0
        ponto_X = 0
        contador_de_rodadas = 0
        contador = 0

        #Bloquear os botoes
        A_1['state'] = 'disable'
        A_2['state'] = 'disable'
        A_3['state'] = 'disable'
        B_1['state'] = 'disable'
        B_2['state'] = 'disable'
        B_3['state'] = 'disable'
        C_1['state'] = 'disable'
        C_2['state'] = 'disable'
        C_3['state'] = 'disable'

        fim = Label(tela_baixo,text='O Jogo Acabou',width=17,relief='flat',anchor='center',font='Ivy 13 bold',bg=fundo)
        fim.place(x=45,y=90)

        #Jogar denovo
        def jogadr_denovo():
            jogador_X_pontos['text'] = '0'
            jogador_O_pontos['text'] = '0'
            fim.destroy()
            botao_play.destroy()
            vitoria.destroy()
            jogadr_denovo.destroy()
            iniciar_jogo()

        #Botao jogar denovo
        jogadr_denovo = Button(tela_baixo,command=jogadr_denovo,text='Jogar Denovo',height=1,font='Ivy 12 bold',bg=fundo)
        jogadr_denovo.place (x=68,y=195)

    #Configurando TELA_BAIXO

    #Linhas Verticais
    linha_vertical_1 =Label(tela_baixo,text='', height=23, relief='flat', pady=5, font='Ivy 5 bold', bg=branco, fg=vermelho)
    linha_vertical_1.place(x=90, y=15)
    linha_vertical_2 =Label(tela_baixo,text='', height=23, relief='flat', pady=5, font='Ivy 5 bold', bg=branco, fg=vermelho)
    linha_vertical_2.place(x=160, y=15)
    #Linhas Horizontais
    linha_horizontal_1 = Label(tela_baixo,text='',width=190,padx=2,relief='flat',font='Ivy 1 bold',bg=branco,fg=vermelho)
    linha_horizontal_1.place(x=30,y=63)
    linha_horizontal_2 = Label(tela_baixo,text='',width=190,padx=2,font='Ivy 1 bold',bg=branco)
    linha_horizontal_2.place(x=30,y=123)

    #Linha X Coluna
    '''           1 | 2 | 3
                A   |   |
                ----|---|----
                B   |   |
                ----|---|----
                C   |   |
                ----|---|----
    '''

    A_1 = Button(tela_baixo,command=lambda:controlar_movimento('A1'),text='',width=3,padx=4,font='Ivy 18 bold',relief='flat',overrelief=RIDGE,bg=fundo,fg=vermelho)
    A_1.place(x=30,y=15)
    A_2 = Button(tela_baixo,command=lambda:controlar_movimento('A2'),text='',width=3,padx=4,font='Ivy 18 bold',relief='flat',overrelief=RIDGE,bg=fundo,fg=vermelho)
    A_2.place(x=98,y=14)
    A_3 = Button(tela_baixo,command=lambda:controlar_movimento('A3'),text='',width=3,padx=4,font='Ivy 18 bold',relief='flat',overrelief=RIDGE,bg=fundo,fg=vermelho)
    A_3.place(x=167,y=14)

    B_1 = Button(tela_baixo,command=lambda:controlar_movimento('B1'),text='',width=3,padx=4,font='Ivy 18 bold',relief='flat',overrelief=RIDGE,bg=fundo,fg=vermelho)
    B_1.place(x=31,y=72)
    B_2 = Button(tela_baixo,command=lambda:controlar_movimento('B2'),text='',width=3,padx=4,font='Ivy 18 bold',relief='flat',overrelief=RIDGE,bg=fundo,fg=vermelho)
    B_2.place(x=98,y=72)
    B_3 = Button(tela_baixo,command=lambda:controlar_movimento('B3'),text='',width=3,padx=4,font='Ivy 18 bold',relief='flat',overrelief=RIDGE,bg=fundo,fg=vermelho)
    B_3.place(x=167,y=72)

    C_1 = Button(tela_baixo,command=lambda:controlar_movimento('C1'),text='',width=3,padx=4,pady=4,font='Ivy 18 bold',relief='flat',overrelief=RIDGE,bg=fundo,fg=vermelho)
    C_1.place(x=30,y=133)
    C_2 = Button(tela_baixo,command=lambda:controlar_movimento('C2'),text='',width=3,padx=4,pady=4,font='Ivy 18 bold',relief='flat',overrelief=RIDGE,bg=fundo,fg=vermelho)
    C_2.place(x=98,y=133)
    C_3 = Button(tela_baixo,command=lambda:controlar_movimento('C3'),text='',width=3,padx=4,pady=4,font='Ivy 18 bold',relief='flat',overrelief=RIDGE,bg=fundo,fg=vermelho)
    C_3.place(x=167,y=133)

#Botão Jogar
botao_play = Button(tela_baixo,command=iniciar_jogo,text='PLAY',width=10,height=1,font='Ivy 12 bold',overrelief=RIDGE,bg=fundo,fg=branco_acizentado)
botao_play.place(x=70,y=195)


janela.mainloop()