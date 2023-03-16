class karaoke:
    def __init__(self):
        self.__musiques = ["never gonna give you up", "despacito", "vapo vapo", "God bless"]

class Player:
    def __init__(self,name):
        self.__nom = name
        self.__score = []


    def getNom(self):
        return self.__nom
    def getScore(self):
        return self.__score
    def afficheNom(self):
        print(self.__nom)
    def ajouteScore(self, scoreObtenu):                     #ajouter des scores
        scoreObtenu = 0
        
        while(scoreObtenu > 50):
            scoreObtenu = input("quel score avez vous obtenu?")
            if(scoreObtenu > 50):
                print("Le score minimum est de 50")
        self.__score.append(scoreObtenu)
    def moyenneScore(self, moyenne):            #calculer la moyenne de tout les scores 
        for i in range(5):
            moyenne += self.__score[i]
        moyenne / 5
    def meilleurScore(self, mScore):           #print le meilleur score 
        mScore = max(self.__score)
        print(mScore)
    def pireScore(self,pScore):                     #print le pire score
        pScore = min(self.__score)
        print(pScore)
    def musiques(self,musique, scoreMusique):               
        for i in range(5):
            musique = i
            scoreMusique.ajouteScore 
            

    


pseudo1 = input("pseudo premier joueur ")
Joueur1 = Player(pseudo1)
pseudo2 = input("pseudo deuxieme joueur ")

Joueur2 = Player(pseudo2)

Joueur1.ajouteScore