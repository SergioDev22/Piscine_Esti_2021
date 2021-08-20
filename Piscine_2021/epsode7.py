
from tkinter import*
# définir la fenêtre:

laFenetre = Tk()
laFenetre.geometry("200x200")
laFenetre.resizable(height=False , width= False)
laFenetre.config(bg='#D3D3D3')

#definir le titre:
titre="CLEAN STRING"
laFenetre.title(titre)

#definir le mot "SOURCE":
mot_source= Label (laFenetre, text = "Source:", bg='#D3D3D3')
mot_source.grid(row=1)
mot_source.pack()


#definir le champ d'ecriture:
frame= Frame(laFenetre, bg='#FFFFFF')
texte=Label(frame, text="\\b\\t80cm\\t60cm\\n")
frame.pack()
texte.pack()


#creation de bouton clean: 
boutton= Button(text="CLEAR" , bg='#008000' , fg='#000000')
boutton.grid(row=3)
boutton.pack()


#destination: 
mot_destination= Label (laFenetre, text = "Destination", bg='#D3D3D3')
mot_destination.grid(row=4)
mot_destination.pack()


#les deux champs côte à côte: 
frame1= Frame(laFenetre, bg='#FFFFFF')
frame1.grid(row=5)
texte1=Label(frame1, text="80cm")
frame1.pack(side=LEFT, ipadx=20, padx=12)
texte1.pack()



frame2= Frame(laFenetre, bg='#FFFFFF')
frame2.grid(row=5)
texte2=Label(frame2, text="60cm")
frame2.pack(side=RIGHT, ipadx=20, padx=12)
texte2.pack()



laFenetre.mainloop( )
