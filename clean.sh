#!/usr/bin
#Copyright 2021 DZERO-M
#Written by: DZERO-M
#Facebook: https://facebook.com/adrian.guillermo.22
#Github: https://github.com/AdrMXR

# Clean DZERO-M

# Colors
red='\e[1;31m'
default='\e[0m'
yellow='\e[0;33m'
green='\033[92m'

# Location
path=$(pwd)

# Check root 
if [ "$(id -u)" != "0" ] > /dev/null 2>&1; then
echo -e '\n$red[x] This script needs root permissions.' 1>&2
exit
fi

tools() {
    sleep 1.5
    if [ -d tools ]; then
    	count="$( find tools/* -mindepth 1 -maxdepth 1 | wc -l )"
    	if ! [ $count -eq 0 ] ; then
 			rm -rf $( find tools/*/* -type d )
 			echo -e "[✔]tools."	
        else
        	echo -e "[x]tools empty."
        fi
    else
    	echo -e "[x]tools no encontrada."
   	fi
}

output() {
	sleep 1.5
	if [ -d output ]; then
		count="$( find output -mindepth 1 -maxdepth 1 | wc -l )"
		if ! [ $count -eq 0 ] ; then
			rm -rf $( find output -type f)
			echo -e "[✔]output."
    	else
        	echo -e "[x]output empty."
       	fi	
    else
    	echo -e "[x]output no encontrada."
   	fi
}

clear
echo -e """ $green
╔──────────────────────────────────────────────╗
| With this script you can delete the content  |
|     that DZERO-M generates in the folders    |
|               tools and output.              |                                            
┖──────────────────────────────────────────────┙"""
echo -e "$green"
echo -e "Seleccione la opción requerida."
echo -e "$default[1]""$yellow tools"
echo -e "$default[2]""$yellow output"
echo -e "$default[3]""$yellow all"
echo -e "$red"
echo -ne "dzero-m >> $default"
read -r option
case "$option" in

1)
tools 
exit 1s
;;

2)
output
exit 1
;;

3)
tools
output
exit 1
;;

*)
echo -e "$red""Invalid option."
;;
esac

