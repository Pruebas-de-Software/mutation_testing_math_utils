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
