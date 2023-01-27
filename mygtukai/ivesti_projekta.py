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
        self.tekstas = Frame(self.main)
        self.langas.geometry = ("400x400")
        self.var = IntVar()

        self.ivesti_projekto_pavadinima_l = Label(self.langas, text="Projekto pavadinimas")
        self.ivesti_projekto_pavadinima_e = Entry(self.langas)
        self.ivesti_projekto_trukme_l = Label(self.langas, text="Projekto trukmė dienomis")
        self.ivesti_projekto_trukme_e = Entry(self.langas)
        self.ivesti_projekto_status_l = Label(self.langas, text="Projekto statusas")
        self.vykdomas = Radiobutton(self.langas, text="Vykdomas", variable=self.var, value=0)
        self.sustabdytas= Radiobutton(self.langas, text="Sustabdytas", variable=self.var, value=1)
        self.baigtas = Radiobutton(self.langas, text="Baigtas", variable=self.var, value=2)
        self.perziureti_komandas_b = Button(self.langas, text="Peržiūrėti komandas", command=self.perziureti_komanda)
        self.perziureti_imones_b = Button(self.langas, text="Peržiūrėti įmones", command=self.perziureti_imone)
        self.ivesti_komandos_id_l = Label(self.langas, text="Komandos ID")
        self.ivesti_komandos_id_e = Entry(self.langas)
        self.ivesti_imones_id_l = Label(self.langas, text="Įmonės ID")
        self.ivesti_imones_id_e = Entry(self.langas)
        self.patvirtinti_ivesta_projekta = Button(self.langas, text="Ivesti duomenis", command=self.ivesti_projekta)
        self.status_projektas = Label(self.langas, text="Laukiama, kol suvesite duomenis", border=10)
        self.parodyti = Text(self.tekstas, width=150, height=25)
        self.parodyti.config(state=DISABLED)
        self.scrol = Scrollbar(self.tekstas)

        self.ivesti_projekto_pavadinima_l.pack()
        self.ivesti_projekto_pavadinima_e.pack()
        self.ivesti_projekto_status_l.pack()
        self.vykdomas.pack()
        self.sustabdytas.pack()
        self.baigtas.pack()
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
        self.parodyti.pack(side=LEFT)
        self.scrol.pack(side=RIGHT, fill=Y)
        self.langas.pack(side=TOP)
        self.tekstas.pack(side=BOTTOM)

        self.langas.mainloop()
   
    def ivesti_projekta(self):
        komandos_id = self.ivesti_komandos_id_e.get()
        imones_id = self.ivesti_imones_id_e.get()
        if self.var.get() == 0:
            statuselis = "Vykdomas"
        if self.var.get() == 1:
            statuselis = "Sustabdytas"
        if self.var.get() == 2:
            statuselis = "Baigtas"
        projektas_i = Projektas(pavadinimas=self.ivesti_projekto_pavadinima_e.get(), trukme_dienomis=self.ivesti_projekto_trukme_e.get(), statusas=statuselis, komanda_id=komandos_id, imone_id=imones_id)
        session.add(projektas_i)
        session.commit()
        self.status_projektas['text'] = "Sėkmingai sukurtas projektas"

    def perziureti_komanda(self):
        self.parodyti.config(state=NORMAL)
        self.parodyti.delete("1.0","end")
        komandos = session.query(Komanda).all()
        for komanda in komandos:
            print(komanda.id, komanda.komandos_pavadinimas, komanda.asmenu_skaicius, komanda.el_pastas)
            self.parodyti.config(state=NORMAL)
            self.parodyti.insert('end',f"Komandos ID: {komanda.id}, Komandos pavadinimas: {komanda.komandos_pavadinimas}\n")
            self.parodyti.config(state=DISABLED)

    def perziureti_imone(self):
        self.parodyti.config(state=NORMAL)
        self.parodyti.delete("1.0","end")
        imones = session.query(Imone).all()
        for imone in imones:
            print(imone.id, imone.pavadinimas)
            self.parodyti.config(state=NORMAL)
            self.parodyti.insert('end',f"Įmonės ID: {imone.id}, Įmonės pavadinimas: {imone.pavadinimas}\n")
            self.parodyti.config(state=DISABLED)