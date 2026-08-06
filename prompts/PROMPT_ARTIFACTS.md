Actúa como coordinador académico, diseñador instruccional, facilitador experto, diseñador de experiencias de aprendizaje y responsable de control de calidad. Genera, en una sola ejecución, el paquete completo de la sesión indicada abajo.

No me entregues primero un plan para aprobación. Si los insumos obligatorios están completos y no existe una contradicción material, procede directamente hasta generar, probar y entregar todos los archivos. No detengas el trabajo por decisiones menores: adopta el supuesto más conservador, regístralo en el informe de calidad y continúa. Solo formula una única pregunta agrupada si existe un conflicto que cambiaría el tema, los resultados de aprendizaje, el CPA, su peso o el contenido de la sesión anterior.

## A. Variables de esta ejecución

Tratar de Completar tanto como puedas y sustituye los valores entre corchetes:
Si algun valor es relevante y no lo puedes determinar, pidelo antes de generar los entregables.

- Programa: [NOMBRE DEL PROGRAMA]
- Curso: [NOMBRE Y NÚMERO DEL CURSO]
- Sesión: [NÚMERO DE SESIÓN] de [TOTAL DE SESIONES]
- Título oficial: [TÍTULO DE LA SESIÓN]
- Duración total: [DURACIÓN; indicar si incluye receso]
- Modalidad: [PRESENCIAL / VIRTUAL / HÍBRIDA]
- Audiencia y nivel: [PERFIL]
- Idioma: [IDIOMA]
- Resultados de aprendizaje aplicables: [RESULTADOS EXACTOS O REFERENCIA AL SÍLABO]
- Temas y límites de alcance: [TEMAS DE ESTA SESIÓN / TEMAS QUE NO DEBEN ADELANTARSE]
- Plan de sesión aprobado: [ARCHIVO O TEXTO]
- Sílabo/programa vigente: [ARCHIVO]
- Material final de la sesión anterior: [ARCHIVOS O CONVERSACIÓN]
- Última versión aprobada de entregables de referencia: [ARCHIVOS O CONVERSACIÓN]
- Fuentes académicas/técnicas autorizadas: [ARCHIVOS O ENLACES]
- Identidad visual: [LOGO, PALETA, TIPOGRAFÍAS, DECK DE REFERENCIA]
- Herramientas aprobadas del curso: [LISTA]
- Acceso a internet durante la clase: [SÍ / NO]
- CPA de esta sesión: [NOMBRE, NÚMERO, PESO, INDIVIDUAL/GRUPAL, SESIÓN DE ENTREGA]
- Presupuesto del taller del CPA: [MINUTOS]
- Trabajo autónomo esperado del CPA: [HORAS]
- Formato y canal de entrega del CPA: [FORMATO / LMS / CONVENCIÓN DE NOMBRE]
- Generar solución modelo del CPA: [NO, salvo instrucción expresa]
- Generar checklist de revisión entre pares: [NO, salvo instrucción expresa]
- Número de preguntas del quiz: [5]
- Carpeta de salida: [NOMBRE O RUTA]

Si una variable no aplica, usa “No aplica” y explica brevemente por qué en el informe de calidad. Para una Sesión 1 sin sesión anterior, reemplaza el quiz de repaso por un diagnóstico de prerrequisitos claramente identificado; no finjas que existe una sesión previa. Si el sílabo establece que esta sesión no abre un CPA, no inventes uno: marca los entregables 5 y 6 como “No aplica según el sílabo” en el manifiesto.

## B. Skills obligatorias y distribución de responsabilidades

Usa activamente las siguientes skills instaladas. No copies sus manuales en la respuesta ni dupliques sus instrucciones; ejecútalas para la responsabilidad indicada:

1. `session-content-builder`: orquesta el paquete completo y garantiza la trazabilidad entre plan, agenda, contenidos, actividades, guías, quiz y CPA.
2. `university-syllabus-designer`: verifica únicamente el alineamiento curricular, los resultados de aprendizaje, la cadencia entre sesiones y la coherencia del peso evaluativo. No rediseñes el sílabo.
3. `premium-pedagogical-presentation-builder` —o el alias instalado `presentation-builder`—: genera y audita la presentación HTML para la audiencia.
4. `speaker-command-center`: genera el HTML independiente para el orador, sincronizado con el deck final.
5. `applied-case-designer`: desarrolla el CPA cuando corresponda, incluida su factibilidad, especificación estudiantil, rúbrica y materiales requeridos.
6. `course-assessment-and-activity-designer`: desarrolla el quiz de repaso y cualquier evaluación/actividad que no sea el CPA.
7. `exercise-designer`: desarrolla los ejercicios guiados de la sesión y mantiene alineadas las versiones para profesor y estudiante, integrándolas en sus respectivas guías; no crees archivos extra salvo que sean necesarios.
8. `academic-grader`: úsala solo si se adjuntan entregas reales de estudiantes y se solicita probar la aplicación de la rúbrica. No la uses para crear la rúbrica, inventar una entrega ni simular evidencia.

