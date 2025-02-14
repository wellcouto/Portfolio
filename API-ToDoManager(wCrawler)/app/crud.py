from sqlalchemy.orm import Session
from app.models import Tarefa

def criar_tarefa(db: Session, titulo: str, descricao: str, estado: str):
    nova_tarefa = Tarefa(titulo=titulo, descricao=descricao, estado=estado)
    db.add(nova_tarefa)
    db.commit()
    db.refresh(nova_tarefa)
    return nova_tarefa

def listar_tarefas(db: Session):
    return db.query(Tarefa).all()

def obter_tarefa(db: Session, tarefa_id: int):
    return db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()

def atualizar_tarefa(db: Session, tarefa_id: int, titulo: str, descricao: str, estado: str):
    tarefa = obter_tarefa(db, tarefa_id)
    if tarefa:
        tarefa.titulo = titulo
        tarefa.descricao = descricao
        tarefa.estado = estado
        db.commit()
        db.refresh(tarefa)
    return tarefa

def deletar_tarefa(db: Session, tarefa_id: int):
    tarefa = obter_tarefa(db, tarefa_id)
    if tarefa:
        db.delete(tarefa)
        db.commit()
    return tarefa

