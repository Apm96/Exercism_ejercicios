# 1 De los n elementos de un vector dado calcule:
#  a. La sumatoria
#  b. La productoria
#  c. El Mayor Elemento
#  d. El menor Elemento

i = 0
vector = []
sumador = 0
producto = 1

while True:
    num = float(input("Ingrese el numero " + str(i + 1) + " , o escriba -1 para salir y continuar."))
    if num == -1:
        break
    vector.append(num)
    i = i + 1

sumador = sum(vector)
i = 0
for i in vector:
    producto = producto * i

numMayor = max(vector)
numMenor = min(vector)

print(f"La sumatoria es: {sumador}")
print(f"La productoria es: {producto}")
print(f"El numero mayor es: {numMayor}")
print(f"El numero menor es: {numMenor}")

#2 De los n elementos de un vector dado calcule:
#  a. Cantidad de elementos pares
#  b. Cantidad de elementos impares
#  c. Cantidad de elementos primos

i = 1
j = 0
f = 0
contadorPrimos = 0
vector = []
contadorPares = 0
contadorImpares = 0
contadorRes = 0

while True:
    num = float(input("Ingrese el numero " + str(i + 1) + " , o escriba -1 para salir y continuar."))
    if num == -1:
        break
    vector.append(num)
    i = i + 1

for f in vector:
    l = 1
    contadorRes = 0
    while l <= l:
        if f % l == 0:
            contadorRes = contadorRes + 1     
        l = l + 1       
    if contadorRes == 2:
        contadorPrimos = contadorPrimos + 1

for j in vector:
    if j % 2 == 0:
        contadorPares = contadorPares + 1
    elif j % 2 == 1:
        contadorImpares = contadorImpares + 1

print(f"La cantidad de numeros pares es: {contadorPares}")
print(f"La cantidad de numeros impares es: {contadorImpares}")
print(f"La cantidad de numeros primos es: {contadorPrimos}")

# 3 Dado un Vector v y un Vector v1 de cómo resultado un Vector resultante de
#   las siguientes operaciones:
#   a. Suma
#   b. Resta

v = []
v1 = []
resResta = []
resSuma = []
restas = 0
sumas = 0
tamanio = int(input("Digite el tamaño de los vectores: "))

for i in range(1,tamanio + 1):
    numv = float(input("Ingrese los valores del Vector A: "))
    v.append(numv)
    
for j in range(1,tamanio + 1):
    numv1 = float(input("Ingrese los valores del Vector B: "))
    v1.append(numv1)

for k in range(0,tamanio):
    sumas = v[k] + v1[k]
    resSuma.append(sumas)
    sumas = 0

for l in range(0,tamanio):
    restas = v[l] - v1[l]
    resResta.append(restas)
    restas = 0
    
print(f"Vector A: {v}")
print(f"Vector B: {v1}")
print(f"El resultado de la suma de los vectores es: {resSuma}")
print(f"El resultado de la resta de los vectores es: {resResta}")

# 4 De los n elementos de un vector dado identifique el número que mas se
#   repite e indique cual es.

i = 1
vector = []
contadorIgual = 0
auxiliarIgual = 0
Numrepetido = 0
auxiliarRepetido = 0
while True:
     num = float(input("Ingrese el numero " + str(i + 1) + " , o escriba -1 para salir y continuar."))
     if num == -1:
        break
     vector.append(num)
     i = i + 1
    
for j in vector:
    for m in vector:
        if j == m:
            contadorIgual += 1
            Numrepetido = m
            
    if contadorIgual > auxiliarIgual:
        auxiliarIgual = contadorIgual
        auxiliarRepetido = Numrepetido
    contadorIgual = 0
    
print(f"El numero {auxiliarRepetido} es el numero que mas se repite.")

# 5 Dado un Vector v de longitud par, divida en 2 partes, en la primera parte
#   realice la productoria y en la segunda la sumatoria. Entregue los valores
#   resultantes.

vector = []
z = 0
x = 0
sumatoria = 0
producto = 1
while True:
    num = int(input("Ingrese el tamaño del vector "))
    if num % 2 != 0:
        print("Debe digitar un numero par")
    else:
        break
    
