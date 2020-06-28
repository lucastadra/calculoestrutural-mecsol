# coding=utf-8
import tkinter as tk
import matplotlib.pyplot as plt

#Variáveis para utilização no matplot
ray = 0.0
rby = 0.0
ms2 = 0.0
ms3 = 0.0
l = 0.0
qs2 = 0.0
qs3 = 0.0
class Application:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")
        self.container1 = tk.Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = tk.Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = tk.Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = tk.Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = tk.Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = tk.Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = tk.Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = tk.Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()

        self.titulo = tk.Label(self.container1, text="Lucas Tadra Mainginski || RA: [*****926] \n Viga: nº2")
        self.titulo["font"] = ("Calibri", "8", "bold")
        self.titulo.pack()

        self.titulo = tk.Label(self.container1, text="Informe os dados:")
        self.titulo["font"] = ("Calibri", "15", "bold")
        self.titulo.pack()

        self.labelp1 = tk.Label(self.container2, text="Carga P1 (kN): ", font=self.fonte, width=15)
        self.labelp1.pack(side=tk.LEFT)

        self.txtp1 = tk.Entry(self.container2)
        self.txtp1["width"] = 15
        self.txtp1["font"] = self.fonte
        self.txtp1.pack(side=tk.LEFT)

        self.labelp2 = tk.Label(self.container3, text="Carga P2 (kN): ", font=self.fonte, width=15)
        self.labelp2.pack(side=tk.LEFT)

        self.txtp2 = tk.Entry(self.container3)
        self.txtp2["width"] = 15
        self.txtp2["font"] = self.fonte
        self.txtp2.pack(side=tk.LEFT)

        self.labellength = tk.Label(self.container4, text="Comprim. (m):", font=self.fonte, width=15)
        self.labellength.pack(side=tk.LEFT)

        self.txtlength = tk.Entry(self.container4)
        self.txtlength["width"] = 15
        self.txtlength["font"] = self.fonte
        self.txtlength.pack(side=tk.LEFT)

        self.labelX1 = tk.Label(self.container5, text="Ponto X MS1:", font=self.fonte, width=15)
        self.labelX1.pack(side=tk.LEFT)

        self.txtX1 = tk.Entry(self.container5)
        self.txtX1["width"] = 15
        self.txtX1["font"] = self.fonte
        self.txtX1.pack(side=tk.LEFT)

        self.labelX2 = tk.Label(self.container6, text="Ponto X MS2:", font=self.fonte, width=15)
        self.labelX2.pack(side=tk.LEFT)

        self.txtX2 = tk.Entry(self.container6)
        self.txtX2["width"] = 15
        self.txtX2["font"] = self.fonte
        self.txtX2.pack(side=tk.LEFT)

        self.labelX3 = tk.Label(self.container7, text="Ponto X MS3:", font=self.fonte, width=15)
        self.labelX3.pack(side=tk.LEFT)

        self.txtX3 = tk.Entry(self.container7)
        self.txtX3["width"] = 15
        self.txtX3["font"] = self.fonte
        self.txtX3.pack(side=tk.LEFT)

        self.bntInsert = tk.Button(self.container8, text="Inserir", font=self.fonte, width=15)
        self.bntInsert["command"] = self.calculaForcas
        self.bntInsert.pack(side=tk.TOP)

        self.bntPlot = tk.Button(self.container8, text="Diagramas", font=self.fonte, width=15)
        self.bntPlot["command"] = self.plota
        self.bntPlot.pack(side=tk.TOP)

        self.mensagem = tk.Label(self.container8, text="", font=self.fonte)
        self.mensagem.pack(side=tk.RIGHT)
	
	#Obtenção dos valores e aplicação nas equações encontradas para a viga
    def calculaForcas(self):
        global ray
        global rby
        global ms2
        global ms3
        global qs2
        global qs3
        p1 = float(self.txtp1.get())
        p2 = float(self.txtp2.get())
        l = float(self.txtlength.get())
        x1 = float(self.txtX1.get()) #Ponto X MS1
        x2 = float(self.txtX2.get()) #Ponto X MS2
        x3 = float(self.txtX3.get()) #Ponto X MS3

        if x1 > (l / 3) or x1 < 0:
            self.mensagem["text"] = ('Erro: O valor de X (MS1) precisa estar entre 0 e {:.2f}!'.format(l / 3))
            return
        if x2 > (2*l / 3) or x2 < (l/3):
            self.mensagem["text"] = ('Erro: O valor de X (MS2) precisa estar entre'
                                     ' {:.2f} e {:.2f}!'.format(l / 3, (2*l/3)))
            return
        if (x3 > l / 3) or x3 < 0:
            self.mensagem["text"] = ('Erro: O valor de X (MS3) precisa estar entre 0 e {:.2f}!'.format(l / 3))
            return
			
        aux = (p1 * (l / 3))
        aux2 = (p2 * ((2 * l) / 3))
        rby = (aux + aux2) / l
        qs3 = -rby
        ms3 = rby * x3
        ray = p1 + p2 - rby
        qs1 = ray
        ms1 = ray * x1
        qs2 = ray - p1
        ms2 = ray * x2 - (p1 * x2) + ((p1 * l) / 3)
        self.mensagem["text"] = ('\nValor de RaY: {:.2f}kN'
                                 '\nValor de RbY: {:.2f}kN'
                                 '\n\nValor de Qs para seção 1: {:.2f}kN'
                                 '\nValor de Ms para seção 1: {:.2f}kN'
                                 '\n\nValor de Qs para seção 2: {:.2f}kN'
                                 '\nValor de Ms para seção 2: {:.2f}kN'
                                 '\n\nValor de Qs para seção 3: {:.2f}kN'
                                 '\nValor de Ms para seção 3: {:.2f}kN'.format(ray, rby, qs1, ms1, qs2, ms2, qs3, ms3))
	#Plotagem de diagramas
    def plota(self): 	
        figure, (x1, x2) = plt.subplots(2)
        figure.canvas.set_window_title('Diagramas')
        figure.tight_layout()
        l = float(self.txtlength.get())
        x = [0, 0, (l / 3), (l / 3), ((2 * l) / 3), ((2 * l) / 3), l]
        y = [0, qs1, qs1, qs2, qs2, qs3, qs3]

        z = [0, (l / 3), ((2 * l) / 3), l]
        w = [ms1, -ms2, -ms3, -ms3]

        x1.set_title('Diagrama Qs')
        x2.set_title('Diagrama Ms')

        x1.grid()
        x2.grid()

        x1.plot(x[2], y[2], marker='v', label='Carga P1')
        x1.plot(x[5], y[4], marker='v', label='Carga P2')
        x2.plot(z[1], w[1], marker='v', label='Carga P1')
        x2.plot(z[2], w[2], marker='v', label='Carga P2')

        x1.plot(x, y)
        x2.plot(z, w)

        x1.legend()
        x2.legend()
        plt.show()


root = tk.Tk()
root.title('Trabalho Computacional')
Application(root)
root.mainloop()

