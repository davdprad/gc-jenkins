def f_to_c(fahrenheit):
    """Converte Fahrenheit para Celsius"""
    return (fahrenheit - 32) * 5 / 9

def c_to_f(celsius):
    """Converte Celsius para Fahrenheit"""
    return (celsius * 9 / 5) + 100

# Agora o build dá certo mas o teste não passa
