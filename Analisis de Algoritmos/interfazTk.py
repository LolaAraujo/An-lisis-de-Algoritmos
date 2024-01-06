"""
Created on Sunday 01/10/23
@author: MariaCervantes
"""

from tkinter import *
import re
from tkinter import messagebox

class aplicacion():
    #Constructor. el self son las funciones del this en c++
    def __init__(self):
        self.raiz = Tk()
        self.raiz.geometry('600x400')
        self.raiz.resizable(width=False,height=False) #para que no redimencione la pantalla
        self.raiz.title('Expresiones regulares')
        label = Label(self.raiz, text="Validación de expresiones regulares") #se debe de señalar a donde se van agregar los elementos, a que ventana
        label.pack(side=TOP) #en donde va aparecer el texto
        
        self.textos = Frame(self.raiz)
        self.textos.pack(side=TOP)
        self.frameDeAbajo = Frame(self.raiz)
        self.frameDeAbajo.pack(side=BOTTOM)
        
        #Primer frame
        self.t1 = Entry(self.textos, width=40)
        self.t1.grid(row=0, column=0, padx=10, pady=10)
        self.t2 = Entry(self.textos, width=40)
        self.t2.grid(row=1, column=0, pady=10)
        self.t3 = Entry(self.textos, width=40)
        self.t3.grid(row=2, column=0, pady=10)
        self.t4 = Entry(self.textos, width=40)
        self.t4.grid(row=3, column=0, pady=10)
        
        self.b1 = Button(self.textos, text='validar', command=lambda:self.validar(1))
        self.b1.grid(row=0, column=1, padx=15, pady=10)
        self.b2 = Button(self.textos, text='validar', command=lambda:self.validar(2))
        self.b2.grid(row=1, column=1)
        self.b3 = Button(self.textos, text='validar', command=lambda:self.validar(3))
        self.b3.grid(row=2, column=1)
        self.b4 = Button(self.textos, text='validar', command=lambda:self.validar(4))
        self.b4.grid(row=3, column=1)
        self.b5 = Button(self.textos, text='validar', command= self.print_selection)
        self.b5.grid(row=4, column=1)
        
        self.l1 = Label(self.textos, text='...')
        self.l1.grid(row=0, column=2)
        self.l2 = Label(self.textos, text='...')
        self.l2.grid(row=1, column=2)
        self.l3 = Label(self.textos, text='...')
        self.l3.grid(row=2, column=2)
        self.l4 = Label(self.textos, text='...')
        self.l4.grid(row=3, column=2)
        self.l5 = Label(self.textos, text='...')
        self.l5.grid(row=4, column=2)
        
        
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.c1 = Checkbutton(self.textos, text='Mostrar un messagebox', variable=self.var1, onvalue=1, offvalue=0)
        self.c1.grid(row=4, column=0)
        self.c2 = Checkbutton(self.textos, text='Cambiar color de fondo',variable=self.var2, onvalue=1, offvalue=0)
        self.c2.grid(row=5, column=0)
        
        
        #segundo frame
        self.bsalir = Button(self.frameDeAbajo, text="Salir", command= self.raiz.destroy)
        self.bsalir.pack(expand=True, side=LEFT, padx=30, pady=50)
        
        self.blimpiar = Button(self.frameDeAbajo, text="Limpiar", command= self.limpiar)
        self.blimpiar.pack(side= LEFT)
        
        
        #elemento principal, siempre tenerlo hasta abajo
        self.raiz.mainloop()
            
        
    def validar(self, numero):
        if(numero == 1):
            txtAValidar = self.t1.get()
             #Expresión regular de ipv4
            x = re.search("^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5|2[0-4]\d|[01]?\d\d?)$", txtAValidar) #mandando a la cadena de la variable txtAValidar
            if (x):
                self.l1.config(fg="green", text="IPv4 valida")
            else:
                self.l1.config(fg="red", text="IPv4 invalida")
                
        elif(numero == 2):
            txtAValidar = self.t2.get()
            #Expresión regular de gmail
            x = re.search("^[\w\.-]+@[\w\.-]+\.\w+$", txtAValidar) 
            if (x):
                self.l2.config(fg="green", text="Gmail valido")
            else:
                self.l2.config(fg="red", text="Gmail invalido")
                
        elif(numero == 3):
            txtAValidar = self.t3.get()
            x = re.search("^\d{2}[-.\s]?\d{2}[-.\s]?\d{2}[-.\s]?\d{2}[-.\s]?\d{2}$", txtAValidar) 
            if (x):
                self.l3.config(fg="green", text="Número valido")
            else:
                self.l3.config(fg="red", text="Número invalido")
                
        elif(numero == 4):
            txtAValidar = self.t4.get()
            x = re.search("^L.*A|l.*a$", txtAValidar) 
            if (x):
                self.l4.config(fg="green", text="Nombre valido")
            else:
                self.l4.config(fg="red", text="Nombre invalido")
                
    
    def print_selection(self):
        var1 = self.var1.get()
        var2 = self.var2.get()
        
        if (var1 == 1) & (var2 == 0):
            print(messagebox.askyesno(message="¿Desea continuar?", title="Mensaje"))
        elif (var1 == 0) & (var2 == 1):
            self.raiz.config(bg='MediumPurple1')
            self.textos.config(bg='MediumPurple1')
            self.frameDeAbajo.config(bg='MediumPurple1')
        elif (var1 == 0) & (var2 == 0):
            self.l5.config(fg='red', text='Sin selección')
        else:
            print(messagebox.askretrycancel(message="Cuidado! Dispositivo sobrecaliente", title="Advertencia"))
            self.raiz.config(bg='MediumPurple1')
            self.textos.config(bg='MediumPurple1')
            self.frameDeAbajo.config(bg='MediumPurple1')

    
    def limpiar(self):
        self.t1.delete(first=0, last='end') #para decirle que va a borrar, el end es porque desconocemos la longitud de la cadena
        self.l1.config(fg='black', text='...')
        self.t2.delete(first=0, last='end') 
        self.l2.config(fg='black', text='...')
        self.t3.delete(first=0, last='end') 
        self.l3.config(fg='black', text='...')
        self.t4.delete(first=0, last='end') 
        self.l4.config(fg='black', text='...')
        self.c1.deselect()
        self.c2.deselect()
        self.raiz.config(bg='gray84')
        self.textos.config(bg='gray84')
        self.frameDeAbajo.config(bg='gray84')
        self.l5.config(fg='black', text='...')
        
        
aplicacion() 