# Informacion para correr el script
## 1. Instalar las dependencias
```bash
  pip install -r requirements.txt 
```
o 
```bash
  python3 -m pip install -r requirements.txt
```

## 2. Configurar el directorio de csv
Crear un directorio que contenga los archivos csv a procesar y modificar la variable `csv_dir` en el archivo `main.py` con la ruta del directorio creado.

```python
  csv_dir = 'ruta/del/directorio'
```

## 3. Correr el script
Abrir una terminal en la carpeta del proyecto (es posible usar click derecho sobre la carpeta para abrir una terminal)  y ejecutar el siguiente comando.

```bash
  python3 main.py
```

## 4. Verificar los resultados
Los resultados se guardan en el mismo directorio en el que se encuentra `main.py` un archivo llamado `output.txt`.