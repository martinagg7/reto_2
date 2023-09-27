numeros_str = input("Introducir la lista de números: ")
lista_numeros_str = numeros_str.split()  
lista_numeros_usuario = list(map(int, lista_numeros_str))


min_moves = abs(lista_numeros_usuario[0])
for x in lista_numeros_usuario:
    if abs(x) < min_moves:
        min_moves = abs(x)

print("El número mínimo de movimientos es:", min_moves)
