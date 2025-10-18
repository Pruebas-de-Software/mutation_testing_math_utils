# Testing de Mutaciones en Python (pytest + mutmut)
Proyecto didáctico que muestra, paso a paso, cómo aplicar mutation testing en Python con pytest y mutmut. La idea es evidenciar la diferencia entre tener cobertura y detectar verdaderos defectos generando mutaciones realistas en el código y verificando si tus pruebas las “matan”

```python -m venv .venv
source .venv/bin/activate           # Windows
pip install -U pip pytest mutmut

# Correr tests regualres
pytest -q

# Ejecutar mutation testing
mutmut run
mutmut results      # Resumen
mutmut show <ID>    # Ver la mutación que sobrevivió
```


# Mutmut: Mutation Testing para Python

**Mutmut** es una herramienta de *mutation testing* para Python. 

La idea detrás del testing de mutaciones es sencilla:  

**Alterar el código productivo con pequeños cambios (“mutaciones”) y volver a ejecutar los tests**. 

- Si los tests **fallan**, “matan” al mutante (bien); 
- Si **pasan**, el mutante **sobrevive** (malo: la suite no detectó un bug plausible).

Aquí va cómo funciona, paso a paso y qué significa cada cosa:

## ¿Qué hace Mutmut?

### 1) Ejecuta un ciclo de los tests
- Mide tiempo y comprueba que la suite pase “en verde”.
- Usa el *runner* que se le diga (ejemplo: `pytest -q`).

### 2) Genera mutaciones del código (archivo por archivo, línea por línea)
Ejemplos típicos de mutaciones:
- Cambiar comparadores: `<=` ↔ `<`, `==` ↔ `!=`
- Invertir booleanos: `True` ↔ `False`, `if cond:` ↔ `if not cond:`
- Alterar aritmética: `+` ↔ `-`, `*` ↔ `//`
- Cambiar retornos por valores por defecto
- Remover/alterar ramas simples  
  *(La idea: introducir “bugs pequeños pero realistas”.)*

### 3) Ejecuta los tests para cada mutante (una mutación activa por vez)
- Si **algún test falla** → **Killed** (mutante “muerto”). ✔️
- Si **todos los tests pasan** → **Survived** (mutante “vivo”). ❌
- Si hay **problemas de ejecución/tiempo** → suele marcarlos como **Timeout** o **Suspicious** (revisar).
- Guarda estado en **`.mutmut-cache`** (acelera ejecuciones posteriores).

### 4) Resume y te deja inspeccionar
- `mutmut results` → conteo por estado.
- `mutmut show <ID>` → *diff* exacto de la mutación.
- `mutmut apply <ID>` → aplica esa mutación al *working tree* (útil para reproducir y escribir el test que la mata).
- Luego ajustas/creas tests y vuelves a correr.

## Flujo de uso típico

```ini
# 1) Configurar (ej. en setup.cfg)
[mutmut]
paths_to_mutate=src
tests_dir=tests
runner=pytest -q
```

```bash
# 2) Ejecutar mutation testing
mutmut run

# 3) Ver resultados
mutmut results

# 4) Inspeccionar mutantes vivos
mutmut show 3
mutmut apply 3   # opcional, para experimentar localmente

# 5) Fortalecer tests y repetir
mutmut run
```

## ¿Cómo interpretar los resultados?
- **Killed** (bien): Los tests (en su conjunto) detectaron el cambio.
- **Survived** (alerta): hay un hueco en tus tests o es un **mutante equivalente** (mutación que no cambia el comportamiento observable; en ese caso se puede ignorar o excluir).
- **Timeout/Suspicious**: el mutante hizo que la suite tarde demasiado o haya señales "raras"; revisar performance/fiabilidad de los tests.

## Tips para velocidad y utilidad
- **Acotar el alcance**: `paths_to_mutate=src` o `--paths-to-mutate src/módulo.py`.
- **Priorizar líneas ejecutadas**: Usar cobertura para mutar solo los tests realmente tocan (requiere generar coverage primero).
- **Paralelizar**: con suites grandes, combinar con `pytest -n auto` (vía `pytest-xdist`) y ajustar el `runner`.
- **CI**: falla el pipeline si hay “Survived > 0” (métrica: *mutation score*).

## ¿Qué se obtienes en la práctica?
- Una medida más **fuerte** que la cobertura: no solo “qué líneas pasan por los tests”, sino **si esos tests, en su conjunto, detectarían cambios relevantes en la lógica**.
- Una lista concreta de **brechas**: cada mutante vivo suele inspirar un caso de prueba específico (bordes, excepciones, comparadores, *off-by-one*, etc.).
