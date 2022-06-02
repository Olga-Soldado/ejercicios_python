print("Condicionales:")
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
print("Ejercicio 1:")
edad=int(input("Ingrese su edad:"))
if (edad<18):
    print("Usted es menor de edad.\n")
else:
    print("Usted es mayor de edad.\n")

#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
# por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
print("Ejercicio 2:")
contraseña="abc123"
confirmarc=str(input("Ingrese su contraseña:"))
if (contraseña==confirmarc):
    print("Ambas contraseñas coinciden\n")
else:
    print("Contraseña invalida.\n")

#Escribir un programa que pida al usuario dos números
#  y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
print("Ejercicio 3:")
num1=int(input("Ingrese un numero :"))
num2=int(input("Ingrese un numero :"))
if (num2==0):
    print("numeros invalidos para la operacion")
else:
    print(num1/num2)

#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
print("Ejercicio 4:")
n=int(input("Ingrese numero :"))
if (n%2==0):
    print("El numero ingresado es par\n")
else:
    print("El numero es impar.\n")
#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales
#  o superiores a 1000 € mensuales. Escribir un programa que pregunte
#  al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
print("Ejercicio 5:")
edad=int(input("Ingrese edad:"))
ingresos=int(input("Ingresos mensuales :"))
if (edad>16) and  (ingresos>1000):
    print ("Segun su cantidad de ingresos corresponde tributar.\n")
else:
    print("No debe tributar.\n")

#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
# El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior 
# a la N y el grupo B por el resto. Escribir
#  un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
print("Ejercicio 6:")
nombre = input("¿Cómo te llamas? ")
sexo = input("¿Cuál es tu sexo (M o H)? ")
if sexo == "M":
    if nombre.lower() < "m":
        group = "A"
    else:
        group = "B"
else:
    if nombre.lower() > "n":
        group = "A"
    else:
        group = "B"
print("Tu grupo es " + group)
#Escribir un programa que pregunte al usuario su renta anual y
#  muestre por pantalla el tipo impositivo que le corresponde.
print ("Ejercicio 7:")
renta=int(input("Ingrese renta:"))
porcentaje=0
if (renta>60000):
    porcentaje=renta*0.45
    print("Usted de pagar ",porcentaje,"€ de impuesto\n")
elif (renta>35000 and renta<60000):
    porcentaje=renta*0.30
    print("Usted de pagar ",porcentaje,"€ de impuesto\n")
elif (renta>20000 and renta<35000):
    porcentaje=renta*0.20
    print("Usted de pagar ",porcentaje,"€ de impuesto\n")
elif (renta>10000 and renta<20000):
    porcentaje=renta*0.15
    print("Usted de pagar ",porcentaje,"€ de impuesto\n")
else:
    porcentaje=renta*0.05
    print("Usted de pagar ",porcentaje,"€ de impuesto \n")

#En una determinada empresa, sus empleados son evaluados al final de cada año.
#  Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando,
#  traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden 
# ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas.
#  A continuación se muestra una tabla con los niveles correspondientes a cada puntuación.
#  La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.
print("Ejercicio 8:")
bonificacion = 2400
inaceptable = 0
aceptable = 0.4
excelente = 0.6
puntos = float(input("Introduce tu calificación: "))
# Clasifiación por niveles de rendimiento
if puntos == inaceptable:
    nivel = "Inaceptable"
elif puntos == aceptable:
    nivel = "Aceptable"
elif puntos >= 0.6:
    nivel = "Excelente"
else:
    nivel = ""
# Mostrar nivel de rendimiento
if nivel == "":
    print("Esta puntuación no es válida\n")
else:
    print("Tu nivel de rendimiento es %s" % nivel,"\n")
    print("Te corresponde cobrar %.2f€" % (puntos * bonificacion),"\n")

#Escribir un programa para una empresa que tiene salas de juegos para todas
#  las edades y quiere calcular de forma automática el precio que debe cobrar a
#  sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente
#  y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, 
# si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
print("Ejercicio 9:")
edadcliente=int(input("Ingrese edad:"))
if (edadcliente<4):
    print("la entrada es gratis.\n")
elif(edadcliente<18 and edadcliente>4):
    print("Debe pagar 5€")
else:
    print("Debe pagar 10€")

print("Ejercicio 10:")
print("Bienvenido a la pizzeria Bella Napoli.\nTipos de pizza\n\t1- Vegetariana\n\t2- No vegetariana\n")
tipo = input("Introduce el número correspondiente al tipo de pizza que quieres:")
# Decisión sobre el tipo de pizza
if tipo == "1":
    print("Ingredientes de pizzas vegetarianas\n\t 1- Pimiento\n\t2- Tofu\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza vegetariana con mozzarella, tomate y ", end="")
    if ingrediente == "1":
        print("pimiento")
    else: 
        print("tofu")
else:
    print("Ingredientes de pizzas no vegetarianas\n\t1- Peperoni\n\t2- Jamón\n\t3- Salmón\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza no vegetarina con mozarrella, tomate y ", end="")
    if ingrediente == "1":
        print("peperoni")
    elif ingrediente == "2":
        print("jamón")
    else:
        print("salmón")

