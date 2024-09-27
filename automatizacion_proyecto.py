
import random

"""
------Notas generales------
cada print vacio y "presione enter para continuar" es para darle un poco de
orden y mejor aspecto al programa
"""

"""
Aqui definimos todas las funciones, arriba de cada funcion dice de que apartado
es y la explica brevemente
"""

#----------Seccion 1, votacion de la temperatura----------

#Crea una lista con 9 elementos aleatorios
def temp_otros_cuartos ():
    temp_vecinos = []
    i=0
    while i<9:
        temp_vecinos.append(random.randint(14,34))
        i = i+1
    return temp_vecinos

#Saca el promedio de la lista ya hecha y de la escrita por el usuario.
#La multiplica por 0.7 pues quiero que el valor de los cuartos solamente valga
#por el 70% y el otro 30% de las areas comunes
def promedio_cuartos (lista,usr_temp):
    avg=0
    for i in lista:
        avg=avg+i
    avg=avg+usr_temp
    avg=avg/(len(lista)+1)
    avg=avg*0.7
    return avg

#Aqui se toma el valor escrito por el usuario y se crea la temperatura de la
#cocina. Luego se multiplica por .3 para darnos el 30% faltante
def promedio_comun(area_c):
    cocina = random.randint(20,40)
    sum=cocina+area_c
    avg=sum/2
    avg=avg*0.3
    return avg


#----------Seccion 2, costo del estacionamiento----------

#aqui es la funcion la que nos dice cuanto diero va a costar el estacionamiento
#si se paga dia por dia
def costo_estacionamiento (d_por_semana):
    dias_por_semestre = d_por_semana*18
    costo_individual = dias_por_semestre*50
    return costo_individual

"""
Aqui va la parte para decidir que parte de el programa vas a querer usar,
voy a usar la estructura de ifs para esto. Tambien va a servir como una
"pantalla de inicio"
"""

print()
print('Bienvenido a "AutomatizaTec", el programa que te ayudara a una variedad\
 de cosas de tu vida diaria en el campus, selecciona una opcion para continuar')

def seleccionador ():
    print("")
    print("Para ver la temperatura de tu edificio, 1")
    print("Para ver cuanto te va a costar el estacionamiento, 2")
    print("Para una pregunta rapida sobre matematicas, 3")
    print("Si quieres salir del programa, 4")
    print("")
    opcion_principal = int(input("Que opcion deseas usar? "))
    return opcion_principal

"""
La situacion es un edificio con 10 cuartos, 1 area comun, y una cocina comun
la idea es que para decidir a que temperatura se va a poner el edificio, cada
persona va a poder votar por su temperatura deseada, pero como en la cocina
y en el area comun hay mas personas, esos votos van a tener mayor importancia
"""

opcion_principal = seleccionador ()

while opcion_principal !=4:
    if opcion_principal ==1:

        print ()
        print("Aqui vas a decidir la temperatura de tu cuarto y la de la cocina\
 sin embargo, como las demas personas tambien votan por su temperatura \
,es muy probable que la temperatura sea algo diferente")
        print()

        usr_temp = int(input("A que temperatura desearias que este tu cuarto? "))

        cuartos_final = promedio_cuartos(temp_otros_cuartos(),usr_temp)
#Aqui se manda a crear la lista de los otros 9 cuartos y se saca el promedio
#ya considerando el escrito por el usuario

        area_comun = int(input("A que temperatura desearias que este el area comun? "))
        areas_comun_final = promedio_comun (area_comun)

        temp_del_edificio = areas_comun_final + cuartos_final

        print ("La temperatura del edificio ahora es:","%.1f" % temp_del_edificio,"°C")
        print()
        continuar = input("Presione enter para continuar")

    if opcion_principal == 2:

        """
        programa el cual te diga cuanto dinero vas a pagar por el estacionamiento a
        partir de cierta fecha, esto debido a la gree fee del tec
        """

        print ()
        print ("Aqui vas a descubrir cuanto dinero vas a pagar por el estaciona\
miento en el tec, esto a causa de la green fee, primero unas preguntas, respond\
e 'S' si es verdadero y 'N' si no lo es")
        print()
        electrico = str(input("Tienes coche electrico o hibrido? "))
        carpool = str(input("Haces carpool (compartes carro con 3 o mas personas)? "))
        residencias = str(input("Vives en residencias tec? "))

        #esto es para dar el caso que algunas de estas situaciones sean verdad no cobrar
        #Pues si alguno de estos fuera el caso, el tec no te cobra la green fee

        if electrico == "s" or carpool == "s" or residencias == "s":
            print ("Tu costo va a ser $0")
        else:
            d_por_semana = int(input("Cuantos dias tienes clase por semana? "))
            print ()
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
        print()
        continuar = input("Presione enter para continuar")


    if opcion_principal==3:
#Pregunta rapida del dia de matematicas
        num1, num2 = random.randint(-10,10), random.randint(-50,50)
        print ("Cuanto es", num1, "por", num2, "? ")
        user_ans = int(input())
        real_ans = num1*num2
        while user_ans != real_ans:
            if user_ans > real_ans:
                hint = str("pequeño")
            else:
                hint = str("grande")
            print ("WRONG!!! :(")
            print ("Pista: el numero que estas buscando es un poco mas", hint)
            user_ans=int(input("Try again "))

        else:
            print("Correct :)")

        print()
        continuar = input("Presione enter para continuar")

    opcion_principal = seleccionador ()

print()
print("Gracias por usar AutomatizaTec, hasta pronto")
print()
