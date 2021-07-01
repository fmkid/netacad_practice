poblacion=[]
nombre=("Pedro", "Juan", "María", "Pablo", "Liliana")
apellido=("Díaz", "Ruiz", "Jerez", "Moreno", "Ortiz")
edad=(30,55,23,42,24)
genero=('M','M','F','M','F')
estatura=(1.70,1.65,1.50,1.67,1.80)
peso=(55,67,80,54,70)

for i in range(len(nombre)):
    persona = {}
    persona["ID"]=i
    persona["Nombre"]=nombre[i]
    persona["Apellido"]=apellido[i]
    persona["Edad"]=edad[i]
    persona["Género"]=genero[i]
    persona["Estatura"]=estatura[i]
    persona["Peso"]=peso[i]
    poblacion.append(persona)

for persona in poblacion:
    if persona["ID"] % 2 == 0:
        persona["Nacionalidad"]="Colombiana"
    else:
        persona["Nacionalidad"]="Venezolana"
    for item in persona:
        print(item+":",persona[item],end="")
        if item == "Edad":
            print(" años")
        elif item == "Estatura":
            print("m")
        elif item == "Peso":
            print("kg")
        else:
            print()
    print()