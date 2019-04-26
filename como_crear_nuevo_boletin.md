# ¿Cómo crear un nuevo boletín?

En este documento describimos los pasos realizados para crear la
versión web de un nuevo Boletín electrónico para la SEMA. Para ello,
supondremos que existe el código LaTeX (incluyendo imágenes) necesario
para generar la versión pdf del boletín. a

Suponemos que vamos a generar el "Boletín N".

## Paso 1. Crear un nuevo repositorio en Github

En Github existe una organización llamada
[BoletínSEMA](https://github.com/BoletinSEMA). Dentro de esta
organización, creamos un repositorio llamado `boletinN`.

### Configuración del nuevo boletín:

Dentro del nuevo repositorio `boletinN`, accedemos al menú *Settings* y en la sección
**GitHub Pages**, apartado **Sources** seleccionamos *master branch*.

Esto hará que el código HTML que introduzcamos en el repositorio
`boletinN` sera publicado en url `https://boletinsema.github.io/boletinN/`

## Paso 2. Crear el "esqueleto" del nuevo boletín

1. Copiar en el directorio raíz del nuevo directorio los siguientes ficheros html, que
están situados en la carpeta "*esqueleto*" del repositorio actual:

	1. El fichero `index.html` (la portada del nuevo boletín)
	2. El fichero `header.html` (la cabecera común a las páginas del nuevo boletín)
	3. El fichero `sidebar.html` (la columna que aparecerá a la izquierda en las páginas del nuevo boletín)

2. Crear en el directorio raíz una carpta llamada `img` que contenga
   todas las imágenes contenidos en el directorio "*esqueleto/img*"
   del repositorio actual

3. Sustituir la imagen `portada_boletin.png` por la primera página del
   fichero pdf del "Boletín N". Esta página deberá ser convertida a
   png, por ejemplo usando *Gimp* [TAREA: Automatizar esto, por
   ejemplo usando *Imagemagic*]. Como orientación, la imagen de
   portada en la web del Boletín 20 tiene _339 x 480 píxeles_.

4. Editar el fichero `header.html` y:
   * sustituir la expresión *Número N, MES AÑO" por el número, el mes
     y el año en que fue publicado
   * sustituir la expresión *???Mb* por el número de megabytes que
     ocupe el pdf del Boletín N.
   * [TAREA: Automatizar esto]

5. Una vez subidos todos estos cambios a Github, el esqueleto del
   boletín será accesible en `https://boletinsema.github.io/boletinN/

## Paso 3. Convertir el código LaTeX en HTML

(...)
