from tkinter import *
from mygtukai.ivesti_komanda import IvestiKomanda
from mygtukai.ivesti_kompanija import IvestiImone
from mygtukai.ivesti_projekta import IvestiProjekta
from mygtukai.keisti_projekto_stat import KeistiStatusa

class PagrindinisLangas():
    def __init__(self, main):
        self.main = main
        self.pasirinkimas = Label(self.main, width=10, text="PASIRINKITE")
        self.ivesti_komanda_b = Button(self.main, width=10, text="ĮVESTI KOMANDĄ", command=self.paleisti_komanda)
        self.ivesti_imone_b = Button(self.main, width=10, text="ĮVESTI ĮMONĘ", command=self.paleisti_imone)
        self.ivesti_projekta = Button(self.main, width=10, text="ĮVESTI PROJEKTĄ", command=self.paleisti_projekta)
        self.keisti_statusa = Button(self.main, width=10, text="KEISTI PROJEKTO STATUSĄ", command=self.paleisti_keisti_statusa)

        self.pasirinkimas.pack(side=TOP)
        self.ivesti_komanda_b.pack()
        self.ivesti_imone_b.pack()
        self.ivesti_projekta.pack()
        self.keisti_statusa.pack()
    
    def paleisti_komanda(self):
        self.window_ivesti_komanda = Toplevel(self.main)
        self.app = IvestiKomanda(self.window_ivesti_komanda)
    
    def paleisti_imone(self):
        self.window_ivesti_imone = Toplevel(self.main)
        self.app = IvestiImone(self.window_ivesti_imone)
    
    def paleisti_projekta(self):
        self.window_ivesti_projekta = Toplevel(self.main)
        self.app = IvestiProjekta(self.window_ivesti_projekta)
    
    def paleisti_keisti_statusa(self):
        self.window_keisti_statusa = Toplevel(self.main)
        self.app = KeistiStatusa(self.window_keisti_statusa)



