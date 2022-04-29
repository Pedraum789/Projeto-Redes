def createFile(name, content):
    try:
        if name == 'delete.py' or name == 'post.py' or name == 'post.py' or name == 'put.py' or name == 'servidor.py':
            return "HTTP/1.1 500 Arquivo nao pode ser recriado\n\n"
        if(content == ''):
            with open(name, 'w') as f:
                f.write(content)
            return "HTTP/1.1 204 Arquivo criado ou substituido\n\n"
        with open(name, 'w') as f:
            f.write(content)
            return "HTTP/1.1 201 Arquivo criado ou substituido\n\n"
    except:
        return "HTTP/1.1 500 Erro ao criar o arquivo\n\n"