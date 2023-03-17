#importando tkinter  para criação de app desktop
from tkinter import *      
from tkinter import ttk
#cores para usar
cor1 = '#333030'    #preto
cor2 = '#2463a6'     #azul
cor3 ='#3d404d'      # cinza
cor4 ='#bf6804'      # laranja
cor5='#fcfcfc'   #branco

janela =Tk()
janela.title('calculadora')
#aqui a largura e comprimento da janela respectivamente
janela.geometry('235x310')
janela.config(background=cor1)





#divisão da janela e display
frame_tela = Frame(janela, width = 235, height=50, background= cor2)
frame_tela.grid(row=0,column =0)

frame_corpo = Frame(janela, width = 235, height=268,)
frame_corpo.grid(row=1,column =0)

todos_valores=''
#criando função
def entrar_valores(event):
    global todos_valores
    todos_valores= todos_valores+ str(event)
   
    valor_text.set(todos_valores)
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_text.set(str(resultado))



    #funcao limpar tela
    
    
def limpar_tela():
        global todos_valores
        todos_valores=''
        valor_text.set('')


#label

valor_text = StringVar()
app_label = Label(frame_tela,textvariable=valor_text, width=16,height =2,padx=7,relief=FLAT,anchor ='e',justify=RIGHT,font=('Ivy 18 '),background=cor2)
app_label.place(x=0,y=0)



# criando botoes
b_1 = Button(frame_corpo,command=limpar_tela,text='C',width=11,height=2,bg=cor3,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b_1.place(x=0, y=0)

b_2 = Button(frame_corpo,text='%',width=5,height=2,bg=cor3,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE,command=lambda:entrar_valores('%'))
b_2.place(x=118, y=0)

b_3 = Button(frame_corpo,text='/            ',width=11,height=2, bg=cor4,fg=cor5,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE,command=lambda:entrar_valores('/'))
b_3.place(x=177, y=0)


b_4 = Button(frame_corpo,text='7',width=5,height=2,bg=cor3,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE,command=lambda:entrar_valores('7'))
b_4.place(x=0, y=52)
b_5 = Button(frame_corpo,text='8',width=5,height=2,bg=cor3,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE,command=lambda:entrar_valores('8'))
b_5.place(x=59, y=52)
b_6 = Button(frame_corpo,text='9',width=5,height=2,bg=cor3,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE,command=lambda:entrar_valores('9'))
b_6.place(x=118, y=52)
b_7 = Button(frame_corpo,text='*            ',width=11,height=2, bg=cor4,fg=cor5,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE,command=lambda:entrar_valores('*'))
b_7.place(x=177, y=52)

b_8 = Button(frame_corpo,text='4',width=5,height=2,bg=cor3,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE,command=lambda:entrar_valores('4'))
b_8.place(x=0, y=104)
b_9 = Button(frame_corpo,text='5',width=5,height=2,bg=cor3,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE,command=lambda:entrar_valores('5'))
b_9.place(x=59, y=104)
b_10 = Button(frame_corpo,text='6',width=5,height=2,bg=cor3,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE,command=lambda:entrar_valores('6'))
b_10.place(x=118, y=104)
b_11= Button(frame_corpo,text='-            ',width=11,height=2, bg=cor4,fg=cor5,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE,command=lambda:entrar_valores('-'))
b_11.place(x=177, y=104)

b_12 = Button(frame_corpo,text='1',width=5,height=2,bg=cor3,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE,command=lambda:entrar_valores('1'))
b_12.place(x=0, y=155)
b_13 = Button(frame_corpo,text='2',width=5,height=2,bg=cor3,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE,command=lambda:entrar_valores('2'))
b_13.place(x=59, y=155)
b_14 = Button(frame_corpo,text='3',width=5,height=2,bg=cor3,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE,command=lambda:entrar_valores('3'))
b_14.place(x=118, y=155)
b_15= Button(frame_corpo,text='+            ',width=11,height=2, bg=cor4,fg=cor5,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE,command=lambda:entrar_valores('+'))
b_15.place(x=177, y=155)

b_16 = Button(frame_corpo,text='0',width=11,height=2,bg=cor3,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE,command=lambda:entrar_valores('0'))
b_16.place(x=0, y=207)

b_17= Button(frame_corpo,text='.',width=5,height=2,bg=cor3,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE,command=lambda:entrar_valores('.'))
b_17.place(x=118, y=207)

b_18= Button(frame_corpo,text='=            ',width=11,height=2, bg=cor4,fg=cor5,font=('Ivy 13 bold'),relief=RAISED,overrelief=RIDGE,command=calcular)
b_18.place(x=177, y=207)

#execução da janela


janela.mainloop()