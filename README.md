# PITII - Projeto Integrador Transdisciplinar em Ciência da Computação II

## Descrição do Projeto
O **PITII** (Projeto Integrador Transdisciplinar em Ciência da Computação II) é um projeto desenvolvido para a disciplina de Projeto Integrador II do curso de Ciência da Computação.

O objetivo deste projeto é criar uma aplicação de software ou dispositivo que integre conhecimentos multidisciplinares adquiridos ao longo do curso, aplicando-os para resolver um problema real.

## Funcionalidades
* **Home**: Página inicial com um Planner integrado para ajudar na organização diária e no acompanhamento de tarefas e metas.
* **Diário**: Espaço dedicado para registrar o humor, descrever o dia, acompanhar a qualidade do sono, registrar o total de horas dormidas, descrever a experiência do sono e anotar os remédios tomados.
* **Remédios**: Módulo para adicionar, remover e atualizar informações sobre os remédios, incluindo horários e dosagens recomendadas.
* **Sono**: Ferramenta de acompanhamento de sono que exibe a média semanal de horas dormidas, além de um gráfico que mostra a qualidade do sono ao longo do tempo.
* **Humor**: Calendário interativo para monitorar e visualizar as variações de humor ao longo do mês, auxiliando na análise de padrões emocionais.

## Tecnologias Utilizadas
O projeto foi desenvolvido utilizando as seguintes tecnologias:

* **Python** - Linguagem utilizada para o desenvolvimento da lógica de backend do projeto.
* **HTML** - Linguagem usada para estruturar o frontend do projeto, definindo a interface do usuário.
* **Django** - Framework web em Python, utilizado para gerenciar o backend e facilitar o desenvolvimento de funcionalidades.
* **Banco de Dados** - MySQL e sqlite3, utilizados para armazenamento e gerenciamento dos dados da aplicação.

## Estrutura do Projeto
Abaixo, uma visão geral da estrutura de pastas e arquivos:
```csharp
Diary/
│
├── Diary/
│   │
│   ├── __init__.py
│   ├── settings.py            # Configurações principais do projeto Django
│   ├── urls.py                # Configuração das URLs principais do projeto
│   └── wsgi.py                # Configurações para o servidor WSGI (servidor web)
│
├── entries/
│   ├── migrations/              # Arquivos de migração para a criação e atualização de tabelas no banco de dados
│   │   ├── __init__.py
│   │   └── [arquivos_de_migracao].py
│   │
│   ├── static/                  # Arquivos estáticos utilizados na aplicação
│   │   └── css/
│   │       ├── Diary_logo.jpg   # Logo específica da aplicação Diary
│   │       ├── diary.css        # Arquivos de estilo CSS específicos da aplicação Diary
│   │
│   ├── templates/entries/       # Templates HTML da aplicação Diary
│   │   ├── base.html            # Template base das páginas
│   │   ├── calendario.html      # Template para exibir o calendário
│   │   ├── entry_confirm_delete.html  # Template de confirmação de exclusão de entrada do diário
│   │   ├── entry_detail.html    # Template de detalhes de uma entrada do diário
│   │   ├── entry_form.html      # Template do formulário de entrada do diário
│   │   ├── entry_list.html      # Template para listar entradas do diário
│   │   ├── home.html            # Página inicial do Diário
│   │   ├── login.html           # Página de login
│   │   ├── register.html        # Página de registro
│   │   ├── remedio_confirm_delete.html  # Template de confirmação de exclusão de remédio
│   │   ├── remedio_detail.html  # Template de detalhes de um remédio
│   │   ├── remedio_form.html    # Formulário para adicionar/editar remédio
│   │   ├── remedio_list.html    # Lista de remédios
│   │   ├── sono_detail.html     # Detalhes do registro de sono
│   │   └── sono_registro_list.html  # Lista de registros de sono
│   │
│   ├── __init__.py              # Arquivo de inicialização do módulo entries
│   ├── admin.py                 # Configurações do módulo entries para o painel de administração do Django
│   ├── apps.py                  # Configurações da aplicação entries no Django
│   ├── forms.py                 # Formulários do Django para entrada de dados no módulo entries
│   ├── models.py                # Modelos de dados (tabelas) para o banco de dados do módulo entries
│   ├── urls.py                  # Configuração das rotas (URLs) para as views do módulo entries
│   └── views.py                 # Lógica das views para processamento das requisições e respostas do módulo entries
│
├── db.sqlite3                   # Banco de dados SQLite utilizado pela aplicação
└── manage.py                    # Comando para execução e gerenciamento do projeto Django


```
## Instalação e Configuração
Para rodar o projeto localmente, siga os passos abaixo:

### Pré-requisitos

* **Python 3.x** - Certifique-se de que o Python está instalado.
* **pip** - Instalador de pacotes Python.

1. Clone o repositório:
```bash
git clone https://github.com/Bluecherry018/PITII.git
cd PITII
```

2. Instale as dependências:
```bash
pip install django
pip install requests
```

3. Execute as migrações do banco de dados:
```bash
python manage.py migrate
```

4. Inicie o servidor:
```bash
python manage.py runserver
```
5. Acesse a aplicação:

Abra o navegador e acesse http://127.0.0.1:8000

## Hospedagem

A aplicação está hospedada no PythonAnywhere e pode ser acessada pelo link abaixo:
https://alexandrafloriano.pythonanywhere.com/

