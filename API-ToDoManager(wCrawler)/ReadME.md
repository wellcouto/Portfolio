# README - API de Gerenciamento de Tarefas

## **Descrição**
Este projeto é uma API para gerenciamento de tarefas (To-Do List) utilizando FastAPI. A API permite criar, listar, atualizar, visualizar e deletar tarefas, com suporte a autenticação JWT, paginação, filtros e caching.

---

## **Requisitos**
- Python 3.10+
- SQLite (ou outro banco de dados relacional)
- Docker (opcional)

---

## **Instalação do Ambiente**

### **1. Clonar o Repositório**
```bash
git clone <link-do-repositorio>
cd gerenciador_tarefas
```

### **2. Criar Ambiente Virtual**
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\\Scripts\\activate  # Windows
```

### **3. Instalar Dependências**
```bash
pip install -r requirements.txt
```

---

## **Configuração do Banco de Dados**

### **1. Inicializar o Banco de Dados Manualmente**
Execute o script para criar o banco:
```bash
python -m app.create_db
```

### **2. Migrações com Alembic**
- Inicialize o Alembic (se não feito):
```bash
alembic init alembic
```
- Atualize o arquivo `alembic/env.py` com:
```python
from app.models import Base
target_metadata = Base.metadata
```
- Criar uma migração:
```bash
alembic revision --autogenerate -m "criação inicial"
```
- Aplicar migrações:
```bash
alembic upgrade head
```

---

## **Execução da Aplicação**
### **Rodar o Servidor com Uvicorn**
```bash
uvicorn app.main:app --reload
```
- Acesse `http://127.0.0.1:8000/docs` para a documentação automática (Swagger).

---

## **Autenticação JWT**
- Gere um token de autenticação em `/token` com as credenciais padrão `admin:admin`.
- Use o botão `Authorize` no Swagger e insira o token para acessar rotas protegidas.

---

## **Dockerização**
### **1. Criar a Imagem Docker**
```bash
docker build -t api-tarefas .
```

### **2. Rodar com Docker Compose**
```bash
docker-compose up --build
```
- Acesse `http://localhost:8000/docs`.

---

## **Crawler para Importar Tarefas Externas**
### **Descrição**
O script `crawler.py` importa tarefas de uma API pública.

### **Execução**
```bash
python descripts/crawler.py
```
- As tarefas importadas serão adicionadas ao banco de dados.

---

## **Comandos Úteis**
- **Criar migração:**
  ```bash
  alembic revision --autogenerate -m "mensagem"
  ```
- **Aplicar migração:**
  ```bash
  alembic upgrade head
  ```
- **Rodar testes:**
  ```bash
  pytest
  ```

---

## **Estrutura de Pastas**
```
.
├── app
│   ├── main.py  # Ponto de entrada
│   ├── models.py  # Modelos SQLAlchemy
│   ├── database.py  # Conexão com DB
│   ├── auth.py  # Funções de autenticação JWT
│   ├── routers
│   │   └── tasks.py  # Endpoints da API
│   └── tests
├── scripts
│   └── crawler.py  # Script de importação de tarefas
├── alembic  # Migrações do banco de dados
├── requirements.txt
├── ReadME.md
├── Dockerfile
└── docker-compose.yml

```

---

## **Considerações Finais**
O projeto é facilmente extensível com novos endpoints e integrações. Em caso de problemas, verifique se as configurações de variáveis de ambiente e caminhos de arquivos estão corretos. Para dúvidas ou melhorias, envie feedback! 🚀
