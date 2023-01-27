from tkinter import *
from tkinter.font import Font
from sqlalchemy.orm import sessionmaker
from .pagrindinis import Projektas, Komanda, engine

session = sessionmaker(bind=engine)()

class ProjektaiPagalKomanda():
    def __init__(self, main):
        self.main = main
        self.main.title("PROJEKTAI PAGAL KOMANDĄ")
        self.langas = Frame(self.main)
        self.tekstas = Frame(self.main)
        self.langas.geometry = ("400x400")
        self.looks = Font(
            family = 'Helvetica',
            size = 18,
            weight = 'bold',
            slant = 'roman',
            )
    
        self.ivesti_imones_id_l = Label(self.langas, text= "Įveskite komandos ID, kurios projektus norite peržiūrėti")
        self.perziureti_komandas_b = Button(self.langas, text="Peržiūrėti komandas", command=self.perziureti_komandas)
        self.ivesti_komanda_id_e = Entry(self.langas)
        self.patvirtinti_komanda_id = Button(self.langas, text="Patvirtinti", command=self.parodyti_projektus)
        self.parodyti = Text(self.tekstas, width=150, height=25)
        self.parodyti.config(state=DISABLED)
        self.scrol = Scrollbar(self.tekstas)

        self.ivesti_imones_id_l.pack()
        self.perziureti_komandas_b.pack()
        self.ivesti_komanda_id_e.pack()
        self.patvirtinti_komanda_id.pack()
        self.parodyti.pack(side=LEFT)
        self.scrol.pack(side=RIGHT, fill=Y)
        self.langas.pack(side=TOP)
        self.tekstas.pack(side=BOTTOM)

        self.langas.mainloop()

    def perziureti_komandas(self):
        self.parodyti.config(state=NORMAL)
        self.parodyti.delete("1.0","end")
        komandos = session.query(Komanda).all()
        for komanda in komandos:
            print(komanda.id, komanda.komandos_pavadinimas)
            self.parodyti.insert('end',f"Komandos ID: {komanda.id}, Komandos pavadinimas: {komanda.komandos_pavadinimas}\n")
            self.parodyti.config(state=DISABLED)
    
    def parodyti_projektus(self):
        self.parodyti.config(state=NORMAL)
        self.parodyti.delete("1.0","end")
        kazkas = self.ivesti_komanda_id_e.get()
        projektai = session.query(Projektas).filter(Projektas.imone_id==kazkas)
        for projektas in projektai:
            print(projektas.id, projektas.pavadinimas, projektas.projekto_pradzia, projektas.trukme_dienomis, projektas.statusas)
            self.parodyti.insert('end',f"Projekto ID: {projektas.id}, Projekto pavadinimas: {projektas.pavadinimas}, Projekto pradžia: {projektas.projekto_pradzia}, Projekto trukmė dienomis: {projektas.trukme_dienomis}, Projekto statusas: {projektas.statusas}\n")
            self.parodyti.config(state=DISABLED)