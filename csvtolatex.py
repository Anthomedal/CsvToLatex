def NombreDeColonnes(premiere_ligne):
    """
    Entree : premiere_ligne est une chaine de caractère contenant la première ligne du fichier
    Sortie : Le nombre de colonnes du tableur csv
    """

    nombre_de_colonne = 0

    for caractere in premiere_ligne:
        if caractere == "&":
            nombre_de_colonne = nombre_de_colonne+1
    
    return nombre_de_colonne+1

print(
    "Bonjour, bienvenue dans le programme CsvToLatex, veuillez entrer le nomdu fichier dans lequel se trouve le tableau au format csv : "
)

nom_du_fichier_source = input()
fichier_source = open(nom_du_fichier_source, "r")

# On lit les lignes du fichier source
lignes = fichier_source.readlines()

# On relève la dimension du tableau
nombre_de_colonnes = str(NombreDeColonnes(lignes[0]))

# On ouvre le fichier final
fichier_final = open("Resultat.txt", "w")

# On remplit le début du fichier avec le code latex 
fichier_final.write("\\")
fichier_final.write("begin{center}\n")
fichier_final.write("\\")
fichier_final.write("begin{tabular}{|*{")
fichier_final.write(nombre_de_colonnes)
fichier_final.write("}{c|}}\n")
fichier_final.write("\\")
fichier_final.write("hline\n")

# On recopie le contenu du fichier source avec le code latex adapté à chaque fin de ligne
for ligne in lignes:
    for carac in ligne:
        if carac != "\n":
            # On ne recopie pas les sauts de lignes
            fichier_final.write(carac)
    
    # On ajoute le code à la fin de la ligne
    fichier_final.write("\\")
    fichier_final.write("\\")
    fichier_final.write(" \\")
    fichier_final.write("hline")
    fichier_final.write("\n")

# On écrit le code latex de la fin tableau
fichier_final.write("\\")
fichier_final.write("end{tabular}\n")
fichier_final.write("\\")
fichier_final.write("end{center}")

fichier_source.close()
fichier_final.close()

print("Conversion terminee, vous pouver retrouver le code latex correspondant a votre tableau dans le fichier Resultat.txt")