
#Hola profe :)

"""
La situacion es un edificio con 10 cuartos, 1 area comun, y una cocina comun
la idea es que para decidir a que temperatura se va a poner el edificio, cada
persona va a poder votar por su temperatura deseada, pero como en la cocina
y en el area comun hay mas personas, esos votos van a tener mayor importancia
"""
import random

#asumo que solamente hay 10 cuartos

def promedio_cuartos(a, b ,c , d, e, f,  g, h, i, j):
    sum_cuartos_sin_dividir = a+b+c+d+e+f+g+h+i+j
    sum_cuartos = sum_cuartos_sin_dividir/10
    valor_cuartos = sum_cuartos*0.7
    return valor_cuartos

#aqui hago el promedio de los cuartos, pero multiplico el valor por 0.7, pues
#quiero que las votaciones de los cuartos solo valgan por el 70% del resultado

def promedio_comun(temp_common):
    valor_common = temp_common*0.15
    return valor_common

#estas temperaturas valen mas pues aqui hay muchas personas, por lo que vale
#mas sus resultados, ejemplo, cocina de piso, area comun

vc0, vc1 = random.randint (14,34), random.randint (14,34)
vc2, vc3 = random.randint (14,34), random.randint (14,34)
vc4, vc5 = random.randint (14,34), random.randint (14,34)
vc6, vc7 = random.randint (14,34), random.randint (14,34)
vc8 = random.randint (14,34)
vc9 = int(input("A que temperatura desearias que este tu cuarto? "))

#aqui hay los valores que cada usuario vota, los creo con random para simular
#los otros habitantes de los demas 9 cuartos

v_f_cuartos = promedio_cuartos (vc0,vc1,vc2,vc3,vc4,vc5,vc6,vc7,vc8,vc9)


cocina = random.randint(20,40)
v_f_cocina = promedio_comun(cocina)

#las personas de la cocina prefieren la temperatura mas alta


area_comun = int(input("A que temperatura desearias que este el area comun? "))
v_f_comun = promedio_comun(area_comun)

#v_f significa votacion final

temp_del_edificio = v_f_comun + v_f_cocina + v_f_cuartos

print ("La temperatura del edificio ahora es:","%.1f" % temp_del_edificio,"°C")
#todos sufrimos temperaturas de 20 grados por culpa de los del team calor :(
