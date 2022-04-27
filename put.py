def createFile(name, content):
    try:
        with open(name, 'w') as f:
            f.write(content)
            return "HTTP/1.1 201 OK\n\n"
    except:
        return "HTTP/1.1 500 ERRO AO CRIAR O ARQUIVO\n\n"