"""
AutomatizaTec
Proyecto hecho por Joel Guadalupe Garcia Guzman
Programa que tiene varias funciones diseñadas
para estudiantes de universidad
"""

#bug revisar todo una ultima vez

#Importamos las librerías
import random

#----------Seccion 0, funciones auxiliares----------
def validar_opcion (valor_min,valor_max):
    """funcion que revisa que un valor este dentro del rango aceptable
recibe valor maximo y valor minimo, comprueba que sea un valor numerico
y que este dentro del rango especificado"""

    revision_completada =  False
    while revision_completada == False:
        opcion = input("Que opcion deseas usar? ")
        while not opcion.isdigit():
            opcion = input("Valor no numerico detectado, ingrese un valor valido ")
        opcion = int(opcion)
        if opcion<=valor_max and opcion>=valor_min:
            revision_completada = True
        else:
            print ("Opcion no valida")
    return opcion


def seleccionador ():
    """no recibe nada, regresa el indice de la opcion que se va a usar, valida
que sea un numero dentro del rango especificado y regresa la opcion principal"""

    print("")
    print("1 para ver la temperatura de tu edificio")
    print("2 para ver cuanto te va a costar el estacionamiento")
    print("3 para una pregunta rapida sobre matematicas")
    print("4 para crear tu calendario")
    print("5 si quieres salir del programa")
    print("")
    opcion_principal = validar_opcion(1,5)
    return opcion_principal



#----------Seccion 1, votacion de la temperatura----------
def opcion_temperatura():
    """opcion 1, funcion de establecer la temperatura de un edificio,
te va a pedir la temperatura de tu cuarto, la de un area comun, y regresa
el promedio segun los valores dados"""

    print("""
Aqui vas a decidir la temperatura de tu cuarto y la de la cocina sin embargo,
como las demas personas tambien votan por su temperatura, es muy probable que
la temperatura sea algo diferente
""")
    usr_temp = int(input(
"A que temperatura desearias que este tu cuarto? "))
    cuartos_final = promedio_cuartos(temp_otros_cuartos(),usr_temp)
    area_comun = int(input(
"A que temperatura desearias que este el area comun? "))
    areas_comun_final = promedio_comun (area_comun)
    temp_del_edificio = areas_comun_final + cuartos_final
    print (
"La temperatura del edificio ahora es:","%.1f" % temp_del_edificio,"°C")
    print()


def temp_otros_cuartos ():
    """Crea una lista con 9 elementos aleatorios
No recibe nada, regresa una lista con 9 valores random entre 14 y 34"""

    temp_vecinos = []
    i=0
    while i<9:
        temp_vecinos.append(random.randint(14,34))
        i = i+1
    return temp_vecinos


def promedio_cuartos (lista,usr_temp):
    """recibe una lista + un valor, les saca el promedio, los multiplica
por 70%, regresa el valor del promedio"""

    sum=0
    for i in lista:
        sum=sum+i
    sum=sum+usr_temp
    avg=sum/(len(lista)+1)
    avg=avg*0.7
    return avg


def promedio_comun(area_c):
    """recibe el valor de un area comun, lo suma con un valor random,
obtiene su promedio, y los multiplica por 30%"""

    cocina = random.randint(20,40)
    sum=cocina+area_c
    avg=sum/2
    avg=avg*0.3
    return avg



#----------Seccion 2, costo del estacionamiento----------
def opcion_green_fee():
    """funcion de opcion 2, pregunta por si eres eligible para no pagar la
green fee, en caso de no serlo, calcula el costo que te costaria la fee y te
recomienda si es mejor pagar dia con dia o todo junto"""

    print ("""
Aqui vas a descubrir cuanto dinero vas a pagar por el estacionamiento en
el tec, esto a causa de la green fee, primero unas preguntas,
responde 'S' si es tu caso
""")
    electrico = str(input("Tienes coche electrico o hibrido? "))
    if caso_especial(electrico):
        print ("Tu costo va a ser $0 por tener un auto electrico o hibrido")
        return
    carpool = str(input("Haces carpool (compartes carro con 3 o mas personas)? "))
    if caso_especial(carpool):
        print ("Tu costo va a ser $0 por hacer carpool")
        return
    residencias = str(input("Vives en residencias tec? "))
    if caso_especial(residencias):
        print ("Tu costo va a ser $0 por vivir en residencias")
        return
    else:
        print ("Cuantos dias vienes al tec por semana? ")
        d_por_semana = validar_opcion(1,7)
        costo_semestre = costo_estacionamiento (d_por_semana)
        print ("Te va a costar",costo_semestre, "pesos por semestre")
        print ("El costo del semestre como pago completo es de $1900")
        if costo_semestre > 1900:
            print (
"Es mas recomendable pagar el estacionamiento semestral")
        else:
            print (
"Es mas recomendable pagar el estacionamiento dia con dia")
    print()


