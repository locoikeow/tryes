cadena1 = "Hola,Maquina,Como,Estas"
cadena2 = "Bienvenido maquinola"

#Que podemos hacer?
print(dir(cadena1))

#convierte a mayusculas
mayusc = cadena1.upper()

#convierte a minusculas

#verificamos si una cadena termina con otra cadena dada, si es asì devuelve True
termina_con = cadena1.endswith("H")

#si el valor 1, se encuentra en la cadena original, remplaza el valor 1 de la misma, por el valor 2
cadena_nueva = cadena1.replace(","," ")

#separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(",")

print(mayusc)
