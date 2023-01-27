from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from sqlalchemy.orm import sessionmaker
from .pagrindinis import Projektas, Komanda, engine

session = sessionmaker(bind=engine)()
query="SELECT distinct(komandos_pavadinimas) as pavadinimas FROM komanda"

class ProjektaiPagalKomanda():
    def __init__(self, main):
        self.main = main
        self.main.title("PROJEKTAI PAGAL KOMANDĄ")
        self.langas = Frame(self.main)
        self.tekstas = Frame(self.main)
        self.langas.geometry = ("400x400")
        self.var = StringVar()
        self.my_data=engine.execute(query)
        self.my_list = [r for r, in self.my_data]
    
        self.ivesti_imones_id_l = Label(self.langas, text= "Pasirinkite komandą")
        self.patvirtinti_komanda_id = Button(self.langas, text="Patvirtinti", command=self.parodyti_projektus)
        self.parodyti = Text(self.tekstas, width=150, height=25)
        self.parodyti.config(state=DISABLED)
        self.scrol = Scrollbar(self.tekstas)
        self.combo_box = ttk.Combobox(self.langas, values=self.my_list, textvariable=self.var)
        self.combo_box.set('Search')

        self.ivesti_imones_id_l.pack()
        self.combo_box.pack()
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
        kazkas = self.var.get()
        print(kazkas)
        for row in session.query(Komanda).filter_by(komandos_pavadinimas=kazkas):
            kazkas = row.id
        projektai = session.query(Projektas).filter_by(komanda_id=kazkas)
        for projektas in projektai:
            print(projektas.id, projektas.pavadinimas, projektas.projekto_pradzia, projektas.trukme_dienomis, projektas.statusas)
            self.parodyti.insert('end',f"Projekto ID: {projektas.id}, Projekto pavadinimas: {projektas.pavadinimas}, Projekto pradžia: {projektas.projekto_pradzia}, Projekto trukmė dienomis: {projektas.trukme_dienomis}, Projekto statusas: {projektas.statusas}\n")
            self.parodyti.config(state=DISABLED)
    