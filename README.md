## [IMPORTANTE] - Para ejecutar los experimentos debemos estar en la carpeta de experimentos.

---

### Sobre multiprocesamiento  en la ejecución

Hemos incluido la librería [__scoop__](https://github.com/soravux/scoop) para poder usar multiprocesamiento con DEAP.
Esta opción es opcional y la ejecución funcionara igualmente sin el multiprocesamiento.

#### Debemos seguir estos simples pasos

1. Importamos futures de scoop:

```python
from scoop import futures
```

2. Y después añadir la sigueinte opción al toolbox.

```python
toolbox.register("map", futures.map)
```

3. Ejecutar main.py o src/sol/main.py usando:

```powershell
python -m scoop main.py
```
