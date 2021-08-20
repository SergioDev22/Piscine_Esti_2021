#coding:utf-8

#Exo_21:

x=int(input("Saisir un nombre: ")) 
for i in range(x): 
	chaine=input("\nSaisissez une texte: ")
	fichier=open("data.txt","a+")
	fichier.write("{}\n".format(chaine))
	fichier.close()

#Exo_22:

fichier=open("data.txt","r")
ligne = fichier.readlines()
for i in ligne:
    email=i.strip("\n")
    print(email)
    if("@" in email) and ".com" in email[-4:]:
        print("Ceci est un mail.\n")
    else:
        print("Ceci n'est pas un mail.\n")

#Exo_23:

deco={}
def compterMots(chaine):
	chaine1=chaine.split()
	a=0
	for mot in chaine1:
		n=chaine1.count(mot)
		l=len(chaine1)
		f=n/l #frequence=nombre des mots presents dans la chaine divisé par le nombre des mots total de la chaine
		deco[a]= {mot:round(f,2)}
		a+=1
	return deco
b=str(input("Entrer: "))

print(compterMots(b))

#Exo_24:

from math import*
def  volumeSphere(r): 
	volume=(4/3)*pi*pow(r,3)
	return volume

calcul=volumeSphere(2)
print("le volume de ce sphere est:{:.2f}".format(calcul))


#Exo_25:

def somme(a,b,c):
	return a+b+c
mon_tuple=(1,2,3)
calcul=somme(mon_tuple[0],mon_tuple[1],mon_tuple[2])
print("la somme des élément de la tuple est:",calcul)