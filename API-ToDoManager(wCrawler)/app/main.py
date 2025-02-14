from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.auth import criar_token
from app.routers import tasks

app = FastAPI(title="API de Gerenciamento de Tarefas(To-Do List)", version="1.0.0")


@app.get("/")
async def root():
    return {"message": "Bem-vindo à API de Gerenciamento de Tarefas"}


app.include_router(tasks.router)

@app.post("/token")
async def gerar_token(form_data: OAuth2PasswordRequestForm = Depends()):
    # Login básico
    if form_data.username == "admin" and form_data.password == "admin":
        token = criar_token({"sub": form_data.username})
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=400, detail="Credenciais inválidas")