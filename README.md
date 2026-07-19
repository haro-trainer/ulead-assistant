# AI Academic Dean

Sistema inteligente para diseño curricular universitario, basado en el flujo presentado en [index.html](index.html). El proyecto combina skills de IA con prompts maestros para generar materiales pedagógicos de forma estructurada y alineada con principios universitarios.

## Qué incluye este repositorio

Este proyecto contiene:

- una interfaz web en [index.html](index.html) con la guía completa del sistema;
- 5 skills listos para instalar en Claude Desktop;
- 3 prompts maestros para generar sílabos, actividades y sesiones;
- documentación de instalación y referencia;
- archivos descargables empaquetados para uso rápido.

## Flujo de producción

El sistema sigue este ciclo de trabajo:

1. Sílabo
2. Actividades de evaluación
3. Contenido de sesiones
4. Ejercicios prácticos
5. Calificación y retroalimentación

Este flujo permite pasar de un curso base a materiales listos para clase con una metodología más consistente y trazable.

## Estructura de carpetas y contenido

```text
ulead-assistant/
├── index.html                    # Página web con la guía completa del sistema
├── README.md                     # Este archivo de documentación
├── ai_academic_dean_folder_structure.svg
├── docs/                         # Documentación de instalación y referencia
│   ├── 00_INDICE_COMPLETO.md
│   ├── COMO_INSTALAR_SKILLS.md
│   └── README_SISTEMA.md
├── downloads/                    # Archivos empaquetados para descarga
│   └── AI_ACADEMIC_DEAN_v1.1.zip
├── prompts/                      # Prompts maestros para generar entregables
│   ├── PROMPT_MAESTRO_ACTIVIDADES.txt
│   ├── PROMPT_MAESTRO_SESION.txt
│   └── PROMPT_MAESTRO_SYLLABUS.txt
└── skills/                       # Skills listos para instalar
    ├── academic-grader.zip
    ├── course-assessment-and-activity-designer.zip
    ├── exercise-designer.zip
    ├── session-content-builder.zip
    └── university-syllabus-designer.zip
```

## Contenido por carpeta

### [docs](docs)
Archivos de referencia, guía de instalación y explicación general del sistema.

### [downloads](downloads)
Paquete descargable del proyecto o de la solución completa.

### [prompts](prompts)
Prompts maestros que activan el proceso de generación de contenido pedagógico.

### [skills](skills)
Skills empaquetados para usar con Claude Desktop o herramientas compatibles.

## Uso recomendado

- Para máxima calidad, usar Claude Desktop con los skills instalados.
- Para uso en ChatGPT o Claude web, usar los prompts maestros sin skills.
- Para ver la guía visual y detallada, abrir [index.html](index.html).

## Referencias rápidas

- Guía de instalación: [docs/COMO_INSTALAR_SKILLS.md](docs/COMO_INSTALAR_SKILLS.md)
- Resumen del sistema: [docs/README_SISTEMA.md](docs/README_SISTEMA.md)
- Página principal: [index.html](index.html)
