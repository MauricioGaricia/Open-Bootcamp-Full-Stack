import tkinter
from tkinter import ttk, StringVar

Window = tkinter.Tk()              
Window.title( 'Ejericicio 1 - Tema GUI' )

default_msg = 'Seleccione Una Opción : '

Seleccion_Lenguaje = tkinter.StringVar()
msg = tkinter.StringVar( value = default_msg )
print( Seleccion_Lenguaje.get() )
print( msg.get() )

def Boton_Cambiar( *args ) :
    msg.set( f'El Lenguaje Que Has Seleccionado { Seleccion_Lenguaje.get() }.' )
    print( msg.get() )

def Seleccionar_Respuesta ( event ) :
     print( f' > { Seleccion_Lenguaje.get() }' )

def Reset( event ) :
    Seleccion_Lenguaje.set( 'Reset ' )
    msg.set( default_msg )
    Label_Respuesta.config( text = msg.get() )

def Set_Label_Respuesta () :
    Label_Respuesta.config( text = msg.get() )

Seleccion_Lenguaje.trace_add( 'write', Boton_Cambiar )

Label_Pregunta = ttk.Label( Window, text = 'El Lenguaje Que Más Te Gusta Es:' )
Label_Pregunta.grid(
    column = 0,
    row = 0,
    sticky = tkinter.W,
    pady = 3,
)

Lenguajes = [ 'JavaScript', 'C#', 'Python', 'Swift' , 'Java', 'C++', 'Ruby', 'Go', 'PHP']
Opcion = []

for idx, Lenguaje in enumerate( Lenguajes ):
    Opcion.append( 
        ttk.Radiobutton(
            Window,
            text = Lenguaje,
            value = Lenguaje.capitalize(),
            variable = Seleccion_Lenguaje,
            command = Set_Label_Respuesta
        ) 
    )
    Opcion[ idx ].grid(
        column = 0,
        row = idx + 1,
        sticky = tkinter.W,
        pady = 3,
        padx = 15
    )

Label_Respuesta = ttk.Label( Window, text = msg.get() )
Label_Respuesta.grid(
    column = 0,
    row = len( Lenguajes ) + 1,
    sticky = tkinter.W,
    pady = 3,
)

Boton_Enviar = ttk.Button( Window, text = 'Responder' )
Boton_Enviar.grid(
    column = 0,
    row = len( Lenguajes ) + 2,
    sticky = tkinter.E,
    padx = 5,
    pady = 5
)
Boton_Enviar.bind(
    '<Button-1>',
    Seleccionar_Respuesta   
)

Boton_Reset = ttk.Button( Window, text = 'Reset' )
Boton_Reset.grid(
    column = 1,
    row = len( Lenguajes ) + 2,
    sticky = tkinter.W,
    padx = 5,
    pady = 5
)
Boton_Reset.bind(
    '<Button-1>',
    Reset         
)
if __name__ == "__main__" :
    Window.mainloop()