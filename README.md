# curso-python

Repositorio con ejemplos y ejercicios de Python.

## Entorno Virtual de Python (venv)

### ¿Qué hace `python -m venv myvenv`?

El comando `python -m venv myvenv` crea un **entorno virtual** de Python en una carpeta llamada `myvenv`.

Un entorno virtual es un entorno aislado de Python que permite:

- **Instalar paquetes específicos** sin afectar la instalación global de Python
- **Controlar versiones** de librerías para diferentes proyectos
- **Evitar conflictos** entre dependencias de distintos proyectos
- **Facilitar la reproducibilidad** del proyecto en otros equipos

### ¿Cómo funciona?

El comando `python -m venv` ejecuta el módulo `venv` de Python, que:
1. Crea una carpeta llamada `myvenv`
2. Copia los ejecutables de Python en esa carpeta
3. Configura un script de activación para usar el entorno virtual

### Activar el Entorno Virtual

#### En Windows (PowerShell)
```powershell
myvenv\Scripts\Activate.ps1
```

Si obtienes un error de permisos, ejecuta este comando primero:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### En Windows (CMD)
```cmd
myvenv\Scripts\activate.bat
```

#### En macOS/Linux
```bash
source myvenv/bin/activate
```

**Indicador de activación**: Cuando el entorno está activo, verás `(myvenv)` al inicio de tu línea de comandos.

### Desactivar el Entorno Virtual

Para salir del entorno virtual y volver a la instalación global de Python, ejecuta:

```bash
deactivate
```

Esto funciona en **todos los sistemas operativos** (Windows, macOS y Linux).

El indicador `(myvenv)` desaparecerá de tu línea de comandos cuando se desactive correctamente.

### Instalar paquetes

Cuando el entorno virtual está activo, puedes instalar paquetes con `pip` sin afectar la instalación global:

```bash
pip install nombre-del-paquete
```

