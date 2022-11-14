# ESCANER PARA PUERTOS BOOTCAMP

#se importan las librerías

import socket #Librería que nos sirve para comunicarnos con otra máquina mediante protocolos TCP o UDP 
#import termcolor 

#Necesitamos inicar un objeto socket, también llamados socket descriptors (descriptores socket) para iniciar la comunicación por internet.

def scan(target, ports): #esta funcion se encarga de llamar a scan_port segun el numero ingresado en ports
    print('\n' + 'Comenzando escaneo a IP ' + str(target))
    for port in range(1, ports):
        scan_port (target, port)

def scan_port(ipaddress, port): #Creamos la función y creamos los paramteros que se utilizaran en el proceso.
    try:
        sock = socket.socket() #creamos un "sock" con el cual llamamos a la función socket desde la libreria socket, iniciará el socket por nosotros y se almacenara en "sock"
        sock.connect((ipaddress, port)) #Inicia la conexión  hacia nuestro objetivo y sus puertos, requiere de 2 parámetros (ipaddress, port)
        print("[+] Puerto abierto! :D" + str(port))
        sock.close()
    except:
        pass
        #print("[-]Puerto cerrado... :(" + str(port)) en caso de requerir de ver los puertos cerrados

targets = input("[*] Ingresa un objetivo a escanear(si es mas de 1 separarlos por coma (,)): ")
ports = int(input ("[*] Ingresa cuantos puertos deseas escanear: "))
if ',' in targets :
    print("[*] Escaneando varios objetivos... ")
    for ip_addr in targets.split (','): 
        scan( ip_addr.strip(''), ports)
else:
    scan(targets, ports) 