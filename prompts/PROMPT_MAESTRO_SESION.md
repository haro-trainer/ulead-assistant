# PROMPT MAESTRO: CONSTRUCCIÓN DE CONTENIDO DE SESIÓN
## Skill complementario: session-content-builder

---

## 🎯 INSTRUCCIÓN PRINCIPAL

Eres un experto en diseño instruccional universitario. Tu tarea es convertir un plan de sesión/clase en TODO EL MATERIAL que el profesor necesita para impartirla:
- Agenda detallada con bloques de 45-50 minutos
- Slides/presentación (outline o PPTX)
- Notas del profesor (dificultades, explicaciones alternativas, timing)
- Guía del estudiante (antes/durante/después)
- Actividades prácticas con entregables
- Quiz formativo (sin calificación, para medir aprendizaje)
- Recursos y bibliografía

**Si tienes cargada la skill `session-content-builder`, actívala y sigue su flujo de trabajo usando las referencias pedagógicas y plantillas incluidas.**

**Si NO tienes la skill cargada**, sigue las instrucciones de este prompt que contienen el proceso completo equivalente.

Principio clave: todo artefacto debe poder trazarse a un bloque, objetivo o actividad del plan original. No generes contenido desalineado del plan.

---

## ENTRADA REQUERIDA: 7 CAMPOS OBLIGATORIOS

### 1️⃣ INFORMACIÓN DE LA SESIÓN

```
Nombre Sesión: [nombre claro]
Número: [Sesión X de Y]
Duración Total: [horas]
Formato: [Sincrónica/Asincrónica/Híbrida]
Tipo: [Teórica/Práctica/Mixta]
Fecha Programada: [fecha]
Plataforma: [Zoom/Teams/Presencial/LMS]
```

**Ejemplo:**
```
Nombre: Natural Language Processing & Transformer Architecture
Número: Sesión 1 de 4
Duración: 4 horas (incluye 2 descansos de 10 min)
Formato: Sincrónica (en vivo)
Tipo: Mixta (60% teoría, 40% práctica)
Fecha: 2026-08-05, 14:00-18:00 CST
Plataforma: Zoom + Colab notebooks
```

---

### 2️⃣ ALINEAMIENTO A LEARNING OUTCOMES

```
Learning Outcomes que Cubre:
  [LO #X: descripción exacta del syllabus]
  [LO #Y: descripción exacta del syllabus]
  [LO #Z: descripción exacta del syllabus]

Bloom's Level:
  - [LO #X → L2 (Understand)]
  - [LO #Y → L3 (Apply)]
  - [LO #Z → L4 (Analyze)]
```

**Ejemplo:**
```
Learning Outcomes:
  [LO #1: Explicar evolución de NLP desde LSTM a Transformers]
  [LO #2: Identificar componentes clave de arquitectura Transformer]
  [LO #3: Aplicar tokenización a textos reales]

Bloom's:
  - LO #1 → L2 (Understand)
  - LO #2 → L2 (Understand)
  - LO #3 → L3 (Apply)
```

---

### 3️⃣ TEMARIO DETALLADO POR BLOQUE

Dividi tu sesión en bloques de 45-50 minutos (con descansos):

```
BLOQUE 1 [Minutos 0-45]: [NOMBRE]
─────────────────────────────────
Duración: 45 minutos
Tipo: [Presentación/Demo/Ejercicio/Discusión]
Temas a Cubrir:
  - [Tema 1 con subtemas]
  - [Tema 2 con subtemas]
  - [Tema 3 con subtemas]

Recursos Necesarios:
  - [Recurso 1]
  - [Recurso 2]

Actividad Principal:
  [Qué harán los estudiantes en este bloque]

Preguntas de Transición:
  - [Pregunta 1 para enganche]
  - [Pregunta 2 para reflexión]

─────────────────────────────────
DESCANSO [Minutos 45-50]: 5 minutos
─────────────────────────────────

BLOQUE 2 [Minutos 50-95]: [NOMBRE]
[Repetir mismo formato]

DESCANSO [Minutos 95-100]: 5 minutos

[Continuar...]
```

**Ejemplo COMPLETO:**

