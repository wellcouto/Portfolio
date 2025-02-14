import requests
from app.crud import criar_tarefa as criar_tarefa_crud
from app.database import SessionLocal

def importar_tarefas():
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    if response.status_code == 200:
        tarefas = response.json()
        with SessionLocal() as db:
            for t in tarefas[:10]:
                criar_tarefa_crud(db, titulo=t["title"], descricao="", estado="pendente")
                print(f"Tarefa '{t['title']}' importada com sucesso.")

if __name__ == "__main__":
    importar_tarefas()