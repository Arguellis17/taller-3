import re

def validar_contraseña(password):
    """
    Verifica si una contraseña cumple con los requisitos mínimos:
    - Al menos 8 caracteres
    - Al menos una letra mayúscula
    - Al menos una letra minúscula
    - Al menos un número
    - Al menos un carácter especial (!@#$%^&*())
    """
    if len(password) < 8:
        return "❌ La contraseña debe tener al menos 8 caracteres."
    
    if not re.search(r'[A-Z]', password):
        return "❌ La contraseña debe tener al menos una letra mayúscula."

    if not re.search(r'[a-z]', password):
        return "❌ La contraseña debe tener al menos una letra minúscula."

    if not re.search(r'\d', password):
        return "❌ La contraseña debe tener al menos un número."

    if not re.search(r'[!@#$%^&*()]', password):
        return "❌ La contraseña debe tener al menos un carácter especial (!@#$%^&*())."
    
    return "✅ La contraseña es segura."

if __name__ == "__main__":
    contraseña = input("Ingresa una contraseña para validar: ")
    print(validar_contraseña(contraseña))