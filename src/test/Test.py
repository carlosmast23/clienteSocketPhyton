# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from cliente.Socket import *
import sys

__author__ = "Carlos Sanchez"
__date__ = "$14-dic-2015 18:04:51$"

if __name__ == "__main__":
    socket_cliente=Socket("localhost",9999)
    print('presione una tecla para conectarse ...')
    input()
    socket_cliente.conectar();
    no_salir=True;
    while no_salir:
        print('ingrese el mensaje a enviar')
        texto=input()
        socket_cliente.escribir(texto)
        if texto=="EXIT":
            no_salir=False
        else:        
            print(socket_cliente.leer())
        
