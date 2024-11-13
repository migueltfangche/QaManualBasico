#   Tecnicas de prueba de software
- Las técnica de prueba de software ayudan a diseñoar mejores casos de prueba. Dado que no es posible realizar pruebas exhaustivas. Es decir NO escribir la maxima cantidad de casos de prueba, sino solamente los casos de prueba apropiados para testear determinada funcionalidad, o la minima cantidad posible.


* Analisis de valor limite ( Boundary )

- Se basa en pruebas entre los limites, entre particiones, incluyen limites maximos, minimos, anteriores y exteriores, valores tipicos y valores de error.
Ej, caja de texto a donde ingresar valores.
- Condición de entrada 1 - 10 
Pruebas:
Deberiamos ingresar 0, 1, 2 y 9, 10 y 11 

De esta manera nos aseguramos que la condicion de entrada se esta cumpliendo

# Partición de clases de equivalencia

- Permite dividir un conjunto de condiciones de prueba en una partición, osea que divide el dominio de dato de entrada en clase de datos y a partir de los cuales se deben diseñar los casos de prueba.

Ej, 
- Condicion de entrada 1 a 10 y 20 a 30
Pruebas:
----- a 0 (Deberia dar no valido)
1 a 10 (Deberia dar valido)
11 a 19 (Deberia dar  no valido)
20 a 30 (Deberia dar  valido)
31 a ----- (Deberia dar no valido)

Seleccionar algunos valores : -2 , 3 , 15 , 25 , 45

# Pruebas basadas en tablas de desiciones

- Condicion de entrada
Tipo de usuario (Estudiante, profesor, miembro público)
Tipo de libro (ficcion, no ficcion, referencia)
Estado del libro (Disponible, no disponible)

Tipo de Usuario	Tipo de Libro	        Estado del Libro	Acción Esperada
Estudiante	    Ficción	                Disponible	        Permitir Préstamo
Estudiante	    Ficción	                Prestado	        Denegar Préstamo
Estudiante	    No Ficción	            Disponible	        Permitir Préstamo
Estudiante	    No Ficción	            Prestado	        Denegar Préstamo
Estudiante	    Referencia	            Disponible	        Denegar Préstamo
Profesor	    Ficción	                Disponible	        Permitir Préstamo
Profesor	    Ficción	                Prestado	        Denegar Préstamo
Profesor	    No Ficción	            Disponible	        Permitir Préstamo
Profesor	    No Ficción	            Prestado	        Denegar Préstamo
Profesor	    Referencia	            Disponible	        Permitir Préstamo
Miembro Público	Ficción	                Disponible	        Permitir Préstamo
Miembro Público	Ficción	                Prestado	        Denegar Préstamo
Miembro Público	No Ficción	            Disponible	        Permitir Préstamo
Miembro Público	No Ficción	            Prestado	        Denegar Préstamo
Miembro Público	Referencia	            Disponible	        Denegar Préstamo

# Transición de estado

- Cuando los cambios en las condiciones de entrada cambian el estado de la aplicación 

Inicio de sesión:
Estado Inicial ( Estado: desconectada )
Transición de estado - Intento de inicio de sesión exitoso ( Estado: Conectado )
Transición de estado - Intento de inicio de sesión fallido 
Transición de estado - Cuenta bloqueada

# Error al adivinar

- Se basa en la experiencia de los analistas y se basa en adivinar donde podría estar el error. 
