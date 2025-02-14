# 💰 Remuneração Externa - Django App

O **Remuneração Externa** é um aplicativo desenvolvido em **Django** para verificar os valores recebidos por servidores emprestados, além de exibir os valores por competência. O sistema permite a consulta de dados de remuneração e a edição das informações relacionadas.

> ⚠ **Importante:** O repositório contém apenas o código referente ao app **Remuneração Externa**. Algumas funcionalidades fazem referência a outros aplicativos do sistema, como `kdastro`, que **não estão incluídos** neste repositório.

---

## 📂 Estrutura do Projeto

O aplicativo possui as seguintes funcionalidades principais:

### 🔹 **Consulta de Servidores**
- Os usuários podem buscar um servidor pelo nome ou número de matrícula.
- A busca retorna os dados do servidor e os valores de remuneração vinculados a ele.

### 🔹 **Visualização por Competência**
- Exibe os valores recebidos pelo servidor em diferentes competências.
- Paginação para facilitar a navegação entre registros.

### 🔹 **Edição e Exclusão de Registros**
- Usuários autorizados podem adicionar, editar ou excluir registros de remuneração.
- As operações são protegidas por autenticação.

### 🔹 **Autenticação e Controle de Acesso**
- Apenas usuários autenticados podem acessar as funcionalidades do sistema.
- Implementação de `LoginRequiredMixin` para restringir acesso.

---

## 🛠 Tecnologias Utilizadas

- ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white) - Framework principal do projeto
- ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) - Linguagem de programação utilizada
- ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) - Estruturação das páginas web
- ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) - Estilização das páginas
- ![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white) - Framework CSS para estilização responsiva
- ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white) - Banco de dados utilizado pelo Django ORM
- ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white) - Banco de dados alternativo suportado
- ![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white) - Controle de versão do código
- ![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white) - Hospedagem do repositório e versionamento do projeto


