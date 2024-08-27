# Primer proyecto de la materia Pensamiento computacional para ingeniería TC1028

Mi proyecto para este primer semestre va a ser un sistema para calcular varias cosas dentro de un recinto con departamentos.
Un ejemplo que quiero implementar es el de como manejar de manera eficientes los elevadores. Programar un sistema el cual
nos ayude a transportar a el mayor número de personas posibles; por ejemplo, si un elevador está subiendo para el piso 6, 
y alguien del piso 5 lo pidió, ¿qué es más rápido? que el elevador del psio uno suba a recoger al del 6, o esperar a que el 
del 7 haga su recorrido y pase por l persona hasta la bajada. Ese tipo de preguntas se podrían solucionar de alguna forma más
eficiente y complicada la cual maximise las personas y trate de reducir el tiempo que les toque esperar a cad pasajero.

Otro problema el cual se resolvería en mi idea de un sistema para manejar todo el recinto, es el manejo de las rutas de los 
transportes, sobre como implementar un sistema basado en lecturas de cuantas personas hay esperando en cada parada para así
redirigir el camión para que, en conjunto, reducir el mayor tiempoo posible de espera.

Otra idea que podría implementar sería el sistema para controlar la temperatura del aire acondicionado en todo un edificio con
varias personas, siendo que solo pueda haber una temperatura para todo el edificio, buscando el promedio de temperatura deseada, 
considerando algunos votos con más peso como el de la cocina en general, etc.

## Beneficios de este proyecto

Considero que este proyecto, pueda que no tenga una probemática importante a solucionar, me parece que tiene bastantes ángulos
los cuales solucionar, se le pueden agregar varios aspectos de distintas áreas debido a que un recinto, tiene bastantes áreas 
las cuales se pueden implementar soluciones con código.

También tiene la ventaja que son soluciones muy variadas entre sí, por lo que es un proyecto que me dará bastante experiencia 
para manejar varias funcionalidades de el programa y a adaptarme a un ambiente donde te pueden pedir que hagas varias cosas en 
diferentes sectores

## Inspiraciones del proyecto

La idea de este proyecto surge de mi vida en las residencias del Tecnológico de Monterrey. El problema del elevador, aunque no
sea un problema, es algo en lo que me quedo pensando mientras espero a que pase por mí, la parte de las rutas de los camiones 
está completamente inspirado en los camiones eléctricos que pasan por todo el campus, considero que esta idea tiene varias 
ramas para poder implementar el mayor código posible, el cual también será variado.



### Ya implementado en el proyecto

**Votación de la temperatura para el edificio**
La forma que está implementado es que el programa te va a pedir a que temperatura tú quieres el cuarto, y tambien va a asumir 
que tu pones la temperatura ese día. Las votaciones de los demás cuartos se deciden aleatoriamente. Idealmente cada persona 
escribiría su temperatura ideal, pero en este momento hago que cada se decida aleatriamente en un rango de temperaturas reales.

### Sin implementar en el programa

**Inventario de bicicletas en diferentes estaciones**
Sistema que tiene la idea de que el programa le pida al usuario en que parada de bicis quiera revisar, después le escriba a 
donde quiere ir y cuantas personas van a ir. Esto con el objetivo de pre-planear las rutas para así ver si en x estación hay
suficientes bicicletas para todas las personas que vienen juntos. También se idea para que cuando alguien "reserve" las bicis
se actuaize la lista para que se descuenten las bicicletas que van a usar

**Predicción de elevador**
Sistema que toma en cuenta que hay 3 elevadores en un edificio, aquí, el usuario va a decir en que piso está y si desea subir
o bajar. Lo que hace el programa es revisar los 3 elevadores, observar el estado de cada uno, y comparar cual de ellos es el 
ideal para que sea ese el que se suba el usuario.

**Precio de el estacionamiento tec**
Función la cual sirve para darte un aproximado de cuanto te va a costar el estacionamiento del campus. Esto considerando cuantas
semanas vas a venir con el auto, si en tu semana hay dias en los que no vienes y tomando en cuenta los días festivos y que 
los fines de semana no vienes a la escuela. También te dice el precio total y si es recomendable que compres el pase semestral.
