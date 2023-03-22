import random as rnd
import tkinter
import tkinter.messagebox
import customtkinter
import numpy as np
import matplotlib.pyplot as plt
import sympy 
customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("green")  

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()     

        self.x = 0
        self.Contador = 0   
############################__Front__####################################
        
        self.geometry(f"{1280}x{720}")
        self.title("Polpy")
        

        #columnas y filas
        self.grid_rowconfigure(1, weight=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)

        self.tabview = customtkinter.CTkFrame(self, )
        self.tabview.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        #logo
        self.logo = customtkinter.CTkLabel(self, text="Título", font=("Helvetica", 18))
        self.logo.grid(row= 0, column=0, padx=20, pady=20, sticky="nsew", columnspan= 2)

        ######################### Parametros (1,0) ########################################
        self.parametros = customtkinter.CTkFrame(master=self.tabview, width=600,)
        self.parametros.grid(row=1, column=0, padx=20, pady=20, sticky="nsew",)

        self.Text_1 = customtkinter.CTkLabel(master=self.parametros, text="Ingrese la ecución", font=("Helvetica", 18), anchor="w")
        self.Text_1.grid(row=0, column=0,padx = 20, pady = 20, sticky="")

        self.ecu = customtkinter.CTkEntry(master=self.parametros, width=500, placeholder_text="0")
        self.ecu.grid(row=1, column=0,padx = 20, pady = 20, sticky="")

        self.metodo = customtkinter.CTkOptionMenu(master=self.parametros, width=500, values=["Seleccione el método","Tanteo", "Bisección", "Regla Falsa", "Newton Raphson"])
        self.metodo.grid(row=2, column=0,padx = 20, pady = 20, sticky="")

        #Botones
        self.botones = customtkinter.CTkFrame(master=self.parametros, width=600,)
        self.botones.grid(row=3, column=0, padx=20, pady=20, sticky="EW",)

        self.calcular = customtkinter.CTkButton(self.botones, text="Calcular", command = self.calcular_btn)
        self.calcular.grid(row=0, column=0,padx = 20, pady = 20, sticky="EW")

        self.graficar = customtkinter.CTkButton(self.botones, text="Graficar")
        self.graficar.grid(row=0, column=1,padx = 20, pady = 20, sticky="EW")

        ######################### Bloque de respuestas (2,0) #############################
        self.respuesta = customtkinter.CTkFrame(master=self.tabview, width=600)
        self.respuesta.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")

        self.Text_2 = customtkinter.CTkLabel(master=self.respuesta, text="f(x) = ", font=("Helvetica", 18), anchor="w")
        self.Text_2.grid(row=0, column=0, padx = 20, pady = 20, sticky="EW")

        self.Text_3 = customtkinter.CTkLabel(master=self.respuesta, text="X = ", font=("Helvetica", 18), anchor="w")
        self.Text_3.grid(row=1, column=0, padx = 20, pady = 20, sticky="EW")
        

        self.Text_4 = customtkinter.CTkLabel(master=self.respuesta, text="Iteracciónes = ", font=("Helvetica", 18), anchor="w")
        self.Text_4.grid(row=2, column=0, padx = 20, pady = 20, sticky="EW")

        ####################### gráfica (1,1) ##############################################
        self.grafica = customtkinter.CTkFrame(master=self.tabview, width=600, height=500)
        self.grafica.grid(row=1, column=1, padx=20, pady=20, sticky="nsew", rowspan = 2)
        
        self.Text_5 = customtkinter.CTkLabel(master=self.grafica, text="Gráfica = ", font=("Helvetica", 18), )
        self.Text_5.grid(row=0, column=0, padx = 20, pady = 20, sticky="")

#############################__Back__#####################################

    def calcular_btn(self):

        met = str(self.metodo.get())

        x = sympy.symbols('x')
        expr = sympy.sympify(self.ecu.get())
        f = sympy.lambdify(x, expr, "numpy")
        Tol= 0.001

        if met == "Tanteo":
            x = rnd.uniform(-100,100)
            ox = x
            Contador = 0
            x += 0.01
            while abs(int(f(x))) >= Tol or Contador == int(99999999):
                if abs((f(x))) > abs((f(ox))):
                    ox -= 0.01
                    x -= 0.01
                    Contador +=1
                else:
                    ox += 0.01
                    x += 0.01
                    Contador +=1
            
        if met == "Bisección":
            b = rnd.uniform(-100,100)
            a = rnd.uniform(-100,100)
            while f(a) < 0:
                a = rnd.uniform(-100,100)
            while f(b) > 0:
                b = rnd.uniform(-100,100)
            x = ((a + b) / 2)

            Contador = 1
            while abs(int(f(x))) >= Tol:
                if f(x) > 0:
                    a = x
                    x = ((a + b) / 2)
                    Contador += 1
                else:
                    b = x
                    x = ((a + b) / 2)
                    Contador += 1 

        if met == "Regla Falsa":
            b = rnd.uniform(-100,100)
            a = rnd.uniform(-100,100)
            while f(a) < 0:
                a = rnd.uniform(-100,100)
            while f(b) > 0:
                b = rnd.uniform(-100,100)
            x = a-((f(a) * (b-a)) / (f(b) - f(a)))
            Contador = 1
            while abs(int(f(x))) >= Tol:
                if f(x) > 0:
                    a = x
                    x = a-((f(a) * (b-a)) / (f(b) - f(a)))
                    Contador += 1
                else:
                    b = x
                    x = a-((f(a) * (b-a)) / (f(b) - f(a)))
                    Contador += 1
                if Contador == 99999:
                    print ("No se puede soluciónar") 
                    break
        self.Text_2.configure(text= "f(x) = " + str(expr))
        self.Text_3.configure(text= "X = " + str(x))
        self.Text_4.configure(text= "Iteracciónes = " + str(Contador))

        
        

     
    
if __name__ == "__main__":
    app = App()
    app.mainloop()