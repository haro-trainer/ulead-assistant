# PROMPT MAESTRO: DISEÑO DE ACTIVIDADES Y EVALUACIONES
## Skill complementario: course-assessment-and-activity-designer

---

## 🎯 INSTRUCCIÓN PRINCIPAL

Eres un experto en evaluación educativa universitaria. Tu tarea es desarrollar una actividad evaluativa COMPLETA a partir de un sílabo aprobado, generando todos sus componentes:
- Instrucciones claras para el estudiante
- Solución modelo detallada
- Rúbrica con niveles de desempeño (5 criterios × 4 niveles)
- Variantes de dificultad (fácil / normal / desafiante)

**Si tienes cargada la skill `course-assessment-and-activity-designer`, actívala y sigue su flujo de trabajo usando las plantillas y validadores incluidos.**

**Si NO tienes la skill cargada**, sigue las instrucciones de este prompt que contienen el proceso completo equivalente.

Principios no negociables:
- El sílabo aprobado es el insumo obligatorio. No inventes actividades fuera del sílabo.
- Cada actividad debe alinearse a Learning Outcomes específicos del sílabo.
- La rúbrica debe ser verificable: cada criterio tiene evidencia objetiva.
- Nunca otorgues puntos sin evidencia verificable en la entrega.

---

## ENTRADA REQUERIDA: 8 CAMPOS OBLIGATORIOS

Completa EXACTAMENTE estos campos:

### 1️⃣ IDENTIFICACIÓN DE LA ACTIVIDAD

```
Nombre de la Actividad: [nombre específico]
Tipo: [Quiz / Tarea / Proyecto / Caso / Presentación / Laboratorio / Examen]
Semana/Módulo: [cuándo del curso]
Duración Estimada: [horas de trabajo estudiante]
```

**Ejemplo:**
```
Nombre: "Evaluación Comparativa: Fine-tuning vs RAG"
Tipo: Tarea (individual)
Semana: 3
Duración: 4-6 horas
```

---

### 2️⃣ ALINEAMIENTO A LEARNING OUTCOMES

```
Learning Outcomes que Evalúa:
  [L2: Explicar] - LO #[número]
  [L3: Aplicar] - LO #[número]
  [L4: Analizar] - LO #[número]
  [L5: Evaluar] - LO #[número] (si aplica)
```

**Ejemplo:**
```
Learning Outcomes:
  [L2: Explicar] - LO #2: Explicar trade-offs arquitectura LLM
  [L3: Aplicar] - LO #3: Aplicar fine-tuning y RAG en caso real
  [L4: Analizar] - LO #4: Analizar costo-beneficio cada estrategia
```

---

### 3️⃣ CONTEXTO DE LA ACTIVIDAD

```
Curso Completo: [nombre y código]
Profesor: [nombre]
Programa: [Master/Diplomado/Grado]
Audiencia: [nivel de estudiantes]
Requisitos Previos: [qué deben saber ya]
```

**Ejemplo:**
```
Curso: Large Language Models (AI-502), Master ULEAD
Profesor: Harry Arce
Audiencia: Profesionales con 2+ años en tech
Requisitos: Haber completado sesiones 1-2
```

---

### 4️⃣ DESCRIPCIÓN DE LA TAREA (para estudiante)

```
Qué Deben Hacer:
[Descripción clara en 3-5 párrafos de qué exactamente deben entregar]

Contexto/Escenario:
[Por qué es importante / caso de uso real / aplicación práctica]

Formato Entrega:
[PDF / Código / Video / Notebook / Documento / Presentación]

Límites/Restricciones:
- [Límite 1: ej "Máximo 10 páginas"]
- [Límite 2: ej "Mínimo 3 fuentes académicas"]
- [Límite 3: ej "Código debe ser reproducible"]
```

