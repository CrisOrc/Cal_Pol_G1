from prompt_toolkit.layout.containers import Container
import random as rnd
import flet as ft
########################### BACK ###########################   

def main(page: ft.Page):
    def button_clicked(e):
        if dd.value!="":
            fun.value = f"Función = {n_1F.value}X + {n_2F.value} = 0."
            ddv.value = f"{dd.value}"
            if dd.value=="Regla Falsa":
                reglaFalsa()
                page.update()
            if dd.value=="Bisección":
                biseccion()
                page.update()
            if dd.value=="Tanteo":
                tanteo()
                page.update()
            page.update()
    
    def reglaFalsa():
        n_1=int(n_1F.value)
        n_2=int(n_2F.value)
        x_a = rnd.randint(-100,100)
        if ((n_1 * x_a) + n_2) >= 0:
            while True: 
                x_a = rnd.randint(-100,100)
                if ((n_1 * x_a) + n_2) <= 0:
                    break

        x_b = rnd.randint(-100,100)
        if ((n_1 * x_b) + n_2) <= 0:
            while True: 
                x_b = rnd.randint(-100,100)
                if ((n_1 * x_b) + n_2) >= 0:
                    break

        y_a = ((n_1 * x_a) + n_2)
        y_b = ((n_1 * x_b) + n_2)
        x_c = x_a-((y_a * (x_b-x_a)) / ((y_b - y_a)))

        if abs((n_1 * x_c) + n_2) <= 0.0001:
            Contador=0
            Contador = Contador + 1

        else:
            Contador=0
        while True:
            if ((n_1 * x_c) + n_2) < 0:
                x_a = x_c
                x_b = x_b
                y_a = ((n_1 * x_a) + n_2)
                y_b = ((n_1 * x_b) + n_2)
                x_c = x_a-((y_a * (x_b-x_a)) / ((y_b - y_a)))
                Contador=Contador+1
                if abs((n_1 * x_c) + n_2) <= 0.0001:
                    break
            if ((n_1 * x_c) + n_2) > 0:
                x_b = x_c
                x_a = x_a
                y_a = ((n_1 * x_a) + n_2)
                y_b = ((n_1 * x_b) + n_2)
                x_c = x_a-((y_a * (x_b-x_a)) / ((y_b - y_a)))
                Contador=Contador+1
                if abs((n_1 * x_c) + n_2) <= 0.0001:
                    break

    def tanteo():
        n_1=int(n_1F.value)
        n_2=int(n_2F.value)
        x_0 = rnd.randint(-100,100)

        if abs((n_1 * x_0) + n_2) <= 0.0001 and abs((n_1 * x_0) + n_2) >= -0.0001:
            print ("Felicidades, la respuesta es: ", x_0)

        else:
            Contador=0

        while True:
            if ((n_1 * x_0) + n_2) < -0.1:
                x_1 = x_0 + 0.1
                x_0 = x_1
                Contador=Contador+1
                if ((n_1 * x_0) + n_2) <= 0.0001 and ((n_1 * x_0) + n_2) >= -0.0001:
                    print ("Felicidades, la respuesta es: ", round(x_0))
                    print ("lleva ", Contador, "intentos")
                    break
            if ((n_1 * x_0) + n_2) > 0.1:
                x_1 = x_0 - 0.1
                x_0 = x_1
                Contador=Contador+1
                if ((n_1 * x_0) + n_2) <= 0.0001 and ((n_1 * x_0) + n_2) >= -0.0001:
                    print ("Felicidades, la respuesta es: ", round(x_0))
                    print ("lleva ", Contador, "intentos")
                    break

    def biseccion():
        n_1=int(n_1F.value)
        n_2=int(n_2F.value)
        x_a = rnd.randint(-100,100)
        if ((n_1 * x_a) + n_2) >= 0:
            while True: 
                x_a = rnd.randint(-100,100)
                if ((n_1 * x_a) + n_2) <= 0:
                    break

        x_b = rnd.randint(-100,100)
        if ((n_1 * x_b) + n_2) <= 0:
            while True: 
                x_b = rnd.randint(-100,100)
                if ((n_1 * x_b) + n_2) >= 0:
                    break

        x_c = ((x_a + x_b) / 2)

        if abs((n_1 * x_c) + n_2) <= 0.0001:
            print ("Felicidades, la respuesta es: ", x_c)  

        else:
            Contador=0
        while True:
            if ((n_1 * x_c) + n_2) < 0:
                x_a = x_c
                x_b = x_b
                x_c = ((x_a + x_b) / 2)
                Contador=Contador+1
                if abs((n_1 * x_c) + n_2) <= 0.0001:
                    print ("Felicidades, la respuesta es: ", (x_c))
                    print ("lleva ", Contador, "intentos")
                    break
            if ((n_1 * x_c) + n_2) > 0:
                x_b = x_c
                x_a = x_a
                x_c = ((x_a + x_b) / 2)
                Contador=Contador+1
                if abs((n_1 * x_c) + n_2) <= 0.0001:
                    print ("Felicidades, la respuesta es:", (x_c))
                    print ("lleva", Contador, "intentos")
                    break
    
########################### Front ###########################    
    
    fun = ft.Text(value="Función =", color="white",)
    page.bgcolor="#0D0D0D"
    page.horizontal_alignment = "CENTER"
    ddv = ft.Text(value=(""))
    t = ft.Text(value="Nombre logo", color="white",size=20,)
    n_1F = ft.TextField(border_color="#D99D55", bgcolor="#734C29",width=60, height=30,text_align="CENTER")
    n_2F = ft.TextField(border_color="#D99D55", bgcolor="#734C29",width=60, height=30,text_align="CENTER")
    x_c = 0
    Contador = 0
    b = ft.ElevatedButton(text="Calcular", on_click=button_clicked, bgcolor="#212026", color="#D99D55")
    dd = ft.Dropdown(width=500, bgcolor="#734C29", focused_color="#D99D55",border_color="#D99D55", options=[ ft.dropdown.Option("Tanteo"),ft.dropdown.Option("Bisección"),ft.dropdown.Option("Regla Falsa"),],)
    page.controls.append(t)
    page.update()
    page.add(
        ft.Card(elevation=15,
            content=ft.Container(bgcolor="#212026",padding=50, width=1220, height=620,
                content=ft.Row([
                
                ft.Column([
                    ft.Container(content=ft.Text("Ingrese los valores numericos"),),
                    ft.Row([n_1F,ft.Text("X +"),n_2F,ft.Text("= 0"),b]),
                    ft.Container(content=ft.Text("Método"),),
                    dd,
                    ft.Container(content=ft.Text("Valores")),
                    ft.Card(elevation=15,content=ft.Container(bgcolor="#734C29",padding=50, width=490, height=315,content=ft.Row([ft.Column([
                        ft.Container(fun,),
                        ft.Container(content=ft.Text("X = ", x_c,),),
                        ft.Container(content=ft.Text("Iteracciónes: ", Contador),),
                        ])])))
                ],width=620),

                ft.Column([
                    ft.Container( content=ft.Text("Gráfico")),
                     ft.Card(elevation=15,content=ft.Container(bgcolor="#734C29",padding=50, width=500, height=500,content=ft.Row([ft.Column([ 
                    ])])))
                    ]),
                ],),
        
            ),
        ), 
    
    ),page.update() 
    

ft.app(target=main)
