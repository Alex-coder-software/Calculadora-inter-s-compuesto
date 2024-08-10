"""Esta ha sido mi fuente de información principal"""
# https://medium.com/@solidlucho/tkinter-crea-interfaces-gr%C3%A1ficas-en-python-de-forma-sencilla-50d131f84883

# Importamos módulos necesarios
import tkinter as tk
from calculadora import compose_interest_calculator

def calcular_interes():
    try:
        # Obtener los valores de las entradas y convertirlos a float para trabajar en la función
        p = float(var1.get())
        r = float(var2.get())
        n = float(var3.get())
        t = float(var4.get())
        d = float(var5.get())

        # Llamar a la función de cálculo
        resultado = compose_interest_calculator(p, r, n, t, d)

        # Mostrar el resultado en la ventana
        resultado_etiqueta.config(text=f"Resultado: {resultado} €")

    # Excepciones de error de valor (si no se ingresan valores numericos) u otras    
    except ValueError:
        resultado_etiqueta.config(text="Por favor, ingresa valores numéricos válidos.")
    except Exception as e:
        resultado_etiqueta.config(text=f"Ocurrió un error en la ejecución: {e}")

# Creamos la ventana y le damos un título
window = tk.Tk()
window.title("Calculadora de interés compuesto")

# Obtener las dimensiones de la pantalla
ancho_pantalla = window.winfo_screenwidth() #método para obtener Ancho
alto_pantalla = window.winfo_screenheight() #método para obtener Alto

# Calcular las coordenadas para centrar la ventana
ancho_ventana = 800
alto_ventana = 600
posicion_x = (ancho_pantalla - ancho_ventana) // 2 
posicion_y = (alto_pantalla - alto_ventana) // 2

# Establecer el tamaño y la posición de la ventana con los valores calculados anteriormente
window.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")

# Añadimos un título
etiqueta = tk.Label(window, text="Calculadora de interés compuesto", font=("Arial", 16), fg="green", height=5)
etiqueta.pack()

# Pedimos las variables en cuadros de texto
etiqueta_1 = tk.Label(window, text="Ingresa la inversión en euros", font=("Arial", 16), height=1)
etiqueta_1.pack()
var1 = tk.StringVar() # Guardamos como variable el valor
cuadro_texto_1 = tk.Entry(window, width=30, textvariable=var1)
cuadro_texto_1.pack()

etiqueta_2 = tk.Label(window, text="Ingresa la tasa de interés anual en decimal", font=("Arial", 16), height=1)
etiqueta_2.pack()
var2 = tk.StringVar() # Guardamos como variable el valor
cuadro_texto_2 = tk.Entry(window, width=30, textvariable=var2)
cuadro_texto_2.pack()

etiqueta_3 = tk.Label(window, text="Ingresa 1 si haces depositos anuales o 12 si haces depositos mensuales", font=("Arial", 16), height=1)
etiqueta_3.pack()
var3 = tk.StringVar() # Guardamos como variable el valor
cuadro_texto_3 = tk.Entry(window, width=30, textvariable=var3)
cuadro_texto_3.pack()

etiqueta_4 = tk.Label(window, text="Ingresa el número de años de la inversión", font=("Arial", 16), height=1)
etiqueta_4.pack()
var4 = tk.StringVar() # Guardamos como variable el valor
cuadro_texto_4 = tk.Entry(window, width=30, textvariable=var4)
cuadro_texto_4.pack()

etiqueta_5 = tk.Label(window, text="Ingresa el deposito anual o mensual, dependiendo de que hayas ingresado en la opción 3", font=("Arial", 14), height=1)
etiqueta_5.pack()
var5 = tk.StringVar() # Guardamos como variable el valor
cuadro_texto_5 = tk.Entry(window, width=30, textvariable=var5)
cuadro_texto_5.pack()

# Declaramos la etiqueta de resultado antes de usarla en la función
resultado_etiqueta = tk.Label(window, text="", font=("Arial", 16), height=2)
resultado_etiqueta.pack()

boton = tk.Button(window, text="Calcular", command=calcular_interes, height=5, width=60, bg="green")
boton.pack()

# Creamos un loop para que la ventana esté abierta
window.mainloop()  