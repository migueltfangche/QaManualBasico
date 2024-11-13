def sumaSoloPositivos( num1, num2):
    if(num1>0):
        resultado = num1 + num2
    else: 
        resultado = num2
    return resultado

def test_sumaSoloLosPositivos():
    assert sumaSoloPositivos(3 , 4) == 7
    assert sumaSoloPositivos(-3, 7 ) == 7
    assert sumaSoloPositivos(-32, -5 ) == -5

test_sumaSoloLosPositivos()
