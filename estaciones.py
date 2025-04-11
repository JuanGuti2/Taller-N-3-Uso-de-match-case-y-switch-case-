
def obtener_estacion(mes):
    match mes:
        case 12 | 1 | 2: 
            return "Invierno"
        case 3 | 4 |5:
            return "Primavera"
        case 6 | 7 | 8|7:
            return "Verano"
        case 9 | 10 | 11:
            return "Otoño"
        case _:
            return "Mes inválido. Debe estar entre 1 y 12."

# Solicitar al usuario un mes
mes = int(input("Ingrese el número del mes (1-12): "))
print("La estación es:", obtener_estacion(mes))
