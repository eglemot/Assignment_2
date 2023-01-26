from tkinter import *
from tkinter.font import Font
from sqlalchemy.orm import sessionmaker
from .pagrindinis import Projektas, Komanda, Imone, engine

session = sessionmaker(bind=engine)()

class IvestiProjekta():

    def __init__(self, main):
        self.main = main
        self.main.title("ĮVESTI PROJEKTĄ")
        self.langas = Frame(self.main)
        self.langas.geometry = ("400x400")
        self.looks = Font(
            family = 'Helvetica',
            size = 18,
            weight = 'bold',
            slant = 'roman',
            )

        self.ivesti_projekta_l = Label(self.langas, text= "ĮVESKITE PROJEKTĄ", font=self.looks)
        self.ivesti_projekto_pavadinima_l = Label(self.langas, text="Projekto pavadinimas")
        self.ivesti_projekto_pavadinima_e = Entry(self.langas)
        self.ivesti_projekto_trukme_l = Label(self.langas, text="Projekto trukmė mėnesiais")
        self.ivesti_projekto_trukme_e = Entry(self.langas)
        self.ivesti_projekto_status_l = Label(self.langas, text="Projekto statusas(Vykdomas/Sustabdytas/Baigtas)")
        self.ivesti_projekto_status_e = Entry(self.langas)
        self.perziureti_komandas_b = Button(self.langas, text="Peržiūrėti komandas", command=self.perziureti_komanda)
        self.perziureti_imones_b = Button(self.langas, text="Peržiūrėti įmones", command=self.perziureti_imone)
        self.parodyti = Text(self.langas, width=150, height=25)
        self.ivesti_komandos_id_l = Label(self.langas, text="Komandos ID")
        self.ivesti_komandos_id_e = Entry(self.langas)
        self.ivesti_imones_id_l = Label(self.langas, text="Įmonės ID")
        self.ivesti_imones_id_e = Entry(self.langas)
        self.patvirtinti_ivesta_projekta = Button(self.langas, text="Ivesti duomenis", command=self.ivesti_projekta)
        self.status_projektas = Label(self.langas, text="Laukiama, kol suvesite duomenis", border=10)

        self.ivesti_projekta_l.pack()
        self.ivesti_projekto_pavadinima_l.pack()
        self.ivesti_projekto_pavadinima_e.pack()
        self.ivesti_projekto_status_l.pack()
        self.ivesti_projekto_status_e.pack()
        self.ivesti_projekto_trukme_l.pack()
        self.ivesti_projekto_trukme_e.pack()
        self.ivesti_komandos_id_l.pack()
        self.perziureti_komandas_b.pack()
        self.ivesti_komandos_id_e.pack()
        self.ivesti_imones_id_l.pack()
        self.perziureti_imones_b.pack()
        self.ivesti_imones_id_e.pack()
        self.patvirtinti_ivesta_projekta.pack()
        self.status_projektas.pack()
        self.parodyti.pack()
        self.parodyti.pack()
        self.langas.pack()

        self.langas.mainloop()
   
    def ivesti_projekta(self):
        komandos_id = self.ivesti_komandos_id_e.get()
        imones_id = self.ivesti_imones_id_e.get()
        projektas_i = Projektas(pavadinimas=self.ivesti_projekto_pavadinima_e.get(), trukme_menesiais=self.ivesti_projekto_trukme_e.get(), statusas= self.ivesti_projekto_status_e.get(), komanda_id=komandos_id, imone_id=imones_id)
        session.add(projektas_i)
        session.commit()
        self.status_projektas['text'] = "Sėkmingai sukurtas projektas"

    def perziureti_komanda(self):
        self.parodyti.delete("1.0","end")
        komandos = session.query(Komanda).all()
        for komanda in komandos:
            print(komanda.id, komanda.komandos_pavadinimas, komanda.asmenu_skaicius, komanda.el_pastas)
            self.parodyti.insert('end',f"Komandos ID: {komanda.id}, Komandos pavadinimas: {komanda.komandos_pavadinimas},\n")

    def perziureti_imone(self):
        self.parodyti.delete("1.0","end")
        imones = session.query(Imone).all()
        for imone in imones:
            print(imone.id, imone.pavadinimas)
            self.parodyti.insert('end',f"Įmonės ID: {imone.id}, Įmonės pavadinimas: {imone.pavadinimas},\n")