# Début du programme
a = int(input("Entrer entier de a : "))
s = int(input("Entrer entier de s : "))
print(f"Valeur de a est de {a} et Valeur de s est de {s}")
# On échange les deux variables
a, s = s, a
# Le résultat de l'échange
print(f"Valeur de a est de {a} et Valeur de s est de {s}")