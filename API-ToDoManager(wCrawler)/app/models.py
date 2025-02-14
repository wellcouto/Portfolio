from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime, timezone

Base = declarative_base()

class Tarefa(Base):
    __tablename__ = "tarefas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
    estado = Column(String, nullable=False)
    data_criacao = Column(DateTime, default=datetime.now(timezone.utc))
    data_atualizacao = Column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
