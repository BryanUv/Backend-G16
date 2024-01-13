numero = 10
# try (intentalo)
# y si es que falla entonces captura el error com un except
try:
  print(10/0)

except ZeroDivisionError:
  # si el error es de tipo division entre 0 entonces regresa aca
  print('no se puede dividir entre 0')

except Exception as error:
  # ver el causante del error
  print(error.args)
  # ver
  print(type(error))
  print('Operacion incorrecta')

print('otro codigo')

# lambda function / funcion anonima
resultado = lambda valor1, valor2, valor3: valor1 + valor2 + valor3
print(resultado(10,20,30))

# Crear una funcion que reciba dos numeros y devuelva cual es el mayor, si el usuario ingresa un valor que no sea un numero
# entonces volver a pedirselo hasta que sea un numero
def numeroMayor(numero1, numero2):
  # forma 1
  if numero1 > numero2:
    return numero1
  else:
    return numero2
  # forma 2
  return numero1 if numero1 > numero2 else numero2

while True:
  try:
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))
    # resultado = numeroMayor(numero1, numero2)
    resultado = lambda numero1, numero2: numero1 if numero1 > numero2 else numero2
    print('El numero mayor es {}'.format(resultado(numero1, numero2)))
    break  
  except:
    print("Tienes que ingresar solo numeros")

# pista: utilicen un while, un if y un try -except

# def numeroMayor():
#     while True:
#         try:
#             numero1 = int(input("Ingrese el primer número: "))
#             numero2 = int(input("Ingrese el segundo número: "))
#             break  
#         except Exception:
#             print("Error: Ingrese un valor numérico válido.")

#     if numero1 > numero2:
#         return f"{numero1} es mayor que {numero2}"
#     elif numero1 < numero2:
#         return f"{numero2} es mayor que {numero1}"
#     else:
#         return "Ambos números son iguales."

# resultado = numeroMayor()
# print(resultado)
