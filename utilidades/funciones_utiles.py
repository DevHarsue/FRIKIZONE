from datetime import datetime
from pyDolarVenezuela.pages import BCV
from pyDolarVenezuela import Monitor

def obtener_fecha():
    # Obtener la fecha y hora actual
    now = datetime.now()
    
    # Formatear la fecha y hora en el formato para sql
    formato = now.strftime('%Y-%m-%d %H:%M:%S')

    return formato

def obtener_tasa_bcv():
    try:
        # Crear una instancia de Monitor para el BCV
        monitor = Monitor(BCV, 'USD')

        # Obtener los valores de cambio del BCV
        valores_cambio = monitor.get_value_monitors()
        return valores_cambio["usd"]["price"]
    
    except Exception as e:
        print(e)