
## Diseño del proyecto 
Analizador Climático – ClimaPy

ClimaPy es una aplicación desarrollada en Python que permite consultar y analizar información meteorológica de cualquier ciudad, especificando también su país,. Obtiene datos climáticos en tiempo 
real de una fuente confiable en Internet"clima" para que los usuarios puedan ver la temperatura, la velocidad del viento y otros aspectos del clima.


En que se diferencia:
Crea un historial de datos de diferentes ciudades.
Genera graficos para su facil comprension.

Hacer el diseño del proyecto
Breve documentación no técnica
Diagrama de flujo
Objetivos que se quieren conseguir
Estructura del proyecto, con la funcionalidad principal comenzada

## Objetivos que se quieren conseguir

El usuario tendrá que introducir los datos mediante la consola, introduciendo el país y la ciudad,

una vez soliticato estos datos, se obtendrá la latitud y  la longitud mediatne una llamada  a una primera api,

después de esto llamaremos a una segunda api, pasándole la latitud y la longitud que hemos obtenido, que son las coordenadas de un país, mediante
estas coordenadas podremos obtener información del timpo climático  de un país y una ciudad en tiempo real,



Después, todo lo que nos devuelva esa api, con los datos que nos han llegado, <<Explicación en la Estrutura del proyecto y la funcionalidad principal>>, se almacenarán
en un excel, que actuará como una base de datos con las siguientes columnas: ,




Contaremos con un menú principal con 10 opciones,  en caso de la primera y segunda opción que son opciones  para introducir  
y eliminar registros climáticos respectivamente, en una base de datos, en nuestro caso será Excel, 


El resto de las opciones excepto la número 10, funcionan con Pandas, que son para filtrar los datos  que el usuario desea obtener,



Una vez obtenidos estos datos, se guardarán y se utilizarán en su uso, para la construcción de gráficos para comparar y analizar
los distintos cambios climáticos en distintas ciudades y países del mundo



Para ello usaremos la librería Plotty

 
## Estrucutra del proyecto y funcionalidad principal

Las funciones principales de la aplicación es proporcionar al usuario información sobre el clima en tiempo real de un país y de una ciudad que se van a especificar  a traves de una interfaz gráfica,en las que este 
puede consultar el tiempo en grados Celsius Cº, la altitud, la velocidad del viento,  la dirección del viento( norte, sur, este, oeste, suroeste, noroeste), el estado en el que se encuentra(Si está  nublado, despejado, está lloviendo, o si está soleado), poder consultar la temperatura máxima, y la máxima velocidad del viento 


Se contará con tres Clases:


La primerra clase llamada Main:  es la encargada del funcionamiento principal de la aplicación, ya que si se introduce un dato  que se desea consultar en la aplicación,


La segunda clase llamada Apiclient:  es la encargada de hacer las llamadas a las correspondientes Apis


La tercera clase  llamada Analisis: sirve para filtrar los datos que el usuario desea obtener,


## Diagrama de flujo

A continuación se muestra un esquema visual de como quedaría la aplicación en cada llamada:
## 📊 Diagrama de Flujo

```
INICIO
   ↓
Mostrar mensaje de bienvenida
   ↓
Solicitar país y ciudad
   ↓
¿Datos válidos?
   ↓           ↓
  NO           SÍ
   ↓           ↓
Mostrar error  Conectar con API
               ↓
        ¿Respuesta correcta?
               ↓         ↓
              NO         SÍ
               ↓          ↓
        Mostrar error   Procesar datos
                          ↓
                    Mostrar información
                          ↓
                   Guardar en historial
                          ↓
                   Generar gráfico
                          ↓
                         FIN
```






