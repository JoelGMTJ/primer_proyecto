
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
def promedio_cuartos (lista,usr_temp):
    sum=0
    for i in lista:
        sum=sum+i
#suma de todos los valores de cada cuarto junto con el del usuario
    sum=sum+usr_temp
    avg=sum/(len(lista)+1)
#lo multiplico por 0.7 pues el total de las temp de los usuarios vale 70%
    avg=avg*0.7
    return avg

#promedio de las areas comunes
def promedio_comun(area_c):
#genera los 2 valores de las areas comunes
    cocina = random.randint(20,40)
    sum=cocina+area_c
    avg=sum/2
#lo multiplica por 0.3 pues las areas comunes valen el 30% del valor total
    avg=avg*0.3
    return avg


#----------Seccion 2, costo del estacionamiento----------

#aqui es la funcion la que nos dice cuanto diero va a costar el estacionamiento
#si se paga dia por dia
def costo_estacionamiento (d_por_semana):
#se multiplica por 18 por que hay 18 semanas por semestre
    dias_por_semestre = d_por_semana*18
# se multiplica por 50 pues ese es el costo de un dia
    costo_individual = dias_por_semestre*50
    return costo_individual


#----------Seccion 4, creacion de un calendario----------

#defino las listas, la de agenda esta orientada al usuario mientras que la de
#horas_ocupadas es para revisar que no se sobrepongan los horarios
agenda = [["lunes"],["martes"],["miercoles"],["jueves"],["viernes"],["sabado"],["domingo"]]
horas_ocupadas = [[],[],[],[],[],[],[]]


#funcion principal, explicada paso por paso dentro de la funcion
def calendario (num_d_dia,materia,inicia,termina):
    #cambia el numero dado por el usuario (comienza en 1) a un indice de
    #listas (comienza en 0)
    num_d_dia = num_d_dia-1
    #usa la funcion para revisar que el nuevo evento no se sobreponga con otro
    overlapping = revisar_agenda(num_d_dia,inicia,termina)
    #en el caso que si se sobreponga, regresa un error y la lista sin editar
    if overlapping:
        return agenda
    #ya que se valido que las horas no se sobreponen, se agregan a la listas
    #de horas ocupadas orientado al sistema
    horas_ocupadas[num_d_dia].append(inicia)
    horas_ocupadas[num_d_dia].append(termina)
    #se convierten los numeros float a un formato de hora que es mas amigable
    #con el usuario
    hora_inicio = decimal_a_tiempo(inicia)
    hora_fin = decimal_a_tiempo(termina)
    #este if es para revisar por si es un evento que no tiene duracion (como una
    #especie de recordatorio) y hace que solamente se escriba una hora
    if inicia == termina:
        bloque_de_cal = (materia + " ---> " + hora_inicio)
    else:
        #agrega la materia con el horario formato hora a la lista orientada al usr
        bloque_de_cal = (materia + " ---> " + hora_inicio + "-" + hora_fin)
    agenda[num_d_dia].append(bloque_de_cal)
    print ()
    #feedback al usuario para que se asegure que si se agrego el evento
    print ("Evento agregado con exito ")
    print (agenda[num_d_dia])
    return agenda

#funcion que revisa la lista orientada a sistema para ver que el nuevo evento
#no coincida con otro ya establecido
def revisar_agenda(num_d_dia,inicia,termina):
    #nos da solamente el dia que vamos a editar
    dia_ocupado = horas_ocupadas[num_d_dia]
    i = 0
    while i < len(dia_ocupado):
        if inicia > dia_ocupado[i] and inicia < dia_ocupado[i+1]:
            print ("Error: hora sobrepuesta sobre otra actividad")
            return True
        if termina > dia_ocupado[i] and termina < dia_ocupado[i+1]:
            print ("Error: hora sobrepuesta sobre otra actividad")
            return True
        #se suma de 2 en 2 para que nos aseguremos que se vayan revisando por
        #pares de horas, pues asi han sido agregadas a la lista horas_ocupadas
        i = i+2
    return False

#funcion que transforma el numero de dia seleccionado a su nombre, solamente
#para funciones esteticas
def num_a_dia(num):
    lis = ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
    return lis[num-1]

#funcion que transforma un numero XX.X a un formato de hora mas
def decimal_a_tiempo(num):
    next_day = False
    #los siguientes 5 if's son para los 5 casos de horas, para que se vuelvan al
    #formato mas amigable de 12h. tambien considera si es las 24 horas y
    #especifica que se va a acabar a las 12am del dia siguiente
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
    #estos 2 ifs son solamente para convertir un numero de float a string
    #esto lo hace revisando si es hora entera o media hora
    if num % 1 == 0:
        num = int(num)
        num = str(num)
        hora = str(num+":00")
    else:
        num = int(num)
        num = str(num)
        hora = str(num+":30")
    #dependiendo si son tarde o no, se les agrega su respectivo am o pm
    if tarde:
        hora = hora + "pm"
    else:
        hora = hora + "am"
        if next_day:
            hora = hora + "del dia siguiente "
    return hora

#valida que la hora dada sea solamente entre o y 24, las horas del dia
def hora_valida (hora):
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

#solo sirve para volver a ver las instrucciones y especificaciones del calendario
def instrucciones ():
    print ("""
Esta es la funcion de crear tu calendario.
Para seleccionar cualquier dia, escribe que numero de dia es
(Ejemplo: lunes = 1, miercoles = 3)
El calendario solo acepta horas enteras o medias horas en formato de 24h,
para ingresar una media hora, ingrese la hora con .5,
(Ejemplo: 1:30pm sería 13.5, 9:30pm seria 21.5)
""")
    return True

