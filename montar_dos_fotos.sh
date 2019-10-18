#!/bin/bash

usage(){
	echo "Montar dos imágenes (izquierda | derecha) en una sola"
	echo "Usage: $0 <fich_img1> <fich_img2> <fich_salida>"
	exit 1
}

file_exits(){
	local f="$1"
	[[ -f "$f" ]] && return 0 || return 1
}

[[ $# -ne 3 ]] && usage

IMG1=$1
IMG2=$2
IMGSALIDA=$3

if ( file_exits "$IMGSALIDA" )
then
    echo "El fichero de salida ya existe!"
    print
else
    convert $IMG1 -resize 1200x800\> $IMG1
    convert $IMG2 -resize 1200x800\> $IMG2
    montage  -geometry +0+0 -border 10  -bordercolor '#FFFFFF' \
	     $IMG1 $IMG2 $IMGSALIDA
fi
