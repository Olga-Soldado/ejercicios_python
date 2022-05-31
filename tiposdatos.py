print("Ejercicios de tipos de datos python.\n")
#Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
print("Ejercicio 1:")
print("¡Hola Mundo! \n")

#Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable
# y luego muestre por pantalla el contenido de la variable.
print("Ejercicio 2:")
saludo="¡Hola Mundo!"
print(saludo,"\n")

#Escribir un programa que pregunte el nombre del usuario en la consola y
#  después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!,
#  donde <nombre> es el nombre que el usuario haya introducido.
print("Ejercicio 3:")
nombre=input("Inserte nombre a imprimir por pantalla:")
print("¡Hola",nombre,"! \n")

#Escribir un programa que muestre por pantalla el resultado 
# de la siguiente operación aritmética ((3+2)/2*5)**2
print("Ejercicio 4:")
print(((3+2)/(2*5))**2,"\n")

#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el 
# coste por hora.Después debe mostrar por pantalla la paga que le corresponde.
print("Ejercicio 5:")
horas=int(input("Inserte horas:"))
coste=int(input("Inserte horas:"))
pagar=(horas*coste)
print("Total a pagar:",pagar,"\n")

#Escribir un programa que lea un entero positivo,n , introducido por el usuario y después muestre en pantalla 
# la suma de todos los enteros desde 1 hasta n. La suma de los  primeros enteros positivos puede ser calculada
# de la siguiente forma:
print ("Ejercicio 6:")
n=int(input("Inserte numero :"))
suma=0
if (n>0):
    for i in range(n):
        suma=suma +i
        resultado=suma/2
    print(suma)
    print (resultado,"\n") 
else:
    print ("Numero ingresado es menor a 0.-\n")
#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y 
# lo almacene en una variable, y muestre por pantalla la frase <<Tu índice de masa corporal es <imc> >> donde 
# <imc> es el índice de masa corporal calculado redondeado con dos decimales.
print ("Ejercicio 7: ")
peso=input("Cual es tu peso (kg):")
medida=input("Cuanto mides (mtr):")
imc = round(float(peso)/float(medida)**2,2)
print("Tu índice de masa corporal es " + str(imc),"\n")

#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un
# resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son  el cociente y el resto de la división entera respectivamente.
print("Ejercicio 8:")
n=int(input("Ingrese numero 1:"))
m=int(input("INgrese numero 2:"))
d=n//m
r=n%m
print(n," entre ", m ,"da un cociente de ",d,"y un resto de ",r,"\n")
#Escribir un programa que pregunte al usuario una cantidad a invertir,
#  el interés anual y el número de años,
#  y muestre por pantalla el capital obtenido en la inversión

print("Ejercicio 9:")
cantidad = float(input("¿Cantidad a invertir? "))
interes = float(input("¿Interés porcentual anual? "))
años = int(input("¿cantidad de años?"))
total=round(cantidad * (interes / 100 + 1) ** años, 2)
print("Capital final: " ,total ,"\n")

#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
# Suele hacer venta por correo y la empresa de logística les cobra por peso de
#  cada paquete así que deben  calcular el peso de los payasos y muñecas que saldrán en cada paquete
#  a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos
#  y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
print("Ejercicio 10:")
payaso = 112
muñeca = 75
payasos = int(input("Introduce el número de payasos a enviar: "))
muñecas = int(input("Introduce el número de muñecas a enviar: "))
peso = payaso * payasos + muñeca * muñecas
print("El peso total del paquete es de " ,peso,"\n")

#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece
#  el 4% de interés al año. Estos ahorros debido a intereses, que no
#  se cobran hasta finales de año, se te añaden al balance final de 
# tu cuenta de ahorros. Escribir un programa que comience leyendo la
#  cantidad de dinero depositada en la cuenta de ahorros, introducida
#  por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y
#  tercer años. Redondear cada cantidad a dos decimales.
print("Ejercicio 11:")
inversion = float(input("Introduce la inversión inicial: "))
interes = 0.04
balance1 = inversion * (1 + interes)
print("Balance tras el primer año:" , str(round(balance1, 2)))
balance2 = balance1 * (1 + interes)
print("Balance tras el segundo año:" ,str(round(balance2, 2)))
balance3 = balance2 * (1 + interes)
print("Balance tras el tercer año:" , str(round(balance3, 2)),"\n")
#Imagina que acabas de abrir una nueva cuenta de ahorros que te
#  ofrece el 4% de interés al año. Estos ahorros debido a intereses,
#  que no se cobran hasta finales de año, se te añaden al balance final
#  de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y 
# tercer años. Redondear cada cantidad a dos decimales.
print("Ejercicio 12:")
barras = int(input("Introduce el número de barras vendidas que no son frescas: "))
precio = 3.49 
descuento = 0.6
coste = barras * precio * (1 - descuento)
print("El coste de una barra fresca es " + str(precio) + "€")
print("El descuento sobre una barra no fresca es " + str(descuento * 100) + "%")
print("El coste final a pagar es " + str(round(coste, 2)) + "€")