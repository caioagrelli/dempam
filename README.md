🖥️ Sistema de Gestão DEMPAM (MPPE)
👥 Membros da Equipe - Responsabilidades
[Seu Nome] – Desenvolvedor Full-Stack (Backend e Frontend), Designer UI/UX

(Adicione outros membros da equipe se houver)

📖 Descrição do Projeto
Sistema DEMPAM é uma aplicação web desenvolvida com Python e Django, criada para gerenciar solicitações de itens e o controle de estoque de um departamento. A aplicação possui duas áreas principais: um portal para solicitantes e uma área administrativa segura para gerenciamento, com um sistema de login robusto fornecido pelo Django.

🏗️ Arquitetura do Projeto
O código foi organizado de forma modular para separar as responsabilidades de backend e frontend:

sistema-dempam/
├── backend/                  # Contém toda a lógica do Django
│   ├── usuarios/             # App do Django para gerenciar usuários, views e URLs
│   │   ├── migrations/
│   │   ├── templates/
│   │   │   └── usuarios/
│   │   │       ├── homepage.html
│   │   │       └── login.html
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── backend/              # Arquivos de configuração do projeto
│   │   ├── settings.py
│   │   └── urls.py
│   └── manage.py             # Ponto de entrada para comandos do Django
├── frontend/                 # Contém os arquivos estáticos
│   └── static/
│       ├── css/
│       │   └── style.css
│       └── images/
│           ├── logo_mppe.png
│           └── brasao_mppe.png
├── venv/                     # Pasta do ambiente virtual
└── requirements.txt          # Dependências do projeto
Essa organização facilita a manutenção, permitindo que a lógica do servidor (backend) e os recursos de estilização (frontend) sejam gerenciados de forma independente.

🖼️ Galeria de Capturas de Tela
(Insira aqui screenshots da sua tela de login e da homepage funcionando!)

🛠️ Ferramentas e Tecnologias Utilizadas
Ferramenta / Biblioteca	Uso	Justificativa
Python 3.x	Linguagem principal do backend	Sintaxe clara e ecossistema robusto, ideal para desenvolvimento web.
Django	Framework web	"Batteries-included", oferece segurança, ORM e sistema de autenticação prontos, acelerando o desenvolvimento.
HTML5 / CSS3	Estrutura e estilização do frontend	Tecnologias padrão da web para criar a interface do usuário.
Figma	Design e Prototipagem de UI/UX	Ferramenta visual para planejar a aparência e o fluxo de navegação do site antes da codificação.
SQLite / PostgreSQL	Banco de Dados	SQLite para simplicidade em desenvolvimento e PostgreSQL para robustez em produção.
Git / GitHub	Controle de versão e repositório	Essencial para o histórico do desenvolvimento e colaboração.

Exportar para as Planilhas
📚 Conceitos Aplicados
Arquitetura MVT (Model-View-Template) — Estrutura padrão do Django para organizar a lógica de dados, de negócio e de apresentação.

Mapeamento Objeto-Relacional (ORM) — Utilização dos Models do Django para interagir com o banco de dados usando apenas Python, sem escrever SQL.

Sistema de Rotas (URL Routing) — Configuração dos arquivos urls.py para mapear endereços web a funções Python (views).

Autenticação e Autorização — Implementação de um sistema de login seguro utilizando o django.contrib.auth nativo.

Gerenciamento de Arquivos Estáticos — Configuração do settings.py (STATICFILES_DIRS) para servir arquivos CSS e imagens de uma pasta dedicada.

Templates com DTL (Django Template Language) — Uso de tags como {% static %} e {% url %} para criar HTML dinâmico e flexível.

⚠️ Desafios, Erros e Lições Aprendidas
❌ Maior Erro:

Erro: TemplateDoesNotExist e erros 404 ao carregar arquivos CSS.

Solução: Correção da estrutura de pastas de templates (templates/app_name/) e da configuração STATICFILES_DIRS no settings.py para apontar para a pasta frontend/static.

🏔️ Maior Desafio:

Desafio: Traduzir fielmente o design criado no Figma para código HTML e CSS, garantindo que a aparência e os espaçamentos fossem consistentes.

Solução: Uso da ferramenta "Inspecionar" do navegador para fazer ajustes finos no CSS em tempo real, comparando lado a lado com o design no Figma.

📘 Lições Aprendidas:

A importância crítica de configurar corretamente o PATH do Python no Windows.

Ambientes virtuais não são opcionais, são essenciais para evitar conflitos de dependências.

Um erro 404 Not Found em arquivos estáticos quase sempre indica um problema de configuração no settings.py ou na estrutura de pastas.

O processo de depuração é sistemático: ler o erro, entender a causa e testar uma solução de cada vez.

📦 Instalação e Execução
1️⃣ Pré-requisitos
Python 3.x instalado e configurado no PATH.

Git instalado.

2️⃣ Clonar o repositório
Bash

git clone [LINK PARA O SEU REPOSITÓRIO NO GITHUB]
cd [NOME-DA-PASTA-DO-PROJETO]
3️⃣ Criar e ativar o ambiente virtual
Bash

# Crie o ambiente
python -m venv venv

# Ative o ambiente (no Windows PowerShell)
.\venv\Scripts\activate
4️⃣ Instalar dependências
Crie um arquivo requirements.txt com o comando pip freeze > requirements.txt. Depois, para instalar:

Bash

pip install -r requirements.txt
5️⃣ Preparar o Banco de Dados
Navegue até a pasta backend e execute as migrações:

Bash

cd backend
python manage.py migrate
6️⃣ Criar um Superusuário (para testar o login)
Bash

python manage.py createsuperuser
(Siga as instruções para criar seu usuário administrador)

7️⃣ Executar o projeto
Bash

python manage.py runserver
O site estará disponível em http://127.0.0.1:8000/.

📋 Dependências
As dependências do projeto estão listadas no arquivo requirements.txt. A principal é:

Django
