import os

def alteraLinha(name, content):
    try:
        if os.path.exists(name):
            with open(name, 'a') as f:
                f.seek(0)
                f.write(content)
                return "HTTP/1.1 200 OK\n\n"
        else:
            return "HTTP/1.1 404 Arquivo não encontrado\n\n"
    except:
        return "HTTP/1.1 500 ERRO AO ADICIONAR NO ARQUIVO\n\n"
    