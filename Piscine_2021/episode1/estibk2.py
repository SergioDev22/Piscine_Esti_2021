#coding:utf-8

#-------DEUXIEME BREAKPOINT---------

#Exo_6: 

email=input("Entrer votre adresse mail: ")
if "@" in email and '.com' in email[-4:]:
		print("Email validé")
else:
	print("Email non validé")


#Exo_7: 

for i in range(10):
	print("Bonjour madame")


#8)Exo_8: 

for i in lettre:
	print(i)


#Exo_9: 

a=0
b=10
a=int(input("Entrer le nombre a: "))
print("\n\n")
while a<b:
	a+=1
	print("La valeur de a incrementée est: ",a)


#Exo_10 decrementation: 

b=int(input("Entrer un nombre: "))
if b%2==1:
	while b!=0:
		b-=1
		print("La valeur decrementatée de b est: ",b)
else:
	print("Valeur incorrecte")


#Exo_11: 

nombre=int(input("Entrer un entier entre 1 à 10: "))
if 1<=nombre<=10:
	print("Bravo, vous avez bien saisit.\nEt le nombre que vous saisissez est:",nombre)
else:
	print("Valeur incorrecte")


#Exo_12:  

chaine=str(input("Entrer un texte: "))
for i in chaine:
	print(i)

#listes: 
liste=["lahatra","sergio","dama"]
for i in liste:
	print(i)

#Exo_13: 
for i in range(0, 14, 3):
	print(f"{i} {i+1} {i+2}")


#Exo_14: 

#pour le boucle while: 
nombre=int(input("Entrer un nombre: "))
i=0
while i<(nombre*2):
	if i%2==0:
		print(i)
		i+=2


#le boucle for:
nombre=int(input("Entrer un nombre: "))
i=0
for i in range(nombre*2):
	if i%2==0:
		print(i)
		