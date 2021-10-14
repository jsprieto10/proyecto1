''' 
Ejercicio 4:
Hacer un programa para ingresar el radio de un circulo y se reporte su área y 
la longitud de la circunferencia
'''
import math

radio = float (input("radio -> "))

area = math.pi * radio**2
longitud = 2 * math.pi * radio

print(f"El ares es: {area}")
print(f"La longitud de la circunferencia es: {longitud} ")

''' 
Ejercicio 4:
Hacer un programa para ingresar el radio de un circulo y se reporte su área y 
la longitud de la circunferencia
'''
import math

radio = float (input("radio -> "))

area = math.pi * radio**2
longitud = 2 * math.pi * radio

print(f"El ares es: {area:.2f}")
print(f"La longitud de la circunferencia es: {longitud:.2f} ")

'''
Ejercicio 5:
una tienda ofrece un descuento del 15% sobre el total de la compra y un 
cliente desea saber cuánto deberá pagar finalmente por su compra.
'''

precio = float(input("Digite el precio: "))

descuento = precio * 0.15
precio_final = precio - descuento

print(f"El precio final a pagar es de ${precio_final:.2f} ")


#Condicionales

numero = int(input("Digite un numero: "))

if numero>0:
    print("El numero es positivo")


print("Fin del programa")


#Condicionales

numero = int(input("Digite un numero: "))

if numero>0:
    print("El numero es positivo")
else:    
    print("El numero es negativo")

print("Fin del programa")

#Condicionales

numero = int(input("Digite un numero: "))

if numero>0:
    print("El numero es positivo")
elif numero==0:
    print("El número es cero")
else:    
    print("El numero es negativo")

print("Fin del programa")


#condicionales combinados

edad = int(input("Digite su edad: "))

if edad>=18:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")


#condicionales combinados

edad = int(input("Digite su edad: "))

if edad>0:
    print("Edad correcta")
    if edad>=0:
        print("Es mayor de edad")
else:
    print("Edad incorreta")


#condicionales combinados

edad = int(input("Digite su edad: "))

if edad>0 and edad<100:
    print("Edad correcta")
    if edad>=18:
        print("Es mayor de edad")
else:
    print("Edad incorreta")


#condicionales combinados

edad = int(input("Digite su edad: "))

if 0<edad<100:
    print("Edad correcta")
    if edad>=18:
        print("Es mayor de edad")
else:
    print("Edad incorreta")


'''
Ejercicio 1:
Hacer un programa que pida 2 números y se de cuenta cuál de ellos es par,
o si ambos lo son.
'''
num1 = int(input("Digite un numero: "))
num2 = int(input("Digite otro numero: "))

if num1%2==0 and num2%2==0:
    print("Ambos numeros son pares")
elif num1%2==0 and num2%2!=0:
    print(f"{num1} es par ")
elif num1%2!=0 and num2%2==0:
    print(f"{num2} es par ")
else:
  print("Ambos numeros son impares")


'''
Ejercicio 2:
Hacer un programa que pida 3 números y derermine cuál es el mayor.
'''

num1 = int(input("Digite un numero: "))
num2 = int(input("Digite un numero: "))
num3 = int(input("Digite un numero: "))

if num1>num2 and num1>num3:
  print(f"{num1} es el numero mayor ")
elif num1<num2 and num3<num2:
    print(f"{num2} es el numero mayor ") 
elif num1==num2==num3:
    print("Son numeros iguales")
else:
  print(f"{num3} es el numero mayor ")

'''
Ejercicio 2:
Hacer un programa que pida 3 números y derermine cuál es el mayor.
'''

num1 = int(input("Digite un numero: "))
num2 = int(input("Digite un numero: "))
num3 = int(input("Digite un numero: "))

if num1>=num2 and num1>=num3:
  print(f"{num1} es el numero mayor ")
elif num1<=num2 and num3<=num2:
    print(f"{num2} es el numero mayor ") 
elif num3>=num1 and num3>=num2:
    print(f"{num3} es el numero mayor ")


'''
Ejercicio 3:
Hacer un programa que pida un carázter e indique si es una 
vocal o no.
'''

carac = input(" Digite un carácter: ")


