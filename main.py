from fastapi import FastAPI
from starlette.responses import RedirectResponse

from apps.users.router import router as users_router
from apps.basetis_names.router import router as basetis_names_router
from apps.posts.router import router as posts_router
from apps.videogames.router import router as videogames_router
from apps.videogames.database_dump import init_db_videogames
from core import models
from core.database import engine

models.Base.metadata.create_all(bind=engine)
init_db_videogames()  # Init videogames database
app = FastAPI()


@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


app.include_router(users_router)
app.include_router(basetis_names_router)
app.include_router(posts_router)
app.include_router(videogames_router)
