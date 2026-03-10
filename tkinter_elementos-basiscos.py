import tkinter as tk
from tkinter import ttk

ventana1= tk.Tk()
ventana1.title("Elementos visuales basicos")

tk.Label(ventana1, text="Primer Apellido").grid(row=0, column=0, padx=10, pady=10, sticky="e")
input_1rApe=tk.Entry(ventana1)
input_1rApe.grid(row=0, column=1, padx=5, pady=10)

tk.Label(ventana1, text="Segundo Apellido").grid(row=0, column=2, padx=10, pady=10, sticky="e")
input_2oApe=tk.Entry(ventana1)
input_2oApe.grid(row=0, column=3, padx=10, pady=10, sticky="e")

tk.Label(ventana1, text="Nombre").grid(row=0, column=4, padx=10, pady=10, sticky="e")
input_nombre=tk.Entry(ventana1)
input_nombre.grid(row=0, column=6, padx=10, pady=10, sticky="e")

tk.Label(ventana1, text="Fecha y lugar de Nacimiento:").grid(row=1, column=0, padx=10, pady=10, sticky="e")

tk.Label(ventana1, text="Día:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
input_dia=tk.Entry(ventana1)
input_dia.grid(row=2, column=1, padx=10, pady=10, sticky="e")
ventana1.mainloop()
