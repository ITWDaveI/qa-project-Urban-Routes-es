# Prueba automatizada de Urban Routes

## Descripción
Esta prueba conlleva la elección de direcciones, pedir un taxi, seleccionar confort, agregar número de teléfono y su código de verificación, agregar método de pago, agregar comentarios y requisitos utilizando switch y contadores para finalmente reservar un taxi.

## Tecnologías utilizadas
- Lenguaje: Python
- Librería principal: Selenium WebDriver
- Módulos de Selenium usados: By (localizadores) y Keys.

Se aplicó el patrón Page Object, separando los localizadores y métodos de interacción (UrbanRoutesPage) de las pruebas en sí (TestUrbanRoutes).

## Cómo ejecutar las pruebas
- Activar un entorno virtual antes de instalar Selenium.
- Usar la consola para instalar Selenium con pip install selenium. 
- Actualizar la URL en data.py.
- Correr las pruebas usando Run en Pycharm.