from datetime import datetime

def tiempo_relativo(fecha):
    if not fecha:
        return ""

    ahora = datetime.now()
    diff = ahora - fecha

    segundos = diff.total_seconds()

    if segundos < 60:
        return "Hace unos segundos"
    elif segundos < 3600:
        return f"Hace {int(segundos//60)} min"
    elif segundos < 86400:
        return f"Hace {int(segundos//3600)} h"
    else:
        return f"Hace {int(segundos//86400)} días"