Usa además las skills de formato disponibles cuando sean necesarias para producir y verificar HTML, Markdown, Word, hojas de cálculo, PDF o ZIP. La responsabilidad académica sigue perteneciendo a las skills anteriores.

## C. Precedencia de fuentes

Resuelve el contenido con este orden de autoridad:

1. Instrucciones explícitas de esta ejecución.
2. Última versión aprobada del plan de la sesión actual.
3. Sílabo o programa vigente.
4. Entregables finales de la sesión anterior, solo para continuidad y para el quiz de repaso.
5. Entregables de referencia, únicamente para estilo, estructura e interacción cuando así se indique.
6. Investigación externa actual y fuentes oficiales, solo cuando sea necesaria o cuando una skill la requiera.

No reutilices contenido académico de una sesión o curso diferente por el solo hecho de que un archivo sea visualmente parecido. No adelantes temas de sesiones posteriores. Si dos fuentes se contradicen, aplica la de mayor precedencia y documenta la decisión.

## D. Entregables obligatorios

Genera exactamente los siguientes entregables, más un informe de calidad y un manifiesto. Usa nombres consistentes con el número de sesión.

### 1. `01_Sesion_[XX]_Presentacion.html`

Presentación HTML autocontenida, lista para proyectar y completamente orientada al estudiante.

Requisitos específicos de esta entrega:

- Todo texto visible debe hablarle a la audiencia; ninguna nota de producción, instrucción del profesor, etiqueta de auditoría o lenguaje interno puede aparecer proyectado.
- Debe desarrollar los conceptos de la sesión con profundidad suficiente, ejemplos aplicados, visualizaciones pertinentes, momentos de interacción, taller, síntesis y conexión con el CPA.
- El quiz de repaso debe aparecer como actividad de apertura o puente, pero sus preguntas corresponden exclusivamente a la sesión anterior.
- Mantén una única barra de controles, idéntica y operativa en todas las diapositivas: anterior, contador, siguiente, notas y pantalla completa; añade navegación por teclado y barra de progreso.
- Incluye notas de orador en el 100% de las diapositivas, ocultas por defecto y accesibles con la tecla `S`, aunque exista un Command Center separado.
- Mantén logo, contenido y controles dentro de zonas seguras, sin superposiciones ni desbordamientos.
- Evita combinaciones de color de bajo contraste. Cumple como mínimo WCAG AA: 4.5:1 para texto normal y 3:1 para texto grande. No uses color como único medio para comunicar significado.
- Debe funcionar sin conexión si así se indica en las variables.
- Audita todas las diapositivas a 1366×768 y 1920×1080. Corrige cualquier problema antes de entregar.

### 2. `02_Sesion_[XX]_Speaker_Command_Center.html`

Centro de comando HTML autocontenido para el segundo monitor del profesor.

Requisitos específicos de esta entrega:

- Sincronización uno a uno con la versión final del deck: mismo número, orden y título de diapositivas.
- Para cada diapositiva incluye un guion oral escaneable, preguntas de participación, ejercicio o acción si corresponde, alertas/énfasis y una transición hablada hacia la siguiente idea.
- Reescribe las notas para uso en vivo; no copies mecánicamente las notas del deck.
- Mantén contador, progreso, botones anterior/siguiente, navegación por teclado y salto directo a una diapositiva.
- Todo debe poder leerse sin scroll en 1366×768 y 1920×1080. Ajusta contenido y diseño hasta lograrlo.
- Es material exclusivo del profesor y nunca debe proyectarse a estudiantes.

### 3. `03_Guia_Profesor_Sesion_[XX].md`

Guía completa, autosuficiente y accionable para impartir la sesión.

Debe incluir, como mínimo:

