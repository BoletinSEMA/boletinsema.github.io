# Tareas pendientes en el proceso de automatización de LaTeX a HTML

1. Colocar en una carpeta las imágenes que resultan de la conversión de ecuaciones LaTeX
   * Una mejora: ¿Cómo se consigue utilizar MathML en vez de imágenes?
2. Eliminar loas etiquetas [tail] [up]" y "[front] [up]" que están, respectivamente, al principio y al final de los ficheros html. 
3. Intentar que todos los párrafos estén justificados
4. Después de la compilacón a HTML (que se hacde fuera del repositorio) copiar automáticamente al repositorio y (añadir automáticamente a git, "git add") todos los ficheros relevantes:
  * Las fotos, que en principio están en la capreta "figuras"
  * Logotipos y otras imágenes, que están en la carpeta img
  * Las gráficas resultantes de convertir las ecuaciones
  * Todos los ficheros HTML
  * Todos los ficheros CSS (?)

### Cambios en el código \LaTeX que mejorarían la conversión en HTML
1. Asegurarse de no usar `<< (...) >>`, al menos en los nombres de capítulos y secciones. Esto produce errores tremendos de compilación a HTML!
2. Definir una orden ("newcommand") que englobe los separadores de tipo línea_diamante_línea.
  No quedan bien en HTML y se podrían sustituir automáticamente por &lt;hr&gt;
