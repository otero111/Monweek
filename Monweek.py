from tkinter import *


raiz = Tk()
raiz.title("Monweek")
raiz.geometry("400x450")
raiz.resizable(0,0)
raiz.config(bg = "black")


##############################################################

first=Label(raiz, text="Weekly sales control",fg="white", bg="black",font=("Courier", 12, "italic"))
first.grid(row=0, column=0, sticky="e", padx=10, pady=10)

lunes=Label(raiz, text="Monday",fg="white", bg="black")
lunes.grid(row=1, column=0, sticky="e", padx=10, pady=10)


martes=Label(raiz, text="Tuesday",fg="white", bg="black")
martes.grid(row=2, column=0, sticky="e", padx=10, pady=10)


miercoles=Label(raiz, text="Wednesday",fg="white", bg="black")
miercoles.grid(row=3, column=0, sticky="e", padx=10, pady=10)


jueves=Label(raiz, text="Thursday",fg="white", bg="black")
jueves.grid(row=4, column=0, sticky="e", padx=10, pady=10)


viernes=Label(raiz, text="Friday",fg="white", bg="black")
viernes.grid(row=5, column=0, sticky="e", padx=10, pady=10)


sabado=Label(raiz, text="Saturday",fg="white", bg="black")
sabado.grid(row=6, column=0, sticky="e", padx=10, pady=10)


##################################################################



#Var = StringVar()


lunesEntry = Entry(raiz, width = 5)####, textvaliable = a)
lunesEntry.grid(row=1, column=1, sticky="e", padx=10, pady=10)

martesEntry = Entry(raiz, width = 5)####, textvaliable = b)
martesEntry.grid(row=2, column=1, sticky="e", padx=10, pady=10)

miercolesEntry = Entry(raiz, width = 5)####, textvaliable = c)
miercolesEntry.grid(row=3, column=1, sticky="e", padx=10, pady=10)

juevesEntry = Entry(raiz, width = 5)####, textvaliable = d)
juevesEntry.grid(row=4, column=1, sticky="e", padx=10, pady=10)

viernesEntry = Entry(raiz, width = 5)####, textvaliable = e)
viernesEntry.grid(row=5, column=1, sticky="e", padx=10, pady=10)

sabadoEntry = Entry(raiz, width = 5)####, textvaliable = f)
sabadoEntry.grid(row=6, column=1, sticky="e", padx=10, pady=10)


######################################################################


def total():
	total=int(lunesEntry.get()) + int(martesEntry.get()) + int(miercolesEntry.get()) + int(juevesEntry.get()) + int(viernesEntry.get()) + int(sabadoEntry.get())
	return total

def promedio():
	total2 = total()
	promedio = int(total2)/6
	promedioR = round(promedio, 2)
	return promedioR



totalLabel = Label(raiz, text="Total:", fg = "white", bg = "black")
totalLabel.grid(row=8, column=0, sticky="e", padx=10, pady=10)

promedioLabel = Label(raiz, text="Mean:", fg = "white", bg = "black")
promedioLabel.grid(row=9, column=0, sticky="e", padx=10, pady=10)

etiqueta1 = Label(raiz)
etiqueta1.grid(row=8, column=1, sticky="w")
etiqueta1.config(fg="white", bg="black", font=("Courier", 20, "italic"))

etiqueta2 = Label(raiz)
etiqueta2.grid(row=9, column=1, sticky="w")
etiqueta2.config(fg="white", bg="black", font=("Courier", 20, "italic"))

def mostrar1():
    totalSemana = total()
    promedioSemanal = promedio()
    etiqueta1["text"]= totalSemana
    etiqueta2["text"]= promedioSemanal




boton=Button(raiz, text="calcular", bg = "black", fg = "white" ,command=mostrar1)
boton.grid(row = 7, column = 1, sticky="e", padx=10, pady=10)


raiz.mainloop()




