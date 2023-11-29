# Initialise une liste vide pour y stocker l'historique des calculs
historique = []

def user_calcul():
    
    a = float(input("Entrez votre premier nombre : "))
    b = float(input("Entrez votre second nombre : "))
    operation = input("Choisissez l'opération (+, -, *, /, %) : ")

    # Vérifie si les chaines selectionnées correspondent au choix de l'utilisateur
    if operation in ("+", "-", "*", "/", "%"):
        # Fait l'évaluation des éléments dans eval()  
        resultat = eval(f"{a} {operation} {b}")
        print(resultat)

        historique.append({
            'a': a,
            'b': b,
            'operation': operation,
            'resultat': resultat
        })
    else:
        print("Opération non valide")

def print_historique():

    print("Historique de la calculatrice")
    for donnee in historique:
        print(donnee)

def select_option():
      
      print("Bienvenue dans Calculette 9000 - Version 1.0")
    # Effectue une boucle infini avec while True pour réitérer le programme à l'infini
      while True:
    
        info = input("Choisissez vos options 'Historique' ou 'Calcul' ou 'Sortir' pour quitter : ")

        if info == "Historique":
            print_historique()
        elif info == "Calcul":
            print("Effectuez un calcul")
            user_calcul()
        elif info == "Sortir":
            print("Sortie du programme")
            break
        else:
            print("Option non valide")

select_option()