if carac=='a' or carac=='e' or carac=='i' or carac=='o'or carac=='u' :
    print("Es una vocal")
else:
  print("No es una vocal")


carac = input(" Digite un carácter: ").lower() #minuscula


if carac=='a' or carac=='e' or carac=='i' or carac=='o'or carac=='u' :
    print("Es una vocal")
else:
  print("No es una vocal")


  '''
Ejercicio 3:
Hacer un programa que pida un carázter e indique si es una 
vocal o no.
'''

carac = input(" Digite un carácter: ").upper() #mayuscula


if carac=='a' or carac=='e' or carac=='i' or carac=='o'or carac=='u' :
    print("Es una vocal")
else:
  print("No es una vocal")


'''
Ejercicio 4:
Construir un programa que simule el funcionamiento de una 
calculadora que puede realizar las cuatro operaciones aritméticas
básicas (suma, resta, multiplicación y división). El usuario debe
especificar la operación con el primer carácter del nombre de la 
operación.
S,s - Suma
R,r - Resta
P,p,M,m - Multiplicación
D,d - División
'''

num1 = float(input("Digite un numero: "))
num2 = float(input("Digite un numero: "))

operacion = input("Digite la operación: ").upper()

if operacion == 'S':
  suma = num1+num2
  print(f"\n La suma es: {suma} ")
elif operacion == 'R':
  resta = num1-num2
  print(f"\n La resta es: {resta} ")
elif operacion == 'M' or operacion == 'P':
  mult = num1*num2
  print(f"\n La multipicacion es: {mult} ")
elif operacion == 'D':
  dic =  num1/num2
  print(f"\n La divicón es: {div:.2f}")
else:
  print(f"\n Se equivocó de operación")




  '''
Ejercicio 5
Hacer un programa que simule un cajero autompatico con un saldo inicial de $1000
y tendrá el siguiente menú de opciones:

1. Ingresar dinero en la cuenta
2. Retirar dinero de la cuenta
3. Mostrar dinero disponible
4. salir
'''
saldo = 1000

print("\t.:MENU:.")
print("1. Ingresar dinero en la cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Mostrar dinero disponible")
print("4. salir")
opcion = int(input("Digite una opcion de menu: "))

print() 

if opcion == 1:
    extra = float(input("Cuanto dinero desea ingresar -> "))
    saldo += extra
    print(f"Dinero en la cuenta: {saldo} ")
elif opcion ==2:
      retirar = float(input("Cuanto dinero desea retirar -> "))
      if retirar>saldo:
        print("No tiene esa cantidad de dinero")
      else:
        saldo -= retirar
        print(f"Dinero en la cuenta: {saldo} ")
elif opcion == 3:
      print(f"Dinero en la cuenta: {saldo} ")
elif opcion == 4:
      print("Gracias por utilizar su cajero automático")
else: 
  print("Error, se equivocó de opcioin de menu")



#Listas

lista = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

print(lista[0:3])


#Listas

lista = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", 40,5.67,[1,2,3],True]

print(lista)

#Listas

lista = [1,2,3,4,5]

lista.append(6)       #añadir al final de la lista
lista.append("Anyi")

print(lista)

#Listas

lista = [1,2,4,5]

lista.insert(2,3)   #INsertar en alguna posición de la lita, en este caso el 3 en la posición 2

print(lista)


#Listas

lista = [1,2,4,5]

lista.insert(2,"amor")

print(lista)

#Listas

lista = [1,2,3,4,5]

lista.extend([6,7,8])

print(lista)

#Listas

lista1 = [1,2,3,4,5]
lista2 = [6,7,8]

lista3 = lista1+lista2

print(lista3)


#Listas

lista = [1,2,3,4,5,"Anyi"] 

print("Anyi" in lista)    #Preguntar si hay algún elemento en la lista



#Listas

lista = [1,2,3,4,5,"Anyi",1,2,3,1,"Anyi", 1]

print(lista.count(1)) #Cuantas veces aparece un número en una lista


#Listas

lista = [1,2,3,4,5,"Anyi"]

lista.pop(3) #Eliminar datos de la lista

print(lista) 

#Listas

