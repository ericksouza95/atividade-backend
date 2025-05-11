## Como executar

- Use os comandos `py -3 -m venv .venv`, `.venv\Scripts\activate`, `pip install Flask`
- Logo após `flask run`


## Paginas

* index
    * Faz o login se o sistema reconhecer algum dos usuarios no arquivo "users.json"
    * Retorna "Usuário ou senha inválidos!" e volta a tela de login, caso as credenciais sejam invalidas.

* home
    * Lista opções de ver lista de musica, sair e uma mensagem de bem vindo ao usuario.


* musicas
    * Tem a opção de adicionar, remover e buscar musicas


## Requisições GET

- Acessar a página de login (`/`)
- Mostrar o formulário de login
- Buscar músicas com parâmetro `?search=` na URL
- Exibir a lista de músicas

## Requisições POST

- Enviar dados do formulário de login
- Adicionar ou remover músicas a partir de um formulário


## Armazenamento

- Os usuarios e as musicas são armazenados em json