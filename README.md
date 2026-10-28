# Pruebas automatizadas de Urban Routes

## Descripción
Esta prueba conlleva la elección de direcciones, pedir un taxi, seleccionar confort, agregar número de teléfono y su código de verificación, agregar método de pago, agregar comentarios y requisitos utilizando switch y contadores para finalmente reservar un taxi.

## Tecnologías utilizadas
- Lenguaje: Python
- Librería principal: Selenium WebDriver
- Módulos de Selenium usados: By (localizadores) y Keys.

Se aplicó el patrón Page Object, separando los localizadores y métodos de interacción (UrbanRoutesPage) de las pruebas en sí (TestUrbanRoutes).

## Estructura del proyecto

- data.py: datos de prueba (direcciones, teléfono, tarjeta, etc.)
- helpers.py: función para obtener el código de confirmación del teléfono
- pages.py: clase UrbanRoutesPage con localizadores y métodos de interacción
- main.py: pruebas (TestUrbanRoutes)

## Cómo ejecutar las pruebas
- Activar un entorno virtual antes de instalar Selenium.
- Usar la consola para instalar Selenium con pip install selenium.
- Instalar pytest con pip install pytest.
- Actualizar la URL en data.py.
- Correr las pruebas usando Run en Pycharm.