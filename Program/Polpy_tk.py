import random as rnd
import customtkinter
import tkinter


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

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")

def button_function():
    print("button pressed")

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

app.mainloop()