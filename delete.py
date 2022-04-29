import os

def deletaArquivo(name):
    try:
        if name == 'delete.py' or name == 'post.py' or name == 'post.py' or name == 'put.py' or name == 'servidor.py':
            return "HTTP/1.1 500 Arquivo nao pode ser deletado\n\n"
        if os.path.exists(name):
            os.remove(name)
            return "HTTP/1.1 200 Arquivo deletado\n\n"
        else:
            return "HTTP/1.1 404 Arquivo não encontrado\n\n"
    except:
        return "HTTP/1.1 500 ERRO AO ADICIONAR NO ARQUIVO\n\n"