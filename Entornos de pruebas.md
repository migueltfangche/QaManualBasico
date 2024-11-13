# ¿ Que es un entorno de pruebas ?

Sitio Principal ->  Replica sitio Principal
      ^                       v
Modificacion            Modificación
Sitio                       Sitio
Principal        <-        Replica

* Tipos de entorno de pruebas

    1.- Entorno de desarrollo ( Develop Environment ):
        Es donde los desarrolladores escriben y prueban el codigo.

    2.- Entorno de pruebas ( Testing Environment ): 
        Es una copia del entorno de producción

    3.- Entorno de Staging ( Staging Environment ): Es una copia exacta del entorno de producción

    4.- Entorno de producción ( Production Environment )

* Pasos para configurar el entorno de pruebas
    1.- Planificación
        - Identificar los requisitos de softwre
        - Determinar que aspectos del software se probarán    

    2.- Configurar software y hardware
        - Configurar servidores y redes similares a las del entorno de producción
        - Instalar software necesario, incluidas las herramientas de prueba y las aplicaciones que se encuentran probandose en el momento.  
    
    3.- Creación de datos de prueba    
        - Se debe tener cuidado con los datos de los clientes.

* Ejecución de pruebas en el entorno de pruebas

        - Ejecución de pruebas
        - Registro y seguimiento
        - Optimización y Retesting
        - Aprobación para despliegue