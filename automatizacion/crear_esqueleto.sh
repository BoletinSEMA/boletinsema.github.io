#!/bin/bash

function printInfo {
    echo "Script para ayudar a crear un nuevo Boletin de SEMA."
    echo ""
    echo "Ejemplo de uso:"
    echo "  $0 boletin29 boletin28 Boletin-N29-febrero2022"
    echo ""
    echo "Se generará una carpeta llamada boletin29 que contiene el esqueleto"
    echo "para un nuevo boletín, generado a partir de un boletín anterior (boletin28)"
    echo
    echo "En el ejemplo se asume que existen dos carpetas  en el directorio actual:"
    echo "- boletin28 (una versión anterior del boletín, usualmente un repositorio git)"
    echo "- Boletin-N29-febrero2022, directorio que debe contener las fuentes .tex"
    echo "  y la versión pdf (en este caso, boletin29.pdf)"
    echo ""
    echo "Como resultado, se generará la carpeta 'boletin29'"
}

printInfo
if [[ $# -le 2 ]] ; then
    exit 0
fi

BOLETIN=$1
BOLETINANTERIOR=$2
SOURCEDIR=$3

# 1) Copiar ficheros html
mkdir -p $BOLETIN/img
HTML="index.html header.html sidebar.html"
for i in $HTML
do
    echo $i
    cp $BOLETINANTERIOR/$i $BOLETIN
done

# 2) Copiar imágenes
mkdir -p $BOLETIN/img
IMAGES="boletin_sema.png logosema.png cuotas-socios-sema.png info.png"
for i in $IMAGES
do
    echo $i
    cp $BOLETINANTERIOR/img/$i $BOLETIN/img
done

# 3) Generar portada a partir de la versión PDF
pdftoppm -f 1 -singlefile -png $SOURCEDIR/$BOLETIN.pdf $BOLETIN/img/portada_boletin
# mv $BOLETIN.png $BOLETIN/img/portada_boletin.png
ls -l $BOLETIN/img/portada_boletin.png
# ... y generar contraportada
pdftk $SOURCEDIR/$BOLETIN.pdf cat r1 output /tmp/lastPage.pdf
pdftoppm -f 1 -singlefile -png /tmp/lastPage.pdf $BOLETIN/img/contraportada_boletin
