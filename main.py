from tkinter import Tk, Label, Button, Toplevel, messagebox
from tkcalendar import DateEntry
import datetime

def calcular_vacaciones():
    # Obtener la fecha de ingreso desde el calendario
    fecha_ingreso = calendario.get_date()
    hoy = datetime.date.today()
    fin_anio = datetime.date(hoy.year, 12, 31)
    # Calcular antigüedad en días y años
    antiguedad_dias = (fin_anio - fecha_ingreso).days
    antiguedad_anios = antiguedad_dias // 365
    
    # Determinar los días de vacaciones según la antigüedad
    # Determinar los días de vacaciones según la antigüedad
    if antiguedad_dias < 183:  # Menor a 6 meses
        if antiguedad_dias < 4 * 7:
            dias_vacaciones = 1
        elif antiguedad_dias < 8 * 7:
            dias_vacaciones = 2
        elif antiguedad_dias < 12 * 7:
            dias_vacaciones = 3
        elif antiguedad_dias < 16 * 7:
            dias_vacaciones = 4
        elif antiguedad_dias < 20 * 7:
            dias_vacaciones = 5

