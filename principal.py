import tkinter as tk
import botao


class Tela():
    def __init__(self):
       self.Tela= tk.Tk() 
       self.Tela.title("Calculadora")
       self.Tela.resizable(width=False, height=False)
       
       
       self.Res = ""
       self.Valores = 0
       self.WIDTH = 10
       self.HEIGTH = 3
       self.FONTE = "Arial 14 bold"
       
       def atualizar(auxBt):
           self.Res+=auxBt
           print(self.Res)
           self.auxResultado.set(self.Res)
       
       def calcular(self):
           Digitos = []
           Oper = []
           Num = []
           for i in self.Res:
               if i.isdigit():
                   Digitos.append(i)
               else:
                   Oper.append(i)
                   Digitos.append("*")
           print(Oper)
           print(Digitos)
           NumStr ="".join(Digitos)
           NumStr = NumStr.split("*") 
        #    for j in NumStr:
        #        Num.append(j)
        #    print(NumStr)
        #    print(Num)

           #operações
           if Oper[0] == "+":
               ResTotal = int(NumStr[0]) + int(NumStr[1])

           if Oper[0] == "-":
               ResTotal = int(NumStr[0]) - int(NumStr[1])

           if Oper[0] == "x":
               ResTotal = int(NumStr[0]) * int(NumStr[1]) 

           if Oper[0] == "÷":
               ResTotal = round(int(NumStr[0]) / int(NumStr[1]), 2)

           self.auxResultado.set(str(ResTotal)) 
           self.Res=[]
       #Label resultado - DISPLAY CALCULADORA
       self.auxResultado = tk.StringVar()
       self.auxResultado.set("---")
       self.lbResultado = tk.Label(self.Tela, textvariable=self.auxResultado, font=self.FONTE)
       self.lbResultado.grid(row=0, columnspan=3)
       
       #botao 0
       self.auxBt0=tk.StringVar()
       self.auxBt0.set(0)
       self.bt0 = tk.Button(self.Tela, textvariable=self.auxBt0, width=self.WIDTH, height= self.HEIGTH, font=self.FONTE, command=lambda: atualizar(self.auxBt0.get()))
       self.bt0.grid(row=1, column=0, padx=2, pady=2)

       #botao 1
       self.auxBt1=tk.StringVar()
       self.auxBt1.set(1)
       self.bt1 = tk.Button(self.Tela, textvariable=self.auxBt1, width=self.WIDTH, height= self.HEIGTH, font=self.FONTE, command=lambda: atualizar(self.auxBt1.get()))
       self.bt1.grid(row=1, column=1, padx=2, pady=2)

       #botao 2
       self.auxBt2=tk.StringVar()
       self.auxBt2.set(2)
       self.bt2 = tk.Button(self.Tela, textvariable=self.auxBt2, width=self.WIDTH, height= self.HEIGTH, font=self.FONTE, command=lambda: atualizar(self.auxBt2.get()))
       self.bt2.grid(row=1, column=2, padx=2, pady=2)

       #botao 3
       self.auxBt3=tk.StringVar()
       self.auxBt3.set(3)
       self.bt3 = tk.Button(self.Tela, textvariable=self.auxBt3, width=self.WIDTH, height= self.HEIGTH, font=self.FONTE, command=lambda: atualizar(self.auxBt3.get()))
       self.bt3.grid(row=2, column=0, padx=2, pady=2)

       #botao 4
       self.auxBt4=tk.StringVar()
       self.auxBt4.set(4)
       self.bt4 = tk.Button(self.Tela, textvariable=self.auxBt4, width=self.WIDTH, height= self.HEIGTH, font=self.FONTE, command=lambda: atualizar(self.auxBt4.get()))
       self.bt4.grid(row=2, column=1, padx=2, pady=2)

       #botao 5
       self.auxBt5=tk.StringVar()
       self.auxBt5.set(5)
       self.bt5 = tk.Button(self.Tela, textvariable=self.auxBt5, width=self.WIDTH, height= self.HEIGTH, font=self.FONTE, command=lambda: atualizar(self.auxBt5.get()))
       self.bt5.grid(row=2, column=2, padx=2, pady=2)

       #botao 6
       self.auxBt6=tk.StringVar()
       self.auxBt6.set(6)
       self.bt6 = tk.Button(self.Tela, textvariable=self.auxBt6, width=self.WIDTH, height= self.HEIGTH, font=self.FONTE, command=lambda: atualizar(self.auxBt6.get()))
       self.bt6.grid(row=3, column=0, padx=2, pady=2)
       
       #botao 7
       self.auxBt7=tk.StringVar()
       self.auxBt7.set(7)
       self.bt7 = tk.Button(self.Tela, textvariable=self.auxBt7, width=self.WIDTH, height= self.HEIGTH, font=self.FONTE, command=lambda: atualizar(self.auxBt7.get()))
       self.bt7.grid(row=3, column=1, padx=2, pady=2)

       #botao 8
       self.auxBt8=tk.StringVar()
       self.auxBt8.set(8)
       self.bt8 = tk.Button(self.Tela, textvariable=self.auxBt8, width=self.WIDTH, height= self.HEIGTH, font=self.FONTE, command=lambda: atualizar(self.auxBt8.get()))
       self.bt8.grid(row=3, column=2, padx=2, pady=2)

       #botao 9
       self.auxBt9=tk.StringVar()
       self.auxBt9.set(9)
       self.bt9 = tk.Button(self.Tela, textvariable=self.auxBt9, width=self.WIDTH, height= self.HEIGTH, font=self.FONTE, command=lambda: atualizar(self.auxBt9.get()))
       self.bt9.grid(row=4, column=0, padx=2, pady=2)

       #botao -
       self.auxBt10=tk.StringVar()
       self.auxBt10.set("-")
       self.bt10 = tk.Button(self.Tela, textvariable=self.auxBt10, width=self.WIDTH, height= self.HEIGTH, bg="Blue", font=self.FONTE, command=lambda: atualizar(self.auxBt10.get()))
       self.bt10.grid(row=4, column=1, padx=2, pady=2)
       
       #botao +
       self.auxBt11=tk.StringVar()
       self.auxBt11.set("+")
       self.bt11 = tk.Button(self.Tela, textvariable=self.auxBt11, width=self.WIDTH, height= self.HEIGTH, bg="Blue", font=self.FONTE, command=lambda: atualizar(self.auxBt11.get()))
       self.bt11.grid(row=4, column=2, padx=2, pady=2)
     

       #botao *
       self.auxBt12=tk.StringVar()
       self.auxBt12.set("x")
       self.bt12 = tk.Button(self.Tela, textvariable=self.auxBt12, width=self.WIDTH, height= self.HEIGTH, bg="Blue", font=self.FONTE, command=lambda: atualizar(self.auxBt12.get()))
       self.bt12.grid(row=5, column=0, padx=2, pady=2)

       #botao /
       self.auxBt13=tk.StringVar()
       self.auxBt13.set("÷")
       self.bt13 = tk.Button(self.Tela, textvariable=self.auxBt13, width=self.WIDTH, height= self.HEIGTH, bg="Blue", font=self.FONTE, command=lambda: atualizar(self.auxBt13.get()))
       self.bt13.grid(row=5, column=1, padx=2, pady=2)

       #botao =
       self.auxBt14=tk.StringVar()
       self.auxBt14.set("=")
       self.bt14 = tk.Button(self.Tela, textvariable=self.auxBt14, width=self.WIDTH, height= self.HEIGTH, bg="Blue", font=self.FONTE, command=lambda: calcular(self))
       self.bt14.grid(row=5, column=2, padx=2, pady=2)

       self.Tela.mainloop()
Tela()