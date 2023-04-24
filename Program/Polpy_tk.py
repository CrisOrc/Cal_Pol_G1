import random as rnd
import tkinter as tk
from tkinter import PhotoImage
import customtkinter
import numpy as np
import matplotlib.pyplot as plt
import sympy 
import os
from PIL import Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("green")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()     

        self.x = 0
        self.Contador = 0   
############################__Front__####################################
        
        self.geometry(f"{1350}x{760}")
        self.title("PySolveX")
        self.iconbitmap("IMG\Logo.ico")
        
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "IMG")
        logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "Logo.png")), size=(500, 500))

        #columnas y filas
        self.grid_rowconfigure(1, weight=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)

        self.tabview = customtkinter.CTkFrame(self, )
        self.tabview.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        #logo
        self.logo = customtkinter.CTkLabel(self, text="PySolveX", font=("Helvetica", 18))
        self.logo.grid(row= 0, column=0, padx=20, pady=20, sticky="nsew", columnspan= 2)

        ######################### Parametros (1,0) ########################################

        self.parametros = customtkinter.CTkFrame(master=self.tabview, width=600,)
        self.parametros.grid(row=1, column=0, padx=20, pady=20, sticky="nsew",)

        self.Text_1 = customtkinter.CTkLabel(master=self.parametros, text="Ingrese la ecución", font=("Helvetica", 18), anchor="w")
        self.Text_1.grid(row=0, column=0,padx = 20, pady = 20, sticky="")

        self.ecu = customtkinter.CTkEntry(master=self.parametros, width=500, placeholder_text="1*x**3 - 2*x**2 - 1*x + 2")
        self.ecu.grid(row=1, column=0,padx = 20, pady = 20, sticky="")

        self.metodo = customtkinter.CTkOptionMenu(master=self.parametros, width=500, values=["Seleccione el método","Tanteo", "Bisección", "Regla Falsa", "Metodo Secante","Newton Raphson","Steffensen"])
        self.metodo.grid(row=2, column=0,padx = 20, pady = 20, sticky="")

        #Botones
        self.botones = customtkinter.CTkFrame(master=self.parametros, width=600,)
        self.botones.grid(row=3, column=0, padx=20, pady=20, sticky="EW",)

        self.calcular = customtkinter.CTkButton(self.botones, text="Calcular", command = self.calcular_btn)
        self.calcular.grid(row=0, column=0,padx = 20, pady = 20, sticky="EW")

        self.graficar = customtkinter.CTkButton(self.botones, text="Graficar", command = self.graficar_btn)
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
        
        self.Text_5 = customtkinter.CTkLabel(master=self.grafica, text="Gráfica", font=("Helvetica", 18), )
        self.Text_5.grid(row=0, column=0, padx = 20, pady = 20, sticky="")

        self.frame_grafica = customtkinter.CTkFrame(master=self.grafica, width=600, height=500, )
        self.frame_grafica.grid(row=1, column=0, padx=20, pady=20, sticky="nsew", rowspan = 2)

        self.frame_img = customtkinter.CTkLabel(master=self.grafica, width=600, height=500, image=logo_image, text="" )
        self.frame_img.grid(row=1, column=0, padx=20, pady=20, sticky="nsew", rowspan = 1)
        
        self.canvas = FigureCanvasTkAgg(master=self.frame_grafica)
        
        