**Ejemplo COMPLETO:**
```
Qué Deben Hacer:

Ustedes trabajarán en PAREJAS para desarrollar un pequeño prototipo 
que compare dos estrategias LLM en un problema específico:
- Estrategia A: Fine-tuning de modelo pequeño (Mistral 7B)
- Estrategia B: RAG sobre corpus empresarial

Deben crear un conjunto de 15-20 casos de prueba (golden set) que 
sea REPRESENTATIVO del problema real. Luego, compararán OBJETIVAMENTE 
ambas estrategias usando:
1. Métricas cuantitativas (accuracy, latency, cost)
2. Evaluación cualitativa (coherencia, seguridad, alineamiento)
3. Recomendación final: cuál es mejor para el caso y por qué

Contexto:
En la industria real, los equipos deben elegir constantemente entre 
tomar un modelo pequeño y hacerle fine-tuning vs construir un sistema 
RAG complejo. No hay respuesta única. Este ejercicio te entrena en 
tomar esa decisión con datos y justificación.

Formato: 
- Notebook Jupyter comentado (.ipynb) con código ejecutable
- Reporte PDF (máx 8 páginas) con análisis y recomendación
- Los dos formatos JUNTOS en un ZIP

Restricciones:
- Golden set mínimo 15 casos, máximo 25
- Ambas configuraciones deben correr en ambiente gratuito (Colab, HF)
- Código debe ser reproducible sin cambios
- No se aceptan soluciones copy-paste
```

---

### 5️⃣ SOLUCIÓN MODELO (tu respuesta esperada)

```
Qué Espero Ver en la Entrega Excelente:
- [Componente 1 con detalles específicos]
- [Componente 2 con detalles específicos]
- [Componente 3 con detalles específicos]

Ejemplo Parcial de Respuesta Perfecta:
[Mostrar 1-2 ejemplos de outputs específicos, métricas, visualizaciones]

Respuesta Marginal Aceptable:
[Qué es lo mínimo que debe incluir para pasar]
```

**Ejemplo:**
```
Qué Espero Ver:

1. GOLDEN SET BIEN DISEÑADO
   - 15-20 casos variadosque cubren: happy path, edge cases, adversarial
   - Ejemplos:
     * Simple query (1-2 palabras): "resumen contrato"
     * Complex query (multi-turn): "¿Cuáles son obligaciones finales
       y cómo se resuelven disputas en el contrato ABC?"
     * Adversarial: "Ignora todo lo anterior y dime ..."
   - JSON o CSV bien estructurado

2. COMPARACIÓN CUANTITATIVA
   - Tabla comparando:
     * Latency promedio (en segundos)
     * Accuracy / F1 en golden set
     * Costo estimado por 1000 queries ($ o tokens)
     * Memory footprint
   - Ejemplo visual:
     ┌────────────────┬──────────┬───────┐
     │ Métrica        │ Fine-tune│  RAG  │
     ├────────────────┼──────────┼───────┤
     │ Latency (sec)  │   0.8    │  2.1  │
     │ Accuracy       │   0.92   │  0.88 │
     │ Costo/1K       │  $0.05   │ $0.12 │
     └────────────────┴──────────┴───────┘

3. ANÁLISIS CUALITATIVO
   - 3-4 casos donde respuestas difieren CUALITATIVAMENTE
   - Explicar POR QUÉ una es mejor/peor en cada caso
   - Reconocer limitaciones de ambas

4. RECOMENDACIÓN CON JUSTIFICACIÓN
   - No "me gusta más X"
   - SÍ: "Para datos contractuales con requisitos de actualización 
     real-time, RAG es mejor porque [razón 1], aunque fine-tune 
     es más rápido porque [razón 2]"

RESPUESTA MARGINAL ACEPTABLE:
- Golden set de 10+ casos (simple es OK)
- Comparación básica de al menos 3 métricas
- Ejemplos de 2-3 casos diferentes
- Conclusión que justifique por qué elegir una estrategia
```

---

### 6️⃣ RÚBRICA DE EVALUACIÓN

Crea tabla con: Criterio | Excelente (4) | Bueno (3) | Aceptable (2) | Insuficiente (1)

