import hashlib
import os

def texto_a_hash(texto, salt=None):
    # Crear un objeto hash usando SHA256
    hash_obj = hashlib.sha256()

    
    # Codificar el texto y el salt a bytes y actualizar el objeto hash
    hash_obj.update(texto.encode())
    
    # Obtener el hash en formato hexadecimal
    hash_hex = hash_obj.hexdigest()
    
    return hash_hex
