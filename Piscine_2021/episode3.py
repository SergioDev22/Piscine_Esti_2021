#coding:utf-8
def conversion(chaine):
	AryAry=0
	Euros=0
	if "EA" in chaine[:2]:
		AryAry=4593.97*10 #pour la valeur de 10€
		print("10Euros est {:.2f} en Ariary Malagasy".format(AryAry))
	elif "AE" in chaine[:2]:
		Euros=12000/4593.97 #pour la valeur de 12000 Ariary
		print("12000Ariary Malagasy est {:.2f} en Euros".format(Euros))
	else:
		print("Valeur invalide")
caractere=input("Saisir 'EA 8' ou 'AE 4000': ")
conversion(caractere)
