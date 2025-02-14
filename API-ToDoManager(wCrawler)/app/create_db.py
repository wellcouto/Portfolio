from app.models import Base
from app.database import engine

# Criar todas as tabelas definidas no modelo (Windows)
print("Criando tabelas no banco de dados...")
Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso!")