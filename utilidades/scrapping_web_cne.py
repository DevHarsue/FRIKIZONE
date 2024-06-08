import requests
from bs4 import BeautifulSoup

class BuscadorPersonas():
    def buscar_persona(self,nacionalidad,ci):
        url = f'http://www.cne.gob.ve/web/registro_civil/buscar_rep.php?nac={nacionalidad}&ced={ci}'
        try:
            respuesta = requests.get(url)
            soup = BeautifulSoup(respuesta.text, 'html.parser')
        except Exception as e:
            print(e)
        nombre = str(soup.findChild("b"))[3:-4].split(" ")
        nombre = [nombre[0],nombre[-2]]
        return nombre