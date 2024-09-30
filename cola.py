from nodo import Nodo
from paciente import Paciente

class ColaPrioridad:
    def __init__(self):
        self.head: Nodo = None
        self.size: int = 0

    def insertar(self, paciente: Paciente) -> None:
        if type(paciente) == Paciente:
            nuevo_nodo = Nodo(paciente)
            if self.head is None or paciente.prioridad > self.head.dato.prioridad:
                nuevo_nodo.next = self.head
                self.head: Nodo = nuevo_nodo
                self.size += 1
            else:
                current_node = self.head
                while current_node.next and current_node.next.dato.prioridad >= paciente.prioridad:
                    current_node = current_node.next
                nuevo_nodo.next = current_node.next
                current_node.next = nuevo_nodo
                self.size += 1

        else:
            raise TypeError("No se puede insertar un dato de ese tipo")

    def atender(self) -> None:
        if self.head is not None:
            print("-------------------------")
            print(f"El cliente {self.head.dato.nombre} fue atendido")
            print("-------------------------")
            self.head = self.head.next
            self.size -= 1
        else:
            print(f"No hay pacientes por atender")

    def mostrar(self) -> None:
        current_node = self.head
        while current_node is not None:
            print(f"El paciente {current_node.dato.nombre} tiene una prioridad de {current_node.dato.prioridad}")
            current_node = current_node.next