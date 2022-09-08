# Quiz : Leer un número entero de 5 dijitos y determinar si es capicúa


print("-----------------------------")
print("-----CINCO DIJITOS CAPICUA---")
print("-----------------------------")

#input
d = int(input("Digite un número de 5 dijitos: "))

#process
if d >= 10000 and d<100000:
    d1 = d %10
    d2 = int((d %100)/10)
    d4 = int((d %10000)/1000)
    d5 = int((d %100000)/10000)
    if d1==d5 and d2==d4:
        dc=" es de 5 digitos capicúa"
    else:
        dc=" es de 5 digitos pero no es capicúa"

else:
    dc=" no es un número de 5 dijitos"
    
    
#output
print("-------------------------")
print("--------RESULTADOS-------")
print("-------------------------")

print("El número ",d,dc)