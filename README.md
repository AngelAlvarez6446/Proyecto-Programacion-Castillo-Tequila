# GestorEncuestasCastillo - Sistema de Análisis de Datos para El Castillo de Tequila

## 1. Introducción
Solución tecnológica desarrollada en **Python con POO** para procesar y analizar datos de visitantes de El Castillo de Tequila. Desarrollado por:
- Carlos Emilio Castro Ramos (Programador)
- Jesus Israel Rodriguez Hernandez (Programador)
- Angel Gael Alvarez Lopez (Project Manager)
- Melany Regina Barrera Gaxiola (Documentadora)

**Misión:** Procesar y verificar rápidamente datos de cualquier base de datos.  
**Visión:** Empresas obtendrán análisis en menos de 1 minuto para toma de decisiones.

## 2. Problemática Resuelta
- Falta de herramientas para recolección y análisis de datos de visitantes
- Carencia de información estratégica (edad, procedencia, intereses, satisfacción)
- Imposibilidad de desarrollar estrategias personalizadas de marketing
- Pérdida de oportunidades de promoción y optimización turística

## 3. Arquitectura del Sistema
```plaintext
Proyecto/
├── src/
│   ├── models.py       # Clases Visitante y subclases
│   ├── gestor.py       # Clase GestorEncuestasCastillo
│   └── main.py         # Punto de ejecución principal
├── data/
│   └── castillo.db     # Base de datos SQLite
└── docs/               # Documentación y diagramas
```

## 4. Flujo de Procesamiento
1. **Inicio del sistema**
2. **Lectura de datos**: 
   - Importa datos de encuestas desde Google Sheets (formato CSV)
   - Verificación: `¿Existen datos en el CSV?` → Si no, muestra error
3. **Clasificación de visitantes**:
   - Crea objetos según motivo de visita:
     - `VisitanteTurismo` (contiene turismo)
     - `VisitanteNegocios` (contiene negocios)
     - `VisitanteEvento` (contiene evento)
     - `VisitanteOtro` (no coincide)
4. **Almacenamiento**: 
   - Guarda DataFrame completo en base de datos SQLite
5. **Análisis**:
   - Ejecuta análisis de mercado
   - Realiza análisis de engagement
   - Calcula correlación de opiniones
6. **Comunicación**:
   - Genera mensajes de follow-up usando polimorfismo
7. **Fin del proceso**

## 5. Tecnologías Utilizadas
| Categoría           | Herramientas                          |
|---------------------|---------------------------------------|
| Lenguaje principal  | Python 3.10+                          |
| Librerías           | pandas, sqlite3, dataclasses          |
| Control de versiones| Git/GitHub                            |
| Base de datos       | SQLite                                |
| Diagramación        | Draw.io                               |
| Entornos            | VS Code, Jupyter Notebook, Anaconda   |

## 6. Metodología de Desarrollo
1. **Análisis de requerimientos** (11-13 nov)
2. **Diseño de clases y diagramas** (14-16 nov)
3. **Desarrollo y pruebas** (17-22 nov)
4. **Documentación** (23-25 nov)
5. **Entrega final** (26 nov)

## 7. Casos de Uso

### Caso 1: Análisis de Visitantes Turísticos
1. Sistema importa datos de encuestas de Google Sheets
2. Clasifica visitantes con motivo "turismo" en `VisitanteTurismo`
3. Almacena datos en SQLite
4. Genera reporte de:
   - Procedencia geográfica
   - Nivel de satisfacción promedio
   - Actividades más populares
5. Envía mensaje personalizado con promociones de eventos locales

### Caso 2: Optimización de Eventos
1. Identifica `VisitanteEvento` en datos históricos
2. Realiza correlación entre tipo de evento y satisfacción
3. Detecta que eventos culturales tienen 40% mayor retención
4. Recomienda incrementar frecuencia de eventos culturales
5. Genera campaña de marketing dirigida a este segmento

### Caso 3: Segmentación de Negocios
1. Filtra `VisitanteNegocios` con más de 3 visitas
2. Analiza patrones de gasto y servicios utilizados
3. Identifica que 70% usa servicios de conferencias
4. Propone paquete premium para empresas frecuentes
5. Automatiza invitaciones a eventos exclusivos