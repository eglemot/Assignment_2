from tkinter import *
from tkinter.font import Font
from mygtukai.ivesti_komanda import IvestiKomanda
from mygtukai.ivesti_kompanija import IvestiImone
from mygtukai.ivesti_projekta import IvestiProjekta
from mygtukai.imones_projektai import ProjektaiPagalImone
from mygtukai.komandu_projektai import ProjektaiPagalKomanda
from mygtukai.keisti_projekto_stat import KeistiStatusa

class PagrindinisLangas():
    def __init__(self, main):
        self.main = main
        self.looks = Font(
            family = 'Helvetica',
            size = 18,
            weight = 'bold',
            slant = 'roman',
            )
        self.pasirinkimas = Label(self.main, width=20, border=5, font=self.looks, text="PASIRINKITE")
        self.ivesti_komanda_b = Button(self.main, width=20, border=5, text="ĮVESTI KOMANDĄ", command=self.paleisti_komanda)
        self.ivesti_imone_b = Button(self.main, width=20,border=5, text="ĮVESTI ĮMONĘ", command=self.paleisti_imone)
        self.ivesti_projekta = Button(self.main, width=20, border=5, text="ĮVESTI PROJEKTĄ", command=self.paleisti_projekta)
        self.ieskoti_pagal_imone = Button(self.main, width=20, border=5, text="PROJEKTAI PAGAL ĮMONĘ", command=self.paleisti_pagal_imone)
        self.ieksoti_pagal_komanda = Button(self.main, width=20, border=5, text="PROJEKTAI PAGAL KOMANDĄ", command=self.paleisti_pagal_komanda)
        self.keisti_statusa= Button(self.main, width=20, border=5, text="KEISTI PROJEKTO STATUSĄ", command=self.paleisti_keisti_statusa)

        self.pasirinkimas.pack(side=TOP)
        self.ivesti_komanda_b.pack()
        self.ivesti_imone_b.pack()
        self.ivesti_projekta.pack()
        self.keisti_statusa.pack()
        self.ieskoti_pagal_imone.pack()
        self.ieksoti_pagal_komanda.pack()
    
    def paleisti_komanda(self):
        self.window_ivesti_komanda = Toplevel(self.main)
        self.app = IvestiKomanda(self.window_ivesti_komanda)
    
    def paleisti_imone(self):
        self.window_ivesti_imone = Toplevel(self.main)
        self.app = IvestiImone(self.window_ivesti_imone)
    
    def paleisti_projekta(self):
        self.window_ivesti_projekta = Toplevel(self.main)
        self.app = IvestiProjekta(self.window_ivesti_projekta)
    
    def paleisti_pagal_imone(self):
        self.window_pagal_imone = Toplevel(self.main)
        self.app = ProjektaiPagalImone(self.window_pagal_imone)
    
    def paleisti_pagal_komanda(self):
        self.window_pagal_komanda = Toplevel(self.main)
        self.app = ProjektaiPagalKomanda(self.window_pagal_komanda)

    def paleisti_keisti_statusa(self):
        self.window_keisti_statusa = Toplevel(self.main)
        self.app = KeistiStatusa(self.window_keisti_statusa)



