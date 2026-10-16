# lab5_listes.py

# Liste initiale
etudiants = ["Alice", "Bob", "Charlie"]
print(etudiants)  # ['Alice', 'Bob', 'Charlie']

# Ajouter à la fin avec append()
etudiants.append("Diana")
print(etudiants)  # ['Alice', 'Bob', 'Charlie', 'Diana']

# Insérer à une position précise avec insert()
etudiants.insert(1, "Eve")  # index 1, entre Alice et Bob
print(etudiants)  # ['Alice', 'Eve', 'Bob', 'Charlie', 'Diana']

# Supprimer par valeur avec remove() (enlève la première occurrence)
etudiants.remove("Bob")
print(etudiants)  # ['Alice', 'Eve', 'Charlie', 'Diana']

# Retirer et récupérer le dernier élément avec pop()
dernier = etudiants.pop()
print(dernier)     # 'Diana'
print(etudiants)   # ['Alice', 'Eve', 'Charlie']
