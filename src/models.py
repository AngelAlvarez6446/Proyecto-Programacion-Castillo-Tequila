from dataclasses import dataclass
from typing import Optional


@dataclass
class Visitante:
    """
    Superclase que representa a un visitante del Castillo de Tequila.
    Cada instancia corresponde a una respuesta (fila) de la encuesta.
    """
    nombre: str
    pais: str
    edad: int
    genero: str
    nos_habias_visitado: str
    motivo_visita: str
    acompanantes: str
    tiempo_visita: str
    parte_favorita: str
    tipo_tour: str
    realizo_compra: str
    tipo_producto: Optional[str]
    gasto_aprox: Optional[str]
    metodo_pago: Optional[str]
    satisfaccion: int
    recomendacion: int
    innovacion: int

    # ============================
    # Métodos de instancia (POO)
    # ============================

    def mensaje_followup(self) -> str:
        """
        Método polimórfico básico.
        Las subclases lo sobreescriben con mensajes más específicos.
        """
        return (
            "Gracias por tu visita al Castillo de Tequila. "
            "Tu opinión nos ayuda a mejorar la experiencia."
        )

    def es_cliente_recurrente(self) -> bool:
        texto = self.nos_habias_visitado.strip().lower()
        return texto.startswith("s") or texto.startswith("y")

    def nivel_satisfaccion(self) -> str:
        if self.satisfaccion >= 8:
            return "Alta"
        elif self.satisfaccion >= 5:
            return "Media"
        return "Baja"


class VisitanteTurismo(Visitante):
    def mensaje_followup(self) -> str:
        return (
            f"Hola {self.nombre or 'visitante'}, gracias por elegirnos como parte de tu experiencia turística. "
            "Esperamos verte pronto explorando nuevas experiencias en El Castillo de Tequila."
        )


class VisitanteNegocios(Visitante):
    def mensaje_followup(self) -> str:
        return (
            f"Hola {self.nombre or 'visitante'}, gracias por considerar El Castillo de Tequila en tus actividades de negocios. "
            "Contamos con experiencias para equipos, socios y clientes."
        )


class VisitanteEvento(Visitante):
    def mensaje_followup(self) -> str:
        return (
            f"Hola {self.nombre or 'visitante'}, nos alegra que hayas asistido a un evento en El Castillo de Tequila. "
            "Mantente pendiente de próximos eventos y actividades especiales."
        )


class VisitanteOtro(Visitante):
    def mensaje_followup(self) -> str:
        return (
            f"Hola {self.nombre or 'visitante'}, gracias por visitarnos. "
            "Tu opinión nos ayuda a innovar y mejorar cada recorrido."
        )