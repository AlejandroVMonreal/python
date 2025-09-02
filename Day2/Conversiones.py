#implicitas
num1 = 20
num2 = 30.5

num1 = num1 + num2 #python hacer converciones implicitas sin hacer cast

print(type(num1))
print(type(num2))

#explicitas
num3 = 5.8
print(num3)
print(type(num3))

num4 = int(num3) #hacemos casting para la variable num3 haciendola int
print(num4)
print(type(num4))

#casting con inputs
edad = input("Dime tu edad: ")
print(int(edad))
print(type(edad))
