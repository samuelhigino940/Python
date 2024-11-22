#A biblioteca sys(sistema) nos ajuda a regenciar
#a janela no sistema operacional.Biblioteca
#nativa do python
import sys
#importar as bibliotecas do pyqt para criar a 
#janela e os elementos graficos, tais como:
#label,caixas de textos, botões e outros
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QVBoxLayout,QPushButton

#Para construir a nossa janela iremos
#montar um classe que tera todos os 
#itens da janela.Esta classe sera chamada para 
#executar a janela e exibi-la em tela.
class Janela(QWidget):
    #função__init__ faz o start da janela, ou seja,
    #faz a janela executar.Inicia a janela
    #o parâmetro self,faz a referência a própria janela
    def __init__(self):
        #O comando super faz referência ao Qwidget
        #que foi chamado na contrução da janela
        #e inicializa uma cópia para classe janela
        super().__init__()
        #Definindo a posição em x e y e também pede o tamanho
        #da janela.
        #O comando SetGeometry pede os seguintes valores:
        # x = posição horizontal de abertura janela
        # y = posição vertical de abertura de janela
        # w = largura da janela
        # h = altura da janela 

        self.setGeometry(50,100,600,500)
        #Vamos fazer a chamada do layout vertical para
        #adicionar os controles: Label,editline e button
        self.v_layout=QVBoxLayout()
        
        #Vamos criar uma label para o nome do cliente
        self.label_nome=QLabel("Nome do Cliente:")  
app=QApplication(sys.argv)
jan=Janela()
jan.show()
app.exec_()