- ficha de la sesión, propósito, resultados y evidencia observable;
- preparación previa, archivos, herramientas y contingencias;
- agenda minuto a minuto alineada al plan;
- desarrollo profundo de cada tema, ejemplos y conexiones profesionales;
- guion de facilitación por bloque, preguntas, transiciones, tiempos, errores frecuentes y cómo intervenir;
- instrucciones exactas para ejercicios, quiz, discusión, receso, taller y cierre;
- respuestas y justificaciones del quiz, visibles solo para el profesor;
- guía para ritmos rápido/lento y fallas técnicas;
- apertura, seguimiento y cierre del CPA, sin incluir una solución modelo cuando la variable correspondiente sea “NO”;
- referencias exactas a los archivos que el profesor debe abrir en cada momento.

No generes un checklist de revisión entre pares si la variable correspondiente es “NO”.

### 4. `04_Guia_Estudiante_Sesion_[XX].docx`

Guía elaborada y completamente orientada al estudiante, no un resumen superficial del deck.

Debe incluir, como mínimo:

- qué logrará, por qué importa y cómo prepararse;
- ruta de aprendizaje y agenda;
- explicación clara y suficiente de todos los temas cubiertos, sin adelantar otros temas;
- ejemplos aplicados, comparaciones, conceptos clave, glosario cuando aporte valor y errores comunes;
- ejercicios guiados paso a paso y preguntas de reflexión sin respuestas;
- espacios, tablas o plantillas breves para trabajar durante la clase;
- síntesis, autoevaluación y próximos pasos;
- conexión explícita con el CPA y listado de archivos de apoyo.

No incluyas notas de facilitación, respuestas del quiz ni instrucciones exclusivas del profesor. Renderiza el DOCX completo y corrige tablas, cortes, páginas vacías, desbordamientos, contraste y accesibilidad antes de entregarlo.

### 5. `05_Especificacion_CPA_[NN]_Estudiante.docx`

Especificación completa, autocontenida, muy pedagógica y escrita 100% para el estudiante. Debe seguir el patrón y nivel de orientación de la última versión aprobada del CPA anterior, sin copiar su contenido académico.

Debe incluir, como mínimo:

- ficha resumen, escenario atractivo, propósito y resultados evaluados;
- relación con el trabajo previo y límites de alcance;
- recursos, herramientas aprobadas y prerrequisitos;
- Parte A: taller en clase, desglosado paso a paso con tiempos cuya suma sea exactamente compatible con el presupuesto disponible;
- Parte B: trabajo autónomo, desglosado paso a paso con tiempo total realista;
- entregables obligatorios, extensión, formato, estructura, canal, fecha/momento de entrega y convención de nombres;
- criterios de éxito, ejemplo parcial de nivel de especificidad que no revele una solución completa, errores que reducen la calificación y recomendaciones de trabajo;
- uso responsable, privacidad, supuestos, límites y controles cuando correspondan;
- rúbrica completa integrada en el mismo documento: 100 puntos, pesos que suman exactamente 100%, cuatro niveles de desempeño y descriptores observables por criterio;
- checklist final de entrega del propio estudiante.

No generes una solución modelo ni un checklist de revisión entre pares cuando esas variables sean “NO”. Renderiza y revisa visualmente el documento completo antes de entregarlo.

### 6. `06_Materiales_CPA_[NN].zip` — cuando sean necesarios

Genera todos los insumos que el estudiante necesita para completar el CPA sin bloqueos: datasets, diccionario de datos, canvas o plantilla editable, hojas de trabajo, archivos de ejemplo, instrucciones técnicas, starter files y recursos adicionales que el caso realmente requiera.

Condiciones:

- No introduzcas herramientas ni contenidos no aprobados.
- Los datos deben ser coherentes con el escenario, suficientes para la tarea, seguros, anonimizados o claramente sintéticos, y estar libres de respuestas incrustadas accidentalmente.
- Todo material debe abrir correctamente y coincidir con las instrucciones y la rúbrica.
- Incluye `README_Materiales_CPA_[NN].md` con inventario, propósito de cada archivo y orden de uso.
- Si solo se necesita un archivo, entrégalo individualmente y explica por qué no fue necesario un ZIP; si son varios, crea el ZIP.
- No empaquetes archivos de auditoría, temporales ni soluciones del profesor.

### 7. `07_Quiz_Repaso_Sesion_[XX-1].html`