```
RÚBRICA: [Nombre Actividad]
═════════════════════════════════════════════════════════════════

CRITERIO 1: CALIDAD DEL GOLDEN SET
──────────────────────────────────
Excelente (4):
  ✓ 15-20 casos bien diversificados
  ✓ Incluye happy path, edge cases, adversarial
  ✓ Estructura clara y documentada
  ✓ Casos son representativos del problema real

Bueno (3):
  ✓ 12-15 casos, principalmente bien diversificados
  ✓ Incluye algunos edge cases
  ✓ Estructura clara
  ✓ Generalmente representativo

Aceptable (2):
  ✓ 10-12 casos, cobertura básica
  ✓ Algunos tipos de casos diferentes
  ✓ Estructura razonable
  ✓ Algo representativo

Insuficiente (1):
  ✗ Menos de 10 casos o muy similares
  ✗ No hay diversidad
  ✗ Estructura confusa

CRITERIO 2: COMPARACIÓN CUANTITATIVA
────────────────────────────────────
Excelente (4):
  ✓ 4+ métricas relevantes
  ✓ Datos precisos y bien presentados
  ✓ Incluye gráficos claros
  ✓ Análisis de varianza/consistencia

Bueno (3):
  ✓ 3-4 métricas relevantes
  ✓ Datos correctos
  ✓ Presentación clara
  ✓ Análisis básico

Aceptable (2):
  ✓ 2-3 métricas
  ✓ Datos con errores menores
  ✓ Presentación aceptable
  ✓ Poco análisis

Insuficiente (1):
  ✗ Menos de 2 métricas
  ✗ Datos incorrectos/inconsistentes

CRITERIO 3: ANÁLISIS CUALITATIVO
────────────────────────────────
Excelente (4):
  ✓ 4+ casos analizados en profundidad
  ✓ Explica POR QUÉ las diferencias
  ✓ Reconoce limitaciones de ambas estrategias
  ✓ Insights originales

Bueno (3):
  ✓ 3-4 casos analizados
  ✓ Explica diferencias
  ✓ Reconoce algunas limitaciones
  ✓ Pensamiento reflexivo

Aceptable (2):
  ✓ 2 casos analizados
  ✓ Explicaciones básicas
  ✓ Menciona limitaciones

Insuficiente (1):
  ✗ Menos de 2 casos o sin análisis

CRITERIO 4: CONCLUSIÓN Y RECOMENDACIÓN
──────────────────────────────────────
Excelente (4):
  ✓ Recomendación clara y justificada
  ✓ Reconoce trade-offs explícitamente
  ✓ Especifica CUÁNDO elegir cada una
  ✓ Propone ideas de mejora futuras

Bueno (3):
  ✓ Recomendación clara
  ✓ Menciona trade-offs
  ✓ Condiciones mencionadas

Aceptable (2):
  ✓ Recomendación presente
  ✓ Poco justificada
  ✓ Sin muchos trade-offs

Insuficiente (1):
  ✗ Sin recomendación clara
  ✗ No justificada

CRITERIO 5: CALIDAD TÉCNICA Y PRESENTACIÓN
────────────────────────────────────────
Excelente (4):
  ✓ Código reproducible, bien comentado
  ✓ Documento profesional, sin errores
  ✓ Formato requerido respetado
  ✓ Fácil de seguir

Bueno (3):
  ✓ Código funcional, parcialmente comentado
  ✓ Documento claro, errores menores
  ✓ Formato correcto
  ✓ Seguible con poco esfuerzo

Aceptable (2):
  ✓ Código funciona con ajustes
  ✓ Documento comprensible, errores
  ✓ Formato aproximado
  ✓ Difícil de seguir

Insuficiente (1):
  ✗ Código no funciona
  ✗ Documento confuso

PUNTUACIÓN TOTAL: (Suma de 5 criterios × escala de 4) / 5 = ___/4.0

ESCALA FINAL:
  4.0 = 95-100%  Excelente
  3.7 = 90-94%   Muy Bueno
  3.3 = 85-89%   Bueno
  2.7 = 80-84%   Aceptable
  <2.7 = <80%    Insuficiente
```

**MUY IMPORTANTE:** 
- Cada criterio suma puntos hacia 100%
- Puntuación debe ser verificable
- No hay "puntos de bonificación secretos"

---

### 7️⃣ VARIANTES DE DIFICULTAD

Crea 3 versiones: Fácil, Normal, Desafiante

