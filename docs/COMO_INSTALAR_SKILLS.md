# 🧠 Cómo Instalar y Usar los Skills

Los **skills son completamente opcionales**. Todos los prompts funcionan sin instalarlos.

---

## ¿Debo instalar los skills?

**Respuesta rápida:**

| Escenario | ¿Instalar? |
|-----------|-----------|
| Solo quiero copiar y pegar prompts | ❌ NO (no necesitas) |
| Uso Claude Desktop | ✅ SÍ (opcional pero útil) |
| Soy desarrollador | ✅ SÍ (para integraciones) |
| Solo tengo acceso a chat.claude.ai web | ❌ NO (los skills no funcionan ahí) |

---

## Opción 1: Usar Solo Prompts (RECOMENDADO para empezar)

**Ventaja:** Cero instalación. Funciona ahora mismo.

Pasos:
1. Copia el prompt de la carpeta `/prompts/`
2. Pégalo en `chat.claude.ai`
3. Descarga tu resultado
4. ¡Listo!

**No necesitas hacer nada más.**

---

## Opción 2: Instalar Skills en Claude Desktop (Opcional)

Si usas **Claude Desktop**, puedes instalar los skills para que se activen automáticamente.

### ¿Qué son los skills?

Son archivos que especializan a Claude en tareas específicas:
- Cuando preguntas "generar sílabo" → activa `university-syllabus-designer`
- Cuando preguntas "diseñar actividad" → activa `course-assessment-and-activity-designer`
- Etc.

### Instalación paso a paso:

**Paso 1: Encuentra la carpeta de skills de Claude Desktop**

| Sistema | Ruta |
|---------|------|
| **Windows** | `C:\Users\[TU_USER]\AppData\Roaming\Claude\` |
| **Mac** | `~/Library/Application Support/Claude/` |
| **Linux** | `~/.config/Claude/` |

**Paso 2: Descarga y extrae los skills**

Tienes 5 skills disponibles:

```
1. university-syllabus-designer.zip
2. course-assessment-and-activity-designer.zip
3. session-content-builder.zip
4. exercise-designer.zip
5. academic-grader.zip
```

Descargalos y extrae TODOS en la carpeta de skills (ver Paso 1).

**Paso 3: Reinicia Claude Desktop**

1. Cierra Claude Desktop completamente
2. Abre de nuevo
3. Espera 30 segundos para que cargue

**Paso 4: Verifica que funcionan**

En Claude Desktop, escribe:
```
¿Qué skills tienes disponibles?
```

Si ves algo como:
```
I have the following skills:
- university-syllabus-designer
- course-assessment-and-activity-designer
- session-content-builder
- exercise-designer
- academic-grader
```

✅ ¡Perfectamente instalados!

### Usar los skills en Claude Desktop

Una vez instalados, puedes escribir naturalmente:

```
"Diseña un sílabo para un curso de IA Generativa..."
→ Automáticamente usa: university-syllabus-designer

"Crea una actividad de evaluación para..."
→ Automáticamente usa: course-assessment-and-activity-designer

"Genera ejercicios prácticos para..."
→ Automáticamente usa: exercise-designer
```

Los skills se activarán automáticamente.

---

## Cada Skill Contiene:

### 1. **university-syllabus-designer**
- SKILL.md (descripción completa)
- README.md (guía de uso)
- /templates/ (plantillas de sílabos)
- /examples/ (ejemplos reales)
- /prompts/ (prompts del sistema)
- /references/ (documentos de referencia)
- /validators/ (checklists de calidad)

### 2. **course-assessment-and-activity-designer**
- SKILL.md (descripción)
- README.md (guía)
- /templates/ (plantillas de tareas, rúbricas)
- /examples/ (ejemplos de actividades)
- /prompts/ (prompts internos)
- /validators/ (checklists)

### 3. **session-content-builder**
- SKILL.md (descripción)
- SKILL.md (guía)
- /templates/ (plantillas para agendas, slides)
- /prompts/ (prompts internos)
- /references/ (principios pedagógicos)
- /validators/ (checklists de calidad)

### 4. **exercise-designer**
- SKILL.md (descripción)
- /references/ (plantillas de ejercicios)
- /templates/ (estructuras)
- /prompts/ (prompts internos)

### 5. **academic-grader**
- SKILL.md (descripción)
- /templates/ (formatos de salida)
- /references/ (checklists de detección)
- /prompts/ (prompts internos)

---

## Troubleshooting

### "Los skills no aparecen después de instalar"

**Solución:**
1. Verifica que extrajiste los 5 ZIPs en la carpeta correcta
2. Reinicia Claude Desktop **completamente** (no solo minimizar)
3. Espera 30 segundos después de abrir
4. Intenta de nuevo

### "Dónde encuentro la carpeta de skills?"

**Windows:**
1. Abre: `C:\Users\[TU_USER]\AppData\Roaming\Claude\`
2. Si no existe, créala manualmente

**Mac:**
1. Abre Finder
2. Presiona Cmd+Shift+G
3. Pega: `~/Library/Application Support/Claude/`
4. Presiona Enter

**Linux:**
1. Abre terminal
2. `mkdir -p ~/.config/Claude/skills`
3. Los ZIPs van ahí

### "Qué pasa si no instalo los skills?"

Nada malo. Los prompts funcionan perfecto sin skills.
Los skills solo aceleran el trabajo en Claude Desktop.

---

## Resumen

| Situación | Acción | Tiempo |
|-----------|--------|--------|
| Quiero empezar rápido | Usa prompts (no instales skills) | 0 min |
| Tengo Claude Desktop | Instala skills (opcional) | 5 min |
| Soy desarrollador | Instala skills + configura MCP | 15 min |

---

## Preguntas?

Ver el archivo `SUPPORT.md` para contactar o abrir el archivo HTML `START_HERE.html` para más información.

---

**Recuerda:** Los prompts funcionan sin skills. Los skills son un BONUS opcional para usuarios de Claude Desktop.

¡Adelante! 🚀
