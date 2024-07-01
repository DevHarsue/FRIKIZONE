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

def texto_a_hash_salt(texto):
    salt = '\x9a\xedd\t\xb3\x80\xa7\xbc:\xd5\xbdW\xcc\x96\xc8\x94'
    hash_obj = hashlib.sha256()

    texto = texto+salt
    # Codificar el texto y el salt a bytes y actualizar el objeto hash
    hash_obj.update(texto.encode())
    
    # Obtener el hash en formato hexadecimal
    hash_hex = hash_obj.hexdigest()
    
    return hash_hex

