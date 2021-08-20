#coding:utf-8

#----------PREMIER BREAKPOINT-------------:


#Exo_1: 
temps=6.892 
distance=19.7
vitesse=distance/temps
print("la valeur de la vitesse est:{:.2f} m/s".format(vitesse))

#Exo_2:
nom=input("Saisir votre nom: ")
age=input("Saisir votre age: ")
print("Votre nom est {}\nVotre age est: {}".format(nom,age))

#pour le bon type: 
nom=input("Saisir votre nom: ") #ou nom=str(input("Saisir votre nom: "))
nom=str(nom)
age=input("Saisir votre age: ") #ou age=int(input("Saisir votre age: "))
age=int(age)
print("Votre nom est {}\nVotre age est: {}".format(nom,age


#Exo_3
from math import*
a=float(input("Entrer un nombre: "))
if a>=0.0:
	print("la racine de carée de ce nombre est: ",sqrt(a))
else:
	print("Valeur incorrecte")


#Exo_4
mot1=str(input("Entrer un mot: "))
mot2=str(input("Entrer un mot encore: "))

if len(mot1)>len(mot2):
	print("le mot:'{}' est plus long que le mot '{}'".format(mot1,mot2))
elif len(mot1)<len(mot2):
	print("le mot:'{}' est plus long que le mot '{}'".format(mot2,mot1))
else:
	print("les deux sont égaux")


#Exo_5: 
pSeuil = 2.3
vSeuil = 7.41
vCourant=float(input("Saisir le volume courant de l'enceinte: "))
pCourant=float(input("Saisir la pression courant de l'enceinte: "))

if vCourant>vSeuil and pCourant>pSeuil:
	print("---Arrêt immédiat---")
elif pCourant>pSeuil:
	print("Merci d'augmenter la volume de l'enceinte")
elif vCourant>vSeuil:
	print("Merci de diminuer le volume de l'enceinte")
else: 
	print("---TOUT VA BIEN---")
