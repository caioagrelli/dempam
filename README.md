# 🖥️ Sistema de Gestão DEMPAM (MPPE)

## 👥 Membros da Equipe - Responsabilidades

* **Caio Agrelli** – Desenvolvedor Full-Stack (Backend e Frontend), Designer UI/UX


## 📖 Descrição do Projeto

**Sistema DEMPAM** é uma aplicação web desenvolvida com Python e Django, criada para gerenciar solicitações de itens e o controle de estoque de um departamento. A aplicação possui duas áreas principais: um portal para solicitantes e uma área administrativa segura para gerenciamento, com um sistema de login robusto fornecido pelo Django.

## 🏗️ Arquitetura do Projeto

O código foi organizado de forma modular para separar as responsabilidades de backend e frontend:

 ````  **<-- ADICIONE ESTA LINHA**
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
` ````  **<-- E ADICIONE ESTA LINHA**

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
