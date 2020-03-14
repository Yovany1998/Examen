from vehiculo import Vehiculo

class Estacionamiento():
    
    def __init__(self):
        """ Inicializa los vehiculos"""
        self.lista_vehiculos = list()

    def nuevo(self, placa, marca,modelo, tipo_de_vehiculo,hora_ingreso,estado):
        """ Crea una nueva nota y la agrega a la libreta """
        self.lista_vehiculos.append(Vehiculo(placa, marca,modelo, tipo_de_vehiculo,hora_ingreso,estado))

    def _search_note(self, vehi_placa):

        for vehi in self.lista_vehiculos:
            if str(vehi.placa) == str(vehi_placa):
                return vehi

        return None



