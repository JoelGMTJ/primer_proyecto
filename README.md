# Primer proyecto de la materia Pensamiento computacional para ingeniería TC1028

Mi proyecto para la materia es el de varias opciones las cuales están orientadas para estudiantes que visitan frecuentemente el 
campus de la universidad. Aquí incluyo varias funciones que ayudan a un gran grupo de personas. Primero esta la opción de establecer
la temperatura de un edificio. Esta función la integré pues dentro de residencias tec considero que puede ser una opción para 
implementar. La situación es que todo el edificio solamente puede estar a una misma temperatura, por lo que va a realizar
una votación de cada habitante en donde cada persona vote por la temperatura deseada (en el programa simule a el resto de 
residentes como números random) y después tu vas a votar a que temperatura quieres que esté tu cuarto y un área común.

Otra función que implementé es la de conocer cuanto te va costar el estacionamiento en el tec debido a la green fee, y si
es más recomendable que lo pages todo de un solo pago. Otra función es la de que contestes una pregunta de matemáticas aleatoria.
Función que es algo para divertirte y mantenerte ocupado un momennto. La última función es la de el calendario, aqui te deja crear
una agenda para todas tus clases que tengas a lo largo de una semana, te ayuda revisando que no haya ninguna clase que se sobreponga
con otra, y guarda la agenda a lo largo de todo el proyecto

## Funciones externas

Importe la librería random. Librería que me ayudó a generar números aleatorios para simular las votaciones de temperatura de 
otros cuartos, y también para generar 2 números aleatorios para la pregunta matemática.
Investigado de la librería de python en https://docs.python.org/3/library/random.html#random.randint sección random.randint(a,b)

Finalmente, también use la funcion de is.digit(), la cual me dice si un valor es un dígito o no, la use para asegurarme que en algunos
casos donde pregunto por una opción, se asegure que me devuelva un valor numérico y no una letra o caracter especial
Investigado de Programiz en https://programiz.com/python-programming/methods/string/isdigit sección principal

## Comentarios de cada una de la sección

### Comentarios generales

En el programa trate de separar lo más posible en funciones para su facilidad de lectura, el programa debido a ser una combinación de 
varias funciones, requiere varias funciones, varios selectores. 

#### Seccion de temperatura

Esta sección se imagina a un edificio que solamente puede tener una temperatura igual para todos, por lo que para que sea justo, se
va a hacer una votación para ver cual será. Aquí hay 10 habitaciones y 2 áreas comunes, el usuario va a poder votar por la temperatura
de su cuarto y de un área común. En total, la ponderación de los cuartos es del 70% y las de las áreas comunes es de 30%.
En un programa real se pediría a otros 10 diferentes usuarios que ingresen la temperatura deseada, pero en mi caso simulo
sus posibles decisiones con la funcion random.randint() para generar un valor dentro de un rango aceptable de temperatura

### Sección de pago de green fee

Esta sección está orientada específicamente a estudiantes del Tec de Monterrey Campus Qro. Aquí tenemos que pagar ua green fee si
estacionamos nuestro auto dentro del tec, aquí el programa va a preguntar si entras en una de las excepciones de las personas
que no pagan la green fee, y luego calcula cuanto dinero te va a costar por semestre y te va a recomendar si es mejor pagarlo día por día
o si es más recomendable pagar todo junto por semestre

### Sección de pregunta matemática

Esta sección te va a hacer una pregunta de 2 números aleatorios multiplicados. Va a comprobar que tengas el resultado correcto y 
si lo tienes mal, te va a dar una pista de si el número es mayor o menor

### Sección de creacion de calendario

Sin duda la sección más compleja de todas, aquí vas a poder crear tu calendario de tus clases para la escuela o cualquier otro uso.
Aquí vas a seleccionar en qué dia quieres agregar un evento, su nombre, a que hora comienza y a que hora termina. Va a revisar varias 
cosas como que los valores numéricos sean dentro del rango especificado, que el evento no pueda comenzar antes de que termine, que
la duración del evento no se interponga con otro evento agregado previamente, te transforma las horas de un valor float a un 
formato de 12 horas y te imprime unamatriz con tu horario.
También te permite borrar la agenda por si quieres comenzar de nuevo.
La función tiene algunas limitaciones como el de solamente escribir números enteros o medias horas. Pero en general es una función
completa que trata de evitar cualquier caso que generaría error.
