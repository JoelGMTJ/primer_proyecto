
import random

"""
Aqui va la parte para decidir que parte de el programa vas a querer usar,
voy a usar la estructura de ifs para esto. Tambien va a servir como una
"pantalla de inicio"
"""
print()
print('Bienvenido a "AutomatizaTec", el programa que te ayudara a una variedad\
 de cosas de tu vida diaria en el campus, selecciona una opcion para continuar')

print("")
print("Para ver la temperatura de tu edificio, 1")
print("Para ver cuanto te va a costar el estacionamiento, 2")
print("Para una pregunta rapida sobre matematicas, 3")
print("Si quieres salir del programa, alt+F4")
print("")
opcion_principal = int(input("Que opcion deseas usar? "))


"""
La situacion es un edificio con 10 cuartos, 1 area comun, y una cocina comun
la idea es que para decidir a que temperatura se va a poner el edificio, cada
persona va a poder votar por su temperatura deseada, pero como en la cocina
y en el area comun hay mas personas, esos votos van a tener mayor importancia
"""

if opcion_principal ==1:

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
    print ()
    print("Aqui vas a decidir la temperatura de tu cuarto y la de la cocina, sin\
 embargo, como las demas personas tambien votan por su temperatura es muy probab\
le que la temperatura sea muy diferente")
    print()
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

if opcion_principal == 2:

    """
    programa el cual te diga cuanto dinero vas a pagar por el estacionamiento a
    partir de cierta fecha, esto debido a la gree fee del tec
    """

    def costo_estacionamiento (d_por_semana):
        dias_por_semestre = d_por_semana*18
        costo_individual = dias_por_semestre*50
        return costo_individual
    #aqui es la funcion la que nos dice cuanto diero va a costar el estacionamiento
    #si se paga individual

    print ()
    print ("Aqui vas a descubrir cuanto dinero vas a pagar por el estacionamiento\
    en el tec, esto a causa de la green fee, primero unas preguntas, responde 'S' \
    si es verdadero y 'N' si no lo es")
    electrico = str(input("Tienes coche electrico o hibrido? "))
    carpool = str(input("Haces carpool (compartes carro con 3 o mas personas)? "))
    residencias = str(input("Vives en residencias tec? "))

    #esto es para dar el caso que algunas de estas situaciones sean verdad no cobrar
    #Pues si alguno de estos fuera el caso, el tec no te cobra la green fee

    if electrico == "s" or carpool == "s" or residencias == "s":
        print ("Tu costo va a ser $0")
    else:
        d_por_semana = int(input("Cuantos dias tienes clase por semana? "))
        if d_por_semana > 7 or d_por_semana < 0:
            print ("Imposible :O")
        else:
            costo_semestre = costo_estacionamiento (d_por_semana)
            print ("Te va a costar",costo_semestre, "pesos por semestre")
            print ("El costo de el semestre como pago completo es de $1900")
            if costo_semestre > 1900:
                print ("Es mas recomendable pagar el estacionamiento semestral")
            else:
                print ("Es mas recomendable pagar el estacionamiento dia con dia")

#Pregunta rapida del dia de matematicas

if opcion_principal==3:
    num1, num2 = random.randint(-30,64), random.randint(-60,50)
    print ("Cuanto es", num1, "por", num2, "? ")
    user_ans = int(input())
    real_ans = num1*num2
    while user_ans != real_ans:
        user_ans=int(input("WRONG! :(, Try again "))
    else:
        print("Correct :)")

#sistema para ver que elevador es el más cercano

"""
situacion: en un edificio hay 3 elevadores y queremos saber cual elevador es el
mas recomendable que pase al piso de alguien que lo esta pidiendo, esto se va a
decidir depende de en que piso esten los elevadores, cual es el mas cercano, si
esta subiendo o bajando, todo esto para hacer la ruta de elevadores mas eficient
"""

#definicion de variables:
#hacer en un futuro
