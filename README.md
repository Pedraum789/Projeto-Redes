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

#### *Caso tenha feito a request corretamente*
```200 OK```

#### *Caso nao seja nenhuma dessas paginas*
```404 Pagina nao encontrada```

## Metodo PUT
| URL | BODY | DESCRICAO |
| ------------------- | ------------------- | ------------------- |
| http://localhost:8080 | ```Anexar um arquivo``` | Cria o arquivo que foi anexado na requisicao ou caso ja tenha sido criado sera substituido |

#### *Caso tenha feito a request corretamente*
```201 Arquivo criado ou substituido```

#### *Caso tenha feito a request corretamente, mas o arquivo anexado esta vazio*
```204 Arquivo criado ou substituido```

#### *Caso o arquivo nao for enviado*
```404 Arquivo nao encontrado```

#### *Caso o arquivo anexado seja muito grande*
```406 Nao foi aceito o tamanho do arquivo```

#### *Caso o arquivo anexado seja um dos arquivos do projeto*
```500 Arquivo nao pode ser recriado```

#### *Caso ocorra algum erro*
```500 Erro ao criar/substituir o arquivo```

## Metodo POST
| URL | BODY | DESCRICAO |
| ------------------- | ------------------- | ------------------- |
| http://localhost:8080 | ```"{name: "teste.txt", content: "teste"}"``` | Adicionada no arquivo (name) o conteudo (content) |

#### *Caso tenha feito a request corretamente*
```200 Arquivo alterado```

#### *Caso o arquivo requisitado nao exista*
```404 Arquivo não encontrado```

#### *Caso o conteudo seja muito grande*
```406 Nao foi aceito o tamanho do arquivo```

#### *Caso o arquivo anexado seja um dos arquivos do projeto*
```500 Arquivo nao pode ser editado```

#### *Caso ocorra algum erro*
```500 Erro ao editar o arquivo```


## Metodo DELETE
| URL | BODY | DESCRICAO |
| ------------------- | ------------------- | ------------------- |
| http://localhost:8080 | ```"{name: "teste.txt"}"``` | Deleta o arquivo pelo nome (name) |

#### *Caso tenha feito a request corretamente*
```200 Arquivo deletado```

#### *Caso o arquivo requisitado nao exista ou nao envie um nome*
```404 Arquivo não encontrado```

#### *Caso o conteudo seja muito grande*
```406 Nao foi aceito o tamanho do arquivo```

#### *Caso o arquivo anexado seja um dos arquivos do projeto*
```500 Arquivo nao pode ser deletado```

#### *Caso ocorra algum erro*
```500 Erro ao deletar arquivo```