def costo_estacionamiento (d_por_semana):
    """recibe un numero, lo multiplica por 18 (semanas) y 50 (pesos por dia)"""

    dias_por_semestre = d_por_semana*18
    costo_individual = dias_por_semestre*50
    return costo_individual


def caso_especial(excepcion):
    """funcion que recibe un string, valida si es la letra 's' y regresa
True en caso de serlo"""

    if excepcion == "s" or excepcion == "S":
        return True



#----------Seccion 3, pregunta matematica----------
def opcion_preg_mate():
    """funcion que te pregunta la multiplicacion de 2 numeros aleatorios
te pide la respuesta, revisa si es la correcta, en caso de no serlo,
te vuelve a preguntar hasta que estes en lo correcto"""

    num1, num2 = random.randint(-15,20), random.randint(-50,50)
    print ("Cuanto es", num1, "por", num2, "? ")
    user_ans = int(input())
    real_ans = num1*num2
    while user_ans != real_ans:
        if user_ans > real_ans:
            hint = str("pequeño")
        else:
            hint = str("grande")
        print ("Respuesta incorrecta")
        print ("Pista: el numero que estas buscando es un poco mas", hint)
        user_ans=int(input("Vuelve a intertarlo "))

    else:
        print("Correct :)")
    print()

#----------Seccion 4, creacion de un calendario----------
#listas iniciales para las agendas
agenda = [["lunes"],
["martes"],
["miercoles"],
["jueves"],
["viernes"],
["sabado"],
["domingo"]]
horas_ocupadas = [[],[],[],[],[],[],[]]


def calendario (num_d_dia,materia,inicia,termina):
    """funcion que recibe dia, materia, horas de inicio y fin. Revisa que el
horario no se sobreponga con otro, cambia el formato de float a formato 12h
agrega la materia
regresa la matriz de agenda con el evento agregado"""

    num_d_dia = num_d_dia-1
    overlapping = revisar_agenda(num_d_dia,inicia,termina)
    if overlapping:
        return agenda
    horas_ocupadas[num_d_dia].append(inicia)
    horas_ocupadas[num_d_dia].append(termina)
    hora_inicio = decimal_a_tiempo(inicia)
    hora_fin = decimal_a_tiempo(termina)
    if inicia == termina:
        bloque_de_cal = (materia + " ---> " + hora_inicio)
    else:
        bloque_de_cal = (materia + " ---> " + hora_inicio + "-" + hora_fin)
    agenda[num_d_dia].append(bloque_de_cal)
    print
    print ("Evento agregado con exito ")
    print (agenda[num_d_dia])
    return agenda


def revisar_agenda(num_d_dia,inicia,termina):
    """recibe un indice de lista para el dia; horas de inicio y fin,
revisa que las horsas no esten ocupadas y regresa true si estan sobrepuestas
o falso si el horario esta libre"""
    dia_ocupado = horas_ocupadas[num_d_dia]
    i = 0
    while i < len(dia_ocupado):
        if inicia > dia_ocupado[i] and inicia < dia_ocupado[i+1]:
            print ("Error: hora sobrepuesta sobre otra actividad")
            return True
        if termina > dia_ocupado[i] and termina < dia_ocupado[i+1]:
            print ("Error: hora sobrepuesta sobre otra actividad")
            return True
        i = i+2
    return False


def num_a_dia(num):
    """recibe un numero de dia, regresa el nombre del dia en string"""

    lis = ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
    return lis[num-1]


def decimal_a_tiempo(num):
    next_day = False
    """recibe un numero float, lo regresa en un formato de 12 horas en string"""
    if num == 0:
        num = 12
        tarde = False
    elif num <12:
        tarde = False
    elif num == 12:
        tarde = True
    elif num>12 and num!=24:
        num = num-12
        tarde = True
    elif num == 24:
        num = 12
        tarde = False
        next_day = True
    if num % 1 == 0:
        num = int(num)
        num = str(num)
        hora = str(num+":00")
    else:
        num = int(num)
        num = str(num)
        hora = str(num+":30")
    if tarde:
        hora = hora + "pm"
    else:
        hora = hora + "am"
        if next_day:
            hora = hora + "del dia siguiente "
    return hora


