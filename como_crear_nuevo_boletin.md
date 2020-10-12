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

Añadir a todos los colaboradores: *Settins*, *Collaborators and teams*

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

5. Subir todos estos cambios a Github

6. En *Settins*, sección *Github Pages* seleccionar la rama *main*. Así se podrá ver el contenido html desde la web https://boletinsema.github.io/boletinN/

## Paso 3. Convertir el código LaTeX en HTML

Supongamos de que el código LaTeX, figuras, etc. está en una carpeta
llamada *Boletin-N-mes20XX*. Esta capeta estará dentro de otra más
general, llamada por ejemplo *../../Boletin-PDF* (precisamente, esta es
la dirección relativa en *sobolev.uca.es*)que contiene al resto de
los boletines y ficheros relacionados para la compilación LaTeX
(imágnees, etc).

1. Fuera del sistema de control de versiones, crear una carpeta llamada,
por ejemplo, `Boletin<N>-LaTeX2HTML`. Por ejemplo, `<N>' es igual a 22
para el número 22. Esta carpeta la utilizaremos para almacenar el código LaTeX y
para realizar el proceso de conversión en HTML. Desde la terminal:

	0. Situarse en esta carpeta.
		```
		cd <ruta_a_la_carpeta>/Boletin<N>-LaTeX2HTML
		```
	1. Por simplicidad, enlazaremos al directorio que contiene todas las
		fuentes LaTeX que ya han sido usadas para componer la versión PDF:
		```
		ln -s ../../Boletin-PDF
		```
	2. Copiar toda la capeta *Boletin-N-mes20XX*:
	   ```
	   cp -a Boletin-PDF/Boletin-<N>-mes20<XX> .
	   ```
	3. Enlazar al resto del contenido, escribendo por ejemplo:
	   ```
	   for i in Boletin-PDF/*; do ln -s $i; done
	   ```
	   La línea anterior dará un error porque *Boletin-N-mes20XX* ya
       existe (perfecto) y enlazará al resto de los contenidos.
	4. Entrar la esta que habíamos copiado, donde haremos todo el proceso
		de conversión de LaTeX en HTML:
		```
		cd Boletin-<N>-mes20<XX>
		```


2. Realizaremos la conversión a HTML en la carpeta en la que habíamos copiado
   las fuentes LaTeX y las figuras. Para ello, empezaremos preparando el entorno:

	 0. Entrar en esta carpeta:
	 ```
	 cd Boletin-<N>-mes20<XX>
	 ```

	 1. Editar el fichero boletinN.tex, situado dentro de la carpeta *Boletin-N-mes20XX*, y descomentar la línea
	   ```
	   \SaltarTikZ % Quitar el comentario para saltar todos los códigos de tikz
	   ```
	 1. Copiar al directorio de trabajo el contenido de la carpeta llamada `latex2html`
		que está en el repositorio principal *boletinsema.github.io*.
		Ésta contiene la configuración para la conversión en HTML.
		Por ejemplo:
	   ```
	   cp ../../boletinsema.github.io/latex2html/* .
	   ```
	 1. Las figuras son muy 'pesadas'. Están sistuadas en distintas subcarpetas
		 del directorio 'figuras'. Hay que pensar bien la forma
		 de reducirles el tamaño. Una posibilad es usar *convert* (de
		 ImageMagic) para reducir el ancho y el alto. Otra que he usado
		 ocasionalmente es jpegoptim:
		```
		cd figuras
		jpegoptim -s -S1000 *.jpg

		for DIR in `ls -l`
		do
			if test -d $DIR
			then
				echo "Directorio $DIR..."
				cd $DIR
				jpegoptim -s -S1000 *.jpg
				ebb -x *.png
				ebb -x *.jpg
				cd ..
			fi
		done
		cd ..
		```
	1. Las órdenes *ebb -x ..." se deben a lo siguiente: Por un motivo
	que aún no conozco con detalle, el conversor de LaTeX en HTML
	necesita conocer las dimensiones de las imágenes. Esto se puede
	hacer ejecutando, en todas las carpetas que contengan figuras, la
	siguiente orden (también para .jpg):
		```
		ebb -x *.png
		```
	Esta orden generará un fichero con estensión *xbb* para cada
	imagen, que contienen información sobre ésta (ancho, alto...). Por simplicidad,
	he introducido esta orden en el código bash que se muestra en el apartado anterior.

3. Conversión en HTML:
   1. Editar el fichero *Makefile* y escribir el valor adecuado en la
       variable `NUMERO_BOLETIN`
   2. Escribir make (y cruzar los dedos). Empezará la compilación en html.
   3. Lo normal es que aparezcan errores, debido a que se utilizan paquetes para los que
	  la conversión en HTML no funciona correctamente.

## Paso 4. Copiar ficheros al repositorio de Github

Para finalizar, se deben copiar los ficheros relevantes (html, imágenes, css...) al repostorio de Github. Entonces comenzará el proceso de revisión y edición manual del HTML.
