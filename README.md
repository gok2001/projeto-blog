# Blog Pessoal em Django - Sistema de Posts, Comentários e Administração

Blog pessoal desenvolvido em Django como projeto de aprendizado, focado em boas práticas de desenvolvimento web.
Permite que o administrador crie posts enquanto usuários autenticados podem comentar e responder comentários.
O foco é aprender boas práticas de Django, gerenciamento de usuários, relacionamentos de models e manipulação de formulários.

---

## Tecnologias usadas

* Python 3.13
* Django 5.2
* SQLite (por enquanto, banco padrão)
* HTML/CSS para templates
* CKEditor para edição de posts (WYSIWWYG)

---

## Funcionalidades implementadas até agora

* Listagem de posts
* Detalhe de post
* Criação de posts (restrito ao admin)
* Registro de usuário e autenticação (login/logout)
* Comentários associados a posts
* Respostas a comentários (replies)
* Edição e deleção de comentários e respostas inline (apenas pelo autor)
* Validação de comentários (mínimo e máximo de caracteres)
* Criação e edição de posts com CKEditor
* Upload de imagens em posts
* Tags e categorias para posts
* Interface responsiva e estilizada

---

## Roadmap

### Em desenvolvimento

* Integração visual completa do CKEditor
* Feedback visual usando Django messages
* Ordenação e filtragem de comentários
* Estilização completa da página de criação de posts

### Planejado

* Sistema de curtidas em posts e comentários
* Testes automatizados

---

## Como rodar localmente

1. Clone o repositório:
```git clone https://github.com/gok2001/projeto-blog```
```cd nome-do-projeto```

2. Crie e ative um ambiente virtual:
```python -m venv venv```
* Windows: ```venv/Scripts/activate```
* macOS/Linux: ```source venv/bin/activate```

3. Instale as dependências:
```pip install -r requirements.txt```

4. Rode as migrations:
```python manage.py migrate```

5. Crie um superuser:
```python manage.py createsuperuser```

6. Inicie o servidor:
```python manage.py runserver```

O projeto estará disponível em ```http://127.0.0.1:8000```

---

## Estrutura do projeto

* `posts/` - App principal com models, views, templates e forms
    * `templates/posts/` – Templates específicos dos posts
* `users` - App com models, views, templates e forms de usuário
    * `templates/users/` – Templates de login, registro e perfil
* `templates/global/` - Templates HTML globais
* `static/` - CSS e arquivos estáticos
* `db.sqlite3` - Banco de dados SQLite (padrão)

---

## Licença

Este projeto está licenciado sob a MIT License.
Veja o arquivo [LICENSE](./LICENSE) para mais detalhes.

---

## Autor

Guilherme Orige Kernbichler

---
