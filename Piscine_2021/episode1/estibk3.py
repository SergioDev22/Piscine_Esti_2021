#coding:utf-8

#Exo_15:
liste =[17, 38, 10, 25, 72]
#--triage et affichage--:

liste.sort()
print(liste)

#--renversé la liste et l'affichez--:

liste.renverse()
print(liste)

#--l'indice de l'élément '17'--:

liste.index(17)

#--Enlevement de l'élément '38' et affichage apres enlevement--:

liste.remove(38)
print(liste)

#--Sous-liste de deux au troisieme element--:

liste[1:3]

#--Sous-liste de début au deuxieme element--:

liste[:2]

#--Sous-liste de troisieme element à la dernier--:

liste[2:]

#--Sous-liste complete: 

liste[:]


#Exo_16: 

chaine=str(input("Entrer une texte: "))
print("L'inverse de cette texte est: ",texte[-1:])
chaine_renverse=''.join(reversed(chaine))
print(chaine_renverse)

#Exo_17: 

texte=str(input("Entrer un texte: "))
chaine=''.join(reversed(texte))
if texte==chaine:
	print("C'est un texte palindrome")
else:
	print("C'est pas un texte palindrome")


#Exo_18:

email=input("Saisir votre adresse mail: ")
if ("@" in email) and "." in email[-4:-2]:
	print("Email validé")
else:
	print("Email non validé")


#Exo_19: 

a=[]
b=[0.0]*5
print(a)
print(b)


#Exo_20: 
#--Affichage des entiers de 0 à 3--:

for in in range(0,4):
	print(i)

#--Affichages des entiers de 4 à 7:

for i in range(4,8):
	print(i)

#--Affichage des entiers 2 à 8 par 2pats: 
i=2
while i in range(2,9):
	print(i)
	i+=2	

#--Chose: 
chose=[0,1,2,3,4,5]
chif=int(input("Entrer le chiffre 3 ou 6: "))
if chif in chose:
	print("Cet element appartient dans la litse")
else: 
	print("Cet element n'appartient pas dans la litse")