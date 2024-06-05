from datetime import datetime

def obtener_fecha():
    # Obtener la fecha y hora actual
    now = datetime.now()
    
    # Formatear la fecha y hora en el formato para sql
    formato = now.strftime('%Y-%m-%d %H:%M:%S')

    return formato