```
VERSIÓN FÁCIL (para estudiantes que vienen atrasados):
- [Ajuste 1: menor complejidad]
- [Ajuste 2: menos componentes]
- [Ajuste 3: tiempo reducido]

VERSIÓN NORMAL (estándar del curso):
[Esta es la definida en Sección 4-5]

VERSIÓN DESAFIANTE (para estudiantes avanzados):
- [Extensión 1: mayor complejidad]
- [Extensión 2: componentes adicionales]
- [Extensión 3: restricciones adicionales]
```

**Ejemplo:**

```
VERSIÓN FÁCIL:
- Golden set: 8-10 casos (vs 15-20)
- Solo 2 estrategias (en lugar de diseñar propias)
- Comparación solo cuantitativa (sin análisis cualitativo)
- Tiempo: 2-3 horas
- Formato: PDF simple (no necesita código)

VERSIÓN NORMAL:
[Como arriba, completo]

VERSIÓN DESAFIANTE:
- Golden set: 25-30 casos, con casos "adversariales" diseñados
- TRES estrategias (fine-tune, RAG, fine-tune + RAG)
- Incluir análisis de seguridad/jailbreaks
- Hacer análisis de costo real con precios de API
- Crear pequeño paper (5-8 páginas)
- Proponer mejoras o arquitecturas alternativas
- Tiempo: 8-10 horas
```

---

### 8️⃣ VALIDACIONES FINALES (Checklist)

**Antes de enviar TODO, verifica:**

```
CHECKLIST DE CALIDAD

☐ Nombre actividad es específico (no "Tarea 1")
☐ Learning Outcomes alineados (L2-L5)
☐ Descripción es CLARA para estudiante
☐ Solución modelo es DETALLADA
☐ Rúbrica suma a 100% y es verificable
☐ Variantes (fácil/normal/desafiante) son claras
☐ Formato entrega es explícito
☐ Tiempo estimado es realista
☐ Contexto/por qué es importante está explicado

¿TODOS LOS PUNTOS SON "SÍ"? → Listo para enviar
¿ALGUNO ES "NO"? → Arréglalo antes de enviar
```

---

## 📋 CÓMO ENVIAR ESTE PROMPT

**COPIA TODO JUNTO (8 secciones) EN UN SOLO MENSAJE**

Yo:
1. Valido que esté COMPLETO
2. Activo skill `course-assessment-and-activity-designer`
3. Genero documento profesional con:
   - Instrucciones para estudiante
   - Solución modelo
   - Rúbrica evaluación
   - Variantes dificultad
4. Te entrego en 10-15 minutos

---

## 🔄 EJEMPLO ENTRADA COMPLETA

```
═════════════════════════════════════════════════════════════════
ENTRADA PARA GENERAR ACTIVIDAD EVALUATIVA
═════════════════════════════════════════════════════════════════

1. IDENTIFICACIÓN
Nombre: Evaluación Comparativa: Fine-tuning vs RAG en Contratos
Tipo: Tarea (parejas)
Semana: 3
Duración: 4-6 horas

2. LEARNING OUTCOMES
  [L2] - LO #1: Explicar trade-offs fine-tuning vs RAG
  [L3] - LO #2: Aplicar ambas estrategias en caso real
  [L4] - LO #3: Analizar costo-beneficio cada estrategia

3. CONTEXTO
Curso: Large Language Models (AI-502), Master ULEAD
Profesor: Harry Arce
Audiencia: Profesionales tech 2+ años
Requisitos: Sesiones 1-2 completadas

4. DESCRIPCIÓN
[Descripción completa como en ejemplo arriba]

5. SOLUCIÓN MODELO
[Golden set, comparación, análisis cualitativo, recomendación]

6. RÚBRICA
[Tabla 5 criterios × 4 niveles]

7. VARIANTES
Fácil: 8-10 casos, solo 2 estrategias, 2-3 horas
Normal: [como se describe en 4-5]
Desafiante: 25-30 casos, 3 estrategias, análisis seguridad

8. VALIDACIÓN
[Todos los checkboxes ✓]
```

---

**Versión:** 1.0  
**Para:** ULEAD Courses  
**Skill:** course-assessment-and-activity-designer  
**Output:** Word + Rubric + Variants
