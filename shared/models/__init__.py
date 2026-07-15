import os
import pkgutil
import sys
from django.db import models

# 1. Obtenemos la ruta absoluta de la carpeta actual (shared/models/)
pkg_dir = os.path.dirname(__file__)

# 2. Buscamos dinámicamente todos los módulos (.py) dentro de esta carpeta
for _, module_name, _ in pkgutil.iter_modules([pkg_dir]):
    
    # Evitamos un bucle infinito importando el propio __init__
    if module_name == "__init__":
        continue
        
    # Construimos la ruta de importación relativa (ej: .departamentos, .municipios)
    full_module_name = f"{__name__}.{module_name}"
    
    # Importamos el archivo dinámicamente
    __import__(full_module_name)
    module = sys.modules[full_module_name]
    
    # 3. Extraemos todas las clases que hereden de Django Models y las registramos en el scope global
    for attr_name in dir(module):
        attr = getattr(module, attr_name)
        
        # Verificamos si es una clase y si hereda de models.Model
        if isinstance(attr, type) and issubclass(attr, models.Model) and attr is not models.Model:
            # Al meterlo en globals(), Python lo expone como si se hubiera escrito a mano
            globals()[attr_name] = attr