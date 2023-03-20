from fastapi import FastAPI
from starlette.responses import RedirectResponse

from apps.users.router import router as users_router

app = FastAPI()


@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


app.include_router(users_router)