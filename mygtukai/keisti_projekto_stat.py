from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from sqlalchemy.orm import sessionmaker
from .pagrindinis import Projektas, engine

session = sessionmaker(bind=engine)()
query="SELECT distinct(pavadinimas) FROM projektas GROUP BY pavadinimas"

class KeistiStatusa():
    def __init__(self, main):
        self.main = main
        self.main.title("KEISTI PROJEKTO STATUSĄ")
        self.langas = self.main
        self.langas.geometry = ("500x500")
        self.var_statusui = IntVar()
        self.var_projektui = StringVar()
        self.my_data_pavadiniams=engine.execute(query)
        self.my_list_pavadinimas = [r for r, in self.my_data_pavadiniams]
        self.looks1 = Font(
            family = 'Helvetica',
            size = 14,
            weight = 'normal',
            slant = "italic",
            underline = 1,
            )
        
        self.pakeisti_statusa_l = Label(self.langas, text="Pasirinkite projektą", border=5)
        self.combo_box = ttk.Combobox(self.langas, values=self.my_list_pavadinimas, textvariable=self.var_projektui)
        self.combo_box.current(0)
        self.patvirtinti_pasirinkima = Button(self.langas, text="PARODYTI STATUSĄ", command=self.parodyti_statusa, border=5, fg="#4E6C50")
        self.parodyti_statusa_pasirinkto = Label(self.langas, text="Laukiama, kol pasirinksite projektą", border=5, font=self.looks1, fg="#F8485E")
        self.pasirinkite_statusa = Label(self.langas, text="Pasirinkite dabartinį statusą", border=5)
        self.vykdomas = Radiobutton(self.langas, text="Vykdomas", variable=self.var_statusui, value=0)
        self.sustabdytas= Radiobutton(self.langas, text="Sustabdytas", variable=self.var_statusui, value=1)
        self.baigtas = Radiobutton(self.langas, text="Baigtas", variable=self.var_statusui, value=2)
        self.patvirtinti_pakeitima = Button(self.langas, text="KEISTI STATUSĄ", command=self.pakeisti_statusa, border=5, fg="#4E6C50")
        self.status = Label(self.langas, text="Laukiama, kol įvesite duomenis", border=5, font=self.looks1, fg="#F8485E")

        self.pakeisti_statusa_l.pack()
        self.combo_box.pack()
        self.combo_box.pack()
        self.patvirtinti_pasirinkima.pack()
        self.parodyti_statusa_pasirinkto.pack()
        self.pasirinkite_statusa.pack()
        self.vykdomas.pack()
        self.sustabdytas.pack()
        self.baigtas.pack()
        self.patvirtinti_pakeitima.pack()
        self.status.pack()

        self.langas.mainloop()
    
    def parodyti_statusa(self):
        statusas = self.var_projektui.get()
        for statusas in session.query(Projektas).filter_by(pavadinimas=statusas):
            parodyti_statusa = statusas.statusas
            parodyti_pavadinima = statusas.pavadinimas
        self.parodyti_statusa_pasirinkto['text'] = f'"{parodyti_pavadinima}" statusas: "{parodyti_statusa}"'
    
    def pakeisti_statusa(self):
        statusas = self.var_projektui.get()
        for statusas in session.query(Projektas).filter_by(pavadinimas=statusas):
            parodyti_id = statusas.id
        projektai = session.query(Projektas).get(parodyti_id)
        if self.var_statusui.get() == 0:
            projektai.statusas = "Vykdomas"
        if self.var_statusui.get() == 1:
            projektai.statusas = "Sustabdytas"
        if self.var_statusui.get() == 2:
            projektai.statusas = "Baigtas"
        session.commit()
        print(f'statusas pakeistas i {projektai.statusas}')
        self.status['text'] = f'Statusas sėkmingai pakeistas į "{projektai.statusas}"'




