# lista simple podemos pedir datos concretos (se pueden modificar)
lista = ['Lucas Dalto','Soy Dalto',True,1.80]
lista [1] = 'hola' #modificacion

print(lista[1]) # Se muestra el valor 1 (empiezan en 0)

# tupla podemos pedir datos (inmodificable)
tupla = ('Lucas Dalto','Soy Dalto',True,1.80)

print(tupla[0]) # Mostramos valor 0

# conjuntos (set) (inmodificable) 
# No se muestran valores repetidos
conjunto = {'Lucas Dalto','Soy Dalto',True,1.80,'Soy Dalto'}

print(conjunto)# No puedes imprimir uno concreto

# Creacion de un diccionario
diccionario = {
    'nombre' : 'Lucas Dalto',
    'canal'  : 'Soy Dalto'
}

print(diccionario['canal']) # Se llama por nombre
