from tkinter import *
from tkinter.font import Font
from sqlalchemy.orm import sessionmaker
from .pagrindinis import Projektas, Komanda, Imone, engine

session = sessionmaker(bind=engine)()

class KeistiStatusa():
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
        
        self.keisim_statusa = Label(self.langas, text= "PAKEISKITE PROJEKTO STATUSĄ", font=self.looks)
        self.ivesti_imones_id_l = Label(self.langas, text= "Įveskite įmonės ID, kurios projekto statusą norėsite pakeisti")
        self.perziureti_komandas_b = Button(self.langas, text="Peržiūrėti įmones", command=self.perziureti_imone)
        self.ivesti_imones_id_e = Entry(self.langas)
        self.patvirtinti_imones_id = Button(self.langas, text="Patvirtinti", command=self.parodyti_projektus)
        self.ivesti_projekto_id_l = Label(self.langas, text="Įveskite projekto ID, kurio statusą norite keiste")
        self.ivesti_projekto_id_e = Entry(self.langas)
        self.pakeisti_statusa_l = Label(self.langas, text="Įveskite, į ką keičiate (Vykdomas/Sustabdytas/Baigtas")
        self.pakeisti_statusa_e = Entry(self.langas)
        self.patvirtinti_pakeitima = Button(self.langas, text="Keisti statusą", command=self.pakeisti_projekto_statusa)
        self.status = Label(self.langas, text="Laukiama, kol įvesite duomenis")
        self.parodyti = Text(self.langas, width=150, height=25)

        self.keisim_statusa.pack()
        self.ivesti_imones_id_l.pack()
        self.perziureti_komandas_b.pack()
        self.ivesti_imones_id_e.pack()
        self.patvirtinti_imones_id.pack()
        self.ivesti_projekto_id_l.pack()
        self.ivesti_projekto_id_e.pack()
        self.pakeisti_statusa_l.pack()
        self.pakeisti_statusa_e.pack()
        self.patvirtinti_pakeitima.pack()
        self.status.pack()
        self.parodyti.pack()
        self.langas.pack()

        self.langas.mainloop()

    def parodyti_projektus(self):
        self.parodyti.delete("1.0","end")
        kazkas = self.ivesti_imones_id_e.get()
        projektai = session.query(Projektas).filter(Projektas.imone_id==kazkas)
        for projektas in projektai:
            print(projektas.id, projektas.pavadinimas, projektas.projekto_pradzia, projektas.trukme_menesiais)
            self.parodyti.insert('end',f"Projekto ID: {projektas.id}, Projekto pavadinimas: {projektas.pavadinimas}, Projekto pradžia: {projektas.projekto_pradzia}, Projekto trukmė mėnesiais: {projektas.trukme_menesiais}\n")
    
    def perziureti_imone(self):
        self.parodyti.delete("1.0","end")
        imones = session.query(Imone).all()
        for imone in imones:
            print(imone.id, imone.pavadinimas)
            self.parodyti.insert('end',f"Įmonės ID: {imone.id}, Įmonės pavadinimas: {imone.pavadinimas},\n")

    def pakeisti_projekto_statusa(self):
        projekto_id = self.ivesti_projekto_id_e .get()
        projektai = session.query(Projektas).get(projekto_id)
        pakeisti = self.pakeisti_statusa_e.get()
        projektai.statusas = pakeisti
        session.commit()
        print(f'statusas pakeistas i {projektai.statusas}')
        self.status['text'] = "Statusas sėkmingai pakeistas"