Quiz interactivo HTML autocontenido de exactamente [NÚMERO DE PREGUNTAS DEL QUIZ] preguntas, dedicado exclusivamente a recuperar aprendizajes de la sesión anterior.

Condiciones:

- Deriva cada pregunta de evidencias verificables del material final de la sesión anterior, no de memoria ni de los temas de la sesión actual.
- Incluye opciones plausibles, retroalimentación inmediata, justificación de la respuesta, progreso, resultado final y opción de reintentar.
- No debe introducir ni evaluar contenido nuevo de la sesión actual.
- Sin calificación, salvo que el sílabo indique expresamente lo contrario.
- Prueba el recorrido completo, todas las respuestas, el cálculo del resultado, el reinicio, el teclado y el contraste.

## E. Coherencia transversal obligatoria

Antes de construir los archivos, crea internamente una matriz única de trazabilidad:

resultado de aprendizaje → bloque/tema → evidencia → diapositiva → sección de guía del profesor → sección de guía del estudiante → ejercicio → quiz o CPA → criterio de rúbrica.

Usa esa matriz para impedir contradicciones y duplicaciones. No es necesario entregarla como archivo independiente, pero resume sus hallazgos en el informe de calidad.

Verifica especialmente que:

- la agenda y los minutos sean idénticos en deck, guías y CPA;
- los títulos y el orden del deck coincidan exactamente con el Command Center;
- el quiz cubra solo la sesión anterior;
- la guía del estudiante desarrolle todo lo enseñado, no solo lo enumere;
- el CPA evalúe únicamente aprendizajes enseñados o practicados antes de la entrega;
- las instrucciones, materiales, entregables y rúbrica del CPA describan el mismo producto;
- los pesos sumen 100% y los niveles de la rúbrica sean aplicables a evidencia observable;
- ningún archivo mencione un recurso inexistente ni una versión anterior reemplazada;
- se respete toda exclusión explícita.

## F. Validación y definición de terminado

No declares el paquete completo hasta cumplir todo lo siguiente:

1. Abrir y validar cada archivo generado.
2. Probar ambos HTML de presentación en 1366×768 y 1920×1080.
3. Verificar controles consistentes en todas las diapositivas y sincronización deck–Command Center.
4. Auditar contraste, legibilidad, navegación, teclado, enlaces, overflow y superposiciones.
5. Recorrer el quiz de principio a fin y validar su clave y retroalimentación contra la sesión anterior.
6. Renderizar cada DOCX página por página y corregir problemas visuales o de accesibilidad.
7. Abrir y validar datasets, plantillas y archivos comprimidos; comprobar el inventario del ZIP.
8. Ejecutar una revisión cruzada de contenido, tiempos, nombres, referencias, entregables y rúbrica.
9. Eliminar archivos temporales del paquete de entrega.

Si una validación técnica no puede realizarse, no afirmes que pasó: documenta exactamente la limitación y marca el archivo como pendiente de validación.

## G. Archivos adicionales de control

Genera:

- `00_Manifiesto_Entregables_Sesion_[XX].md`: lista de archivos, propósito, audiencia y estado de validación.
- `08_Informe_Calidad_Sesion_[XX].md`: fuentes usadas, supuestos, decisiones ante conflictos, trazabilidad, pruebas realizadas, resultados, exclusiones confirmadas y pendientes de aprobación humana.
- `Paquete_Completo_Sesion_[XX].zip`: todos los entregables finales para uso del profesor, sin capturas, archivos temporales ni artefactos internos de auditoría. Conserva también los archivos individuales.

## H. Forma de entrega

Al finalizar:

1. Presenta primero el resultado, no el proceso.
2. Proporciona enlaces individuales a todos los archivos y al ZIP completo.
3. Resume en pocas líneas qué se generó y qué validaciones pasaron.
4. Señala únicamente supuestos o pendientes que realmente requieran decisión humana.
5. No pegues el contenido completo de los documentos en el chat y no reproduzcas las instrucciones internas de las skills.

Trata todos los materiales como borradores académicos listos para validación final del profesor/coordinador antes de publicarlos en el LMS.

Recomendación de uso

Adjunta en la misma solicitud el sílabo vigente, el plan aprobado de la sesión, los entregables finales de la sesión anterior, el CPA anterior como referencia de nivel de detalle y los activos de marca. Sustituye las variables de la sección A y pega el bloque completo en una conversación nueva donde las skills estén preinstaladas.