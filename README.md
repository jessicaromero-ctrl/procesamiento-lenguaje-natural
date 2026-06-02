# PLN — Procesamiento de Lenguaje Natural · Primer Corte
 
> **Materia:** Procesamiento de Lenguaje Natural  
> **Programa:** Maestría en Ingeniería en Inteligencia Artificial (Especialidad Big Data)  
> **Institución:** Universidad Politécnica Metropolitana de Hidalgo (UPMH)  
> **Docente:** M.C. Pablo Ricardo Sánchez Gómez  
> **Ciclo escolar:** 2025–2026  
 
---
 
## Integrantes
 
| Matrícula | Nombre completo | Grupo |
|-----------|-----------------|-------|
| 253220116 | Romero Lora, Jessica Melani | 3° A |
| 253220020 | Santos Martínez, Víctor Manuel | 3° A |
 
---
 
## Descripción del repositorio
 
Este repositorio concentra los entregables del **primer corte** de la materia *Procesamiento de Lenguaje Natural*, correspondientes a tres componentes evaluativos: prácticas en clase, mini retos y el proyecto integrador. El hilo conductor de todos los entregables es el análisis computacional de texto en español con énfasis en corpus institucionales de dominio específico.
 
---
 
## Estructura del repositorio
 
```
PLN/
├── Bitácora Integradora/
│   └── 253220116_RomeroLora_JessicaMelani_PLN_Corte01_Bitacora.pdf
│
├── Mini retos/
│   ├── files mini reto 1 y 2.zip          # Salidas: BoW, TF, TF-IDF, similitud coseno
│   ├── PLN_Clase2_codigo_datos_salidas.zip
│   ├── PLN_Clase3_A.zip
│   ├── PLN_Clase4_Kaggle_Modelos_codigo_datos_salidas_A.zip
│   └── 253220116_Romero y Santos_…_Producto_Corte01.pdf
│
├── Practicas en Clase/
│   ├── Clase 01 primeras actividades/
│   │   ├── 253220116-253220020_Romero-Santos_…_Practica01_Corte01.pdf
│   │   └── Cuestionario diagnóstico.pdf
│   ├── Clase_4_PLN_UPMH_3roA_Kaggle_Modelos.pptx.zip
│   └── files clase 04 practica.zip
│
└── Proyecto Integrador 1er Corte/
    └── 01_pipeline_primer_corte.ipynb      # Pipeline principal (Jupyter)
```
 
---
 
## Proyecto Integrador — Detección de Tema en Chats de Atención Ciudadana (RUTS Hidalgo)
 
### Motivación
 
La Subdirección de Atención Ciudadana del **RUTS** (Registro Único de Trámites y Servicios del Estado de Hidalgo) atiende diariamente consultas vía chat sobre trámites heterogéneos: registro civil, placas vehiculares, predial, becas, avisos sanitarios, entre otros. Estas conversaciones se archivan sin clasificación temática sistemática, lo que impide análisis de demanda, priorización de recursos y auditoría de calidad del servicio. Este proyecto aborda la tarea como un problema de **detección de tema** (*topic detection*) sobre texto corto en español de dominio gubernamental.
 
### Objetivo general
 
Construir un corpus anonimizado de conversaciones ciudadanas y establecer una representación vectorial del texto que sirva de base para un clasificador temático multi-clase en cortes posteriores.
 
### Pipeline (Corte 1)
 
El pipeline está implementado íntegramente en `01_pipeline_primer_corte.ipynb` e invoca el módulo reproducible `src/pipeline.py`.
 
| Etapa | Descripción técnica |
|-------|---------------------|
| **1. Construcción del corpus** | Concatenación de mensajes del visitante por conversación; un documento = una sesión de chat |
| **2. Anonimización (LGPDPSO)** | Sustitución de PII estructurada: `[NOMBRE]`, `[EMAIL]`, `[CURP]`, `[RFC]`, `[TEL]`, `[NUM]`; descarte de chats con < 3 tokens útiles |
| **3. Etiquetado por supervisión débil** | Prioridad (1) señal fuerte: término de búsqueda del *referer*; prioridad (2) señal débil: coincidencia de palabras clave de taxonomía |
| **4. Normalización y tokenización** | Minúsculas → eliminación de acentos (Unicode NFKD) → filtrado no-alfabético → tokenización por espacio → remoción de *stopwords* de chat |
| **5. Exploración del corpus** | Estadísticas globales, distribución de etiquetas, histograma de longitud, top-20 términos por TF y por TF-IDF, términos discriminativos por categoría |
| **6. Guardado** | Corpus serializado en CSV (`id`, `texto`, `etiqueta`) + vocabulario con frecuencias |
 
