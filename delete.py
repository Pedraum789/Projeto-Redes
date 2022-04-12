import os

def deletaArquivo():
    try:
        path = "C:\Projeto-Redes"
        dir = os.listdir(path)
        for file in dir:
            if file == "produtos.csv":
                os.remove(file)
    except:
        return print("Arquivo nao encontrdo!")