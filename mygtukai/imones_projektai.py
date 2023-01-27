from tkinter import *
from tkinter.font import Font
from sqlalchemy.orm import sessionmaker
from .pagrindinis import Projektas, Imone, engine

session = sessionmaker(bind=engine)()

class ProjektaiPagalImone():
    def __init__(self, main):
        self.main = main
        self.main.title("PROJEKTAI PAGAL ĮMONĘ")
        self.langas = Frame(self.main)
        self.tekstas = Frame(self.main)
        self.langas.geometry = ("400x400")
        self.looks = Font(
            family = 'Helvetica',
            size = 18,
            weight = 'bold',
            slant = 'roman',
            )

        self.ivesti_imones_id_l = Label(self.langas, text= "Įveskite įmonės ID, kurios projektus norite peržiūrėti")
        self.perziureti_imones_b = Button(self.langas, text="Peržiūrėti įmones", command=self.perziureti_imone)
        self.ivesti_imones_id_e = Entry(self.langas)
        self.patvirtinti_imones_id = Button(self.langas, text="Patvirtinti", command=self.parodyti_projektus)
        self.parodyti = Text(self.tekstas, width=150, height=25)
        self.parodyti.config(state=DISABLED)
        self.scrol = Scrollbar(self.tekstas)

        self.ivesti_imones_id_l.pack()
        self.perziureti_imones_b.pack()
        self.ivesti_imones_id_e.pack()
        self.patvirtinti_imones_id.pack()
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

