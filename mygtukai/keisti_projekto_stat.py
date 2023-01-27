from tkinter import *
from tkinter.font import Font
from sqlalchemy.orm import sessionmaker
from .pagrindinis import Projektas, Imone, engine

session = sessionmaker(bind=engine)()

class KeistiStatusa():
    def __init__(self, main):
        self.main = main
        self.main.title("KEISTI PROJEKTO STATUSĄ")
        self.langas = Frame(self.main)
        self.tekstas = Frame(self.main)
        self.langas.geometry = ("400x400")
        self.var = IntVar()
        self.looks = Font(
            family = 'Helvetica',
            size = 18,
            weight = 'bold',
            slant = 'roman',
            )
        
        self.ivesti_imones_id_l = Label(self.langas, text= "Įveskite įmonės ID, kurios projekto statusą norėsite pakeisti")
        self.perziureti_komandas_b = Button(self.langas, text="Peržiūrėti įmones", command=self.perziureti_imone)
        self.ivesti_imones_id_e = Entry(self.langas)
        self.patvirtinti_imones_id = Button(self.langas, text="Patvirtinti", command=self.parodyti_projektus)
        self.ivesti_projekto_id_l = Label(self.langas, text="Įveskite projekto ID, kurio statusą norite keiste")
        self.ivesti_projekto_id_e = Entry(self.langas)
        self.pakeisti_statusa_l = Label(self.langas, text="Pasirinkite projekto statusą")
        self.vykdomas = Radiobutton(self.langas, text="Vykdomas", variable=self.var, value=0)
        self.sustabdytas= Radiobutton(self.langas, text="Sustabdytas", variable=self.var, value=1)
        self.baigtas = Radiobutton(self.langas, text="Baigtas", variable=self.var, value=2)
        self.patvirtinti_pakeitima = Button(self.langas, text="Keisti statusą", command=self.pakeisti_projekto_statusa)
        self.status = Label(self.langas, text="Laukiama, kol įvesite duomenis")
        self.parodyti = Text(self.tekstas, width=150, height=25)
        self.parodyti.config(state=DISABLED)
        self.scrol = Scrollbar(self.tekstas)

        self.ivesti_imones_id_l.pack()
        self.perziureti_komandas_b.pack()
        self.ivesti_imones_id_e.pack()
        self.patvirtinti_imones_id.pack()
        self.ivesti_projekto_id_l.pack()
        self.ivesti_projekto_id_e.pack()
        self.pakeisti_statusa_l.pack()
        self.vykdomas.pack()
        self.sustabdytas.pack()
        self.baigtas.pack()
        self.patvirtinti_pakeitima.pack()
        self.status.pack()
        self.parodyti.pack(side=LEFT)
        self.scrol.pack(side=RIGHT, fill=Y)
        self.langas.pack(side=TOP)
        self.tekstas.pack(side=BOTTOM)

        self.langas.mainloop()

    def parodyti_projektus(self):
        self.parodyti.config(state=NORMAL)
        self.parodyti.delete("1.0","end")
        kazkas = self.ivesti_imones_id_e.get()
        projektai = session.query(Projektas).filter(Projektas.imone_id==kazkas)
        for projektas in projektai:
            print(projektas.id, projektas.pavadinimas, projektas.projekto_pradzia, projektas.trukme_dienomis, projektas.statusas)
            self.parodyti.insert('end',f"Projekto ID: {projektas.id}, Projekto pavadinimas: {projektas.pavadinimas}, Projekto pradžia: {projektas.projekto_pradzia}, Projekto trukmė dienomis: {projektas.trukme_dienomis}, Projekto statusas: {projektas.statusas}\n")
            self.parodyti.config(state=DISABLED)

    def perziureti_imone(self):
        self.parodyti.config(state=NORMAL)
        self.parodyti.delete("1.0","end")
        imones = session.query(Imone).all()
        for imone in imones:
            print(imone.id, imone.pavadinimas)
            self.parodyti.insert('end',f"Įmonės ID: {imone.id}, Įmonės pavadinimas: {imone.pavadinimas}\n")
            self.parodyti.config(state=DISABLED)

    def pakeisti_projekto_statusa(self):
        projekto_id = self.ivesti_projekto_id_e .get()
        projektai = session.query(Projektas).get(projekto_id)
        if self.var.get() == 0:
            projektai.statusas = "Vykdomas"
        if self.var.get() == 1:
            projektai.statusas = "Sustabdytas"
        if self.var.get() ==2:
            projektai.statusas = "Baigtas"
        session.commit()
        print(f'statusas pakeistas i {projektai.statusas}')
        self.status['text'] = "Statusas sėkmingai pakeistas"



