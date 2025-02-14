import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from sqlalchemy.orm import declarative_base   
from fastapi.testclient import TestClient
from app.main import app

Base = declarative_base()

client = TestClient(app)

def obter_token():
    response = client.post(
        "/token",
        data={"username": "admin", "password": "admin"},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    assert response.status_code == 200, f"Erro ao obter token: {response.json()}"
    return response.json().get("access_token")

def get_query_auth_params():
    token = obter_token()
    return {"token": token}

class TarefaEntrada:
    def __init__(self, titulo: str, descricao: str, estado: str):
        self.titulo = titulo
        self.descricao = descricao
        self.estado = estado

def get_headers():
    token = obter_token()
    return {"Authorization": f"Bearer {token}"}

def verificar_resposta(response, status_code_esperado=200):
    assert response.status_code == status_code_esperado, f"Erro: {response.status_code}, Detalhes: {response.json()}"
    
# Teste: Criar uma nova tarefa
def test_criar_tarefa():
    payload = {
        "titulo": "Teste Tarefa",
        "descricao": "Descrição de teste",
        "estado": "pendente"
    }
    response = client.post(
        "/tasks/",
        json=payload,
        params=get_query_auth_params()
    )
    verificar_resposta(response)
    assert "mensagem" in response.json(), "Mensagem de sucesso não encontrada na resposta."
    assert "id" in response.json(), "ID da tarefa não foi retornado na resposta."

# Teste: Listar tarefas
def test_listar_tarefas():
    response = client.get("/tasks/", params=get_query_auth_params())
    verificar_resposta(response)
    assert isinstance(response.json(), list), "Resposta não é uma lista de tarefas."

# Teste: Obter uma tarefa específica
def test_obter_tarefa():
    payload = TarefaEntrada(titulo="Tarefa para teste de GET", descricao="Teste GET", estado="pendente").__dict__
    response = client.post(
        "/tasks/",
        json=payload,
        params=get_query_auth_params()
    )
    verificar_resposta(response)
    tarefa_id = response.json().get("id", None)

    assert tarefa_id is not None, "Erro: tarefa não foi criada corretamente, ID não encontrado na resposta."

    get_response = client.get(f"/tasks/{tarefa_id}", headers=get_headers())
    verificar_resposta(get_response)
    assert get_response.json().get("titulo") == "Tarefa para teste de GET", "Título da tarefa não corresponde ao esperado."

# Teste: Atualizar uma tarefa
def test_atualizar_tarefa():
    payload = TarefaEntrada(titulo="Tarefa Atualizar", descricao="Teste PUT", estado="pendente").__dict__
    response = client.post(
        "/tasks/",
        json=payload,
        params=get_query_auth_params()
    )
    verificar_resposta(response)
    tarefa_id = response.json().get("id", None)

    assert tarefa_id is not None, "Erro: tarefa não foi criada corretamente, ID não encontrado na resposta."

    update_payload = TarefaEntrada(titulo="Tarefa Atualizada", descricao="Atualizada com sucesso", estado="concluída").__dict__
    update_response = client.put(
        f"/tasks/{tarefa_id}",
        json=update_payload,
        params=get_query_auth_params()
    )
    verificar_resposta(update_response)
    assert update_response.json().get("mensagem") == "Tarefa atualizada com sucesso!", "Mensagem de atualização não corresponde ao esperado."

# Teste: Deletar uma tarefa
def test_deletar_tarefa():
    payload = TarefaEntrada(titulo="Tarefa para Delete", descricao="Teste DELETE", estado="pendente").__dict__
    response = client.post(
        "/tasks/",
        json=payload,
        params=get_query_auth_params()
    )
    verificar_resposta(response)
    tarefa_id = response.json().get("id", None)

    assert tarefa_id is not None, "Erro: tarefa não foi criada corretamente, ID não encontrado na resposta."

    delete_response = client.delete(f"/tasks/{tarefa_id}", params=get_query_auth_params())
    verificar_resposta(delete_response)
    assert delete_response.json().get("mensagem") == "Tarefa deletada com sucesso!", "Mensagem de exclusão não corresponde ao esperado."

    # Verificação intermediária após exclusão
    verificar_get = client.get(f"/tasks/{tarefa_id}", params=get_query_auth_params())
    assert verificar_get.status_code == 404, "A tarefa ainda está disponível após a exclusão."