#############################__Back__#####################################

    def calcular_btn(self):
        
        ###### Comprobador del método #########
        met = str(self.metodo.get())

        ###### Extraer la ecuación de la entrada ###########
        x = sympy.symbols('x')
        expr = sympy.sympify(self.ecu.get())
        f = sympy.lambdify(x, expr, "numpy")
        Tol= 0.001
        soluciones = []
        totS = 0
        Contador = 0

        if met == "Tanteo":
            while totS < 100:
                x = rnd.randint(-10,10)
                ox = x
                x += 0.01

                while abs(f(x)) > Tol or Contador == 10000:

                    if abs(f(x)) > abs(f(ox)):
                        ox -= 0.01
                        x -= 0.01
                        Contador +=1
                    else:
                        ox += 0.01
                        x += 0.01
                        Contador +=1

                totS += 1
                ######### Guardar en la lista ##########
                if (round(x, 3)) not in soluciones:
                    soluciones.append(round(x, 3))
      
            
        if met == "Bisección":
            while totS < 100:

                ######### Random ##########
                b = rnd.randint(-10,10)
                a = rnd.randint(-10,10)
                while f(a) < 0:
                    a = rnd.randint(-10,10)
                while f(b) > 0:
                    b = rnd.randint(-10,10)
                x = ((a + b) / 2)

                while abs(f(x)) > Tol or Contador == 10000:
                    if f(x) > 0:
                        a = x
                        x = ((a + b) / 2)
                        Contador += 1
                    else:
                        b = x
                        x = ((a + b) / 2)
                        Contador += 1
                    
                totS += 1
                ######### Guardar en la lista ##########
                if (round(x, 3)) not in soluciones:
                    soluciones.append(round(x, 3))

        if met == "Regla Falsa":
            while totS < 100:

                ######### Random ##########
                b = rnd.randint(-10,10)
                a = rnd.randint(-10,10)
                while f(a) < 0:
                    a = rnd.randint(-10,10)
                while f(b) > 0:
                    b = rnd.randint(-10,10)

                ######### comprobar si es 0 ##########
                if (f(b) - f(a)) == 0:
                    continue
                else:
                    x = a-((f(a) * (b-a)) / (f(b) - f(a)))

                    while abs(f(x)) > Tol or Contador == 10000:
                        if f(x) > Tol:
                            a = x
                            x = a-((f(a) * (b-a)) / (f(b) - f(a)))
                            Contador += 1
                        else:
                            b = x
                            x = a-((f(a) * (b-a)) / (f(b) - f(a)))
                            Contador += 1
                
                    totS += 1

                    ######### Guardar en la lista ##########
                    if (round(x, 3)) not in soluciones:
                        soluciones.append(round(x, 3))
      

        
        if met == "Metodo Secante":
            def dxf(x):
                return (f(a) - f(b)) / (a - b)
            
            while totS < 100:

                ######### Random ##########
                a = rnd.randint(-10,10)
                b = rnd.randint(-10,10)
                while f(a) < 0:
                    a = rnd.randint(-10,10)
                while (f(b) > 0):
                    b = rnd.randint(-10,10)

                ######### comprobar si es 0 ##########
                if ((a - b) == 0):
                    continue
                else:
                    if dxf(a) == 0:
                        continue
                    else:
                        x = a - (f(a)/dxf(a))

                while abs(f(x)) > Tol or Contador == 10000:
                    if f(x) > Tol:
                        a = x
                        x = x - (f(x)/dxf(x))
                        Contador += 1
                    else:
                        b = x
                        x = x - (f(x)/dxf(x))
                        Contador += 1

                totS += 1
                ######### Guardar en la lista ##########
                if (round(x, 3)) not in soluciones:
                    soluciones.append(round(x, 3))

        if met == "Newton Raphson":
            def dxf(x):
                return (f(x + Tol) - f(x)) / Tol

            while totS < 100:
                x = rnd.randint(-10,10)

                x1 = x - (f(x)/dxf(x))

                while abs(f(x)) > Tol or Contador == 10000:
                        x = x1
                        x1 = x - (f(x)/dxf(x))
                        Contador += 1
                totS += 1
                ######### Guardar en la lista ##########
                if (round(x, 3)) not in soluciones:
                    soluciones.append(round(x, 3))

        if met == "Steffensen":
            while totS < 100:
                x = rnd.randint(-10,10)

                ######### comprobar si es 0 ##########
                if (f(x+f(x))-f(x)) == 0:
                    continue
                else:
                    x1 = x - ((f(x)**2)/(f(x + f(x))-f(x)))
                    while abs(f(x)) > Tol or Contador == 10000:
                        x = x1
                    
                ######### comprobar si es 0 ##########
                        if (f(x+f(x))-f(x)) == 0:
                            continue
                        else:
                            x1 = x - ((f(x)**2)/(f(x+f(x))-f(x))) 
                            Contador += 1
                    totS += 1

                ######### Guardar en la lista ##########
                    if (round(x, 3)) not in soluciones:
                        soluciones.append(round(x, 3))
        
        self.Text_2.configure(text= "f(x) = " + str(expr))
        self.Text_3.configure(text= "X = " + str(soluciones))
        self.Text_4.configure(text= "Iteracciónes = " + str(Contador))


    def graficar_btn(self):

        self.frame_grafica = customtkinter.CTkFrame(master=self.grafica, width=600, height=500, )
        self.frame_grafica.grid(row=1, column=0, padx=20, pady=20, sticky="nsew", rowspan = 2)

        a = sympy.symbols('x')
        expr = sympy.sympify(self.ecu.get())
        f = sympy.lambdify(a, expr, "numpy")

        X=np.linspace(-5, 5, 50).astype(float)
        Y=f(X)

        self.canvas.get_tk_widget().pack_forget()
            
        
        fig, ax = plt.subplots(facecolor=('#333333'))
        ax.set_facecolor('#e6e6e6')
        ax.plot(X, Y, '#106a43')
        ax.axhline(y=0, color='#303030')
        ax.axvline(x=0, color='#303030')
        ax.set_xlim([-10, 10])
        ax.set_ylim([-10, 10])
        ax.tick_params(labelcolor='w')

        self.canvas = FigureCanvasTkAgg(fig, master=self.frame_grafica)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

    
if __name__ == "__main__":
    app = App()
    app.mainloop()