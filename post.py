
def alteraLinha(name, content):
    try:
        with open(name, 'a') as f:
            f.seek(0)
            f.write(content)
            return "HTTP/1.1 200 OK\n\n"
    except:
        return "HTTP/1.1 500 ERRO AO ADICIONAR NO ARQUIVO\n\n"
    