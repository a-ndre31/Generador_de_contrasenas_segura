import random
import string

#Definir caracteres
mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
minusculas = "abcdefghijklmnñopqrstuvwxyz"
numeros = "0123456789"
simbolos = "!@#$%^&*"

#Juntas todos
todos = mayusculas + minusculas + numeros + simbolos

#Longitud fija de 20 caracteres
longitud = 20

#Generar contraseña
contrasena = []
contrasena.append(random.choice(mayusculas))
contrasena.append(random.choice(minusculas))
contrasena.append(random.choice(numeros))
contrasena.append(random.choice(simbolos))

for i in range(longitud - 4):
    contrasena.append(random.choice(todos))
    
random.shuffle(contrasena)
contrasena_final = ''.join(contrasena)

#Mostrar resultado
print("CONTRASEÑA SEGURA GENERADA PRUEBA")
print(contrasena_final)
print(f"longitud: {len(contrasena_final)} caracteres")
