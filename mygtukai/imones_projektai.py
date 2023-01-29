from tkinter import *
from tkinter import ttk
from sqlalchemy.orm import sessionmaker
from .pagrindinis import Projektas, Imone, engine

session = sessionmaker(bind=engine)()
query="SELECT distinct(pavadinimas) as pavadinimas FROM imone GROUP BY pavadinimas"

class ProjektaiPagalImone():
    def __init__(self, main):
        self.main = main
        self.main.title("PROJEKTAI PAGAL ĮMONĘ")
        self.langas = Frame(self.main)
        self.tekstas = Frame(self.main)
        self.langas.geometry = ("300x300")
        self.var = StringVar()
        self.my_data=engine.execute(query)
        self.my_list = [r for r, in self.my_data]
        

        self.ivesti_imones_id_l = Label(self.langas, text= "Pasirinkite įmonę")
        self.patvirtinti_imones_id = Button(self.langas, text="Patvirtinti", command=self.parodyti_projektus, border=5, fg="#4E6C50")
        self.parodyti = Text(self.tekstas, width=55, height=15)
        self.parodyti.config(state=DISABLED)
        self.combo_box = ttk.Combobox(self.langas, values=self.my_list, textvariable=self.var)
        self.combo_box.current(0)
        
        self.ivesti_imones_id_l.pack()
        self.combo_box.pack()
        self.patvirtinti_imones_id.pack()
        self.parodyti.pack()
        self.langas.pack()
        self.tekstas.pack()

        self.langas.mainloop()

    def parodyti_projektus(self):
        self.parodyti.config(state=NORMAL)
        self.parodyti.delete("1.0","end")
        i_pavadinimas = self.var.get()
        print(i_pavadinimas)
        for row in session.query(Imone).filter_by(pavadinimas=i_pavadinimas):
            i_pavadinimas = row.id
        projektai = session.query(Projektas).filter_by(imone_id=i_pavadinimas)
        for projektas in projektai:
            print(projektas.id, projektas.pavadinimas, projektas.projekto_pradzia, projektas.trukme_dienomis, projektas.statusas)
            self.parodyti.insert('end',f"Projekto ID: {projektas.id},\n Projekto pavadinimas: {projektas.pavadinimas},\n Projekto pradžia: {projektas.projekto_pradzia},\n Projekto trukmė dienomis: {projektas.trukme_dienomis},\n Projekto statusas: {projektas.statusas}\n")
        self.parodyti.config(state=DISABLED)
       




