import validator

def test_contraseña_segura():
    assert validator.validar_contraseña("Aa1!abcd") == "✅ La contraseña es segura."

def test_contraseña_corta():
    assert validator.validar_contraseña("Aa1!") == "❌ La contraseña debe tener al menos 8 caracteres."

def test_sin_mayuscula():
    assert validator.validar_contraseña("aa1!abcd") == "❌ La contraseña debe tener al menos una letra mayúscula."

def test_sin_minuscula():
    assert validator.validar_contraseña("AA1!ABCD") == "❌ La contraseña debe tener al menos una letra minúscula."

def test_sin_numeros():
    assert validator.validar_contraseña("AA!abcd") == "❌ La contraseña debe tener al menos un número."

def test_sin_caracter_especial():
    assert validator.validar_contraseña("Aa1abcd") == "❌ La contraseña debe tener al menos un carácter especial (!@#$%^&*())."