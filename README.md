# Ghostfuscator
The Python Password-Protected Obfuscator

# Uso

Simplemente ejecutar el script, y seguir el menu para especificar ruta de entrada, ruta de salida y una contraseña para el script protegido.

# Info

Si uno de tus scripts protegidos recoge datos de sys.argv, hazlo igual que lo haces cuando no esta ofuscado, por ejemplo si tu script normal `script.py` lo ejecutas con `python script.py test` ejecuta el script obfuscado asi `python encrypted.py test` al hacer el exec sobre el codigo recogera tambien los sys.argv y los pasara a tu programa en memoria.
