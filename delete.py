import os

def deletaArquivo(name):
    try:
        if os.path.exists(name):
            os.remove(name)
            return "HTTP/1.1 200 OK\n\n"
        else:
            return "HTTP/1.1 404 Arquivo não encontrado\n\n"
    except:
        return print("Arquivo nao encontrdo!")