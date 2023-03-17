from fastapi import FastAPI

from core import models
from core.database import engine
from routers import users

models.Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="Friketis",
    description="Aplicacion realizada para el bootcamp de welcome de Basetis para probar FastAPI, con fines puramente "
                "educativos.",
    version="0.0.1",)

app.include_router(users.router)


