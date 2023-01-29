from tkinter import *
from tkinter.font import Font
from sqlalchemy.orm import sessionmaker
from .pagrindinis import Imone, engine

session = sessionmaker(bind=engine)()

class IvestiImone():

    def __init__(self, main):
        self.main = main
        self.main.title("ĮVESTI ĮMONĘ")
        self.langas = self.main
        self.langas.geometry = ("500x500")
        self.looks1 = Font(
            family = 'Helvetica',
            size = 14,
            weight = 'normal',
            slant = "italic",
            underline = 1,
            )
        
        self.ivesti_imones_pavadinima_l = Label(self.langas, text="Pavadinimas")
        self.ivesti_imones_pavadinima_e = Entry(self.langas, bg="#F0E9D2", fg="#181D31")
        self.ivesti_imones_pasta_l = Label(self.langas, text="El.Paštas")
        self.ivesti_imones_pasta_e = Entry(self.langas, bg="#F0E9D2", fg="#181D31")
        self.patvirtinti_ivesti = Button(self.langas, text="PATVIRTINTI", command=self.ivesti_imone, border=5, fg="#4E6C50")
        self.status_imone = Label(self.langas, text="Laukiama, kol suvesite duomenis", border=10, font=self.looks1, fg="#F8485E")

        self.ivesti_imones_pavadinima_l.grid(row=1, column=0)
        self.ivesti_imones_pavadinima_e.grid(row=2, column=0)
        self.ivesti_imones_pasta_l.grid(row=3, column=0)
        self.ivesti_imones_pasta_e.grid(row=4, column=0)
        self.patvirtinti_ivesti.grid(row=5, column=0)
        self.status_imone.grid(row=6, column=0)

        self.langas.mainloop()
    
    def ivesti_imone(self):
        ivesti_i = Imone(pavadinimas=self.ivesti_imones_pavadinima_e.get(), el_pastas=self.ivesti_imones_pasta_e.get())
        session.add(ivesti_i)
        session.commit()
        self.ivesti_imones_pavadinima_e.delete(0, END)
        self.ivesti_imones_pasta_e.delete(0, END)
        self.status_imone['text'] = "Įmonė sėkmingai pridėta"
    

