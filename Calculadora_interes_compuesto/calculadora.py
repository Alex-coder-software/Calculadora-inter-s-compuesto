
def compose_interest_calculator(p: float, r: float, n: float, t: float, d: float) -> float:

    # Asegurarse de que todos los valores sean floats
    r = float(r)
    n = float(n)
    
    # Al ser un cálculo complejo y largo, he decidido dividirlo en 4 partes
    first_part = (1 + (r / n)) ** (n * t)
    second_part = p * first_part
    third_part = (d * (first_part - 1)) / (r / n)
    fourth_part = second_part + third_part
    result = round(fourth_part, 2)  # Redondeamos el resultado a dos decimales
    return result

# Esta es la formula del interes compuesto: VF=P×((1+(r/n)) ** nt + (d*((1+(r/n)) ** nt) - 1)/(r/n)
# Siendo: VF = Valor futuro de la inversión. P = Inversión inicial o monto principal. r = Tasa de interés anual (en decimal, por ejemplo, 5% se escribe como 0.05). n = Número de veces que se capitaliza el interés en un año (por ejemplo, 12 para mensual, 1 para anual). t = Número de años que dura la inversión. D = Depósito adicional realizado en cada período.
# print(compose_interest_calculator(10000, 0.06, 12, 10, 200)) Comprobar que funciona bien, resultado: 50969.84€