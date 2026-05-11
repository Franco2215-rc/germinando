# def saludar(nombre):
#     return f"hola {nombre}"
# print(saludar("Franco"))
# def devolver_mayor(num1 , num2):
#     if num1 > num2:
#         return num1
#     else:
#         return num2
# print(devolver_mayor(10 , 7))

# try:
#     num1 = float(input("Ingrese el primer numero: "))
#     num2 = float(input("Ingrese el segundo numero: "))
#     resultado = num1/num2
#     print("el resultado de la division es: ", resultado)
# except ZeroDivisionError:
#     print("No se puede dividir por 0")
# except ValueError:
#     print("Ingrese valores validos")
# with open("notas.txt", "w", encoding="utf-8") as archivo:
#       archivo.write("HOLAAAAA")
#       archivo.write("ROJO AMARGO")
#       archivo.write("UWO")
#       print ("Archivo creado")
try:
      with open("notas.txt", "r", encoding="utf-8") as archivo:
           for linea in archivo:
                print(linea.strip())
except FileNotFoundError:
      print("El archivo solicitado no existe")























