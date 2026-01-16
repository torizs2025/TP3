"""
Santiago Toriz
402
Jeu de vie avec des combats de monstres
"""
import random

niveau_vie = 20
numero_adversaire = 0
nombre_victoires = 0
nombre_defaites = 0
numero_combat = 0
showed_rules = False
force_adversaire = 0

while niveau_vie > 0: 
    if showed_rules is False:
        if numero_combat % 3 == 0 and numero_combat != 0:
            force_adversaire = random.randint(2, 5) + random.randint(2, 5)
            print('BOSSFIGHT!')
        else:
            force_adversaire = random.randint(1, 5) + random.randint(1, 5)

    print('vous tombez face à face avec un adversaire de difficulté : ', force_adversaire)
    print('vous avez', niveau_vie, 'point de vie')
    print("""Que voulez-vous faire ? 
1- Combattre cet adversaire
2- Contourner cet adversaire et aller ouvrir une autre porte
3- Afficher les règles du jeu
4- Quitter la partie""")

    choix = int(input())
    if choix == 1:
        numero_adversaire += 1
        print(f"Adversaire : {numero_adversaire}")
        print(f"Force de l'adversaire : {force_adversaire}")
        dtotal = random.randint(1, 6) + random.randint(1, 6)
        print('lancer du dé:', dtotal, )
        showed_rules = False
        if dtotal <= force_adversaire:
            statut_combat = 1
            niveau_vie -= force_adversaire
            numero_combat += 1
            nombre_defaites += 1
            print(f"Combat {numero_combat}:  {nombre_victoires} victoire vs {nombre_defaites} défaite")
            print('')
        if dtotal > force_adversaire:
            statut_combat = 2
            niveau_vie += force_adversaire
            numero_combat += 1
            nombre_victoires += 1
            print(f"Combat {numero_combat}:  {nombre_victoires} victoire vs {nombre_defaites} défaite")
            print('')

    elif choix == 2:
        print('Vous perdez un point de vie')
        niveau_vie -= 1
        print('', niveau_vie, 'point de vie restant')
        print('')

    elif choix == 3:
        showed_rules = True
        print("""Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  
        
        
        .Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.
Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  
Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.

La partie se termine lorsque les points de vie de l’usager tombent sous 0.

L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.
""")
        print('')
    elif choix == 4:
        print('Merci et au revoir... ')
        break

    if niveau_vie <= 0:
        print('vous êtes mort')
        break
