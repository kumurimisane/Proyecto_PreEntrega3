# Proyecto_PreEntrega3
PreEntrega 3 para CoderHouse

Proyecto desarrollado en Django que permite: 
Registrar Estudiantes, Cursos y Trabajos entregado. 
La aplicación incluye una interfaz web que permite a los usuarios registrarse, crear cursos y entregar trabajos con sus nombres,
y también ofrece una funcionalidad de búsqueda para encontrar los cursos en la base de datos a partir de la camada.

Requisitos.
Para ejecutar este proyecto, necesitarás tener instalado Python 3 y Django en tu equipo.
Puedes instalar Django utilizando pip, el gestor de paquetes de Python, de la siguiente manera:
"pip install django" desde la terminal.

Uso del proyecto.
Una vez que hayas configurado el proyecto, puedes ejecutarlo utilizando el siguiente comando:
"python manage.py runserver"

Esto iniciará un servidor local en tu equipo y podrás acceder a la interfaz web del proyecto desde tu navegador, utilizando el localhost.

Desde la interfaz web, podrás registrarte como usuario, crear posteos y grupos. 
También podrás utilizar la funcionalidad de búsqueda para encontrar posteos en la base de datos.

Estructura del proyecto.
El proyecto está estructurado de la siguiente manera:

manage.py: Archivo principal del proyecto de Django, utilizado para ejecutar comandos de gestión del proyecto (como iniciar el servidor o ejecutar migraciones).

App: Directorio que contiene la configuración principal del proyecto, incluyendo el archivo settings.py y las URLs del proyecto.

templates: Directorio que contiene las plantillas HTML utilizadas por las aplicaciones del proyecto.

static: Directorio que contiene archivos estáticos utilizados por las plantillas HTML (como hojas de estilo CSS o scripts JavaScript).

db.sqlite3: es un archivo de base de datos SQLite utilizado en el proyecto de Django para almacenar la información de los usuarios, posteos y grupos.
            Contiene todas las tablas y relaciones necesarias para almacenar los datos del proyecto.
