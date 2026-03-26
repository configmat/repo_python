ROUNDS = 3
import random
import string
letras_validas = string.ascii_lowercase
categorias = {
    "programacion": ["python", "programa", "variable", "funcion", "bucle"],
    "datos": ["cadena", "entero", "lista"]
}
points = 0
round_actual = 1
print("¡Bienvenido al Ahorcado!")
print()
print("Ingrese una categoria: ")
print()
for categoria in categorias:
    print(f"  |{categoria}|", end=" ")
print()
###### eleccion de categoria y retry en caso de error 3
eleccion = input()
while eleccion not in categorias:
    print("Categoria no valida. Intente de nuevo")
    eleccion = input("Elegi una categoria: ")
cat_elegida = categorias[eleccion]
words = random.sample(cat_elegida,ROUNDS)

for word in words:
    if round_actual == ROUNDS:
        print("    | Ronda final |    ")
    else:
        print(f"   | Ronda {round_actual} |   ")

    guessed = []
    attempts = 6 
    while attempts > 0:
        # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)# Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            print("¡Ganaste!")
            points += 6
            break
        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")
        letter = input("Ingresá una letra: ").lower()
        if len(letter) != 1 or letter not in letras_validas:
            print("Entrada no valida")
            continue 
        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            print("Esa letra no está en la palabra.")
            points -= 1
        print()
    else:
        print(f"¡Perdiste! La palabra era: {word}")
        points = 0
    round_actual += 1

print(f"Hiciste {points} puntos")