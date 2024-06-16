def main(): # << def définie une fonction
    username = "Maxime"         
    age = 21
    wallet = 1500

    print("Votre prénom est " + username)  # << il est Relié au username qui dit Maxime
    print("Vous avez " + str(age) + "ans et un porte monnaie de " + str(wallet) + " d'argents.")
    print("Nous allons passer sur vos notes d'écoles.")    # << écrit 

    note1 = int(input("Entrez la premiere note"))    # << Entre la première note
    note2 = int(input("Entrez la segonde note"))
    note3 = int(input("Entrez la derniere note"))
    resultat = (note1 + note2 + note3) / 3    # << La moyenne en 3

    print ("La moyenne de l'élève est de " + str(resultat)) # << str convertit des données en chaîne
main()