for z in range(0,num):
    number = float(input(f"Ingrese el elemento {z} "))
    vector.append(number)

mitades = len(vector)/2
mitad = int(mitades)
v = vector[:mitad]
v1 = vector[mitad:]

sumatoria = sum(v1)
for x in v:
    producto = producto * x 

print(f"La  productoria de la primera parte del vector es: {producto}") 
print(f"La sumatoria de la segunda parte del vector es: {sumatoria}")


# 6 Dado un vector v, indique si es simétrico, un vector es simétrico si siendo
# longitud par los números de la primera mitad son iguales al inverso de la
# otra mitad por ejemplo: X=[1,2,3,3,2,1], en el ejemplo x es un vector
# simétrico, en caso que la longitud del vector sea impar, se ignorará el
# elemento central y se seguirá la misma lógica anterior, por ejemplo:
# Y=[3,5,7,8,7,5,3], en este ejemplo Y es simétrico.

tamanio = int(input("Digite la cantidad de valores del vector "))
i = 0
j = 0
k = 0

contador = 0
vector = []

for i in range(0, tamanio):
    vector.append(int(input("Digite el valor No " + str(i+1) )))
    
i = 0
if len(vector) % 2 == 0 :
    
    for i in range(0, int(len(vector) / 2)): 
        k = len(vector) - i - 1
        j = 0
        while( j < int(len(vector) / 2) ): 
            if (vector[i] == vector[k]):
                contador = contador + 1
            j = j + 1
            k = k - 1
else:
    
    media = int((len(vector) - 1) / 2)
    vector.pop(media)
    
    for i in range(0, int(len(vector) / 2)):
        k = len(vector) - i - 1
        j = 0
        while( j < int(len(vector) / 2) ):  
            if (vector[i] == vector[k]):
                contador = contador + 1
            j = j + 1
            k = k - 1

#print(f"Contador: {contador}")
if (contador == int(len(vector) / 2) + 1):
    print("El vector es simetrico")
else:
    print("El vector no es simetrico")
    


# 7 Dado dos vectores númericos A y B debe realizar las siguiente operaciones
#   con conjuntos:
#   a. Unión: Conjunto que contiene(sin repetir) los elementos de A y B.
#   b. Intersección: Conjunto que contiene los elementos comunes que
#   aparecen en los conjuntos A y B
#   c. Diferencia(A-B) Conjunto formado por los elementos que pertenecen
#   al conjunto A y no pertenecen al conjunto B.
#   d. Diferencia (B-A) Conjunto formado por los elementos que pertenecen
#   al conjunto B y no pertenecel al conjunto A. 


tamanioA = int(input("Digite la cantidad de valores del vector A "))
tamanioB = int(input("Digite la cantidad de valores del vector B "))


vectorA = []
vectorB = []
vectorInterseccion = []
vectorA_B = []
vectorB_A = []
validar = False
i = 0
j = 0

for i in range(0, tamanioA):
    vectorA.append(int(input("Digite el valor No " + str(i+1) + " del vector A" )))
i = 0
for i in range(0, tamanioB):
    vectorB.append(int(input("Digite el valor No " + str(i+1) + " del vector B" )))
i = 0

for i in range(0, len(vectorA)):
    for j in range(0, len(vectorB)):
        if (vectorA[i] == vectorB[j - 1]):
            vectorB.pop(j - 1)
            vectorInterseccion.append(vectorB[j - 1])
        else:
            validar = True
    if (validar):
        vectorA_B.append(vectorA[i])
        validar = False
        
validar = False
i = 0
j = 0     
for i in range(0, len(vectorB)):
    for j in range(0, len(vectorA)):
        if (vectorB[i] != vectorA[j - 1]):
            validar = True
    if (validar):
        vectorB_A.append(vectorB[i])
        validar = False

print("Union Vector A y B: " +  str(vectorA + vectorB))
print(f"Interseccion Vector A y B: {vectorInterseccion}")
print(f"Diferencia A-B: {vectorA_B}")
print(f"Diferencia B-A: {vectorB_A}")












