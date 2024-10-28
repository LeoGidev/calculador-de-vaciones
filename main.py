from tkinter import Tk, Label, Button, Toplevel, messagebox
from tkcalendar import DateEntry
import datetime

def calcular_vacaciones():
    # Obtener la fecha de ingreso desde el calendario
    fecha_ingreso = calendario.get_date()