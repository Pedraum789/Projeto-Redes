# Projeto-Redes
Projeto desenvolvido por:
* Pedro Henrique Guilherme Sanchez 22120069-2
* Pedro Henrique Braga
* Gustavo Velecico


## Metodo GET
| URL | BODY | DESCRICAO |
| ------------------- | ------------------- | ------------------- |
| http://localhost:8080/index.html | - | Recebe a pagina HTML principal com os links para os metodos **POST**, **PUT** e **DELETE** |
| http://localhost:8080/post.html | - | Pagina HTML de execucao do metodo **POST** |
| http://localhost:8080/put.html | - | Pagina HTML de execucao do metodo **PUT** |
| http://localhost:8080/delete.html | - | Pagina HTML de execucao do metodo **DELETE** |

## Metodo PUT
| URL | BODY | DESCRICAO |
| ------------------- | ------------------- | ------------------- |
| http://localhost:8080 | ```Anexar um arquivo``` | Cria o arquivo que foi anexado na requisicao ou caso ja tenha sido criado sera substituido |

## Metodo POST
| URL | BODY | DESCRICAO |
| ------------------- | ------------------- | ------------------- |
| http://localhost:8080 | ```"{name: "teste.txt", content: "teste"}"``` | Adicionada no arquivo (name) o conteudo (content) |

## Metodo DELETE
| URL | BODY | DESCRICAO |
| ------------------- | ------------------- | ------------------- |
| http://localhost:8080 | ```"{name: "teste.txt"}"``` | Deleta o arquivo pelo nome (name) |
