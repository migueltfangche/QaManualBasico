import math
import pytest

def calcular_area_circulo(radio):
    if radio < 0:
        raise ValueError("El radio no puede ser negativo")
    return math.pi * radio ** 2

def test_calcular_area_circulo():
    # Caso de prueba con radio positivo        
    assert calcular_area_circulo(1) == math.pi, "El area del círculo con radio 1 no es igual a pi"

    # Caso de prueba con radio cero
    assert calcular_area_circulo(0) == 0, "El área del círculo con radio 0 deberia ser 0 "

    # Caso de prueba con radio negativo, se espera que lance un error
    with pytest.raises(ValueError):
        calcular_area_circulo(-1), "No se lanzo una excepción para un radio negativo"

if __name__ == "__main__":
    pytest.main([__file__])
    print("!Todas las pruebas han pasado correctamente!")