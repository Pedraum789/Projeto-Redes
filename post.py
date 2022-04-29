import os

def alteraLinha(name, content):
    try:
        if name == 'delete.py' or name == 'post.py' or name == 'post.py' or name == 'put.py' or name == 'servidor.py':
            return "HTTP/1.1 500 Arquivo nao pode ser editado\n\n"
        elif os.path.exists(name):
            with open(name, 'a') as f:
                f.seek(0)
                f.write(content)
                return "HTTP/1.1 200 Arquivo alterado\n\n"
        else:
            return "HTTP/1.1 404 Arquivo não encontrado\n\n"
    except:
        return "HTTP/1.1 500 Erro ao editar o arquivo\n\n"
    