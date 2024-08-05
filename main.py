import tkinter as tk
from tkinter import ttk
import requests
import json

def getCurrency():#keysOrValues:int):
    req = requests.get('https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json')
    moedas = json.loads(req.text)
    temp = {}
    for c, v in moedas.items():
        if v == '':
            v = "Criptomoeda"
        temp[c.upper()] = f"({v})"
    retorno = []
    for i in temp:
        retorno.append(f'{i} {temp[i]}')
    
    return retorno

class App:
    def __init__(self, master=None):
        self.moeda1completa = self.moeda2completa = self.primeiraMoeda = self.segundaMoeda = ''
        self.m1 = self.m2 = 1
        self.moedas = getCurrency()
        self.arial = ("Arial", "12")

        self.container1 = tk.Frame(master)
        self.container1['pady'] = 10
        self.container1.pack()

        self.text1 = tk.Label(self.container1, text="Moeda a converter - Quantidade\n", font=self.arial)
        self.text1['width'] = 30
        self.text1.pack()


        self.selecao1 = ttk.Combobox(self.container1, values=self.moedas, background='white')
        self.selecao1['width'] = 22
        self.selecao1.pack(side=tk.LEFT)

        self.qnt1 = tk.Entry(self.container1,background='white',fg='black')
        self.qnt1['width'] = int(self.text1['width'] - self.selecao1['width'])
        self.qnt1.pack(side=tk.RIGHT)
        
        # ---------------
        
        self.container2 = tk.Frame(master)
        self.container2['pady'] = 10
        self.container2.pack()

        self.text2 = tk.Label(self.container2, text="Para\n", font=self.arial)
        self.text2['width'] = 30
        self.text2.pack()

        self.selecao2 = ttk.Combobox(self.container2, values=self.moedas, background='white')
        self.selecao2['width'] = 22
        self.selecao2.pack()

        # self.qnt2 = tk.Entry(self.container2,background='white',fg='black')
        # self.qnt2['width'] = int(self.text1['width'] - self.selecao1['width'])
        # self.qnt2.pack(side=tk.RIGHT)
         
        # ---------------
        
        self.container3 = tk.Frame(master)
        self.container3['pady'] = 10
        self.container3.pack()

        self.converter = tk.Button(self.container3, font=self.arial, text="Converter")
        self.converter.bind("<Button-1>", self.changeCurrency)
        self.converter.pack(side=tk.LEFT, padx=10)

        # --------------- 
        self.container4 = tk.Frame(master)
        self.container4['pady'] = 10
        self.container4.pack()

        self.conversao = tk.Label(master,font=self.arial)
        self.conversao.pack()

        # ---------------
        
        self.inverter = tk.Button(self.container3, font=self.arial, text="Inverter ")
        self.inverter.bind("<Button-1>", self.inverterMoedas)
        self.inverter.pack(side=tk.RIGHT, padx=10)

    def getCurrency(self):
        self.moeda1completa = self.selecao1.get()
        self.primeiraMoeda = self.moeda1completa[0:self.moeda1completa.find(' ')].lower()
        self.moeda2completa = self.selecao2.get()
        self.segundaMoeda = self.moeda2completa[0:self.moeda2completa.find(' ')].lower()

    def changeCurrency(self,event):
        try:
            self.getCurrency()
            # ---------
            if self.qnt1.get() == '':
                self.m1 = 1
            else:
                self.m1 = float(self.qnt1.get())

            # ---------
            req = requests.get(f'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{self.primeiraMoeda}.json').text
            moedas = json.loads(req)
            print(moedas)
            coeficiente = moedas[self.primeiraMoeda][self.segundaMoeda]
            v = self.m1 * float(coeficiente) * self.m2
            self.conversao['text'] = f"{v:.2f} {self.segundaMoeda.upper()}"
        except:
            self.conversao['text'] = 'ERRO'
        

    def inverterMoedas(self,event):
        try:
            self.getCurrency()
            aux = self.segundaMoeda
            self.segundaMoeda = self.primeiraMoeda
            self.primeiraMoeda = aux

            aux = self.moeda2completa
            self.moeda2completa = self.moeda1completa
            self.moeda1completa = aux

            self.selecao1.set(self.moeda1completa)
            self.selecao2.set(self.moeda2completa)
        except:
            self.conversao['text'] = 'ERRO'


root = tk.Tk()
App(root)
root.mainloop()
