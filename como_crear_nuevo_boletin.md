# ¿Cómo crear un nuevo boletín?

En este documento describimos los pasos realizados para crear la
versión web de un nuevo Boletín electrónico para la SEMA. Para ello,
supondremos que existe el código LaTeX (incluyendo imágenes) necesario
para generar la versión pdf del boletín. a

Suponemos que vamos a generar el "Boletín N".

## Paso 1. Crear un nuevo repositorio en Github

- En Github existe una organización llamada
[BoletínSEMA](https://github.com/BoletinSEMA). Dentro de esta
organización, creamos un repositorio llamado `boletinN`.

- [*¿Es esto necesario, los colaboradores no tienen acceso por defecto?*] Añadimos a este nuevo repositorio, `boletinN`, todos los colaboradores para que tengan permiso de edición (*writting*). Esto lo podemos hacer desde *Settings*, *Collaborators and teams* (menú `...` a la derecha)

- Dentro del nuevo repositorio `boletinN`, accedemos al menú *Settings* y en la sección
**Pages** (menú a la izquierda), apartado **Sources** seleccionamos la rama (*branch*) *main* y pulsamos (*Save*).

Después del último punto, el código HTML que introduzcamos en el repositorio
`boletinN` sera publicado en url `https://boletinsema.github.io/boletinN/`

## Paso 2. Crear el "esqueleto" del nuevo boletín

1. Copiar en el directorio raíz del nuevo directorio los siguientes ficheros html, que
están situados en el directorio "***esqueleto***" del repositorio actual (o, quizás mejor,
   del último boletín, pueden estar más actualizados):

	1. El fichero `index.html` (la portada del nuevo boletín)
	2. El fichero `header.html` (la cabecera común a las páginas del nuevo boletín)
	3. El fichero `sidebar.html` (la columna que aparecerá a la izquierda en las páginas del nuevo boletín)

2. Crear en el directorio raíz una carpeta llamada `img` que contenga
   todas las imágenes contenidos en el directorio "*esqueleto/img*"
   del repositorio actual (o, quizás mejor, los contenidos de la
   carpeta *img* del último boletín).

3. Sustituir la imagen `portada_boletin.png` por la primera página del
   fichero pdf del "Boletín N". Esta página deberá ser convertida a
   png, por ejemplo usando *Gimp* (TAREA: Automatizar esto, por
   ejemplo usando *Imagemagic*]. Como orientación, habitualmente usamos una imagen 
   con _340 x 480 píxeles_. Además, habrá que extraer la primera página del boletín
   (por ejemplo, imprimir a un archivo) <a un fichero llamado `portada.pdf`.
   
3. Del mismo modo, crear los fichreos `contraportada_boletin.png` y `contraportada.pdf`.

4. Editar el fichero `header.html` y:
   * sustituir la expresión *Número N, MES AÑO" por el número, el mes
     y el año en que fue publicado
   * sustituir la expresión *???Mb* por el número de megabytes que
     ocupe el pdf del Boletín N.
   * [TAREA: Automatizar esto]

5. Subir todos estos cambios a Github


## Paso 3. Convertir el código LaTeX en HTML

Supongamos de que el código LaTeX, figuras, etc. está en una carpeta
con un nombre del tipo *Boletin-NXX-mes20YY*.

1. Fuera del sistema de control de versiones, crear una carpeta llamada,
por ejemplo, `LaTeX2HTML-BoletinN`. Por ejemplo, `<N>' es igual a 22
para el número 22. Esta carpeta la utilizaremos para almacenar el código LaTeX y
para realizar el proceso de conversión en HTML. Desde la terminal:

	0. Situarse en esta carpeta.
		```
		cd <ruta_a_la_carpeta>/LaTeX2HTML-BoletinN
		```
	1. **Compilar** el fichero `boletinN.tex`. Probablemente haya muchos errores, imágenes perdidas, etc. Pero hay que arreglarlo: si no compila el LaTeX a pdf, difícilmente compilará a HTML. Posiblemente, cuando todo funcione, se desee eliminar los ficheros de compilación, por ejemplo con `latexmk -c boletinN`.
 	2. Copiar toda el contenido de la capeta que contiene las fuentes LaTeX y las imágenes
	   ```
	   cp -a ../Boletin-NXX-mes20YY/* .
	   ```


2. En esta carpeta `Boletin<N>-LaTeX2HTML`, realizaremos la conversión a HTML.  Empezaremos preparando el entorno:

	 1. Editar el fichero `boletinN.tex`, y descomentar la línea
	   ```
	   \SaltarTikZ % Quitar el comentario para saltar todos los códigos de tikz
	   ```
	 1. Para asegurarnos de que todo funciona correctamente, compilar y generar el fichero pdf: `pdflatex boletinNN.tex`. Si hay errores, deberemos corregirlos antes de comenzar a convertir en html.
	 1. Copiar al directorio de trabajo el contenido de la carpeta llamada `latex2html`
		que está en el repositorio principal *boletinsema.github.io*.
		Ésta contiene la configuración para la conversión en HTML.
		Por ejemplo:
	   ```
	   cp ../../Boletin-Web/boletinsema.github.io/latex2html/* .
	   ```
	 1. Las figuras son muy 'pesadas'. Están sistuadas en distintas subcarpetas
		 del directorio 'figuras'. Hay que pensar bien la forma
		 de reducirles el tamaño. Una posibilad es usar *convert* (de
		 ImageMagic) para reducir el ancho y el alto. Otra que he usado
		 ocasionalmente es jpegoptim:
		```
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
	1. Las órdenes *ebb -x ..." anteriores se deben a lo siguiente: Por un motivo
	que aún no conozco con detalle, el conversor de LaTeX en HTML
	necesita conocer las dimensiones de las imágenes. Esto se puede
	hacer ejecutando, en todas las carpetas que contengan figuras, la
	siguiente orden (también para .jpg):
		```
		ebb -x *.png
		```
	Esta orden generará un fichero con estensión *xbb* para cada imagen, que contienen información sobre ésta (ancho, alto...). Por simplicidad, he introducido esta orden en el código bash que se muestra en el apartado anterior.
    1. En ocasiones, el fichero .tex contiene imágenes en formato .pdf. El conversor a HTML no parece reconocerlas. Puede ser buena idea convertirlas, por ejemplo a .png, con::
		```
		pdftoppm -png fichero.pdf > fichero.png
		```
3. Conversión en HTML:
   1. Editar el fichero *Makefile* y escribir el valor adecuado en la
       variable `NUMERO_BOLETIN`
   2. Escribir make (y cruzar los dedos). Empezará la compilación en html.
   3. Lo normal es que aparezcan errores, debido a que se utilizan paquetes para los que
	  la conversión en HTML no funciona correctamente.

4. Una vez la compilación en HTML ha terminado, podemos eliminar los ficheros LaTeX para no exponerlos en el repositorio git:
	```
	rm *.tex *.aux *.log *.toc *.dvi boletinN.pdf
	```
	
## Paso 4. Copiar ficheros al repositorio de Github

Para finalizar, se deben copiar los ficheros relevantes (html, imágenes, css...) al repostorio de Github. Entonces comenzará el proceso de revisión y edición manual del HTML.
