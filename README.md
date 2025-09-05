# 🖥️ Sistema de Gestão DEMPAM (MPPE)

## 👥 Membros da Equipe - Responsabilidades

* **[Seu Nome]** – Desenvolvedor Full-Stack (Backend e Frontend), Designer UI/UX

*(Adicione outros membros da equipe se houver)*

## 📖 Descrição do Projeto

**Sistema DEMPAM** é uma aplicação web desenvolvida com Python e Django, criada para gerenciar solicitações de itens e o controle de estoque de um departamento. A aplicação possui duas áreas principais: um portal para solicitantes e uma área administrativa segura para gerenciamento, com um sistema de login robusto fornecido pelo Django.

## 🏗️ Arquitetura do Projeto

O código foi organizado de forma modular para separar as responsabilidades de backend e frontend:

sistema-dempam/
├── backend/
│   ├── usuarios/
│   │   ├── templates/
│   │   │   └── usuarios/
│   │   │       ├── homepage.html
│   │   │       └── login.html
│   │   ├── urls.py
│   │   └── views.py
│   ├── backend/
│   │   └── settings.py
│   └── manage.py
├── frontend/
│   └── static/
│       ├── css/
│       └── images/
└── requirements.txt


## 🖼️ Galeria de Capturas de Tela

*(Insira aqui screenshots da sua tela de login e da homepage funcionando!)*

## 🛠️ Ferramentas e Tecnologias Utilizadas

| Ferramenta / Biblioteca | Uso | Justificativa |
| :--- | :--- | :--- |
| **Python 3.x** | Linguagem principal do backend | Sintaxe clara e ecossistema robusto, ideal para desenvolvimento web. |
| **Django** | Framework web | "Batteries-included", oferece segurança, ORM e autenticação prontos. |
| **HTML5 / CSS3** | Estrutura e estilização do frontend | Tecnologias padrão da web para criar a interface do usuário. |
| **Figma** | Design e Prototipagem de UI/UX | Ferramenta visual para planejar a aparência e o fluxo de navegação. |
| **SQLite / PostgreSQL**| Banco de Dados | SQLite para desenvolvimento, PostgreSQL para produção. |
| **Git / GitHub** | Controle de versão e repositório | Essencial para o histórico do desenvolvimento e colaboração. |

## 📚 Conceitos Aplicados

* **Arquitetura MVT (Model-View-Template)**
* **Mapeamento Objeto-Relacional (ORM)**
* **Sistema de Rotas (URL Routing)**
* **Autenticação e Autorização**
* **Gerenciamento de Arquivos Estáticos**
* **Templates com DTL (Django Template Language)**

## ⚠️ Desafios, Erros e Lições Aprendidas

* **❌ Maior Erro:** Erros `404 Not Found` ao carregar arquivos CSS devido à configuração incorreta do `STATICFILES_DIRS` no `settings.py`.
* **🏔️ Maior Desafio:** Traduzir fielmente o design do Figma para código HTML e CSS responsivo.
* **📘 Lições Aprendidas:** A importância de ambientes virtuais, a necessidade de reiniciar o servidor após mudanças no `settings.py` e o processo de depuração sistemática.

## 📦 Instalação e Execução

### 1️⃣ Pré-requisitos
* Python 3.x instalado e configurado no PATH.
* Git instalado.

### 2️⃣ Clonar o repositório
```bash
git clone [LINK PARA O SEU REPOSITÓRIO NO GITHUB]
cd [NOME-DA-PASTA-DO-PROJETO]
3️⃣ Criar e ativar o ambiente virtual
Bash

# Criar o ambiente
python -m venv venv

# Ativar no Windows PowerShell
.\venv\Scripts\activate
4️⃣ Instalar dependências
Bash

pip install -r requirements.txt
5️⃣ Preparar o Banco de Dados
Navegue até a pasta backend:

Bash

cd backend
python manage.py migrate
6️⃣ Criar um Superusuário
Bash

python manage.py createsuperuser
7️⃣ Executar o projeto
Bash

python manage.py runserver
O site estará disponível em http://127.0.0.1:8000/.

📋 Dependências
Django
