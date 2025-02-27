import tkinter as tk
from tkinter import messagebox
import validator  # Importamos el módulo de validación de Camilo

def verificar_contraseña():
    password = entry.get()
    resultado = validator.validar_contraseña(password)
    messagebox.showinfo("Validación de Contraseña", resultado)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Validador de Contraseñas")

# Crear elementos de la interfaz
label = tk.Label(root, text="Ingresa tu contraseña:")
label.pack(pady=5)

entry = tk.Entry(root, show="*")  # Oculta la contraseña
entry.pack(pady=5)

button = tk.Button(root, text="Validar", command=verificar_contraseña)
button.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()