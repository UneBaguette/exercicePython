# Début du programme
x = int(input("Entrer entier de x : "))
y = int(input("Entrer entier de y : "))
z = int(input("Entrer entier de z : "))
# La vérification des entiers est fait ici
if y > x and y > z:
    print("y est le plus grand entier\n")
elif x > y and x > z:
    print("x est le plus grand entier\n")
elif z > x and z > y:
    print("z est le plus grand entier\n")
elif x == y and x == z and y == z:
    print("Tous les entiers sont égaux\n")
else:
    print("Il y a deux entiers égaux\n")