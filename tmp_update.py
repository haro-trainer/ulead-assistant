from pathlib import Path
p = Path('index.html')
text = p.read_text(encoding='utf-8')
old = '"prompt": null, "order": 5}};'
new = '"prompt": null, "downloadUrl": "skills/academic-grader.zip", "order": 6}, "presentation-builder": {"icon": "📽️", "title": "Diseñador de Presentaciones", "desc": "Convierte contenidos pedagógicos en presentaciones claras y visualmente estructuradas para clases, talleres y sesiones de formación.", "produces": "Presentación con estructura, diapositivas, mensajes clave y referencias visuales", "input": "Tema, objetivos de sesión y contenido pedagógico", "time": "15 min por presentación", "prompt": null, "downloadUrl": "skills/presentation-builder.zip", "order": 7}};'
if old not in text:
    raise SystemExit('target snippet not found')
p.write_text(text.replace(old, new, 1), encoding='utf-8')
print('updated')
