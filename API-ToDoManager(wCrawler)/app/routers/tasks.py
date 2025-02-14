from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models import Base, Tarefa
from app.crud import criar_tarefa as criar_tarefa_crud, obter_tarefa as obter_tarefa_crud, atualizar_tarefa as atualizar_tarefa_crud, deletar_tarefa as deletar_tarefa_crud
from app.auth import verificar_token
from pydantic import BaseModel
from app.database import get_db
from aiocache import cached

router = APIRouter(prefix="/tasks", tags=["Tasks"])


class TarefaEntrada(BaseModel):
    titulo: str
    descricao: str = None
    estado: str


@router.post("/", response_model=dict, dependencies=[Depends(verificar_token)])
def criar_tarefa(tarefa: TarefaEntrada, db: Session = Depends(get_db)):
    nova_tarefa = criar_tarefa_crud(db, **tarefa.model_dump())
    return {"id": nova_tarefa.id, "mensagem": "Tarefa criada com sucesso!"}


@router.get("/")
@cached(ttl=60)
async def listar_tarefas(estado: str = None, offset: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    query = db.query(Tarefa)
    if estado:
        query = query.filter(Tarefa.estado == estado)
    tarefas = query.offset(offset).limit(limit).all()
    return tarefas


@router.get("/{tarefa_id}")
async def obter_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
    tarefa = obter_tarefa_crud(db, tarefa_id)
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefa


@router.put("/{tarefa_id}", dependencies=[Depends(verificar_token)])
async def atualizar_tarefa(tarefa_id: int, tarefa: TarefaEntrada, db: Session = Depends(get_db)):
    tarefa_atualizada = atualizar_tarefa_crud(db, tarefa_id, tarefa.titulo, tarefa.descricao, tarefa.estado)
    if not tarefa_atualizada:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return {"mensagem": "Tarefa atualizada com sucesso!"}


@router.delete("/{tarefa_id}", dependencies=[Depends(verificar_token)])
async def deletar_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
    tarefa_deletada = deletar_tarefa_crud(db, tarefa_id)
    if not tarefa_deletada:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return {"mensagem": "Tarefa deletada com sucesso!"}
