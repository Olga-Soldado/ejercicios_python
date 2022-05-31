from audioop import avgpp


print("Ejercicios varios:,\n")
print("Ejercicio 1:")
print("Obtén del 1 al 255.")
for i in range (256):
        print(i)
print("\n")

print("Ejercicio 2:")
print("Consigue pares hasta 1000. ")
for i in range (1000):
    if (i%2==0):
        print(i)
print("\n")

print ("Ejercicio 3:")
print("Suma impares hasta 5000")
suma =0
for i in range (5000):
    if i%2==1:
        suma =suma +i
print (suma,"\n")

print ("ejercicio 4:")
print("Itera un array")
arreglo=[1,2,5] 
suma2=0
for i in range (len(arreglo)):
    suma2 =suma2+arreglo[i]
print (suma2,"\n")

print ("Ejercicio 5:")
print("Encuentra el mayor (max)")
a=[-3,3,7,5]
print (max(a),"\n")

print ("Ejercicio 6: ")
print("Encuentra el promedio (avg)")
b=[1,3,5,7,20]
prom1=0
for i in range(len(b)):
    prom1=prom1+b[i]
    s=prom1/len(b)
print(s,"\n")

print("Ejercicio 7:")
print("Array de impares")
c=[]
for i in range (50):
    if (i%2==1):
        c.append(i)
print(c,"\n")

print ("ejercicio 8:")
print("Mayor que Y:")
d=[1,3,5,7] 
Y = 3
contar=0
for i in range(len(d)):
    if (Y<d[i]):
        contar+=1
print(contar,"\n")

print("Ejercicio 9")
print("Cuadrados")
e=[1,5,10,-2]
for i in range(len(e)):
    e[i]=e[i]**2
print (e,"\n")

print("Ejercicio 10:")
print("Negativos")
f=[1,5,10,-2]
for i in range(len(f)):
    if (f[i]<0):
        f[i]=0
print(f,"\n")

print("Ejercicio 11:")
print("Max/Min/Avg")
g=[1,5,10,-2]
new=[]
prom=0
for i in range(len(g)):
    prom=prom+g[i]
    s=prom/len(g)

new.append(max(g))
new.append(min(g))
new.append(s)
print(new,"\n")


print("Ejercicio 12:")
print("Intercambia Valores")
h=[1,5,10,-2]
r=h[0]
if (len(h)>2):
    h[0]=h[-1]
    h[-1]=r
print(h,"\n")



print("Ejercicio 13:")
print("De Número a String")
u=[-1,-3,2]
for i in range(len(u)):
    if (u[i]<0):
        u[i]="Dojo"
print(u,"\n")
