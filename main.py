import sys
import subprocess
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, QGridLayout, QWidget, QMessageBox
from PyQt5.QtCore import QSize

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setup_main_window()
        self.initUI()

    def setup_main_window(self):
        self.x = 640
        self.y = 480
        self.setMinimumSize(QSize(self.x, self.y))
        self.setWindowTitle("Processamento Digital de Imagem")
        self.wid = QWidget(self)
        self.setCentralWidget(self.wid)
        self.layout = QGridLayout()
        self.wid.setLayout(self.layout)

    def initUI(self):
        #Criando a barr de menu
        self.barrademenu = self.menuBar()

        #Criar os menus
        self.menuarquivo = self.barrademenu.addMenu("&Arquivo")
        self.menutranformacao = self.barrademenu.addMenu("&Transformações")
        self.menuSobre = self.barrademenu.addMenu("&Sobre")


        #Criar as actions

        #Menu Arquivo
        self.opcaoabrir = self.menuarquivo.addAction("&Abrir Imagem")
        self.opcaoabrir.triggered.connect(self.open_file)
        #Quando voce usa o open file no action n o lugar de clicked voce coloca triggered
        self.opcaoabrir.setShortcut("Ctrl+A")

        self.menuarquivo.addSeparator()

        self.opcaosalvar = self.menuarquivo.addAction("&Salvar Arquivo")
        self.opcaosalvar.triggered.connect(self.open_file)
        self.opcaosalvar.setShortcut("Ctrl+S")

        self.menuarquivo.addSeparator()        

        self.opcaofechar = self.menuarquivo.addAction("&Encerrar Aplicativo")
        self.opcaofechar.setShortcut("Ctrl+X")
        self.opcaofechar.triggered.connect(self.close)

        #Menu Transformaçao
        self.opcaoSharpen = self.menutranformacao.addAction("Transformaçao &Mediana")
        self.opcaoSharpen.setShortcut("Ctrl+M")
        self.opcaoSharpen.triggered.connect(self.transform_me1)
        
        self.menuarquivo.addSeparator()

        self.opcaoEdge = self.menutranformacao.addAction("Filtro &Sharpen")
        self.opcaoEdge.setShortcut("Ctrl+F")
        self.opcaoEdge.triggered.connect(self.transform_me2)

        self.menuarquivo.addSeparator()

        self.opcaoEdge = self.menutranformacao.addAction("Detecção de &Camada Blue")
        self.opcaoEdge.setShortcut("Ctrl+D")
        self.opcaoEdge.triggered.connect(self.transform_me3)

        self.menuarquivo.addSeparator()

        self.opcaoCinza = self.menutranformacao.addAction("Conversão &Escala Cinza")
        self.opcaoCinza.setShortcut("Ctrl+Z")
        self.opcaoCinza.triggered.connect(self.transform_me4)        

        self.menuarquivo.addSeparator()

        self.opcaoPretoBranco = self.menutranformacao.addAction("Conversão &Preto e Branco")
        self.opcaoPretoBranco.setShortcut("Ctrl+E")
        self.opcaoPretoBranco.triggered.connect(self.transform_me5)         

        self.menuarquivo.addSeparator()

        self.opcaoNegativo = self.menutranformacao.addAction("Transformação &Negativa")
        self.opcaoNegativo.setShortcut("Ctrl+N")
        self.opcaoNegativo.triggered.connect(self.transform_me6)          

        self.menuarquivo.addSeparator()

        self.opcaoGreen = self.menutranformacao.addAction("Detecção de &Camada Green")
        self.opcaoGreen.setShortcut("Ctrl+H")
        self.opcaoGreen.triggered.connect(self.transform_me7) 

        self.menuarquivo.addSeparator()

        self.opcaoRed = self.menutranformacao.addAction("Detecção de &Camada Red")
        self.opcaoRed.setShortcut("Ctrl+J")
        self.opcaoRed.triggered.connect(self.transform_me8) 

        self.menuarquivo.addSeparator()

        self.opcaoGamma = self.menutranformacao.addAction("Filtro &Gamma")
        self.opcaoGamma.setShortcut("Ctrl+R")
        self.opcaoGamma.triggered.connect(self.transform_me9) 

        self.menuarquivo.addSeparator()

        self.opcaoLog = self.menutranformacao.addAction("Transformação &Logarítmica")
        self.opcaoLog.setShortcut("Ctrl+U")
        self.opcaoLog.triggered.connect(self.transform_me10)                 


        #Menu Sobre
        self.opcaosobre = self.menuSobre.addAction("Sobre o Aplicativo")
        self.opcaosobre.triggered.connect(self.exibe_mensagem)

        self.opcaoInformacao = self.menuSobre.addAction("Sobre a Imagem")
        self.opcaoInformacao.triggered.connect(self.exibe_mensagem2)       

        #Criar barra de status
        self.barradestatus = self.statusBar()
        self.barradestatus.showMessage("Olá!!! Seja bem vindo!!!", 3000)

        #Criando Label
        self.texto = QLabel("Aplicação de filtros e transformações", self)
        self.texto.adjustSize()
        self.largura = self.texto.frameGeometry().width()
        self.altura = self.texto.frameGeometry().height()
        self.texto.setAlignment(QtCore.Qt.AlignCenter)
        
        #Criando as imagens
        self.imagem1 = QLabel(self)
        self.endereco1 = 'aguia.ppm'
        self.pixmap1 = QtGui.QPixmap(self.endereco1)
        self.pixmap1 = self.pixmap1.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem1.setPixmap(self.pixmap1)
        self.texto.setAlignment(QtCore.Qt.AlignCenter)

        
        self.imagem2 = QLabel(self)
        self.endereco2 = 'aguia.ppm'
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.texto.setAlignment(QtCore.Qt.AlignCenter)

        self.imagem3 = QLabel(self)
        self.endereco3 = 'aguia.pgm'
        self.pixmap3 = QtGui.QPixmap(self.endereco3)
        self.pixmap3 = self.pixmap3.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem3.setPixmap(self.pixmap3)
        self.texto.setAlignment(QtCore.Qt.AlignCenter)        

        #organizando os widgets dentro do grid layout
        self.layout.addWidget(self.texto, 0, 0, 1, 2)#layout, linha, coluna/ n° de linhas, n° de colunas
        self.layout.addWidget(self.imagem1, 1, 0)
        self.layout.addWidget(self.imagem2, 1, 1)
        self.layout.setRowStretch(0, 0)#posiçao(linha), tamanho do espaço(0-minimo/1-um pouco maior)
        self.layout.setRowStretch(1, 1)
        self.layout.setRowStretch(2, 0)

    #metodo para a ações dos botões
    def exibe_mensagem(self):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle("Sobre")
        self.msg.setText("By William Rouvier Macedo")
        self.msg.setInformativeText("Ituiutaba-MG\n11/08/2020")
        self.msg.setDetailedText("Foram usados neste aplicativo o Filtro para Camada Azul, camada Verde, camada vermelha, Filtro Sharpen e a Transformação Mediana, Conversão em Escala de cinza, Conversão em Preto e Branco, Transformação Negativa")
        self.msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.msg.exec_()# exibir a caixa de mensagens, ou caixa de diálogo
        self.reply = self.msg.clickedButton()
        self.barradestatus.showMessage("Você selecionou: " + self.reply.text())

    def exibe_mensagem2(self):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle("Informações da Imagem")
        self.msg.setText("By William Rouvier Macedo")
        
        self.entrada = open(self.endereco1, "r+")
        self.saida = open("aguia.ppm", "w+")
        self.linha = self.entrada.readline() #P3
        self.linha2 = self.entrada.readline() #Comentário
        self.linha1 = self.entrada.readline() #Dimensões
        self.dimensoes = self.linha1.split()
        self.largura = self.dimensoes[0]
        self.altura = self.dimensoes[1]

        self.string = self.endereco1
        self.parts = self.string.rpartition('/')
        self.parts2 = self.string.rpartition('.')
        print(self.string)
        print(self.parts)
        self.msg.setText("Nome: " + self.parts[2] + "\n" + "Extensão do Arquivo: " + self.parts2[2] + "\n" + "Comentario : " + self.linha2 + "\n" + "Largura : " +  self.largura + "\n" + "Altura: " +  self.altura)

        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.exec_()# exibir a caixa de mensagens, ou caixa de diálogo
        self.reply = self.msg.clickedButton()
        self.barradestatus.showMessage("Você selecionou: " + self.reply.text())
    

    def transform_me1(self):
        self.entrada = self.endereco1
        self.saida = 'aguia_mediana.ppm'
        self.script = 'mediana.py'
        self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        
    def transform_me2(self):
        self.entrada = self.endereco1
        self.saida = 'aguia_sharpen.ppm'
        self.script = 'sharpen.py'
        self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

    def transform_me3(self):
        self.entrada = self.endereco1
        self.saida = 'aguia_azul.ppm'
        self.script = 'camada_azul.py'
        self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)              

    def transform_me4(self):
        self.entrada = self.endereco1
        self.saida = 'aguia_greyScale.pgm'
        self.script = 'ConverteEscalaCinza.py'
        self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)                      

    def transform_me5(self):
        self.entrada = self.endereco3
        self.saida = 'aguia_pretoBranco.pbm'
        self.script = 'ConvertePretoBranco.py'
        self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)
        self.endereco3 = self.saida
        self.pixmap3 = QtGui.QPixmap(self.endereco3)
        self.pixmap3 = self.pixmap3.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem3.setPixmap(self.pixmap3) 

    def transform_me6(self):
        self.entrada = self.endereco1
        self.saida = 'aguia_negativo.ppm'
        self.script = 'negativo.py'
        self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2) 

    def transform_me7(self):
        self.entrada = self.endereco1
        self.saida = 'aguia_green.ppm'
        self.script = 'camada_green.py'
        self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)         

    def transform_me8(self):
        self.entrada = self.endereco1
        self.saida = 'aguia_red.ppm'
        self.script = 'camada_red.py'
        self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2) 

    def transform_me9(self):
        self.entrada = self.endereco1
        self.saida = 'aguia_gamma.pgm'
        self.script = 'gamma.py'
        self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2) 

    def transform_me10(self):
        self.entrada = self.endereco1
        self.saida = 'aguia_log.pgm'
        self.script = 'logaritmica.py'
        self.program = 'python' + ' \"' + self.script + '\" ' + self.entrada + ' ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)              

    def open_file(self): 
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, caption = 'Open Image', directory=QtCore.QDir.currentPath(), filter='All files (*.*);;Images (*.ppm;*.pgm;*.pbm)', initialFilter='Images (*.ppm;*.pgm;*.pbm;)')
        if fileName != '':
            self.endereco1 = fileName
            self.pixmap1 = QtGui.QPixmap(self.endereco1)
            self.pixmap1 = self.pixmap1.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
            self.imagem1.setPixmap(self.pixmap1)
            
    def save_file(self): 
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, caption = 'Save File', directory=QtCore.QDir.currentPath(), filter='All files (*.*);;Images (*.ppm;*.pgm;*.pbm)', initialFilter='Images (*.ppm;*.pgm;*.pbm;)')
        if fileName != '':
            self.endereco1 = fileName
            self.pixmap1 = QtGui.QPixmap(self.endereco1)
            self.pixmap1 = self.pixmap1.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
            self.imagem1.setPixmap(self.pixmap1)             
        
        print(fileName)
    

    def button_clicked(self):
        self.texto.setText("Congratulations!!!")
        self.texto.adjustSize()
        self.novoEndereco = QtGui.QPixmap("aguia.ppm")
        self.imagem1.setPixmap(self.novoEndereco)
        self.imagem2.setPixmap(self.novoEndereco)

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

    print(sys.argv)

window()

