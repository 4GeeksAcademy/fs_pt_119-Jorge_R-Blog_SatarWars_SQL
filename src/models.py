from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, DateTime, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    userId: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(80), nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(16), nullable=False)
    suscripcion: Mapped[int] = mapped_column(DateTime, nullable=False)
    active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    personajesLike: Mapped[list['PersonajeFav']] = relationship(back_populates='userLike')

class Planeta(db.Model):
    __tablename__ = 'planeta'
    planetaId: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String, nullable=False)
    extension: Mapped[int] = mapped_column(Integer, nullable=False)
    ubicacionGalaxia: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)

class Personaje(db.Model):
    __tablename__ = 'personaje'
    personajeId: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[int] = mapped_column(String(80), nullable=False)
    cargo_rango: Mapped[str] = mapped_column(String)
    estatura: Mapped[int] = mapped_column(Integer)
    peso: Mapped[int] = mapped_column(Integer)
    piloto: Mapped[bool] = mapped_column(Boolean, nullable=False)
    usersLiked: Mapped[list['PersonajeFav']] = relationship(back_populates='personajeLiked')

class Nave(db.Model):
    __tablename__ = 'nave'
    naveId: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(80), nullable=False)
    modelo: Mapped[str] = mapped_column(String, nullable=False)
    velocidad: Mapped[int] = mapped_column(Integer, nullable=False)
    salto_HiperEspacio: Mapped[bool] = mapped_column(Boolean)

class PersonajeFav(db.Model):
    __tablename__ = 'personaje_fav'
    personajeFavId: Mapped[int] = mapped_column(primary_key=True)
    userId: Mapped[int] = mapped_column(ForeignKey('user.userId'))
    userLike: Mapped['User'] = relationship(back_populates='personajesLike')
    personajeId: Mapped[int] = mapped_column(ForeignKey('personaje.personajeId'))
    personajeLiked: Mapped['Personaje'] = relationship(back_populates='usersLiked')




