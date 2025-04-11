
num1=int(input("numeroUno: "))
num2=int(input("numeroDos: "))
operacion= input("introduzca una operacion (+ - / *): ")
match operacion :
    case "+" : 
        res= num1+num2
    case "-" : 
        res= num1-num2
    case "/":
        if num2 == 0:
            res = "Error: No se puede dividir entre cero."
        else:
            res = num1 / num2
    case "*" : 
        res= num1*num2
    case "^" :
        res=("operacion no valida")
print(f"El resultado de {num1} {operacion} {num2} = {res} ")