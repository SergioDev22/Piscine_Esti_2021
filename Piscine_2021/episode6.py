import os
path="C:\\Users\\SERGIO-PC\\Desktop\\Piscine_2021"
nom_fichier=input("Saisissez le nom de fichier: ")
if nom_fichier in os.listdir(path):
	fichier=open(nom_fichier,"r")
	ligne=fichier.readlines()
	for valeur in ligne:
		print(valeur)
		if valeur[2:5]<valeur[8:10]:
			print("OUI")
		else:
			print("NON")
else:
	print("le fichier n'existe pas")


