from tkinter import Text, Label, Button


class MainFrame:
    def __init__(self, ventana):
        #Inicializar la ventana con un titulo
        self.ventana=ventana
        self.ventana.title("Herramienta Analizador de JavaScript")
        self.ventana.config(background="#5ABF72")


        self.pantalla=Label(ventana, text="En este analizador al dar click se mostrara solo los ingresos que correspondan al lenguaje JavaScript",background="#5ABF72", font=("Helvetica"))
        self.pantalla.grid(row=1, column=2, columnspan=4, padx=5, pady=5)

        #Agregar una caja de texto donde se ingresará el codigo a analizar
        self.pantalla=Text(ventana, width=20, height=20, background="white", foreground="black", font=("Helvetica",15))

        #Ubicar la pantalla en la ventana
        self.pantalla.grid(row=2, column=0, columnspan=4, padx=5, pady=5)

        #Agregar una caja de texto donde se mostrará0 el codigo analizado
        self.pantalla=Text(ventana, width=20, height=20, background="black", foreground="white", font=("Helvetica",15))

        #Ubicar la pantalla en la ventana
        self.pantalla.grid(row=2, column=4, columnspan=4, padx=5, pady=5)

        botonA=self.crearBoton("Analizar")
        botonA.grid(row=3, column=2, columnspan=4)




    def crearBoton(self, valor, ancho=10, alto=2):
        return Button(self.ventana, text=valor, width=ancho, height=alto, font=("Helvetica",15), background="green3")
