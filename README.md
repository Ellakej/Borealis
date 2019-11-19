# Rover_Finder

Rover de exploración con el objetivo de encontrar un objeto en un área no conocida

## Introduccion

Se trata de un rover que tiene la tarea de encontrar 1 objeto en un area desconocida, implementando reconocimiento de objetos con inteligencia artificial decide si es el objeto o no, ademas de determinar por donde ir autonomamente, de esta manera se puede optar por usarlo manualmente o no.

La idea es usar una raspberry pi que mande los datos de la camara por un arreglo a una PC que tome este arreglo y lo pase por el modelo de reconocimiento de objetos, se ha hecho pruebas con 3 frameworks y el mas estable y/o compatible se determino como Darknet + YOLO (You Only Look Once), aunque tambien Tensorflow.js es una buena opcion para comenzar, aunque lamentablemente dependeria de internet para funcionar

## Materiales

### Para el funcionamiento de la Raspberry Pi
* [Raspberry Pi](https://www.raspberrypi.org/products/) (se uso el raspberry pi 1 model b porque era el unico con el que se contaba, pero deberia funcionar cualquiera)
* Cable micro USB (para la alimentacion del raspberry pi
* [Power Bank 20000 mah](https://www.amazon.com.mx/ADATA-Powerbank-AP20000D-Negro-20000/dp/B01MQH3LZQ/ref=asc_df_B01MQH3LZQ/?tag=gledskshopmx-20&linkCode=df0&hvadid=295434261084&hvpos=1o2&hvnetw=g&hvrand=9387375807151858672&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1010103&hvtargid=pla-326626302364&psc=1) (Seria mejor usar una pila y soldarlo a un cable usb por el tamaño)
* [Adaptador Usb Wifi Alfa Awus036h 5dbi Chipset 3070](https://articulo.mercadolibre.com.mx/MLM-554104389-adaptador-usb-wifi-alfa-awus036h-5dbi-chipset-3070-_JM?matt_tool=66041105&matt_word&gclid=CjwKCAiAh5_uBRA5EiwASW3IarN2ggarsCXDmuDBRuBcFo_mLwaloWPb_kRmo6VT-AdX7aAX41mLLxoCrMAQAvD_BwE&quantity=1)(De igual manera una antena wifi USB hubiera sido una mejor opcion, pero solo se contaba con esto)
* [Tarjeta microSD 64 GB](https://www.amazon.com.mx/Kingston-SDCS-64GB-Memoria-Clase/dp/B079GVC5B8/ref=sr_1_3?__mk_es_MX=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=microsd+64+gb&qid=1573428925&sr=8-3)
* [Punto de Acceso MiFi Verizon](https://www.ebay.com/i/254330977351?chn=ps&_ul=MX&dispctrl=1) (Se puede usar un punto de acceso desde el celular, pero como se contaba con esto se decidio usar)

### Hardware
* [Chasis y Oruga](https://articulo.mercadolibre.com.mx/MLM-677625346-chasis-tanque-robot-inteligente-con-orugas-de-aleacion-_JM?quantity=1#position=12&type=item&tracking_id=155d977e-a25a-4323-a8ff-f58f262ab9b4)
* [Modulo Puente H](https://articulo.mercadolibre.com.mx/MLM-598749309-modulo-puente-h-l298-motor-driver-arduino-raspberry-_JM?matt_tool=65873753&matt_word&gclid=CjwKCAiAh5_uBRA5EiwASW3IavpmI3be5RWneecMGmFAzkDXtg-L7HHHGSMOKlMkin2pTge4kUzNkxoCYYQQAvD_BwE&quantity=1)


* [Modulo Camara para Raspberry Pi](https://articulo.mercadolibre.com.mx/MLM-614192648-modulo-camara-para-raspberry-pi-5mpx-v13-1080p-_JM?matt_tool=65873753&matt_word&gclid=CjwKCAiAh5_uBRA5EiwASW3Iaue4MctQ4I00T3wE6B6P18gmAPQ59TWTjXNG3MxVG4DiQx7TYu4V9RoCFS8QAvD_BwE&quantity=1)
* Laptop o PC con antenta de red

## Desarrollo

### Flujo de Trabajo
Primero se necesita definir cuales seran los datos de entrada, el proceso y los datos de salida y comenzar a trabajar desde ahi. <br />
El dato principal de entrada es el objeto a buscar, este objeto se almacena como variable global que compara los objetos detectados por el modelo de inteligencia artificial, lo segundo es recibir datos de la camara; la camara de la raspy empezara a tomar capturas de lo que ve en un ciclo hasta que termine el proceso total (Encontrar el objeto), cada captura se rompera en un mapa de bits dentro de un arreglo, este arreglo se transmite a la PC por Wifi y en la PC se procesa con el modelo de inteligencia artificial para finalmente comparar los objetos de la imagen con el objeto a buscar, si lo encuentra entoces se detiene el programa de busqueda, si no, continua mandando ordenes de movimiento. <br />

<b> Bosquejo Rapido del funcionamiento</b>
![Bosquejo1](https://github.com/Ellakej/rover_finder/blob/master/assets/bosquejo1.png)

### Preparando Raspbian
Para comenzar se necesita instalar un sistema operativo en la Raspberry Pi, se opto por usar la version no grafica de Raspbian Buster, SO basado en Debian Buster. </br></br>
Se necesita descargar la imagen del SO [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) desde su pagina oficial.</br> Una vez descargado debe cargarse en una microSD o tarjeta SD para su booteo en la Raspberry Pi, para ello se empleo el software [BalenaEtcher](https://www.balena.io/etcher/)</br>
Con BalenaEtcher se selecciona la imagen .iso, la tarjeta microSD o SD y se inicia el proceso.
</br><b>NOTA: ASEGURATE DE NO TENER NADA EN LA TARJETA MICROSD O SD, YA QUE SE FORMATEARA CON ESTE PROCESO</b>
</br>Al finalizar el proceso, retira la SD y colocala en la Raspberry Pi.

### Configurando la Raspberry Pi
La primera vez necesitaras un teclado y mouse ademas de un monitor y cable HDMI y/o RCA (dependiendo del modelo de la Raspberry Pi) para configurarlo graficamente, despues de deshabilitara la interfaz grafica para ahorrar recursos y se creara una conexion SSH inalambrica para su control desde la PC o laptop </br>

Conecta la Raspberry Pi al monitor con el cable HDMI o RCA </br>
Conecta la Raspberry Pi a una fuente de alimentacion con el cable Micro USB </br>
Conecta el teclado y el Mouse a la Raspberry Pi mediante USB </br>
Espera a que inicie el sistema operativo y configura el idioma, pais, nombre de usuario, etc... </br></br>
__Escritorio__</br>
![escritorio](https://github.com/Ellakej/rover_finder/blob/master/assets/img1.png)

Una vez que la configuracion inicial este finalizada y te encuentres en el escritorio abre la configuracion de la raspberry pi y activa la conexion SSH en la pestaña Interfaces </br>
![ssh](https://github.com/Ellakej/rover_finder/blob/master/assets/img.png)

</br>Te pedira que reinicies, acepta y al reiniciar configura una tarjeta de red y conectala a una red WiFi (aqui es donde entra el punto de acceso).

</br> Ahora abre una sesion de terminal presionando __[Ctrl] + [Alt] + [F2]__, ingresa tu contraseña y despues revisa tu IP con el comando
```
hostname -I
```
Esa sera la IP necesaria para realizar una conexion remota.</br></br>
Falta deshabilitar el booteo con GUI para ahorrar recursos, para esto escribe
````
sudo raspi-config
````
Entraras a la Raspberry Pi Software Configuration Tool, ahi selecciona <b>Boot Options</b> </br>
![raspyconfig](https://github.com/Ellakej/rover_finder/blob/master/assets/img3.png)
</br> Despues selecciona Desktop/CLI
![desktop](https://github.com/Ellakej/rover_finder/blob/master/assets/img4.png)
</br> Finalmente selecciona Console Autologin, para evitar introducir la contraseña cada vez que se inice la raspberry pi
![autologin](https://github.com/Ellakej/rover_finder/blob/master/assets/img5.png)
</br> Cuando termines no olvides darle en Finalizar y aceptar el reinicio del sistema, la proxima vez que inicie el sistema ya sera directo a la linea de comandos.

### Conexion de los modulos a la Raspberry Pi
Primero es necesario crear una carpeta para trabajar con el proyecto dentro de la Raspberry Pi, asi que desde nuestra PC abrimos una terminal y creamos una conexion SSH con el siguiente comando
````
ssh pi@[IP]
````
Donde [IP] (sin corchetes) lo sustituyes con la IP de la raspberry pi.</br>
Una vez que se tenga acceso a la Raspberry Pi remotamente se crea una nueva carpeta llamada __roverpi__ </br>
````
mkdir roverpi
cd roverpi
````

Dentro de esta carpeta se trabajaran todos los archivos de transferencia entre los modulos y la PC</br>
* __Modulo Camara__</br></br>
Para comenzar a trabajar con la camara se debe conectar el cable flex entre los puertos HDMI y Ethernet.
</br>Despues desde la conexion SSH solo hace falta abrir raspi-config
````
sudo raspi-config
````
Seleccionar __Enable camera__  presionar __Enter__ y luego ir a __Finish__ para finalmente reiniciar el sistema y tener habilitado el modulo camara

__
### Streaming de video desde Raspberry Pi
Originalmente se habia decidido grabar en la Raspberry Pi y cortar por fotogramas el video en tiempo real y enviarlo a la PC, archivo png por archivo, pero esto supone una carga pesada para la raspberry pi y el protocolo __SCP__, lo cual generaria una latencia extrema aun sin contar el procesado por inteligencia artificial. </br> Por lo que tras investigar un poco se encontro el protocolo __RTSP__ el cual es perfecto para enviar el video directamente por streaming a la PC y despues dejarle la carga y procesado directo a la PC, se recorta la fatiga del ancho de banda que se pensaba con SCP al pasar imagen por imagen y se reduce la carga de procesado en la raspberry pi.</br>
El comando para realizar el streaming es
```
raspivid
```
Y solo funcionara si esta activado el modulo camara

## En construccion...
