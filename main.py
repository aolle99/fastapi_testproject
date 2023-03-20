from fastapi import FastAPI
from starlette.responses import RedirectResponse

from apps.users.router import router as users_router
from apps.basetis_names.router import router as basetis_names_router

app = FastAPI()


@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


app.include_router(users_router)
app.include_router(basetis_names_router)