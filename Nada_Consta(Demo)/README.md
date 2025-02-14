# 📌 Nada Consta - Django App

O **Nada Consta** é um aplicativo desenvolvido em Django para verificação das pendências dos servidores por setor. Ele permite que usuários autenticados consultem a situação de funcionários, vejam atribuições pendentes e editem informações relacionadas a essas atribuições.

> ⚠ **Importante:** O repositório contém apenas o código referente ao app **nada-consta**. Algumas funcionalidades fazem referência a outros aplicativos do sistema, como `kdastro`, que **não estão incluídos** neste repositório.

---

## 📂 Estrutura do Projeto

O aplicativo possui as seguintes funcionalidades principais:

### 🔹 **Autenticação e Controle de Acesso**
- O sistema exige que os usuários façam login para acessar a maioria das funções.
- Utiliza `django.contrib.auth` para autenticação e controle de usuários.

### 🔹 **Consulta de Funcionários**
- Os usuários podem buscar um funcionário usando o número de matrícula.
- Atribuições são carregadas com base no setor do usuário autenticado.

### 🔹 **Gerenciamento de Atribuições**
- Cada funcionário pode ter atribuições associadas, que podem ser editadas por usuários autorizados.
- A edição das atribuições é feita por meio do formulário `EdicaoAtribuicaoForm`.

### 🔹 **Cadastro e Login**
- O app oferece um sistema de cadastro de novos usuários através do formulário `SignUpForm`.
- A autenticação é realizada com `authenticate()` e `login()` do Django.

## 🛠 Tecnologias Utilizadas

- ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white) - Framework principal do projeto
- ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) - Linguagem de programação utilizada
- ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) - Estruturação das páginas web
- ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) - Estilização das páginas
- ![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white) - Framework CSS (opcional)
- ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white) - Banco de dados padrão do Django ORM
- ![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white) - Controle de versão