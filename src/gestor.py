import sqlite3
from pathlib import Path
from typing import List
import pandas as pd
import unicodedata  

from .models import (
    Visitante,
    VisitanteTurismo,
    VisitanteNegocios,
    VisitanteEvento,
    VisitanteOtro,
)


class GestorEncuestasCastillo:
    """
    Clase que gestiona todo el flujo del sistema:
    - Leer CSV desde Google Sheets
    - Crear objetos Visitante* (subclases)
    - Guardar datos en SQLite
    - Generar analíticas
    """

    def __init__(self, df: pd.DataFrame, visitantes: List[Visitante], db_path: str = "data/castillo.db"):
        self.df = df
        self.visitantes = visitantes
        self.db_path = db_path

    # ============================
    # Métodos de clase
    # ============================

    @classmethod
    def from_google_sheet(cls, sheet_id: str, db_path: str = "data/castillo.db"):
        """Carga datos desde Google Sheets → CSV"""
        url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"
        df = pd.read_csv(url)
        df["¿De qué País nos visitas?"] = df["¿De qué País nos visitas?"].apply(cls._normalizar_pais)
        #ese def es para que se imprima correctamente sin repetir letras diferentemente escritas
        visitantes = cls._crear_visitantes(df)
        return cls(df, visitantes, db_path)

    # =================================================
    # la funcion para normalizar las respuestas de pais  
    # =================================================
    @staticmethod
    def _normalizar_pais(pais: str) -> str:
        """
        Normaliza el país:
        - elimina acentos
        - convierte a minúsculas
        - elimina espacios alrededor
        """
        if not isinstance(pais, str):
            return pais

        # eliminar acentos
        nfkd = unicodedata.normalize("NFKD", pais)
        sin_acentos = "".join([c for c in nfkd if not unicodedata.combining(c)]) 
        #Separa caracteres y aplica equivalencia, y porque nfkd? es solo la abreviacion en ingles del modo 
        #Compatibility Decomposed
        return sin_acentos.strip().lower()

    @staticmethod
    def _crear_visitantes(df: pd.DataFrame) -> List[Visitante]:
        lista = []

        for _, row in df.iterrows():
            motivo = row["¿Cuál fue el principal motivo de tu visita?"].lower()

            if "turis" in motivo:
                cls_v = VisitanteTurismo
            elif "negoc" in motivo:
                cls_v = VisitanteNegocios
            elif "evento" in motivo:
                cls_v = VisitanteEvento
            else:
                cls_v = VisitanteOtro

            visitante = cls_v(
                nombre=row.get("Nombre (Opcional)", ""),

                # =====================================
                # ** AQUI SE USA LA FUNCIÓN NUEVA **
                # =====================================
                pais=GestorEncuestasCastillo._normalizar_pais(
                    row["¿De qué País nos visitas?"]
                ),

                edad=int(row["¿Cuántos años tienes?"]),
                genero=row["¿Con qué género te identificas?"],
                nos_habias_visitado=row["¿Nos habías visitado anteriormente?"],
                motivo_visita=row["¿Cuál fue el principal motivo de tu visita?"],
                acompanantes=row["¿Con quién viniste acompañado?"],
                tiempo_visita=row["¿Cuánto tiempo estimas que duró tu visita?"],
                parte_favorita=row["¿Qué parte del recorrido te resultó más interesante?"],
                tipo_tour=row["¿Qué tipo de tour realizaste?"],
                realizo_compra=row["¿Realizaste alguna compra durante tu visita?"],
                tipo_producto=row.get("¿Qué tipo de producto compraste?", None),
                gasto_aprox=row.get(
                    "¿Aproximadamente cuánto gastaste durante tu visita? (En caso de considerar esta información sensible, no responderla)",
                    None,
                ),
                metodo_pago=row.get("¿Qué método de pago utilizaste?", None),
                satisfaccion=int(row["¿Qué tan satisfecho(a) quedaste con tu experiencia en general?"]),
                recomendacion=int(row["¿Qué tan probable es que recomiendes la experiencia a otras personas?"]),
                innovacion=int(row["¿Qué tan innovadora te pareció la experiencia?"]),
            )

            lista.append(visitante)

        return lista

    # ============================
    # Base de datos
    # ============================

    def _crear_directorio(self):
        Path(self.db_path).parent.mkdir(parents=True, exist_ok=True)

    def guardar_en_bd(self, tabla: str = "encuestas_castillo"):
        """Guarda todo el DataFrame en SQLite"""
        self._crear_directorio()
        conn = sqlite3.connect(self.db_path)
        self.df.to_sql(tabla, conn, if_exists="replace", index=False)
        conn.close()

    # ============================
    # Analítica
    # ============================

    def analitica_mercado(self):
        print("=== Países ===")
        print(self.df["¿De qué País nos visitas?"].value_counts())

        print("\n=== Motivo de visita ===")
        print(self.df["¿Cuál fue el principal motivo de tu visita?"].value_counts())

        print("\n=== Tipo de tour ===")
        print(self.df["¿Qué tipo de tour realizaste?"].value_counts())

    def analitica_engagement(self):
        cols = [
            "¿Qué tan satisfecho(a) quedaste con tu experiencia en general?",
            "¿Qué tan probable es que recomiendes la experiencia a otras personas?",
            "¿Qué tan innovadora te pareció la experiencia?",
        ]
        print("=== Promedios ===")
        print(self.df[cols].mean())

        print("\n=== Variabilidad (STD) ===")
        print(self.df[cols].std())

    def correlacion_opiniones(self):
        cols = [
            "¿Qué tan satisfecho(a) quedaste con tu experiencia en general?",
            "¿Qué tan probable es que recomiendes la experiencia a otras personas?",
            "¿Qué tan innovadora te pareció la experiencia?",
        ]
        print("=== Matriz de correlaciones ===")
        print(self.df[cols].corr())

    # ============================
    # Polimorfismo visible
    # ============================

    def mostrar_mensajes_followup(self, limite: int = 5):
        print("=== Polimorfismo: mensajes personalizados ===")
        for visitante in self.visitantes[:limite]:
            print(f"- {type(visitante).__name__}: {visitante.mensaje_followup()}")
            print(f"  → Recurrente: {visitante.es_cliente_recurrente()}")
            print(f"  → Satisfacción: {visitante.nivel_satisfaccion()}")
            print()
