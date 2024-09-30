from paciente import Paciente

class Nodo:
    def __init__(self, dato: Paciente):
        self.dato: Paciente = dato
        self.next: Nodo = None