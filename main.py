from tkinter import Tk, Label, Button, Toplevel, messagebox
from tkcalendar import DateEntry
import datetime

def calcular_vacaciones():
    # Obtener la fecha de ingreso desde el calendario
    fecha_ingreso = calendario.get_date()
    hoy = datetime.date.today()
    fin_anio = datetime.date(hoy.year, 12, 31)
    # Calcular antigüedad en días y años