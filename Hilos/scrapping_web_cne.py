import requests
from bs4 import BeautifulSoup

class BuscadorPersonas():
    def buscar_persona(self,nacionalidad,ci):
        url = f'http://www.cne.gob.ve/web/registro_civil/buscar_rep.php?nac={nacionalidad}&ced={ci}'
        nombre = ""
        try:
            respuesta = requests.get(url)
            soup = BeautifulSoup(respuesta.text, 'html.parser')
            nombre = str(soup.findChild("b"))[3:-4].split(" ")
            nombre = [nombre[0],nombre[-2]]
            if nombre[0] == "Http/1.1":
                raise Exception
        except Exception as e:
            return e
        return nombre