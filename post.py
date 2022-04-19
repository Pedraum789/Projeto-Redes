import pandas as pd

def alteraLinha(id, nome, valor):
    try:
        data = {
            "id": [id], 
            "nome": [nome], 
            "valor":[valor]
        }
        df = pd.DataFrame(data)
        df.to_csv("produtos.csv", mode="a", index=False, header=False,line_terminator='\n')
    except:
      return  print("Arquivo fora do padrao ou desconhecido")
    