# Tareas pendientes en el proceso de automatización de LaTeX a HTML

1. Colocar en una carpeta las imágenes que resultan de la conversión de ecuaciones LaTeX
   * Una mejora: ¿Cómo se consigue utilizar MathML en vez de imágenes?
2. Eliminar loas etiquetas [tail] [up]" y "[front] [up]" que están, respectivamente, al principio y al final de los ficheros html. 
3. Intentar que todos los párrafos estén justificados

### Cambios en el código \LaTeX que mejorarían la conversión en HTML
1. Asegurarse de no usar `<< (...) >>`. Esto produce errores tremendos de compilación a HTML!
2. Definir una orden ("newcommand") que englobe los separadores de tipo línea_diamante_línea.
  No quedan bien en HTML y se podrían sustituir automáticamente por HREF
