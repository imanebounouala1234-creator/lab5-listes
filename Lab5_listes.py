# lab5_listes.py
import copy
from pprint import pprint

# ========== Étape 1 : Créer et modifier une liste ==========
print("=== Étape 1 ===")
etudiants = ["Alice", "Bob", "Charlie"]
print(etudiants)  # ['Alice', 'Bob', 'Charlie']

etudiants.append("Diana")
print(etudiants)  # ['Alice', 'Bob', 'Charlie', 'Diana']

etudiants.insert(1, "Eve")  # index 1, entre Alice et Bob
print(etudiants)  # ['Alice', 'Eve', 'Bob', 'Charlie', 'Diana']

etudiants.remove("Bob")
print(etudiants)  # ['Alice', 'Eve', 'Charlie', 'Diana']

dernier = etudiants.pop()
print(dernier)     # 'Diana'
print(etudiants)   # ['Alice', 'Eve', 'Charlie']

# ========== Étape 2 : Accéder aux éléments par index ==========
print("\n=== Étape 2 ===")
print(etudiants[0])    # 'Alice'
print(etudiants[2])    # 'Charlie'
print(etudiants[-1])   # 'Charlie'
print(etudiants[-2])   # 'Eve'
print(len(etudiants))  # 3

# ========== Étape 3 : Slicing ==========
print("\n=== Étape 3 ===")
notes = [12, 15, 9, 18, 14, 16]
print(notes[1:4])   # [15, 9, 18]
print(notes[:3])    # [12, 15, 9]
print(notes[3:])    # [18, 14, 16]
print(notes[::2])   # [12, 9, 14]
print(notes[::-1])  # [16, 14, 18, 9, 15, 12]

# ========== Étape 4 : Liste de listes ==========
print("\n=== Étape 4 ===")
classe = [
    ["Alice", 20, 15.5],
    ["Eve", 19, 14.0],
    ["Charlie", 21, 16.5]
]

classe.append(["Diana", 22, 13.0])
print(classe)

for index, (nom, age, note) in enumerate(classe, start=1):
    print(f"Étudiant {index} : {nom} ({age} ans) - note {note}")

age_charlie = classe[2][1]
print(age_charlie)  # 21

classe[2][2] = 17.0  # met à jour la note de Charlie
print(classe[2])

for etudiant in classe:
    print(etudiant[0], etudiant[2])

# ========== Étape 6 : Exercices complémentaires ==========
print("\n=== Étape 6 ===")

# 1. Tri et statistiques
classe_triee = sorted(classe, key=lambda ligne: ligne[2], reverse=True)
print("Tri décroissant par note :", classe_triee)

total = 0
for ligne in classe:
    total += ligne[2]
print("Moyenne :", total / len(classe))

# 2. Recherche
nom_cherche = "Alice"  # tu peux utiliser input("Nom : ") à la place
trouve = next((l for l in classe if l[0] == nom_cherche), None)
print("Résultat :", trouve if trouve else "Introuvable")

# 3. Copie superficielle vs profonde
classe_copie = classe[:]
classe_copie[0][1] = 99
print("Original après copie superficielle :", classe[0])  # changé aussi !
classe[0][1] = 20  # on remet la valeur

classe_profonde = copy.deepcopy(classe)
classe_profonde[0][1] = 99
print("Original après deepcopy :", classe[0])  # inchangé

# 4. Conversion en dictionnaires
classe_dict = [{"nom": n, "age": a, "note": no} for n, a, no in classe]
print(classe_dict[0]["nom"])

# ========== Étape 7 : Astuces supplémentaires ==========
print("\n=== Étape 7 ===")
liste_a = [1, 2]
liste_a.extend([3, 4])
print(liste_a)  # [1, 2, 3, 4]

bonnes_notes = [note for _, _, note in classe if note >= 15]
print(bonnes_notes)

pprint(classe)

# ========== Mini-projet : Gestion simplifiée d'une classe ==========
classe = [
    ["Alice", 20, 15.5],
    ["Bob", 19, 12.0],
    ["Charlie", 22, 16.0]
]


def afficher_classe(classe):
    if not classe:
        print("La classe est vide.")
        return
    for index, (nom, age, note) in enumerate(classe, start=1):
        print(f"{index}. {nom} - {age} ans - note {note}")


def ajouter_etudiant(classe):
    nom = input("Nom : ").strip()
    try:
        age = int(input("Âge : "))
        note = float(input("Note : "))
    except ValueError:
        print("Saisie invalide.")
        return
    classe.append([nom, age, note])
    print(f"{nom} ajouté.")


def supprimer_etudiant(classe):
    if not classe:
        print("Rien à supprimer.")
        return
    try:
        index = int(input("Numéro de l'étudiant à supprimer : ")) - 1
        etudiant = classe.pop(index)
        print(f"{etudiant[0]} supprimé.")
    except (ValueError, IndexError):
        print("Index invalide.")


def mettre_a_jour_etudiant(classe):
    if not classe:
        print("Classe vide.")
        return
    try:
        index = int(input("Numéro de l'étudiant à modifier : ")) - 1
        etudiant = classe[index]
    except (ValueError, IndexError):
        print("Index invalide.")
        return

    print(f"Modification de {etudiant[0]} (laisser vide pour ne pas changer).")
    nouveau_nom = input("Nouveau nom : ").strip()
    if nouveau_nom:
        etudiant[0] = nouveau_nom

    entree_age = input("Nouvel âge : ").strip()
    if entree_age:
        try:
            etudiant[1] = int(entree_age)
        except ValueError:
            print("Âge ignoré (saisie invalide).")

    entree_note = input("Nouvelle note : ").strip()
    if entree_note:
        try:
            etudiant[2] = float(entree_note)
        except ValueError:
            print("Note ignorée (saisie invalide).")


def afficher_statistiques(classe):
    if not classe:
        print("Pas de données.")
        return
    notes = [etudiant[2] for etudiant in classe]
    moyenne = sum(notes) / len(notes)
    meilleure = max(classe, key=lambda e: e[2])
    pire = min(classe, key=lambda e: e[2])
    print(f"Moyenne des notes : {moyenne:.2f}")
    print(f"Meilleure note : {meilleure[2]} ({meilleure[0]})")
    print(f"Moins bonne note : {pire[2]} ({pire[0]})")


while True:
    print("\nGestion de la classe")
    print("1. Afficher tous les étudiants")
    print("2. Ajouter un étudiant")
    print("3. Supprimer un étudiant")
    print("4. Modifier un étudiant")
    print("5. Statistiques")
    print("q. Quitter")

    choix = input("Choix : ").strip().lower()

    if choix == "1":
        afficher_classe(classe)
    elif choix == "2":
        ajouter_etudiant(classe)
    elif choix == "3":
        supprimer_etudiant(classe)
    elif choix == "4":
        mettre_a_jour_etudiant(classe)
    elif choix == "5":
        afficher_statistiques(classe)
    elif choix == "q":
        print("Au revoir.")
        break
    else:
        print("Option inconnue.")
