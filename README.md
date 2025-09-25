# Blog Pessoal em Django

Um projeto pessoal criado para aprendizado com Django, onde somente o admin pode criar posts e usuários podem comentar.

## Tecnologias usadas

* Python 3.13
* Django 5.2
* SQLite (por enquanto, banco padrão)

## Como rodar localmente

* Passos básicos:
    * Clonar repositório
    * Criar ambiente virtual
    * Instalar dependências (```pip install -r requirements.txt```)
    * Rodar migrations (```python manage.py migrate```)
    * Criar superuser (```python manage.py createsuperuser```)
    * Subir servidor (```python manage.py runserver```)

## Funcionalidades implementadas até agora

* Listagem de posts
* Detalhe de post
* Criação de posts (somente admin)
* Registro de usuário
* Comentários associados a posts

## O que está por vir (roadmap)

* Melhorar sistema de comentários (ex:edição/remoção)
* Autenticação com login/logout
* Interface mais elaborada
* Testes automatizados

## Licença

Este projeto está licenciado sob a MIT License.  
Veja o arquivo [LICENSE](./LICENSE) para mais detalhes.