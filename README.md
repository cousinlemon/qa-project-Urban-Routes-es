Hugo Martínez, 
grupo 14, Sprint 8


*Proyecto de Pruebas Automatizadas con Selenium:*

Este proyecto utiliza Selenium y Pytest para realizar pruebas automatizadas de una aplicación web de servicios de taxis privados con nuevas funciones incorporadas. El proyecto está estructurado utilizando el método Page Object Model (POM), lo que facilita el mantenimiento y la escalabilidad de las pruebas.Requisitos:

Descripción de las tecnologías y técnicas utilizadas
*Selenium WebDriver* es un controlador de navegador. Puedes usarlo para implementar el código de control del navegador y para emular las acciones de usuario.
Imagina que necesitas probar el sitio web de YouTube. Una de las pruebas es reproducir un vídeo desde la página de inicio.
En lugar de abrir todas las pestañas por tu cuenta, puedes ahorrar tiempo y utilizar Selenium.
Esto es lo que puede hacer Selenium:
Abrir la página de inicio de YouTube — https://www.youtube.com/
Selenium imita la mayoría de las acciones de usuario en el navegador:
* Hacer clic en un elemento: un botón, un botón de opción, una casilla de verificación, una lista desplegable.
* Rellenar campos de entrada.
* Navegar entre páginas: retroceder y avanzar, o usar una dirección URL.
* Navegar por la página: actualizar la página o desplazarse por ella.

Chrome WebDriver
1. Instala el controlador del navegador
Todos los navegadores populares son compatibles con Selenium WebDriver. Cada navegador tiene su propia versión del controlador.
Descarga WebDriver a través de este enlace.https://googlechromelabs.github.io/chrome-for-testing/
2. Busca la línea con la versión de Chromedriver que coincida con la versión de tu navegador y de tu sistema operativo. Necesitas la versión que coincida con la versión de tu navegador, al menos la parte antes del primer punto. Por ejemplo, si la versión de tu navegador es 102.0.5005.115, funcionarán tanto la versión 102.0.5005.27 como la 102.0.5005.61 del controlador. Si no puedes encontrar ninguna coincidencia, descarga la última versión estable. Para averiguar tu versión de Chrome, abre el navegador. Pega chrome://settings/help en la barra de direcciones y presiona Enter. Verás la versión de tu navegador en la nueva ventana. En la segunda columna de la tabla, puedes ver diferentes sistemas operativos: Linux, mac o win para Windows.
3. Copia el enlace al Chromedriver que seleccionaste y pégalo en la pestaña del navegador; debería comenzar a descargarse automáticamente.
4. Descomprime el archivo. Crea una carpeta llamada WebDriver/bin y guarda el archivo allí.
5. Agrega la ruta de bin a la variable de entorno PATH. El algoritmo depende del sistema operativo
6. Para Windows abre el Panel de control. Ve a Sistema → Configuración avanzada del sistema → Variables de entorno. Edita la variable del sistema PATH agregando la ruta a bin. Por ejemplo: C:\\\\WebDriver\\\\bin.

*Instala Selenium para Python*
Para poder utilizar Selenium con Python, necesitas instalar el paquete de Selenium. Sigue los siguientes pasos:
1. Abrir la Consola o Terminal Terminal desde las aplicaciones o usando el buscador de aplicaciones.
2. Ejecutar el Comando de Instalación
3. Escribe el siguiente comando para instalar el paquete de Selenium: pip install selenium

*Instalando Pytest*
Existen dos métodos para instalar Pytest. Elige el que te resulte más conveniente. Usando el comando "pip" en la terminal:
1. Abre la terminal o consola.
2. Ingresa el comando pip install pytest.
3. pip es el gestor de paquetes de Python. Te permite instalar y gestionar bibliotecas, así como herramientas adicionales. A través de la interfaz de PyCharm en "Python Packages":
4. En tu proyecto de PyCharm, dirígete al panel inferior y selecciona la pestaña "Python Packages".
En el campo de búsqueda, introduce "Pytest".
Localiza y selecciona el paquete "Pytest" de la lista y haz clic en el botón "Install".Siguiente

*PyCharm (Opcional)*
Instalación
* Clona este repositorio a tu directorio local.
* git clone git@github.com:QAquiceno14/qa-project-Urban-Routes-es.main.git
* Asegúrate de tener Python instalado.
* Se recomienda la instalación del entorno "PyCharm" para la ejecución de las pruebas
* Descarga Chrome WebDriver y configura la ruta en tu sistema.
* Instala Selenium (Verifica que la version sea compatible con tu version de Chrome)
* pip install selenium
* instala "pytest" utilizando pip en la terminal de comandos:
* pip install pytest

Contenido del proyecto:

"data.py": Archivo de configuración con los datos de prueba
"localizadores.py": Archivo que contiene los localizadores de todos los metodos utilizados
"main.py": Archivo principal que contiene las pruebas automatización para el flujo de la aplicación.
"metodos.py": Archivo que define los metodos de "UrbanRoutesPage".
"codigo.py": Archivo que contiene la funcion para establecer la confirmación del código del telefono.

*Ejecución de Pruebas*
Para ejecutar las pruebas, simplemente utiliza el comando pytest en la terminal de comandos:
pytest
Asegúrate de estar en el directorio raíz del proyecto para ejecutar el comando. Otra alternativa es utilizar el entorno "PyCharm" para correr las pruebas con Pytest.
Pruebas Disponibles
1. Establecer las direcciones de origen y destino.
2. Seleccionar la tarifa "Comfort".
3. Rellenar el número de teléfono.
4. Agregar tarjeta de crédito.
5. Escribir un mensaje para el controlador.
6. Pedir manta y pañuelos.
7. Pedir helados.
8. Buscar un taxi.