print("Bucles")
#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
print("Ejercicio 1:")
palabra=str(input("Ingrese una palabra:"))
for i in range(10):
    print(palabra)
print("\n")

#Escribir un programa que pregunte al usuario
#  su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
print("Ejercicio 2:")
edad=int(input("Ingrese su edad:"))
for i in range(edad+1):
    print(i)
print("\n")

#Escribir un programa que pida al usuario un número entero positivo y muestre por
#  pantalla todos los números impares desde 1 hasta ese número separados por comas.
print("Ejercicio 3:")
n=int(input("Ingrese numero:"))
for i in range (n):
    if(i%2==1):
        print(i ,end=", ")
print("\n")

#Escribir un programa que pida al usuario un número entero positivo y 
# muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
print("Ejercicio 4:")
entero=int(input("Ingrese numero: "))
for i in range(entero,-1,-1):
    print(i,end=",")
print("\n")

#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
# y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
print("Ejercicio 5:")
cantidad=float(input("Ingrese cantidad a invertir: "))
interes=float(input("Ingrese interes anual : "))
años=int(input("Ingrese cantidad de años: "))
capital=0
for i in range(años):
    cantidad*= 1 + interes / 100 
    print("Su ganancia es :",round(cantidad,2),"en el año ",i+1,"de su inversion.")
print("\n")

#Escribir un programa que pida al usuario un número entero y muestre 
# por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
print("Ejercicio 6:")
numero=int(input("Ingrese numero:"))
for i in range(numero):
    for j in range(i+1):
        print("*", end="")
    print("")
print("\n")
#Tablas de multiplicar 1,10
print("Ejercicio 7:")
for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end="\t")
    print("")
print("\n")
#Escribir un programa que pida al usuario 
# un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
print("Ejercicio 8:")
entero=int(input("Ingrese numero: "))
for i in range(1,entero, 2):
    for j in range(i,0,-2):
        print(j,end=" ")
    print("")
print("\n")

#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
print("Ejercicio 9:")
contraseña="password"
confirmar=""
while contraseña != confirmar:
    confirmar = input("Introduce la contraseña: ")
print("Contraseña correcta")
print("\n")
#Escribir un programa que pida al usuario un número entero 
# y muestre por pantalla si es un número primo o no.
print("Ejercicio 10:")
primo = int(input("Introduce un número mayor que 2: "))
i = 2
while primo % i != 0:
    i += 1
if i == primo:
    print(str(primo) + " es primo\n")
else:
    print(str(primo) + " no es primo\n")

#Escribir un programa que pida al usuario una palabra y 
# luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
print("Ejercicio 11:")
palabra=input("Ingresa una palabra:")
for i in range(len(palabra)-1, -1, -1):
    print(palabra[i])
print("\n")
#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por
#  pantalla el número de veces que aparece la letra en la frase.
print("Ejercicio 12:")
frase=input("Ingresa una frase:")
letra=input("Ingresa letra:")
contador=0
for i in frase:
    if i == letra:
        contador += 1
print("La letra <",letra,"> se repite ",cantidad,"en la frase ",frase,"\n")

#Escribir un programa que muestre el eco de todo lo que el usuario introduzca 
# hasta que el usuario escriba “salir” que terminará.
print("Ejercicio 13")
salir="salir"
eco=""
while salir != eco:
    eco = input("Introduce una palabra: ")
    print(eco)
print("Success!!\n")

