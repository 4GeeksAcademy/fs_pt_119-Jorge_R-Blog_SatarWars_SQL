from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(80), nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(16), nullable=False)
    active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    personajes_like: Mapped[list['PersonajeFav']] = relationship(back_populates='user_like')
    naves_like: Mapped[list['NaveFav']] = relationship(back_populates='user_like_nave')
    planetas_like: Mapped[list['PlanetaFav']] = relationship(back_populates='user_like_planeta')
    suscripcion_user: Mapped['int'] = mapped_column(ForeignKey('suscripcion.suscripcion_id'), unique=True)
    suscripcion_fecha: Mapped[list['Suscripcion']] = relationship('suscripcion_activa')

class Suscripcion(db.Model):
    __tablename__ = 'suscripcion'
    suscripcion_id: Mapped[int] = mapped_column(primary_key=True)
    fecha: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    plan: Mapped[str] = mapped_column(String, nullable=False)
    creditos: Mapped[int] = mapped_column(Integer, nullable=False)
    user_suscripcion: Mapped[int] = mapped_column(ForeignKey('user.id'), unique=True)
    suscripcion_activa: Mapped[list['User']] = relationship('suscripcion_fecha')
    
class Planeta(db.Model):
    __tablename__ = 'planeta'
    planeta_id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String, nullable=False)
    extension: Mapped[int] = mapped_column(Integer, nullable=False)
    ubicacion_galaxia: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    users_liked_planeta: Mapped[list['PlanetaFav']] = relationship(back_populates='planeta_liked')
    habitantes: Mapped[list['Personaje']] = relationship(back_populates='planeta_personaje')

class Personaje(db.Model):
    __tablename__ = 'personaje'
    personaje_id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(80), nullable=False)
    cargo_rango: Mapped[str] = mapped_column(String)
    estatura: Mapped[int] = mapped_column(Integer)
    peso: Mapped[int] = mapped_column(Integer)
    piloto: Mapped[bool] = mapped_column(Boolean, nullable=False)
    users_liked: Mapped[list['PersonajeFav']] = relationship(back_populates='personaje_liked')
    nacionalidad: Mapped[int] = mapped_column(ForeignKey('planeta.planeta_id'))
    planeta_personaje: Mapped[list['Planeta']] = relationship(back_populates='habitantes')

class Nave(db.Model):
    __tablename__ = 'nave'
    nave_id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(80), nullable=False)
    modelo: Mapped[str] = mapped_column(String, nullable=False)
    velocidad: Mapped[int] = mapped_column(Integer, nullable=False)
    salto_hiperespacio: Mapped[bool] = mapped_column(Boolean)
    users_liked_nave: Mapped[list['NaveFav']] = relationship(back_populates='nave_liked')

class PersonajeFav(db.Model):
    __tablename__ = 'personaje_fav'
    personaje_fav_id: Mapped[int] = mapped_column(primary_key=True)
    usuario_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    user_like: Mapped['User'] = relationship(back_populates='personajes_like')
    character_id: Mapped[int] = mapped_column(ForeignKey('personaje.personaje_id'))
    personaje_liked: Mapped['Personaje'] = relationship(back_populates='users_liked')

class NaveFav(db.Model):
    __tablename__ = 'nave_fav'
    nave_fav_id: Mapped[int] = mapped_column(primary_key=True)
    usuario_id_nave: Mapped[int] = mapped_column(ForeignKey('user.id'))
    user_like_nave: Mapped['User'] = relationship(back_populates='naves_like')
    starsihp_id: Mapped[int] = mapped_column(ForeignKey('nave.nave_id'))
    nave_liked: Mapped['Nave'] = relationship(back_populates='users_liked_nave')
    
class PlanetaFav(db.Model):
    __tablename__ = 'planeta_fav'
    planeta_fav_id: Mapped[int] = mapped_column(primary_key=True)
    usuario_id_planeta: Mapped[int] = mapped_column(ForeignKey('user.id'))
    user_like_planeta: Mapped['User'] = relationship(back_populates='planetas_like')
    planet_id: Mapped[int] = mapped_column(ForeignKey('planeta.planeta_id'))
    planeta_liked: Mapped['Planeta'] = relationship(back_populates='users_liked_planeta')