def hora_valida (hora):
    """recibe una hora y se asegura que este entre 0 y 24, de no ser el caso
vuelve a preguntar por una hora valida"""
    while hora > 24:
        hora = float(input("Hora mayor a 24, escribir una hora valida "))
    while hora < 0:
        hora = float(input("Hora menor a 0, escribir una hora valida "))
    #si el valor no es entero o 0.5, se vuelve a pedir que lo escriba
    while hora %0.5 != 0:
        hora = float(input("""
Este programa solo acepta horas cerradas o medias horas,
escribir una hora valida
"""))
    return hora


#-----sub-funciones del calendario-----
def calendario_instrucciones ():
    """no recibe nada ni regresa nada, solo imprime las instrucciones"""

    print ("""
Esta es la funcion de crear tu calendario.
Para seleccionar cualquier dia, escribe que numero de dia es
(Ejemplo: lunes = 1, miercoles = 3)
El calendario solo acepta horas enteras o medias horas en formato de 24h,
para ingresar una media hora, ingrese la hora con .5,
(Ejemplo: 1:30pm sería 13.5, 9:30pm seria 21.5)
""")
    return True


def calendario_agregar(agenda,horas_ocupadas):
    """funcion para agregar un evento al calendario,
aqui te pregunta que dia quieres editar, como se llama la materia que
vas a agregar, su horario, revisa que no se sobreponga a otro, regresa
la agenda con el evento agregado"""

    print()
    print ("Escribe el dia que quieras editar")
    print()
    num_d_dia = validar_opcion(1,7)
    dia = num_a_dia(num_d_dia)
    materia = str(input(
f"Que materia vas a agregar el dia {dia} "))
    hora_inicio = float(input(
f"A que hora comienza {materia}? "))
    hora_inicio = hora_valida(hora_inicio)
    hora_fin = float(input(f"A que hora termina {materia}? "))
    hora_fin = hora_valida(hora_fin)
    if hora_fin<hora_inicio:
        print()
        print(
"La clase termina antes de que comience, favor de corregir ")
        return agenda,horas_ocupadas
    agenda = calendario(num_d_dia,materia,hora_inicio,hora_fin)
    return agenda,horas_ocupadas


def calendario_borrar (agenda,horas_ocupadas):
    """recibe 2 listas, regresa 2 las 2 listas con su valor default"""

    confirmacion = input('Escribe "BORRAR" para confirmar ')
    #confirmacion extra para asegurarse que si lo va a borrar definitivamente
    if confirmacion == "BORRAR":
        agenda = [["lunes"],
        ["martes"],
        ["miercoles"],
        ["jueves"],
        ["viernes"],
        ["sabado"],
        ["domingo"]]
        horas_ocupadas = [[],[],[],[],[],[],[]]
        print ("Agenda borrada con exito")
    else:
        print("La agenda no ha sido borrada")
    return agenda,horas_ocupadas




#_____________________________________________________________
#--------------------COMIENZO DEL PROGRAMA--------------------
#_____________________________________________________________

print('''
Bienvenido a "AutomatizaTec", el programa que te ayudara a una variedad de
cosas de tu vida diaria en el campus, selecciona una opcion para continuar''')

opcion_principal = seleccionador ()

#ciclo while para que puedan ejecutar las funciones cuantas veces quieran
while opcion_principal !=5:

    if opcion_principal ==1:
        opcion_temperatura()

    elif opcion_principal == 2:
        opcion_green_fee ()

    elif opcion_principal==3:
        opcion_preg_mate ()


    elif opcion_principal ==4:
        """funcion del calendario, donde te pregunta que sub-opcion quieres
    hacer dentro del calendario"""

        cal_opcion = 4
        while cal_opcion != 5:
            if cal_opcion == 1:
                agenda,horas_ocupadas = calendario_agregar(agenda,horas_ocupadas)

            elif cal_opcion == 2:
                print ()
                for fila in agenda:
                    print(fila)
                print ()
            elif cal_opcion == 3:
                agenda,horas_ocupadas = calendario_borrar(agenda,horas_ocupadas)

            elif cal_opcion == 4:
                calendario_instrucciones()

            continuar = input("Presione enter para continuar")
            print ("""
Que funcion quieres realizar
1 para agregar un evento
2 para ver la agenda
3 para borrar la agenda (no se puede deshacer)
4 para volver a ver las instrucciones
5 para salir del calendario""")
            cal_opcion = validar_opcion(1,5)

    continuar = input("Presione enter para continuar")
    opcion_principal = seleccionador ()

print("""
Gracias por usar AutomatizaTec, hasta pronto
""")
