from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///data/projektai.db')
Base = declarative_base()

class Komanda(Base):
    __tablename__ = "komanda"
    id = Column(Integer, primary_key=True)
    komandos_pavadinimas = Column(String)
    asmenu_skaicius = Column(Integer)
    el_pastas = Column(String)
    projektai = relationship("Projektas", back_populates="komanda")

class Imone(Base):
    __tablename__ = "imone"
    id = Column(Integer, primary_key=True)
    pavadinimas = Column(String)
    el_pastas = Column(String)
    projektai = relationship("Projektas", back_populates="imone")

class Projektas(Base):
    __tablename__ = "projektas"
    id = Column(Integer, primary_key=True)
    pavadinimas = Column(String)
    projekto_pradzia = Column(DateTime, default = datetime.utcnow)
    trukme_dienomis = Column(Integer)
    statusas = Column(String)
    komanda_id = Column(Integer, ForeignKey('komanda.id'))
    komanda = relationship(Komanda, back_populates="projektai")
    imone_id = Column(Integer, ForeignKey('imone.id'))
    imone = relationship("Imone", back_populates="projektai")

if __name__ == "__main__":
    Base.metadata.create_all(engine)

