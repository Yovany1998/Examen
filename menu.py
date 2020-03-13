# -*- coding: utf8 -*-
#nombre:menu
#funcion:simula el funcionamiento de un estacionamiento
#autor: Yovany Hernandez
#fecha:03/13/2020
import sys
import platform
import datetime
import random


class Menu:
    """
    Despliega las opciones.
    """

    def __init__(self):
            """ Inicializa las listas """
            self.Vehiculo = list()
        
            self.options = {"1":self.ingreso,
                            "2":self.totalVehiculos,
                            "3":self.salidas,
                            "4":self.gananciasDia,
                            "5":self.salir
                            }

    def display_menu(self):
        """ Despliega el menu """
        print("""
             Menú principal

            1:Insgreso de vehiculo
            2:Total de vehiculos
            3:Salidas
            4:Ganancias del dia
            5:salir
             """)
    def ingreso(self):
        placa = input("Ingrese la placa del vehiculo: ")
        marca = input("Ingrese la placa del vehiculo: ")
        modelo = input("Ingrese la placa del vehiculo: ")
        tipo_de_vehiculo = input("Ingrese la placa del vehiculo: ")
        print("la placa se agrego correctamente")
        pass

    def totalVehiculos(self):
 
        for vehi in vehiculos:
            print("placa: {0}\nmarca: '{1}'\nmodelo: {2}\ntip: {3}"
                  .format())



    def salida(self):
         pass

    def gananciasDia(self):
         pass

    def salir(self):
          """ Cierra la aplicación """
        print("Se cerro la aplicacion")
        sys.exit(0)




    def horas(self):
        horas_vehiculo=random(1,5)
        print(horas_vehiculo)

