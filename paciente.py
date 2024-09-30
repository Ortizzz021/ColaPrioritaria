class Paciente:
    def __init__(self, nombre: str, descripcion_consulta: str):
        self.nombre: str = nombre
        self.descripcion_consulta: str = descripcion_consulta
        self.prioridad: int = self.calcular_prioridad()

    def calcular_prioridad(self) -> int:
        urgente_prioridad: list[str] = ["ataque", "derrame", "infarto", "parto", "asfixia"]
        alta_prioridad: list[str] = ["dolor agudo", "fractura", "quemadura"]
        media_prioridad: list[str] = ["fiebre", "tos", "gripa", "cortada"]
        baja_prioridad: list[str] = ["revisión", "control"]
        prioridad = 0

        for palabra in urgente_prioridad:
            if palabra in self.descripcion_consulta.lower():
                prioridad = 7
        for palabra in alta_prioridad:
            if palabra in self.descripcion_consulta.lower():
                prioridad = 5
        for palabra in media_prioridad:
            if palabra in self.descripcion_consulta:
                prioridad = 3
        for palabra in baja_prioridad:
            if palabra in self.descripcion_consulta.lower():
                prioridad = 1
        return prioridad

    def __str__(self):
        return f"El nombre del paciente es: {self.nombre}\nSu consulta es debido a un(a): {self.descripcion_consulta}\nY su prioridad de atención es de: {self.prioridad}"
