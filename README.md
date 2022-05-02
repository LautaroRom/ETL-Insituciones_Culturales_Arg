# Alkemy_Challenge-Data_Analytics

Para deployar el proyecto en un entorno virtual ejecutar las siguientes instrucciones en la consola del comandos:

1- instalar la libreria venv con el comando:
```
pip install virtualenv
```

2- Dirigirse al directorio donde se desea instalar el entorno virtual y ejecutar:
```
virtualenv nombre_del_entorno_virtual
```

3- Activar el entorno virtual:
```
.\nombre_del_entorno_virtual\Scripts\activate
```

4- Una vez activado el entorno virtual proceder a instalar las dependencias:
```
pip install pandas
pip install SQLAlchemy
pip install requests
pip install python-decouple
```

5- Para comprobar las dependencias instaladas ejecutar:
```
pip freeze
```

6- Con el entorno virtual activado y posicionado en la carpeta del proyecto donde se encuentren los archivos del proyecto, ejecutar en el siguiente orden:
```
python extraccionDatos.py
python procesamientoDatos.py
python baseDatos.py
```