### Taxonomía de categorías
 
| Etiqueta | Trámites representativos |
|----------|--------------------------|
| `registro_civil` | Actas de nacimiento, matrimonio, defunción, divorcio; CURP |
| `vehicular` | Placas, verificación, infracciones, tenencia, cambio de propietario |
| `impuestos_predial` | Predial, declaración patrimonial, contribuciones municipales |
| `educacion` | Becas, equivalencias, kardex, títulos |
| `empleo` | Bolsa de trabajo, IMSS, constancias laborales |
| `salud_sanitario` | Avisos sanitarios, COFEPRIS, licencias sanitarias |
| `sin_clasificar` | Sin señal suficiente; pendiente de revisión manual (Corte 2) |
 
### Métricas mínimas del corte
 
- ≥ 300 documentos con etiqueta temática válida  
- Vocabulario único documentado  
- PII estructurada residual = 0 filas  
---
 
## Mini Retos
 
### Mini Reto 1 & 2 — Representación Vectorial del Texto
 
Corpus de trabajo: comentarios de retroalimentación académica en español.
 
| Salida | Descripción |
|--------|-------------|
| `01_preprocesamiento.csv` | Texto original → texto limpio → tokens útiles |
| `02_matriz_bow.csv` | Representación Bag-of-Words (conteos absolutos) |
| `03_matriz_tf.csv` | Frecuencia de término normalizada por documento |
| `04_matriz_tfidf.csv` | Ponderación TF-IDF sobre el corpus completo |
| `05_top_terminos_tfidf.csv` | Términos con mayor peso TF-IDF por documento |
| `06_similitud_documentos.csv` | Similitud coseno entre pares de documentos |
 
### Mini Reto 4 — Clasificación de Texto con Modelos Clásicos (Kaggle)
 
Pipeline de clasificación multi-clase con vectorización TF-IDF y comparación de cuatro clasificadores:
 
- `MultinomialNB` — Naive Bayes multinomial  
- `ComplementNB` — Naive Bayes complementario (robusto ante desbalance)  
- `LogisticRegression` — Regresión logística (regularización L2)  
- `LinearSVC` — Máquina de Vectores de Soporte lineal  
**Salidas del mini reto:** métricas por modelo (`accuracy`, `precision`, `recall`, `F1`), matriz de confusión por clasificador, archivo de errores de predicción y reporte comparativo en CSV.
 
**Ejecución:**
```bash
conda activate pln311
python clasificacion_texto_kaggle_clase4.py \
  --csv datos/comentarios_ampliados_clase4.csv \
  --text-col texto --label-col categoria \
  --output-dir salidas_clase4
```
 
---
 
## Entorno de ejecución
 
| Componente | Versión / detalle |
|------------|-------------------|
| Python | 3.11 (Miniconda, entorno `pln311`) |
| pandas | ≥ 2.0 |
| scikit-learn | ≥ 1.4 |
| matplotlib / seaborn | última estable |
| Jupyter Notebook | ejecutado en VS Code + Google Colab |
 
**Instalación de dependencias:**
```bash
conda activate pln311
pip install -r requirements_clase4.txt
```
 
---
 
## Consideraciones éticas y de privacidad
 
El corpus de chats ciudadanos contiene información personal sensible. El pipeline implementa anonimización automatizada conforme a la **Ley General de Protección de Datos Personales en Posesión de Sujetos Obligados (LGPDPSO)** vigente en México. Todo dato personal identificable es sustituido por marcadores semánticos antes de cualquier análisis o almacenamiento intermedio. El corpus resultante no contiene PII directa verificada.
 
---
 
## Trabajo futuro (Cortes 2 y 3)
 
- Etiquetado manual de la partición `sin_clasificar` para alcanzar 1,000 documentos anotados  
- Entrenamiento y evaluación del clasificador temático multi-clase  
- Análisis de sesgo por categoría minoritaria (`empleo`, `salud_sanitario`) con estrategias de balanceo  
- Evaluación de representaciones semánticas densas (Word2Vec, FastText para español)  
---
 
## Licencia
 
Repositorio de uso académico interno. Queda prohibida su reproducción o distribución sin autorización expresa de los autores y de la institución. Los datos del corpus ciudadano son propiedad del RUTS/Gobierno del Estado de Hidalgo y están sujetos a la normativa de datos abiertos aplicable.
 
---
 
*Universidad Politécnica Metropolitana de Hidalgo · Ingeniería en Inteligencia Artificial · 2025–2026*
