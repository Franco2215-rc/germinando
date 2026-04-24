# numeros = [1 , 2 , 3 , 4 , 5]
# keku = []
# print(keku)
# nombres = ["Franco", "Lucia", "Carlos", "Luis" , "Bana"]
# print(nombres[1])
# nombres[1] = "Lucia"
# nombres.append("Jesus")
# # print(nombres)
# # for nombres in nombres:
# #     print(nomb
# usuario = {
#     "nombre": "Juan",
#     "edad": 30
# }
# print(usuario["nombre"])
# usuario["edad"] = 31
# print(usuario["edad"])
# usuario["email"] = "juampitorrico.com"
# print(usuario["email"])
# for clave, valor in usuario.items():
#     print(f"el {clave} de Juan es {valor}")


# usuarios = [
#     {"nombre": "Ansu", "edad": 21 },
#     {"nombre": "Lamine", "edad": 18},
#     {"nombre": "Pepe" , "edad": 15}
# ]
# for usuario in usuarios:
#     if usuario["edad"] >= 18:
#         print(usuario["nombre"])
#     else:
#         print("Usuario menor de edad")


# import random
# numeros = []
# for i in range (12):
#     numero_aleatorio = random.randint(1,750)
#     numeros.append(numero_aleatorio)
# print(f"lista generada:{numeros}")  
# print(f"El numero mas grande de la lista es: {max(numeros)}")

# usuarios = [
#      {"nombre": "Castro" ,"email": "castro@gmail.com"},
#      {"nombre": "Javier" ,"email": "javier@gmail.com"},
#      {"nombre": "Elias" , "email": "elias@gmail.com"}
#  ]
# print("Nombres de los usuarios: ")
# for usuario in usuarios:
#      print(f"-{usuario['nombre']}")

usuarios = {}


print(" REGISTRO ")
nombre_nuevo = input("Registra un nombre: ").lower()
direccion_nueva = input(f"Cuál es la dirección de {nombre_nuevo}?: ")


usuarios[nombre_nuevo] = direccion_nueva
print("Guardado con éxito")

print(" BÚSQUEDA ")

nombre = input("A quién buscas?: ").lower()

resultados = usuarios.get(nombre)

if resultados:
    print(f" Usuario encontrado, la direccion es {resultados}")
else:
    print(f" Usuario no encontrado, intente devuelta boludazo")



  