```
BLOQUE 1 [0-45 min]: Evolución NLP y Motivación Transformers
──────────────────────────────────────────────────────────
Duración: 45 minutos
Tipo: Presentación + interacción

Temas:
  1. ¿Por qué NLP es difícil? (contexto, ambigüedad)
  2. Evolución: Bag-of-Words → RNN/LSTM → Attention → Transformers
  3. Limitaciones de LSTM: gradiente desvaneciente, secuencial lento
  4. Insight: Attention is All You Need (Vaswani 2017)

Recursos:
  - Slide 1-10 (PDF incluido)
  - Video "Attention is All You Need" (3 min clip)
  - Código: LSTM vs Transformer speed comparison (Colab)

Actividad Principal:
  - Mostrar misma frase en LSTM vs Transformer
  - Profesor: "¿Cuál es más rápido?" → estudiantes adivinan
  - Revelar: Transformer 100x más rápido en batch
  - Muestra cómo LSTM procesa secuencialmente vs Transformer paralelo

Preguntas Transición:
  - "¿Ven por qué secuencial es lento?"
  - "¿Qué problema resuelve poder procesar TODO en paralelo?"

──────────────────────────────────────────────────────────
DESCANSO: 5 minutos (15:45-15:50)
──────────────────────────────────────────────────────────

BLOQUE 2 [50-95 min]: Arquitectura Transformer en Profundidad
──────────────────────────────────────────────────────────
Duración: 45 minutos
Tipo: Presentación + Demo interactiva

Temas:
  1. Embedding + Positional Encoding
  2. Multi-Head Attention (Query/Key/Value)
  3. Feed-Forward Network
  4. Decoder (brief overview)

Recursos:
  - Slides 11-25
  - Transformer diagram (ilustrado Alammar)
  - Interactive Jupyter: "Attention Weights Visualizer"

Actividad Principal:
  - DEMO EN VIVO: Mostrar cómo attention pesa palabras
  - Ejemplo: frase "El gato se comió el ratón en la sala"
  - Visualizar attention weights: "gato" → "se comió" (high weight)
  - Estudiantes predicen: ¿A qué palabras attendería "lo"?

Preguntas Transición:
  - "¿Ven cómo cada palabra 'mira' a TODAS las otras?"
  - "¿Por qué multi-HEAD es mejor que single attention?"
```

---

### 4️⃣ ACTIVIDADES Y EJERCICIOS PRÁCTICOS

```
ACTIVIDAD 1: [Nombre]
─────────────────────
Duración: [minutos]
Formato: [Individual/Parejas/Grupo]
Plataforma: [Zoom breakout / Notebook / Chat / Documento]
Objetivo: [Qué aprenden con esto]

Instrucciones:
[1-2 párrafos claros de qué hacer]

Entregable:
[Qué deben mostrar al final]

Ejemplo Solución:
[Mostrar 1 ejemplo de respuesta correcta]

─────────────────────

ACTIVIDAD 2: [Nombre]
[Repetir formato]
```

**Ejemplo:**
```
ACTIVIDAD 1: Tokenizador Comparativo
─────────────────────────────────────
Duración: 15 minutos
Formato: Individual + plenaria
Plataforma: Notebook Colab compartido
Objetivo: Entender impacto tokenización en precisión

Instrucciones:
1. Abrí Colab notebook compartido
2. Tenés una frase en español: "¿Cómo estás? ¡Muy bien!"
3. Aplica 3 tokenizadores (espacio, BPE, SentencePiece)
4. Observa: ¿Cuántos tokens genera cada uno?
5. Predice: ¿Cuál es más eficiente para textos cortos?
6. Anota tu predicción en el chat

Entregable:
- Screenshot de los 3 resultados en tu notebook
- Respuesta en chat: "Tokenizador X es mejor porque..."

Solución Esperada:
Espacio: 6 tokens (simple, pierde info)
BPE: 8 tokens (balance)
SentencePiece: 4 tokens (más eficiente)
→ Respuesta: "SentencePiece es mejor para textos cortos"
```

---

### 5️⃣ NOTAS DEL PROFESOR (Teaching Notes)

```
NOTAS PEDAGÓGICAS
═════════════════

Dificultades Esperadas:
  - [Concepto 1 que estudiantes suelen no entender]
  - [Concepto 2 que causa confusión]

Explicaciones Alternativas:
  Para [Concepto], si ven caras raras:
  - Explicación A (más técnica)
  - Explicación B (más visual)
  - Analogía C (mundo real)

Errores Comunes:
  - [Error 1 que cometen]: Solución es...
  - [Error 2 que cometen]: Solución es...

Timing Real:
  - Este bloque SUELE tomar +10 min si haces muchas preguntas
  - Si te atrasas, puedes saltar [Tema X, ya está en lectura]

Variaciones por Nivel:
  - Estudiantes avanzados: pregunta sobre [tema avanzado]
  - Estudiantes básicos: salta [tema avanzado], enfócate en [lo esencial]

Engagement Tips:
  - [Pregunta/actividad que genera discusión]
  - [Demostración interactiva]
  - [Anécdota/historia relevante]

Recursos Contingencia:
  Si [problema técnico], alternativa es [recurso alternativo]
```

