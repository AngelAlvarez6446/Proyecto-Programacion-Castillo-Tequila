# Interfaz de Inteligencia — El Castillo de Tequila

## Documentación Técnica del Proyecto

### Proyecto Final — Programación II

### Universidad de Guadalajara
### Licenciatura en Inteligencia artificial y ciencia de datos

### Integrantes
	•	Melany Regina Barrera Gaxiola — Documentadora
	•	Angel Gael Álvarez López — Project Manager
	•	Jesús Israel Rodríguez Hernández — Programador
	•	Carlos Emilio Castro Ramos — Programador

---

# 1. Problemática

El Castillo de Tequila carece de un sistema formal para la recolección, centralización y análisis de datos provenientes de visitantes y turistas. Actualmente:
```
	•	No existe un mecanismo para capturar sistemáticamente edad, procedencia, intereses, motivo de visita y nivel de satisfacción.
	•	La organización no cuenta con una plataforma que permita análisis rápidos y confiables.
	•	Se pierden oportunidades en:
	•	Marketing digital personalizado
	•	Fidelización de clientes
	•	Promoción de eventos
	•	Optimización operativa y logística
```
La falta de analítica implica pérdida de valor, mala toma de decisiones y procesos informales.

---

# 2. Solución Propuesta: “GestorEncuestasCastillo”

Se desarrolla una interfaz de inteligencia construida bajo Programación Orientada a Objetos (POO), cuyo objetivo es:

✔ Procesar automáticamente datos desde Google Forms

    Mediante exportación en formato .csv desde Google Sheets.

✔ Modelar cada visitante como un objeto

Con una superclase Visitante y subclases específicas según motivo de visita:
```
	•	VisitanteTurismo
	•	VisitanteNegocios
	•	VisitanteEvento
	•	VisitanteOtro
```
✔ Demostrar conceptos clave de POO:
```
	•	Herencia
	•	Polimorfismo (mensaje_followup)
	•	Métodos de clase (from_google_sheet)
	•	Encapsulamiento del flujo en GestorEncuestasCastillo
```
✔ Guardar datos en una base SQL local

    Utilizando SQLite.

✔ Ejecutar análisis estratégicos:
```
	•	Analítica de mercado
	•	Analítica de engagement
	•	Correlación de opiniones (satisfacción / recomendación / innovación)
```
---

3. Arquitectura del Sistema
``` plaintext
Proyecto/
├── src/
│   ├── models.py                  # Clases Visitante y subclases
│   ├── gestor.py                  # Clase GestorEncuestasCastillo
│   └── main.py                    # Punto de ejecución del programa
│
├── data/
│   └── castillo.db                # Base de datos SQLite generada
│
├── docs/
│   ├── problema.pdf                # Descripción formal del problema
│   ├── diagramas.pdf               # Diagramas de flujo y clases
│   ├── presentacion.pdf           # Slides del proyecto
│   └── documentacion.pdf          # Documento final entregable
│
├── requirements.txt               # Dependencias
└── README.md                      # Este archivo

```
---

# 4. Metodología de Desarrollo

El sistema fue diseñado siguiendo un proceso iterativo:

1. Análisis de requerimientos
```
	•	Identificación de columnas del formulario
	•	Diseño del modelo Visitante
	•	Selección de herramientas
```
2. Diseño POO
```
	•	Diagrama de clases
	•	Diagrama de flujo
	•	Separación modular
```
3. Implementación
```
	•	models.py: Superclase y subclases
	•	gestor.py: Carga, BD y analítica
	•	main.py: Orquestación general
```
4. Persistencia   
	•	Guardado automático en SQLite

5. Analítica  
```
	•	Estadísticas con pandas
	•	Clasificación por motivo
	•	Demostración de polimorfismo
```
6. Documentación y Presentación
```
	•	Documentación en Markdown y PDF
	•	Presentación del proyecto
	•	Publicación en GitHub
```
---

# 5. Herramientas Utilizadas

| Categoría            | Herramienta                  |
|----------------------|------------------------------|
| Lenguaje             | Python 3.10+                 |
| Librerías            | pandas, sqlite3, dataclasses |
| Control de versiones | Git / GitHub                 |
| Base de datos        | SQLite                       |
| Diagramación         | Draw.io, Lucidchart          |
| IDE                  | VS Code, Jupyter Notebook    |


