#Importando tkinter
from tkinter import*

#Importando pillow
from PIL import Image,ImageTk

#Importando Teste de Conexao
import speedtest

#Importando Font
from tkextrafont import Font

def Teste_de_Conexao():
    speed = speedtest.Speedtest()
    donwload = speed.download()/1024/1024
    upload = speed.upload()/1024/1024
    l_download['text'] = f'{donwload:.2f}'
    l_upload['text'] = f'{upload:.2f}'


preto = '#242424'
branco = '#feffff'
verde = '#359c8c'
vermelho = '#c45149'
azul = '#4a88e8'

#Configuração janela
janela = Tk()
'''Font(File='Snow.otf')'''
font_caminho = 'Snow.otf'
Snow = Font(family=font_caminho,size=20)
janela.title('Speed Test')
janela.geometry('350x200')
janela.resizable(width= False , height= False)
janela.configure(background=branco)


#Tela de Cima

tela_logo = Frame(janela, width=350,height=60,background=branco)
tela_logo.grid(row = 0, column = 0 ,padx = 0 , pady = 1, sticky = NSEW)


#Tela de Baixa

tela_corpo = Frame(janela, width=350,height=140,background=branco)
tela_corpo.grid(row= 1 , column = 0 , padx = 0 ,pady =1 , sticky = NSEW)

#Configurando Tela Cima

#Importando imagem

imagem = Image.open('icon_speed.png')
imagem = imagem.resize((55,55))
imagem = ImageTk.PhotoImage(imagem)

#Imagem

l_logo_image = Label(tela_logo,height=60, image=imagem, compound='left', padx= 10, anchor='nw', font='ivy 16 bold',background= branco,fg= preto)
l_logo_image.place(x = 20 , y = 0)
#Titulo

l_logo_nome = Label(tela_logo, text='Internet Speed Test',font=Snow,padx=10,anchor=NE,bg=branco)
l_logo_nome.place(x= 75, y = 10)
#Linha divisoria da tela de cima/baixo

l_logo_linha = Label(tela_logo,width=350,text='',anchor=NW,font=('Ivy 1'),bg=verde)
l_logo_linha.place(x=0,y=57)

#Configurando Tela Baixo, Lado Esquerdo

l_download = Label(tela_corpo,text='',anchor=NW,font=('arial 28'),bg=branco)
l_download.place(x=30,y=28)
l_download_mb = Label(tela_corpo,text='Mbps Download',anchor=NW,font=('Snow 10'),bg=branco)
l_download_mb.place(x=30,y=70)

#Importando e Configurando Imagem Download

imagem_down=Image.open(('icon_down.png'))
imagem_down= imagem_down.resize((50,50))
imagem_down=ImageTk.PhotoImage(imagem_down)
l_down_image = Label(tela_corpo,height=60,image=imagem_down,compound=LEFT,padx=10,anchor='nw',bg=branco)
l_down_image.place(x=130,y=35)

#Configurando Tela Baixo,Lado direito

l_upload = Label(tela_corpo,text='',anchor=NW,font=('arial 28'),bg=branco)
l_upload.place(x=240,y=28)
l_upload_mb = Label(tela_corpo,text='Mbps Upload',anchor=NE,font=('Ivy 10'),bg=branco)
l_upload_mb.place(x=240,y=70)

#Importando e Configurando Imagem Upload

imagem_up = Image.open('icon_up.png')
imagem_up = imagem_up.resize((50,50))
imagem_up = ImageTk.PhotoImage(imagem_up)
l_up_image = Label(tela_corpo,height=60,image=imagem_up,compound=LEFT,padx=10,anchor='ne',bg=branco)
l_up_image.place(x=180,y=35)

#Botao

l_botao = Button(tela_corpo,command=Teste_de_Conexao,text='TESTAR CONEXÃO',font=('Ivy 10 italic'),width=15,overrelief=RIDGE,bg=azul,fg=branco)
l_botao.place(x=118,y=100)



janela.mainloop()