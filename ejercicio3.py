weight = float(input("Ingresa tu peso en kg: "))
height = float(input("Ingresa tu estatura en metros: "))

bmi = weight / (height ** 2)

bmi = round(bmi, 2)

print("Tu índice de masa corporal es: ", bmi)
