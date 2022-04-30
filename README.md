# Projeto-Redes
Projeto desenvolvido por:
* Pedro Henrique Guilherme Sanchez 22120069-4
* Pedro Henrique Braga  22.120.064-5
* Gustavo Velecico 22.120.044-7


# Metodo GET

| URL | DESCRICAO |
| ------------------- | ------------------- |
| http://localhost:8080/index.html ou http://localhost:8080 | Recebe a pagina HTML principal com os links para os metodos **POST**, **PUT** e **DELETE** |
| http://localhost:8080/post.html | Pagina HTML de execucao do metodo **POST** |
| http://localhost:8080/put.html | Pagina HTML de execucao do metodo **PUT** |
| http://localhost:8080/delete.html | Pagina HTML de execucao do metodo **DELETE** |

***
### *O usuario deve escolher uma das requisicoes desejadas.*

![image](https://user-images.githubusercontent.com/35739467/166007716-2fd5831d-a93e-460d-ad40-8e93441e8c74.png)
***

#### *Caso tenha feito a request corretamente*
```200 OK```

#### *Caso nao seja nenhuma dessas paginas*
```404 Pagina nao encontrada```

# Metodo PUT

| URL | BODY | DESCRICAO |
| ------------------- | ------------------- | ------------------- |
| http://localhost:8080 | ```Anexar um arquivo``` | Cria/substitui o arquivo que foi anexado (**PASTA DO PROJETO**) |

***
### *O usuario deve escolher um arquivo e enviar para a criacao/substituicao.*

![image](https://user-images.githubusercontent.com/35739467/166008090-9d1ff220-122e-4a41-acbf-3f71e7808706.png)
***

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

# Metodo POST

| URL | BODY | DESCRICAO |
| ------------------- | ------------------- | ------------------- |
| http://localhost:8080 | ```"{name: "teste.txt", content: "teste"}"``` | Adicionada no arquivo (name) o conteudo (content) (**PASTA DO PROJETO**) |

***
### *O usuario de digitar o nome do arquivo desejado e o conteudo que deseja adicionar naquele arquivo.*

![image](https://user-images.githubusercontent.com/35739467/166008007-549705fa-c6b4-41f3-9ea7-e11c4dd94a7c.png)
***

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


# Metodo DELETE

| URL | BODY | DESCRICAO |
| ------------------- | ------------------- | ------------------- |
| http://localhost:8080 | ```"{name: "teste.txt"}"``` | Deleta o arquivo pelo nome (name) (**PASTA DO PROJETO**) |

***
### *O usuario deve digitar o nome do arquivo a ser deletado.*

![image](https://user-images.githubusercontent.com/35739467/166008119-217eb7ca-7b34-4512-8564-1e6fc5d9923e.png)
***

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

