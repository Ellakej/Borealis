# Borealis <img src="https://github.com/Ellakej/8store/blob/master/assets/8code/8codelogo.png" alt="logo" width="50" align="right"/>

Rover explorador autónomo multiproposito y multientorno.

Para informacion detallada del desarrollo del Rover, por favor revisa la [Wiki](https://github.com/Ellakej/Rover_Explorer/wiki), ubicada en la pestaña del mismo nombre de este repositorio. 

## Changelog y fallas detectadas:

### V1. Rover_Finder 
* Con un modulo de motores se usaron pilas como fuente de energia, hubo un fallo que quemo un par de cables pero nada grave y reparable
* Se uso finalmente un Arduino Uno con un script para mover los motores por PWM usando [WASD] para el movimiento y [i, k] para el control de velocidad (i aumenta, k reduce)
* Se desarrollo una GUI en python con curses para su uso en terminal, pero debido a la complejidad y poco uso real, se descarto a ultima hora, para pensar en una portabilidad a web y/o app con el framework Flutter
* El unico modo de operabilidad fue hacer una conexion SSH desde la PC escaneando los puertos de las IP conectadas a wifi mediante wireshark y dentro controlar un script para la captura de las teclas
* El script de python no funciono como deberia ya que hay una incompatibilidad con el ciclo realizado contra los datos que recibe Arduino, provocando una desconexion continua y dejando al rover avanzando infinitamente
* Se intento usar un arduino nano, pero este no era original, usaba un controlador CH34x, existente en el kernel de la raspberry pi, pero debido a que el puerto serie solo funciona por ACMx y el CH34x solo recibia datos por USBx, este problema no permitio continuar, la unica opcion que se nos ocurrio fue desarrollar un controlador, pero debido a falta de experiencia y tiempo se descarto su desarrollo

### V2. Rover_Explorer (Cambio de nombre a Rover_Explorer, debido a su poder multiproposito)
* Reanalisis del proyecto
* Cambio de nombre
* Estandarizacion con Wifi y Bluetooth
* Creacion del Punto de Acceso

### V2.1 Borealis (Cambio de nombre por sucesion espiritual del Proyecto Aurora y por practicidad de memorizacion)
* En Progreso

## Lluvia de ideas para el desarrollo
* Uso de un socket para intercambio de datos inmediato entre la raspberry pi y la PC
* Desarrollo de una app y/o web en Flutter para el control multiplataforma del rover
* Fabricacion de placa para el rover, reduciendo asi la posibilidad de accidente por cables
* Desarrollo de cubierta para mejor diseño
* Cambio del script de python removiendo curses y enviando datos usando echo para resolver el problema de sincronizacion con Arduino
* Uso de un arduino nano original para reduccion de espacio
* Cambio a baterias LiPo como fuente de energia
* Uso de Panel solar para recargar la bateria LiPo
* Propuesta para hibridizar el rover al agregarle propelas desplegables y que pueda volar para alcanzar otras superficies
* Incluir el uso de AR para que el usuario pueda visualizar datos de una manera mas sencilla desde su pantalla y/o agregar mas herramientas y funciones al rover
* Uso de procesador portatil neural Movidius para agilizar el reconocimiento de objetos y desde la raspberry pi realizar la tarea
* Creacion de un punto de acceso en el propio Raspberry Pi para evitar uso de puntos de acceso extras que entorpescan la comunicacion
* Compatibilidad con multiples controles Bluetooth (Wiimote, prueba piloto, usando Bluetooth HID y drivers especificos)
* Pantalla de estado conectado al Rover (es requerido un controlador AV)

