# -*- coding: utf8 -*-

class Vehiculo:
    """
    representa un vehiculo
    """

    def __init__(self, placa, marca,modelo, tipo_de_vehiculo,hora_ingreso,estado):
        """representa un vehiculo"""
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.tipo_de_vehiculo = tipo_de_vehiculo
        self.hora_ingreso = hora_ingreso
        self.estado = estado
    
