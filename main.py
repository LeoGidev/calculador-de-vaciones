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
    elif antiguedad_anios < 5:
        dias_vacaciones = 14
    elif antiguedad_anios < 10:
        dias_vacaciones = 21
    elif antiguedad_anios < 20:
        dias_vacaciones = 28
    else:
        dias_vacaciones = 35
    # Mostrar el resultado
    resultado_label.config(text=f"Antigüedad: {antiguedad_anios} años\nDías de vacaciones: {dias_vacaciones}")

# Crear la ventana principal
ventana = Tk()
ventana.title("Calculadora de Vacaciones")
ventana.geometry("400x300")

# Etiqueta y calendario para seleccionar la fecha de ingreso
Label(ventana, text="Seleccione su fecha de ingreso:").pack(pady=10)
calendario = DateEntry(ventana, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
calendario.pack(pady=10)

# Botón para calcular
Button(ventana, text="Calcular vacaciones", command=calcular_vacaciones).pack(pady=20)