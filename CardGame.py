

# L'ordinateur est le donneur des cartes.
import random


def attend_le_joueur():
    '''()->None
    Pause le programme jusqu'a ce que l'usager appuie Enter
    '''
    try:
         input("Appuyez Enter pour continuer. ")
    except SyntaxError:
         pass


def prepare_paquet():
    '''()->list of str
        Retourne une liste des chaines de caractères qui représente toutes les cartes,
        sauf le valet noir.
    '''
    paquet=[]
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for val in valeurs:
        for couleur in couleurs:
            paquet.append(val+couleur)
    paquet.remove('J\u2663') # élimine le valet noir (le valet de trèfle)
    return paquet

def melange_paquet(p):
    '''(list of str)->None
       Melange la liste des chaines des caractères qui représente le paquet des cartes    
    '''
    random.shuffle(p)

    
def donne_cartes(p):
     '''(list of str)-> tuple of (list of str,list of str)

     Retournes deux listes qui représentent les deux mains des cartes.  
     Le donneur donne une carte à l'autre joueur, une à lui-même,
     et ça continue jusqu'à la fin du paquet p.
     '''
     

     donneur=[]
     autre=[]
     for i in range(0,len(p)-1,2):
         autre.append(p[i])#pour chaque pair on ajoute le premier element à autre 
         donneur.append(p[i+1])#pour chaque pair on ajoute le deuxième element à donneur
     autre.append(p[len(p)-1])#le dernier element sera ajouté à autre (car on a 51 cartes et 51 est impair et donc le dernier element ne serait pas atteint par la boucle for)
     return (donneur, autre)


def elimine_paires(l):
    '''
     (list of str)->list of str

     Retourne une copie de la liste l avec toutes les paires éliminées 
     et mélange les éléments qui restent.

    '''
    

    resultat=[]
    l.sort()
    flag = False # ce booleen traque si on a detecté une paire
    for i in range(0,len(l)-1):
        if flag:
            flag = False #flag est trouvé true, donc l'element present est parti d'une paire. On le remet à false pour continuer notre itération de la liste
        elif l[i][0] == l[i+1][0]:
            flag = True #flag devient true car on a detecté une paire
        else :
            resultat.append(l[i]) # on ajoute l'element au resultat car il ne fait pas partie d'une paire
    if not flag :
        resultat.append(l[len(l)-1])# si le dernier element ne fait pas partie d'une paire, la boucle for ne pourra pas l'ajouter puisque son index ne l'atteint pas et donc on l'ajoute à resultat ici        
    random.shuffle(resultat)
    return resultat


def affiche_cartes(p):
    '''
    (list)-None
    Affiche les éléments de la liste p séparées par d'espaces
    '''

    for i in p:
        print(i,end=' ')#affiche l'element i de p
    print('')
    
def entrez_position_valide(n):
     '''
     (int)->int
     Retourne un entier lu au clavier, de 1 à n (1 et n inclus).
     Continue à demander si l'usager entre un entier qui n'est pas entre 1 et n
     
     Précondition: n>=1
     '''

     a = int(input("SVP entrer un entier de 1 à "+str(n)+":")) #l'index de l'element choisi +1
     while a > n or a <1 :
         a = int(input("Votre entier n'est pas entre 1 et "+str(n)+".SVP entrer un entier de 1 à "+str(n)+":")) #on continue à demander à l'utilisateur d'entrer un nombre entre 1 et n
     return a
     
     

def joue():
     '''()->None
     Cette fonction joue le jeu'''
    
     p=prepare_paquet()
     melange_paquet(p)
     tmp=donne_cartes(p)
     donneur=tmp[0]
     humain=tmp[1]

     print("Bonjour. Je m'appelle Robot et je distribue les cartes.")
     print("Votre main est:")
     affiche_cartes(humain)
     print("Ne vous inquiétez pas, je ne peux pas voir vos cartes ni leur ordre.")
     print("Maintenant défaussez toutes les paires de votre main. Je vais le faire moi aussi.")
     attend_le_joueur()
     donneur=elimine_paires(donneur)
     humain=elimine_paires(humain)

     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI
     termine = False #booleen indiquant si le jeu est terminé ou pas
     player = 1 #l'indice du joueur
     if len(humain) == 0:
            termine = True #ici c'est le cas où si au debut l'humain n'a que des paires et donc n'aura plus de cartes lorsqu'on elimine les paires, donc termine devient true (ceci n'est pas possible pour le robot car il a initialement un nombre de cartes impaire)
     while not termine:
         if player == 1:
             print("***********************************************************")
             print("Votre tour.")
             print("Votre main est:",end = "\n")
             affiche_cartes(humain) #affiche les cartes de l'humain
             print("J'ai",len(donneur),"cartes. Si 1 est la position de ma première carte et",len(donneur),"est la position de ma dernière carte, laquelle de mes cartes vous voulez?")
             choixHumain = entrez_position_valide(len(donneur)) #l'humain choisit l'index de la carte 
             if choixHumain == 1:
                 print("Vous avez demande ma 1ère carte.")
             else :
                 print("Vous avez demande ma",str(choixHumain)+"ème carte.")
             print("La voila. C'est un",donneur[choixHumain-1])
             print("Avec",donneur[choixHumain-1],"ajouté, votre main est:")
             humain.append(donneur[choixHumain-1]) #ajoute la carte choisi au cartes de l'humain
             affiche_cartes(humain)
             print("Après défaussé toutes les paires et mélanger les cartes, votre main est:")
             humain = elimine_paires(humain) #elimine les paires des cartes de humain 
             affiche_cartes(humain)
             donneur.remove(donneur[choixHumain-1]) #elimine la carte choisie des cartes du robot
             if len(donneur) == 0 or len(humain) == 0:
                 termine = True #devient true si l'un des joueurs n'a plus de cartes
             player = 2 #change le tour
             attend_le_joueur()
         else :
             print("***********************************************************")
             print("Mon tour.")
             choixRobot = random.randint(1,len(humain)) #l'index de la carte choisi aléatoirement par le robot
             if choixRobot == 1:
                 print("J'ai pris votre 1ère carte.")
             else :
                 print("J'ai pris votre",str(choixRobot)+"ème carte.")
             donneur.append(humain[choixRobot-1])#ajoute la carte choisi au cartes du robot
             donneur = elimine_paires(donneur)#elimine les paires des cartes du robot
             humain.remove(humain[choixRobot-1])#elimine la carte choisie des cates de l'humain
             if len(donneur) == 0 or len(humain) == 0:
                 termine = True#devient true si l'un des joueurs n'a plus de cartes
             player = 1 #change le tour
             attend_le_joueur()
     
     print("***********************************************************")
     if len(donneur) == 0 : #le robot n'a plus de cartes
        print("J'ai terminé toutes les cartes.\nVous avez perdu! Moi, Robot, j'ai gagné.")
     else : #l'humain n'a plus de cartes
        print("Vous avez terminé toutes les cartes.\nFelicitations! Vous, Humain, vous avez gagné.")
        
             
         
         
         
         

joue()