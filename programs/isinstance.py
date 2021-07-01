class miClase:
    pass

miObjeto = miClase()

def esTipo(valor, tipo) -> bool: 
#funcion que evalúa si un valor pertenece a un tipo especifico de variable,
#similar a usar la funcion isinstance(), teniendo en cuenta que los tipos de
#variables se definen como clases en sí (se puede usar la propiedad __name__)
    try:
        for elem in tipo:
            if type(valor).__name__ == elem.__name__:
                return True
        return False
    except:
        return type(valor).__name__ == tipo.__name__


tipo_var = (int, float, str, bool, list, tuple, dict, object)
valor = "Hola mundo"
for elem in tipo_var:
    print(elem.__name__ + ":\t", esTipo(valor, elem), "-", isinstance(valor, elem))