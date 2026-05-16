# procesamiento-lenguaje-natural
Notas, prácticas y proyectos del curso de PLN — UPMH
#!/bin/bash
# =============================================================
#  Procesamiento del Lenguaje Natural — GitHub Repo Setup
#  Autor: jessicaromero-ctrl
#  Uso:   bash setup_pln_repo.sh
# =============================================================

set -e

REPO_NAME="procesamiento-lenguaje-natural"
DESCRIPTION="Notas, prácticas y proyectos del curso de Procesamiento del Lenguaje Natural (PLN) — UPMH"
GITHUB_USER="jessicaromero-ctrl"

echo ">>> Creando estructura local..."

mkdir -p "$REPO_NAME"
cd "$REPO_NAME"

# -----------------------------------------------------------
# Estructura de directorios por unidad
# -----------------------------------------------------------
mkdir -p \
  "unidad1-introduccion/notas" \
  "unidad1-introduccion/practica" \
  "unidad2-analisis-sintactico/notas" \
  "unidad2-analisis-sintactico/practica" \
  "unidad3-analisis-semantico/notas" \
  "unidad3-analisis-semantico/practica" \
  "unidad4-semantica-lexica/notas" \
  "unidad4-semantica-lexica/practica" \
  "unidad5-sistemas-aplicacion/notas" \
  "unidad5-sistemas-aplicacion/practica" \
  "proyecto-final" \
  "recursos"

# -----------------------------------------------------------
# .gitkeep en cada subdirectorio vacío
# -----------------------------------------------------------
find . -type d -empty -exec touch {}/.gitkeep \;

# -----------------------------------------------------------
# README principal
# -----------------------------------------------------------
cat > README.md << 'EOF'
# Procesamiento del Lenguaje Natural (PLN)

Repositorio de notas, prácticas y proyectos del curso de **Procesamiento del Lenguaje Natural**.  
Universidad Politécnica Metropolitana de Hidalgo (UPMH) — Ingeniería en IA.

---

## Estructura del repositorio

```
.
├── unidad1-introduccion/
│   ├── notas/          # Apuntes teóricos
│   └── practica/       # Ejercicios y scripts
├── unidad2-analisis-sintactico/
├── unidad3-analisis-semantico/
├── unidad4-semantica-lexica/
├── unidad5-sistemas-aplicacion/
├── proyecto-final/     # Proyecto PLN aplicado (Unidad 5.2.9)
└── recursos/           # Datasets, referencias, corpus
```

---

## Plan de estudios

### Unidad 1 — Introducción al PLN (10 h)
- 1.1 Fundamentos: conceptos básicos, relación con ML/IA, aplicaciones, desafíos éticos  
- 1.2 Preprocesamiento: limpieza, normalización, tokenización, lematización, vectorización  
- 1.3 Herramientas: NLTK, TextBlob, spaCy, Gensim, web scraping, modelos modernos  

### Unidad 2 — Análisis sintáctico y gramáticas (10 h)
- 2.1 Gramática y teoría lingüística: CFG, gramáticas de dependencias  
- 2.2 Algoritmos de parsing: CYK, Earley, análisis de dependencias y transiciones  
- 2.3 Modelado estadístico y ML: gramáticas probabilísticas, RNN, Transformers, BERT, GPT  

### Unidad 3 — Análisis semántico (12 h)
- 3.1 Ambigüedades: léxica, sintáctica, semántica, pragmática; resolución por contexto  
- 3.2 Gramáticas libres de contexto: árboles sintácticos, FrameNet, WordNet  
- 3.3 Integración sintáctico-semántica: coherencia, lógica formal, sistemas integrados  

### Unidad 4 — Semántica léxica (8 h)
- 4.1 Relaciones semánticas: sinonimia, antonimia, hiponimia, meronimia  
- 4.2 Desambiguación semántica: polisemia, algoritmos, similitud contextual  
- 4.3 Redes léxicas: WordNet, representaciones vectoriales, clasificación, sentimientos  

### Unidad 5 — Sistemas de aplicación (20 h)
- 5.1 Procesamiento de texto: corrección, resumen, traducción, generación automática  
- 5.2 Interacción y análisis: clasificación, análisis de sentimientos, chatbots, QA  
- 5.2.9 **Proyecto PLN aplicado**  

---

