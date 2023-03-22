import datetime

from core import models
from core.database import SessionLocal
import csv


def __get_or_add_genre(db, genre_name):
    db_genre = db.query(models.Genre).filter(models.Genre.name == genre_name).first()
    if db_genre:
        return db_genre
    db_genre = models.Genre(name=genre_name)
    db.add(db_genre)
    db.commit()
    db.refresh(db_genre)
    return db_genre


def __get_or_add_platform(db, param):
    db_platform = db.query(models.Platform).filter(models.Platform.name == param).first()
    if db_platform:
        return db_platform
    db_platform = models.Platform(name=param)
    db.add(db_platform)
    db.commit()
    db.refresh(db_platform)
    return db_platform


def init_db_videogames():
    db = SessionLocal()
    if db.query(models.Videogame).count() == 0:
        with open('./apps/videogames/Video_Games.csv', mode='r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                release_date = None
                if row['Year_of_Release'] != 'N/A':
                    release_date = datetime.datetime(int(row['Year_of_Release']), 1, 1)
                db_videogame = models.Videogame()
                db_videogame.title = row['Name']
                db_videogame.release_date = release_date
                db_videogame.publisher = row['Publisher']
                db_videogame.developer = row['Developer']
                db_videogame.genre_id = __get_or_add_genre(db, row['Genre']).genre_id
                db_videogame.platform_id = __get_or_add_platform(db, row['Platform']).platform_id
                db.add(db_videogame)
                db.commit()
                db.refresh(db_videogame)
