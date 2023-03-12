import random as rnd
import flet as ft
########################### BACK ###########################   

def main(page: ft.Page):

    def f(x):
        return (int(n_1F.value))*x**3 + (int(n_2F.value))*x**2 + (int(n_3F.value))*x + (int(n_4F.value))
    
    def reglaFalsa():
        global Contador, x
        b = rnd.randint(-100,100)
        a = rnd.randint(-100,100)
        while f(a) < 0:
            a = rnd.randint(-100,100)
        while f(b) > 0:
            b = rnd.randint(-100,100)
        x = a-((f(a) * (b-a)) / (f(b) - f(a)))
        Contador = 0
        Tol = 0.001
        while abs(f(x)) > Tol:
            if f(x) > 0:
                a = x
                x = a-((f(a) * (b-a)) / (f(b) - f(a)))
                Contador += 1
            else:
                b = x
                x = a-((f(a) * (b-a)) / (f(b) - f(a)))
                Contador += 1
        return Contador, x
               
    def tanteo():
        global Contador, x
        x = rnd.randint(-100,100)
        ox = x
        Contador = 0
        Tol=0.001
        x += 0.01
        while abs(f(x)) >= Tol:
            if abs(f(x)) > abs(f(ox)):
                ox -= 0.01
                x -= 0.01
                Contador +=1
            else:
                ox += 0.01
                x += 0.01
                Contador +=1
        return Contador, x

    def biseccion():
        global Contador, x
        b = rnd.randint(-100,100)
        a = rnd.randint(-100,100)
        while f(a) < 0:
            a = rnd.randint(-100,100)
        while f(b) > 0:
            b = rnd.randint(-100,100)
        x = ((a + b) / 2)

        Contador = 0
        Tol = 0.001

        while abs(f(x)) > Tol:
            if f(x) > 0:
                a = x
                x = ((a + b) / 2)
                Contador += 1
            else:
                b = x
                x = ((a + b) / 2)
                Contador += 1
        return Contador, x
    
    def button_clicked(e):
        if dd.value!="":
            fun.value = f"Función = {n_1F.value}X³ + {n_2F.value}x² {n_3F.value}X + {n_4F.value} = 0."
            ddv.value = f"{dd.value}"
            if dd.value=="Regla Falsa":
                reglaFalsa()
                Contador, x = reglaFalsa()
                page.update()
            if dd.value=="Bisección":
                biseccion()
                Contador, x = biseccion()
                page.update()
            if dd.value=="Tanteo":
                tanteo()
                Contador, x = tanteo()
                page.update()
            xv.value = f"Xs = {x}"
            count.value = f"Iteracciónes: {Contador}"
            page.update()
       

########################### Front ###########################    
    fun = ft.Text(value="Función =", color="white",)
    page.bgcolor="#0D0D0D"
    page.horizontal_alignment = "CENTER"
    ddv = ft.Text(value=(""))
    t = ft.Text(value="Pypol", color="white",size=20,)
    n_1F = ft.TextField(border_color="#D99D55", bgcolor="#734C29",width=60, height=30,text_align="CENTER")
    n_2F = ft.TextField(border_color="#D99D55", bgcolor="#734C29",width=60, height=30,text_align="CENTER")
    n_3F = ft.TextField(border_color="#D99D55", bgcolor="#734C29",width=60, height=30,text_align="CENTER")
    n_4F = ft.TextField(border_color="#D99D55", bgcolor="#734C29",width=60, height=30,text_align="CENTER")
    count = ft.Text("Iteracciónes: ")
    xv = ft.Text("X = ")
    b = ft.ElevatedButton(text="Calcular", on_click=button_clicked, bgcolor="#212026", color="#D99D55")
    dd = ft.Dropdown(width=500, bgcolor="#734C29", focused_color="#D99D55",border_color="#D99D55", options=[ ft.dropdown.Option("Tanteo"),ft.dropdown.Option("Bisección"),ft.dropdown.Option("Regla Falsa"),],)
    page.controls.append(t)
    page.update()
    page.add(

        ft.Card(elevation=15,content=ft.Container(bgcolor="#212026",padding=50, width=1220, height=620,content=ft.Row([
        
            ft.Column([
                ft.Container(content=ft.Text("Ingrese los valores numericos. Si no tiene una de las x ingrese 0"),),
                    ft.Row([n_1F,ft.Text("X³ +"),n_2F,ft.Text("x² + "),n_3F,ft.Text("X +"),n_4F,ft.Text("= 0"),b]),
                        ft.Container(content=ft.Text("Método"),),
                        dd,
                        ft.Container(content=ft.Text("Valores")),
                        ft.Card(elevation=15,content=ft.Container(bgcolor="#734C29",padding=50, width=490, height=315,content=ft.Row([ft.Column([
                            ft.Container(fun,),
                            ft.Container(content=xv,),
                            ft.Container(content=count,),
                                ])])))],width=620),

            ft.Column([
                ft.Container(content=ft.Text("Gráfico"),),
                    ft.Card(elevation=15,content=ft.Container(bgcolor="#734C29",padding=50, width=500, height=500,content=ft.Row(width=490, height=315,),))]),],),),), 
    
    
    ),page.update() 


ft.app(target=main, route_url_strategy="hash")