---

# 6. Descripción Técnica del Funcionamiento

## 6.1 Carga de datos desde Google Sheets

Método utilizado:

GestorEncuestasCastillo.from_google_sheet(sheet_id)

Descargamos el CSV y construimos el DataFrame con pandas.


## 6.2 Construcción de objetos Visitante

Cada fila del CSV se convierte en un objeto:  
	•	Se analiza la columna:
“¿Cuál fue el principal motivo de tu visita?”  
```
	•	Según palabras clave:
	•	"turis" → VisitanteTurismo
	•	"negoc" → VisitanteNegocios
	•	"evento" → VisitanteEvento
	•	De lo contrario → VisitanteOtro
```
Las subclases sobrescriben:

def mensaje_followup(self):

Demostrando polimorfismo real.


## 6.3 Guardado en Base de Datos SQLite

self.df.to_sql("encuestas_castillo", conn, if_exists="replace")

Permite:
```
	•	Análisis posteriores
	•	Históricos de datos
	•	Integración con dashboards
```


## 6.4 Analítica del Proyecto

● Analítica de mercado
```
	•	Países visitantes
	•	Motivos principales
	•	Tipos de tour
```
● Analítica de engagement
```
	•	Promedio de satisfacción
	•	Probabilidad de recomendación
	•	Innovación percibida
```
● Correlación de opiniones

Calculada con:

self.df[cols].corr()




## 6.5 Demostración de polimorfismo

gestor.mostrar_mensajes_followup()

Ejemplo:

VisitanteTurismo -> Hola Juan, gracias por elegirnos para tu experiencia turística...
VisitanteNegocios -> Hola Laura, gracias por considerar El Castillo de Tequila...
VisitanteEvento -> Hola Miguel, esperamos que hayas disfrutado el evento...
VisitanteOtro -> Hola visitante, tu opinión nos impulsa a mejorar...


---

# 7. Diagramas de Flujo del Sistema

(Vincula con docs/diagramas.md)
``` plaintext
Inicio
│
├─ Leer CSV desde Google Sheets
│
├─ ¿Archivo válido?
│    ├─ No → Terminar
│    └─ Sí
│
├─ Construir objeto Visitante según motivo
│
├─ Guardar DataFrame en SQLite
│
├─ Analítica de mercado
├─ Analítica de engagement
├─ Correlación de opiniones
│
├─ Mostrar mensajes follow-up (polimorfismo)
│
Fin

```
---

# 8. Casos de Uso Ejemplificados



🟦 Caso 1: Procesar los datos del día

from src.gestor import GestorEncuestasCastillo  
gestor = GestorEncuestasCastillo.from_google_sheet  ("1s7WBbLg5wff3R0BGnn-aM9VokQU2C4u60OJ-PIOEExE")  
gestor.guardar_en_bd()  
gestor.analitica_mercado()  




🟩 Caso 2: Obtener correlación entre satisfacción e innovación

gestor.correlacion_opiniones()




🟨 Caso 3: Mostrar mensajes de follow-up

gestor.mostrar_mensajes_followup(limite=3)

Salida:

VisitanteTurismo -> Gracias por elegirnos...  
VisitanteNegocios -> Podemos ayudarte con eventos corporativos...  
VisitanteEvento -> Gracias por asistir al evento...  




🟥 Caso 4: Extender el sistema   

class VisitanteVIP(Visitante):  
    def mensaje_followup(self):  
        return "Gracias por formar parte de nuestro programa VIP..."


---

# 9. Conclusiones

El proyecto Interfaz de Inteligencia — El Castillo de Tequila demuestra:
```
	•	Programación Orientada a Objetos
	•	Herencia y polimorfismo
	•	Métodos de clase
	•	Persistencia con SQLite
	•	Analítica en Python
	•	Organización modular
	•	Documentación profesional
```
El sistema está listo para escalar hacia:
```
	•	Dashboards
	•	Aplicaciones web
	•	Integración con CRM
	•	Recepción masiva de formularios
```
