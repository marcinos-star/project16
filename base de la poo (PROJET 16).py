# ____DEBUT D'APPRENTISSAGE POO____

class Utilisateur:
    def __init__(self, nom, passion, activites, age, niveau_d_etude):
        self.nom = nom
        self.passion = passion
        self.activites = activites
        self.age = age
        self.niveau_detude = niveau_d_etude
        self.domaines = []

    def afficher_profil(self):
        print(f"Nom : {self.nom}")
        print(f"Age : {self.age}")
        print(f"Passion : {self.passion}")
        print(f"Niveau d'étude : {self.niveau_detude}")
        print(f"Domaines : {self.domaines}")

    def ajouter_domaine(self, domaine):
        self.domaines.append(domaine)
        print(f"Domaine '{domaine}' ajouté avec succès.")
    
class Domaine:
    def __init__(self, nom):
        self.nom = nom
        self.resultats = []

    def ajouter_resultat(self, valeur):
        self.resultats.append(valeur)
        print(f"Résultat '{valeur}' ajouté au domaine {self.nom}.")

    def afficher_resultats(self):
        print(f"\n--- {self.nom} ---")
        if self.resultats:
            for r in self.resultats:
                print(f"  {r}")
        else:
            print("  Aucun résultat enregistré.")
nom = input("Ton nom : ")
passion = input("Ta passion : ")
activites = input("Tes activités : ")
age = int(input("Ton âge : "))
niveau = input("Ton niveau d'étude : ")

marc = Utilisateur(nom, passion, activites, age, niveau)

continuer = True
while continuer:
    domaine = input("Ajouter un domaine (ou 'stop' pour terminer) : ")
    if domaine == "stop":
        continuer = False
    else:
        marc.ajouter_domaine(domaine)

marc.afficher_profil()