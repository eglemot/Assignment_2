from tkinter import *
from tkinter.font import Font
from sqlalchemy.orm import sessionmaker
from tkinter import ttk
from tkinter.font import Font
from .pagrindinis import Projektas, Komanda, Imone, engine

session = sessionmaker(bind=engine)()
query1="SELECT distinct(komandos_pavadinimas) as pavadinimas FROM komanda GROUP by komandos_pavadinimas"
query2="SELECT distinct(pavadinimas) as pavadinimas FROM imone GROUP by pavadinimas"

class IvestiProjekta():

    def __init__(self, main):
        self.main = main
        self.main.title("ĮVESTI PROJEKTĄ")
        self.langas = Frame(self.main)
        self.tekstas = Frame(self.main)
        self.langas.geometry = ("500x500")
        self.var = IntVar()
        self.var1 = StringVar()
        self.var2 = StringVar()
        self.my_data1=engine.execute(query1)
        self.my_list1 = [r for r, in self.my_data1]
        self.my_data2=engine.execute(query2)
        self.my_list2 = [r for r, in self.my_data2]
        self.looks1 = Font(
            family = 'Helvetica',
            size = 14,
            weight = 'normal',
            slant = "italic",
            underline = 1,
            )

        self.ivesti_projekto_pavadinima_l = Label(self.langas, text="Projekto pavadinimas")
        self.ivesti_projekto_pavadinima_e = Entry(self.langas, bg="#F0E9D2", fg="#181D31")
        self.ivesti_projekto_trukme_l = Label(self.langas, text="Projekto trukmė dienomis")
        self.ivesti_projekto_trukme_e = Entry(self.langas, bg="#F0E9D2", fg="#181D31")
        self.ivesti_projekto_status_l = Label(self.langas, text="Projekto statusas", border=5)
        self.vykdomas = Radiobutton(self.langas, text="Vykdomas", variable=self.var, value=0)
        self.sustabdytas= Radiobutton(self.langas, text="Sustabdytas", variable=self.var, value=1)
        self.baigtas = Radiobutton(self.langas, text="Baigtas", variable=self.var, value=2)
        self.patvirtinti_ivesta_projekta = Button(self.langas, text="PATVIRTINTI", command=self.ivesti_projekta, border=5, fg="#4E6C50")
        self.status_projektas = Label(self.langas, text="Laukiama, kol suvesite duomenis", border=10, font=self.looks1, fg="#F8485E")
        self.pasirinkti_komanda_l = Label(self.langas, text="Pasirinkite komandą", border=5)
        self.combo_box1 = ttk.Combobox(self.langas, values=self.my_list1, textvariable=self.var1)
        self.combo_box1.current(0)
        self.pasirinkti_imone_l = Label(self.langas, text="Pasirinkite įmonę", border=5)
        self.combo_box2 = ttk.Combobox(self.langas, values=self.my_list2, textvariable=self.var2)
        self.combo_box2.current(0)

        self.ivesti_projekto_pavadinima_l.pack()
        self.ivesti_projekto_pavadinima_e.pack()
        self.ivesti_projekto_status_l.pack()
        self.vykdomas.pack()
        self.sustabdytas.pack()
        self.baigtas.pack()
        self.ivesti_projekto_trukme_l.pack()
        self.ivesti_projekto_trukme_e.pack()
        self.pasirinkti_komanda_l.pack()
        self.combo_box1.pack()
        self.pasirinkti_imone_l.pack()
        self.combo_box2.pack()
        self.patvirtinti_ivesta_projekta.pack()
        self.status_projektas.pack()
        self.langas.pack(side=TOP)
        self.tekstas.pack(side=BOTTOM)

        self.langas.mainloop()
   
    def ivesti_projekta(self):
        komanda = self.var1.get()
        for komanda in session.query(Komanda).filter_by(komandos_pavadinimas=komanda):
            komanda_gal = komanda.id
        imone = self.var2.get()
        for imone in session.query(Imone).filter_by(pavadinimas=imone):
            imones_id = imone.id
        if self.var.get() == 0:
            statuselis = "Vykdomas"
        if self.var.get() == 1:
            statuselis = "Sustabdytas"
        if self.var.get() == 2:
            statuselis = "Baigtas"
        projektas_i = Projektas(pavadinimas=self.ivesti_projekto_pavadinima_e.get(), trukme_dienomis=self.ivesti_projekto_trukme_e.get(), statusas=statuselis, komanda_id=komanda_gal, imone_id=imones_id)
        session.add(projektas_i)
        session.commit()
        self.ivesti_projekto_pavadinima_e.delete(0, END)
        self.ivesti_projekto_trukme_e.delete(0, END)
        self.status_projektas['text'] = "Sėkmingai sukurtas projektas"