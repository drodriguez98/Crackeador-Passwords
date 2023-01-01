#   https://www.youtube.com/watch?v=RwgRuc1s4uQ

#   Crear contraseña hasheada en md5 --> https://www.md5.cz

#   Cuantos más diccionarios de passwords se incluyan en la carpeta mejor.

import hashlib

encontrada = 0
input_hash = input("\nInserta la contraseña hasheada:   ")
pass_doc = input("\nInserte el diccionario:     ")

try: 

    pass_file = open(pass_doc, 'r')
    
except: 

    print("\nError:" + pass_doc + " no ha sido encontrada")
    
for palabra in pass_file:

    palabra_cifrada = palabra.encode('utf-8')
    palabra_hasheada = hashlib.md5(palabra_cifrada.strip())
    digest = palabra_hasheada.hexdigest()
    
    if digest == input_hash: 
    
        print("\nContraseña encontrada!!")
        print("La contraseña es: " + palabra)
        encontrada = 1
        break
        
if not encontrada:

    print("\nContraseña no encontrada en el archivo " + pass_doc)