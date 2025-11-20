import pandas as pd #para que la matriz de correlación se muestre completa
from .gestor import GestorEncuestasCastillo
#============================================

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

SHEET_ID = "1s7WBbLg5wff3R0BGnn-aM9VokQU2C4u60OJ-PIOEExE"


def main():
    gestor = GestorEncuestasCastillo.from_google_sheet(SHEET_ID)

    gestor.guardar_en_bd()

    print("\n--- Analítica de mercado ---")
    gestor.analitica_mercado()

    print("\n--- Analítica de engagement ---")
    gestor.analitica_engagement()

    print("\n--- Correlación de opiniones ---")
    gestor.correlacion_opiniones()

    print("\n--- Mensajes (polimorfismo) ---")
    gestor.mostrar_mensajes_followup(limite=5)


if __name__ == "__main__":
    main()