"""
Aqui va la parte para decidir que parte de el programa vas a querer usar,
voy a usar la estructura de ifs para esto. Tambien va a servir como una
"pantalla de inicio"
"""

print('''
Bienvenido a "AutomatizaTec", el programa que te ayudara a una variedad de cosas
de tu vida diaria en el campus, selecciona una opcion para continuar''')


#Funcion para que sepan como acceder a cada fucion del programa
def seleccionador ():
    print("")
    print("Para ver la temperatura de tu edificio, 1")
    print("Para ver cuanto te va a costar el estacionamiento, 2")
    print("Para una pregunta rapida sobre matematicas, 3")
    print("Para crear tu calendario, 4")
    print("Si quieres salir del programa, 5")
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

#ciclo while para que puedan ejecutar las funciones cuantas veces quieran
while opcion_principal !=5:
    if opcion_principal ==1:
        print("""
Aqui vas a decidir la temperatura de tu cuarto y la de la cocina sin embargo,
como las demas personas tambien votan por su temperatura, es muy probable que
la temperatura sea algo diferente
""")

        usr_temp = int(input(
"A que temperatura desearias que este tu cuarto? "))

        cuartos_final = promedio_cuartos(temp_otros_cuartos(),usr_temp)
#Aqui se manda a crear la lista de los otros 9 cuartos y se saca el promedio
#ya considerando el escrito por el usuario

        area_comun = int(input(
"A que temperatura desearias que este el area comun? "))
        areas_comun_final = promedio_comun (area_comun)

        temp_del_edificio = areas_comun_final + cuartos_final

        print (
"La temperatura del edificio ahora es:","%.1f" % temp_del_edificio,"°C")
        print()
        continuar = input("Presione enter para continuar")

    if opcion_principal == 2:

        """
        programa que te dice cuanto dinero vas a pagar por el estacionamiento a
        partir de cierta fecha, esto debido a la gree fee del tec
        """

        print ("""
Aqui vas a descubrir cuanto dinero vas a pagar por el estacionamiento \
en el tec, esto a causa de la green fee, primero unas preguntas, \
responde 'S' si es verdadero y 'N' si no lo es
""")
        electrico = str(input("Tienes coche electrico o hibrido? "))
        carpool = str(input(
"Haces carpool (compartes carro con 3 o mas personas)? "))
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
                    print (
"Es mas recomendable pagar el estacionamiento semestral")
                else:
                    print (
"Es mas recomendable pagar el estacionamiento dia con dia")
        print()
        continuar = input("Presione enter para continuar")

    if opcion_principal==3:
#Pregunta rapida del dia de matematicas
        num1, num2 = random.randint(-15,20), random.randint(-50,50)
        print ("Cuanto es", num1, "por", num2, "? ")
        user_ans = int(input())
        real_ans = num1*num2
        while user_ans != real_ans:
            if user_ans > real_ans:
                hint = str("pequeño")
            else:
                hint = str("grande")
            print (" *EXTREMELY LOUD INCORRECT BUZZER SOUND EFFECT* WRONG!!!!")
            print ("Pista: el numero que estas buscando es un poco mas", hint)
            user_ans=int(input("Vuelve a intertarlo "))

        else:
            print("Correct :)")

        print()
        continuar = input("Presione enter para continuar")

    if opcion_principal ==4:

        #hago que la opcion del calendario sea 4 primero para que inmediatamente
        #me imprima las reglas
        cal_opcion = 4

        while cal_opcion != 5:
            #la primera opcion agrega un evento al calendario
            if cal_opcion == 1:
                print ()
                num_d_dia = int(input("Que dia quieres editar? "))
                #revisa que sea un dia de la semana valido
                while num_d_dia > 7 or num_d_dia < 1:
                    print ("Ingrese un valor valido porfavor")
                    num_d_dia = int(input("Que dia quieres editar? "))
                #crea la palabra de dia segun su numero
                dia = num_a_dia(num_d_dia)
                materia = str(input(f"Que materia vas a agregar el dia {dia} "))
                #pregunta por las horas de inicio/fin y valida que sean correctas
                hora_inicio = float(input(f"A que hora comienza {materia}? "))
                hora_inicio = hora_valida(hora_inicio)
                hora_fin = float(input(f"A que hora termina {materia}? "))
                hora_fin = hora_valida(hora_fin)
                #si el evento termina antes de comanzar, se regresa al inicio
                #para que pueda volver a escribir el evento
                #esto lo hago por que un error comun va a ser no leer las
                #instrucciones o simplemente olvidar que el formato es de 24h
                #y cometer un error. (me paso varias veces querer escribir
                # la 1pm como 1 envez de 13)
                if hora_fin<hora_inicio:
                    print()
                    print(
"La clase termina antes de que comience, favor de corregir ")
                    continue
                #corre la funcion principal
                agenda = calendario(num_d_dia,materia,hora_inicio,hora_fin)
            #esta opcion es para revisar el calendario completo
            elif cal_opcion == 2:
                print ()
                for fila in agenda:
                    print(fila)
                print ()
            #regresa el calendario a su estado original con una confirmacion
            #extra pues es un borrado definitivo
            elif cal_opcion == 3:
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
            #imprime las instrucciones
            elif cal_opcion == 4:
                instrucciones()
            else:
                print ("Opcion no valida")
            continuar = input("Presione enter para continuar")
            print ("""
Que funcion quieres realizar
para agregar un evento, 1
para ver la agenda, 2
para borrar la agenda (no se puede deshacer), 3
para volver a ver las instrucciones, 4
para salir del calendario, 5""")
            cal_opcion = int(input())


    opcion_principal = seleccionador ()

print("""
Gracias por usar AutomatizaTec, hasta pronto
""")
