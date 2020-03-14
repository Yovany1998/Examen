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
        marca = input("Ingrese la marca del vehiculo: ")
        modelo = input("Ingrese el modelo del vehiculo: ")
        tipo_de_vehiculo = input("Ingrese tipo de  vehiculo: ")
        horas_vehiculo = input("Ingrese la hora de ingreso del vehiculo: ")
        estado = input("Estado por defecto True: ")
        print("El vehiculo se ingreso correctamente")
        pass

    def totalVehiculos(self):
        """Muestra el total de vehiculos"""
 
        for vehi in vehiculos:
            print("placa: {0}\nmarca: '{1}'\nmodelo: {2}\ntipo: {3}\ntipo_de_vehiculo: {4}\hora_ingreso: {5}\nestado: "
                  .format(vehi.placa,vehi.marca,vehi.modelo,vehi.tipo_de_vehiculo,vehi.horas_vehiculo,vehi.estado))

    

    def salida(self):
        """Se ingresala placa del vehiculo para buscar su tarifa"""
        
        buscar=input("Ingrese la placa del vehiculo que saldra")

        if(vehi.tipo_de_vehiculo == "Motocicleta"):
            tipo = 10
            total = vehi.horas_vehiculo*tipo-((vehi.horas_vehiculo-1)*1)
        elif(vehi.tipo_de_vehiculo == "Automovil"):
            tipo = 20
            total = vehi.horas_vehiculo*tipo-((vehi.horas_vehiculo-1)*4)
        else:
            prinf("No se reconoce el tipo de vehiculo")
            total = 0

        print("El total a pagar por las horas es ",total)

    def gananciasDia(self):
         pass

    def salir(self):
          """ Cierra la aplicación """
        print("Se cerro la aplicacion")
        sys.exit(0)




    def horas(self):
        horas_vehiculo=random(1,5)
        print(horas_vehiculo)

