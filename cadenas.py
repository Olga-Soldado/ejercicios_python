print ("Ejercicios de cadena\n")
#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en 
# líneas distintas el nombre del usuario tantas veces como el número introducido.
print("Ejercicio 1:")
num=int(input("Ingrese cantidad a repetir:"))
nom=str(input("Ingrese nombre a repetir :"))
for i in range(num):
    print (nom)



print("ejercicio 2:")
nombre=str(input("Ingrese nombre:"))
print(nombre.lower())
print(nombre.upper())
print(nombre.title(),"\n")

print ("ejercicio3:")
nom=str(input("Ingrese nombre:"))
print((nom.upper()),len(nom),"\n")

print ("ejercicio 4:")
tel = input("Introduce un número de teléfono con el formato +xx-xxxxxxxxx-xx: ")
print('El número de teléfono es ', tel[4:-3],"\n")

print ("Ejercicio 5:")
frase=input("Frase a invertir:")
print(frase[::-1])

print("Ejercicio 6:")
email = input("Introduce tu correo electrónico: ")
print(email[:email.find('@')] + '@gmail.com')

print("Ejercicio 7: ")
precio = input("Introduce el precio del producto con dos decimales:  ")
print(precio[:precio.find('.')], 'euros y', precio[precio.find('.')+1:], 'céntimos.')

print ("Ejercicio 8:")
fecha = input("Introduce la fecha de tu nacimiento en formato dd/mm/aaaa: ")
print('Día', fecha[:2])
print('Mes', fecha[3:5])
print('Año', fecha[6:])


print ("Ejercicio 10")
cesta = input('Introduce los productos de la cesta de la compra separados por comas: ')
print(cesta.replace(',', '\n'))