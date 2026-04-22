
#2.7
tipo_de_vehiculo = (input("Ingrese su tipo de vehiculo (auto,moto,camioneta): ")).lower()
horas = float(input("Ingrese la cantidad de horas estacionado: "))
if tipo_de_vehiculo == "moto":
    precio_moto = 300 * horas
    print(f"El total es {precio_moto}")
elif tipo_de_vehiculo == "auto":
    precio_auto = 600 * horas
    print(f"El total es {precio_auto}")
elif tipo_de_vehiculo == "camioneta":
    precio_camioneta = 800 * horas
    print(f"El total es {precio_camioneta}")









  