**Ejemplo:**
```
NOTAS PEDAGÓGICAS
═════════════════

Dificultades Esperadas:
  - Self-attention es MUY abstracto al inicio
  - Confunden Query/Key con búsqueda literal
  - No entienden por qué "multi-head" es mejor que uno solo

Explicaciones Alternativas:
Para Self-Attention:
  Explicación Técnica: "Cada token genera Q, K, V. Se calcula 
  dot(Q, K) normalizado, se multiplica por V → output"
  
  Explicación Visual: "Piensa que cada palabra hace PREGUNTAS (Q) 
  a todas las otras. Esas responden (K,V). Se promedia."
  
  Analogía Real: "Como cuando en reunión, alguien pregunta algo 
  (Q), miras a quien tiene la respuesta (K), y escuchas su 
  perspectiva (V). Haces esto con TODOS simultáneamente"

Errores Comunes:
  - Error: "Query es una búsqueda de BD"
    Solución: "No, Query es solo 'parámetros' de atención. 
    No busca nada, es matemática pura"
  
  - Error: "Multi-head es para paralelizar"
    Solución: "No realmente, es porque diferentes heads capturan 
    diferentes patrones (sintaxis, semántica, dependencias, etc)"

Timing Real:
  - Este bloque TIPICAMENTE toma 50 min (no 45)
  - Si te atrasas, puedes congelar explicación de positional encoding

Variaciones:
  Avanzados: pregunta "¿Cómo se comparan cosine similarity vs dot product?"
  Básicos: salta análisis de diferentes attention patterns

Engagement:
  - Cuando expliques attention, pide: "¿A cuál palabra miraría 
    el LLM aquí?" → predicciones → revelar gráfico
  - Demo en vivo > cualquier slide
```

---

### 6️⃣ GUÍA DEL ESTUDIANTE (Student Guide)

```
ANTES DE LA SESIÓN:
──────────────────
Materiales a leer/ver:
  - [Lectura 1, tiempo: X minutos]
  - [Video X, tiempo: Y minutos]
  - [Opcional pero recomendado: Z]

Conceptos Previos Necesarios:
  Debes entender: [Concepto 1], [Concepto 2]
  Si no estás seguro, repasa [Recurso A]

Preparación Técnica:
  - Necesitarás: [Software/Herramienta 1]
  - Asegúrate de: [Requisito 1]
  - Link Colab: [URL]

DURANTE LA SESIÓN:
──────────────────
Agenda:
  [Tabla: Hora | Bloque | Qué hacer]

Materiales Disponibles:
  - Slides (PDF)
  - Notebook con ejercicios
  - Chat para preguntas
  - Breakout rooms para discusiones

Cómo Participar:
  - Levanta mano (Zoom) para preguntas
  - Responde polls
  - Prueba código en tu copia del notebook

DESPUÉS DE LA SESIÓN:
────────────────────
Actividades de Refuerzo:
  - [Lectura 1]
  - [Ejercicio extra]
  - [Video explicativo]

Preguntas Reflexivas:
  - ¿Podés explicar [concepto] en tus palabras?
  - ¿Dónde ves aplicación de [concepto] en tu trabajo?
  - Si cambio [parámetro], ¿qué pasa?

Recursos Adicionales:
  - Artículo seminal: [Link]
  - Tutorial: [Link]
  - Q&A disponible en [lugar]
```

---

### 7️⃣ QUIZ FORMATIVO Y CIERRE

```
QUIZ FORMATIVO (sin calificación, solo para medir aprendizaje)
──────────────────────────────────────────────────────────

Pregunta 1: [Tipo: MC / V-F / Corta]
Respuesta: [Correcta es...]
Explicación: [Por qué es esa]

[Repetir preguntas 2-5]

CIERRE DE SESIÓN
─────────────────
Resumen en 2-3 minutos:
  - [Punto clave 1]
  - [Punto clave 2]
  - [Conexión a próxima sesión]

Reflección Final:
  "¿Qué fue lo más importante que aprendiste hoy?"
  [Esperar respuestas]

Previsualización Próxima Sesión:
  "La próxima sesión exploraremos [tema]. Traemos las 
  ideas de hoy y las combinamos con [nuevo concepto]"
```

---

## 📋 CÓMO ENVIAR ESTE PROMPT

**COPIA TODO (7 secciones) EN UN SOLO MENSAJE**

Yo:
1. Valido integridad
2. Activo skill `session-content-builder`
3. Genero paquete COMPLETO:
   - Slides profesionales (PPTX)
   - Agenda detallada (PDF)
   - Notas profesor (DOCX)
   - Guía estudiante (PDF)
   - Notebook con ejercicios (IPYNB)
   - Quiz (PDF interactivo)
4. Te entrego en 20-30 minutos

---

## ✅ CHECKLIST ANTES DE ENVIAR

```
☐ Nombre sesión específico (no "Sesión 1")
☐ Duración realista (45-50 min por bloque)
☐ Learning Outcomes alineados a syllabus
☐ Bloques tienen temas, actividades, preguntas
☐ Actividades tienen entregables claros
☐ Notas profesor abordan dificultades reales
☐ Guía estudiante es usable por estudiantes reales
☐ Quiz es representativo de LO
☐ Transición a próxima sesión es clara
```

---

**Versión:** 1.0  
**Para:** ULEAD Sessions  
**Skill:** session-content-builder  
**Output:** Slides + Guide + Notes + Quiz
