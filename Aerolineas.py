from tkinter import *
import sqlite3
from  tkinter import ttk
from tkinter import *

def salir():aeroline.withdraw()

def vientos():
    vuelo = Toplevel(aeroline)
    vuelo.title("Vuelos")
    vuelo.geometry("700x500")

    kda = ttk.Style()
    kda.configure('BW.TNotebook')
    notebook = ttk.Notebook(vuelo)
    notebook.pack(fill='both',expand='yes')
    pag1 = ttk.Frame(notebook, style='BW.TNotebook')
    pag2 = ttk.Frame(notebook, style='BW.TNotebook')
   
    
    notebook.add(pag1,text='  Vuelos   ')
    notebook.add(pag2,text='  Configuracion  ')
    
    lst = Listbox(pag1, width=35, height=21)

    con = sqlite3.connect('Aeroline.s3db')
    con.row_factory=sqlite3.Row
    cursor=con.cursor()
    cursor.execute("SELECT Vuelo, Hora, Fech, Origen, Destino, Duracion FROM Datosv where vuelo>0")
    lineas = cursor.fetchall()
    for i in lineas:
        lst.insert(0,"------------------------------------------","  VUELO: "+str(i[0]),"           HORA DE PARTIDA: "+str(i[1]),"           FECHA: "+str(i[2]),"           ORIGEN: "+str(i[3]),"           DESTINO: "+str(i[4]),")")
        cursor.close()
    lst.place(x=0, y=65)

    encabezado = Label(pag2, text="INFORMACION DE VUELOS").place(x=100, y=15)
    hour = Label(pag2, text="Hora de salida: ").place(x=20, y=50)
    hourE = Entry(pag2, width=25).place(x=110, y=53)
    fecha = Label(pag2, text="Fecha: ").place(x=63, y=70)
    fechaE = Entry(pag2, width=25).place(x=110, y=73)
    origen = Label(pag2, text="Origen: ").place(x=58, y=90)
    origenE = Entry(pag2, width=25).place(x=110, y=93)
    destino = Label(pag2, text="Destino: ").place(x=53, y=110)
    destinoE  = Entry(pag2, width=25).place(x=110, y=113)
    duracion = Label(pag2, text="Duracion: ").place(x=45, y=130)
    duracionE = Entry(pag2, width=25).place(x=110, y=133)

    ward = Button(pag2, text="Gurdar").place(height=30, width=60, x=120, y=170)
    ex = Button(pag2, text="Salir").place(height=30, width=60, x=180, y=170)


        
aeroline = Tk()
aeroline.title("Aerolineas Garcia")
aeroline.geometry("930x613")

ave=PhotoImage(file="avion.png")
lbl=Label(aeroline, image=ave).place(x=0, y=0)

vuelos = Button(aeroline, text="Vuelos", command=vientos).place(bordermode=OUTSIDE, height=45, width=150, x=0, y=200)
reservas = Button(aeroline, text="Reservas").place(bordermode=OUTSIDE, height=45, width=150, x=0, y=250)
registros = Button(aeroline, text="Registros").place(bordermode=OUTSIDE, height=45, width=150, x=0, y=300)
pagar = Button(aeroline, text="Pagar").place(bordermode=OUTSIDE, height=45, width=150, x=0, y=350)
imprenta = Button(aeroline, text="Impimir Pase B").place(bordermode=OUTSIDE, height=45, width=150, x=0, y=400)
consulta = Button(aeroline, text="Consultar Itinerario").place(bordermode=OUTSIDE, height=45, width=150, x=0, y=450)
salir = Button(aeroline, text="Retirarse de este fino programa", command=salir).place(bordermode=OUTSIDE, height=45, width=200, x=700, y=550)


aeroline.mainloop()
