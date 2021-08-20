#coding:utf-8: 
fichier=open("fichier.txt","r")
ligne=fichier.readlines()
i=0
dico={}
for mot in ligne:
	b=list(mot.split()) 
	dico[int(b[i+1])]=str(b[i])
for kle, valeur in sorted(dico.items(), key=lambda x: x[0]):
	print("%s: %s" % (kle, valeur))