## Stack principal

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![spaCy](https://img.shields.io/badge/spaCy-3.x-09a3d5?logo=spacy)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-yellow?logo=huggingface)
![NLTK](https://img.shields.io/badge/NLTK-3.x-green)

---

## Autor

**Jessica Melani Romero Lora** · [@jessicaromero-ctrl](https://github.com/jessicaromero-ctrl)
EOF

# -----------------------------------------------------------
# README por unidad
# -----------------------------------------------------------
cat > unidad1-introduccion/README.md << 'EOF'
# Unidad 1 — Introducción al Procesamiento del Lenguaje Natural

**Horas:** 10 (Teoría: 5 | Práctica: 5)

## Temas
- 1.1 Fundamentos del PLN (conceptos, relación ML/IA, aplicaciones, desafíos éticos)
- 1.2 Preprocesamiento y representación de texto
- 1.3 Modelos y herramientas (NLTK, TextBlob, spaCy, Gensim, web scraping)
EOF

cat > unidad2-analisis-sintactico/README.md << 'EOF'
# Unidad 2 — Análisis Sintáctico y Gramáticas

**Horas:** 10 (Teoría: 5 | Práctica: 5)

## Temas
- 2.1 Gramática y teoría lingüística (CFG, gramáticas de dependencias)
- 2.2 Algoritmos de análisis sintáctico (CYK, Earley, transiciones)
- 2.3 Modelado estadístico y ML (RNN, Transformers, BERT, GPT)
EOF

cat > unidad3-analisis-semantico/README.md << 'EOF'
# Unidad 3 — Análisis Semántico

**Horas:** 12 (Teoría: 5 | Práctica: 7)

## Temas
- 3.1 Ambigüedades y resolución por contexto
- 3.2 Gramáticas libres de contexto, FrameNet, WordNet
- 3.3 Integración parsing + semántica, lógica formal
EOF

cat > unidad4-semantica-lexica/README.md << 'EOF'
# Unidad 4 — Semántica Léxica

**Horas:** 8 (Teoría: 4 | Práctica: 4)

## Temas
- 4.1 Relaciones semánticas (sinonimia, antonimia, hiponimia, meronimia)
- 4.2 Desambiguación semántica (polisemia, algoritmos, similitud contextual)
- 4.3 Redes léxicas (WordNet, representaciones vectoriales)
EOF

cat > unidad5-sistemas-aplicacion/README.md << 'EOF'
# Unidad 5 — Sistemas de Aplicación en Lenguaje Natural

**Horas:** 20 (Teoría: 10 | Práctica: 10)

## Temas
- 5.1 Procesamiento y mejora de texto (corrección, resumen, traducción, generación)
- 5.2 Interacción y análisis (clasificación, sentimientos, chatbots, QA)
- 5.2.9 Proyecto PLN aplicado
EOF

# -----------------------------------------------------------
# .gitignore
# -----------------------------------------------------------
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*.egg-info/
dist/
build/
.eggs/
*.egg

# Entornos virtuales
.venv/
env/
venv/

# Jupyter
.ipynb_checkpoints/
*.ipynb_checkpoints

# Datos y modelos grandes
*.csv
*.pkl
*.h5
*.bin
*.pt
*.pth
data/raw/
models/

# IDEs
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# Variables de entorno
.env
EOF

# -----------------------------------------------------------
# requirements.txt base
# -----------------------------------------------------------
cat > requirements.txt << 'EOF'
# PLN — Herramientas principales
nltk>=3.8
textblob>=0.18
spacy>=3.7
gensim>=4.3
transformers>=4.40
torch>=2.2
scikit-learn>=1.4
pandas>=2.1
numpy>=1.26
matplotlib>=3.8
seaborn>=0.13
beautifulsoup4>=4.12
requests>=2.31
jupyter>=1.0
EOF

# -----------------------------------------------------------
# Inicializar git y primer commit
# -----------------------------------------------------------
git init
git add .
git commit -m "feat: estructura inicial del repositorio PLN

- Árbol de directorios por unidad (U1–U5)
- READMEs con plan de estudios completo
- .gitignore y requirements.txt base"

echo ""
echo ">>> Estructura local lista. Ahora ejecuta:"
echo ""
echo "  gh repo create $GITHUB_USER/$REPO_NAME \\"
echo "    --public \\"
echo "    --description \"$DESCRIPTION\" \\"
echo "    --source=. \\"
echo "    --remote=origin \\"
echo "    --push"
echo ""
echo ">>> O si prefieres HTTPS sin gh CLI:"
echo ""
echo "  git remote add origin https://github.com/$GITHUB_USER/$REPO_NAME.git"
echo "  git branch -M main"
echo "  git push -u origin main"
echo ""
echo ">>> ¡Listo! Repo en: https://github.com/$GITHUB_USER/$REPO_NAME"