lista = [1,2,3,4,5,"Anyi"]

lista.clear() #eliminar la lista

print(lista)

#Listas

lista = [1,2,3,4,5,"Anyi"]

lista.__reversed__() #voltear la lista

print(lista)

#Listas

lista = [1,2,3,4,5,"Anyi"] * 2  #doblicar la lista

print(lista)


#Listas

lista = [5,4,-7,9,0,1,3]

lista.sort() #ordenar ascencentemente

print(lista)

lista = [5,4,-7,9,0,1,3]

lista.sort(reverse=True) #ordenar decencentemente

print(lista)


# Tuplas

tupla = (4,"Reyes",6.78, [1,2,3],4)

lista=list(tupla) #transformar dupla en lista, las dupla no se pueden cambiar


print(lista)

#Conjuntos

conjunto = set()

conjunto = {1,2,3,"Reyes,4.56"}

print(conjunto)

#Conjuntos

conjunto = set()

conjunto = {1,2,3,"Reyes",4.561,2,3,}

conjunto.add(5)
conjunto.add("Adiós")
conjunto.add('a')

print(conjunto)

#Conjuntos
a = {1,2,3}
b = {3,1,2}

print(a == b)

#Conjuntos
a = {1,2,3}
b = {3,4,5}

c= a|b #unir conjuntos

print(c)

#Conjuntos
a = {1,2,3}
b = {3,4,5}

c= a&b #interseción

print(c)
#Conjuntos
a = {1,2,3}
b = {3,4,5}

c= a-b #diferencia

print(c)

#Conjuntos
a = fronzenset({1,2,3}) #inmutable paracido a la dupla
b = {3,4,5}

c= {1,2,3,4,5}
print(a.isdisjoint(b))

#Diccionarios

diccionario  = {"azul":"blue","rojo":"red","verde":"green"}

print(diccionario)

#Diccionarios

diccionario  = {"azul":"blue","rojo":"red","verde":"green"}

print(diccionario["azul"]) #me muestra el valor de azul, o sea blue

#Diccionarios

diccionario  = {"azul":"blue","rojo":"red","verde":"green"}

diccionario["amarillo"] = "yellow" #añadir al diccionario

print(diccionario)

#Diccionarios

diccionario  = {"azul":"blue","rojo":"red","verde":"green"}

del(diccionario["verde"]) #eliminar diccionario

print(diccionario)

#Diccionarios

equipo = {10:"Paulo Dibala", 11:"Douglas Costa", 7:"Cristiano Ronaldo", 17:"Mario Mandzukic"}

print(equipo)


#Diccionarios

equipo = {10:"Paulo Dibala", 11:"Douglas Costa", 7:"Cristiano Ronaldo", 17:"Mario Mandzukic"}

print(equipo[10]) #pasa la clave es 10 la cual es de paula diabala.

#Diccionarios

equipo = {10:"Paulo Dibala", 11:"Douglas Costa", 7:"Cristiano Ronaldo", 17:"Mario Mandzukic"}

print(equipo.get(9, "No existe un jugador con ese dorsal"))

#pilas

pila = [1,2,3]

#Se agrega elementos por el final
pila.append(4)
pila.append(5)

print(pila)
#Sacando elementos por el final
pila.pop()

print(pila)

#pilas

pila = [1,2,3]

#Se agrega elementos por el final
pila.append(4)
pila.append(5)

print(pila)
#Sacando elementos por el final
n = pila.pop()
print(f"Sacando el elemento {n} ")
print(pila)


#Colas

cola = ["Maria","Anyi","Jose", "Stiven"]

#Agregamos elementos al final de la cola
cola.append("Fabian")
cola.append("Didier")

print(cola)

#sacando elementos por el principio de la cola
n = cola.pop(0) #atendiendo la primera persona que llogó a la cola
print(f"Atendiendo a {n} ")

print(cola)

'''
Ejerccio 1:
Escriba un progrma donde tenga una lista y que, a continuación,
elimine los elementos repetidos de una lista.
'''

lista = [1,2,3,"Anyi",2,2,1,"Anyi",3]

conjunto = set(lista) #eliminar conjuntos repetidos

print(conjunto)