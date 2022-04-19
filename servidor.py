import socket
import json
import post
import put
#from post import alteraLinha

REQUESTS = {
    "GET": "/index.html", 
    "POST": "/post.html", 
    "PUT": "/put.html", 
    "DELETE": "/post.html"
    }

SEPARADOR = ';'

message=''
serverPort = 8080

#cria o socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#atribuir o socket a uma porta especifica
serverSocket.bind(("", serverPort))

#inicia o "listening"
serverSocket.listen(1)

print("Servidor HTTP/1.1 Inicializado")

while True:
    connectionSocket, addr = serverSocket.accept()
    print("Cliente {} conectado ao servidor".format(addr))
    request = connectionSocket.recv(1024).decode()

    split_request = request.split()
    try:
        if split_request[0] == 'GET':
            
            if split_request[1] == '/' or split_request[1] == REQUESTS['GET']:
                fin = open("web" + REQUESTS['GET'])
                content = fin.read()
                fin.close()
                response = "HTTP/1.1 200 OK\n\n" + content
            elif split_request[1] == REQUESTS['POST']:
                fin = open("web" + REQUESTS['POST'])
                content = fin.read()
                fin.close()
                response = "HTTP/1.1 200 OK\n\n" + content
            elif split_request[1] == REQUESTS['PUT']:
                fin = open("web" + REQUESTS['PUT'])
                content = fin.read()
                fin.close()
                response = "HTTP/1.1 200 OK\n\n" + content
            elif split_request[1] == REQUESTS['DELETE']:
                fin = open("web" + REQUESTS['DELETE'])
                content = fin.read()
                fin.close()
                response = "HTTP/1.1 200 OK\n\n" + content
                

        elif split_request[0] == 'POST':
            body = request.split('\r\n\r\n')
            if( len(body) > 1 ):
                json = json.loads(body[1])
                post.alteraLinha(json['id'], json['name'], json['valor'])
                
            response = "HTTP/1.1 200 OK\n\n" + content
            
        elif split_request[0] == 'PUT':
            body = request.split('\r\n\r\n')
            if( len(body) > 1 ):
                id = []
                nome = []
                valor = []
                linhas = body[1].split('\n')[1:]
                for linha in linhas:
                    if(len(linha.split(SEPARADOR)) > 1):
                        id.append(linha.split(SEPARADOR)[0])
                        nome.append(linha.split(SEPARADOR)[1])
                        valor.append(linha.split(SEPARADOR)[2])
                put.createFile(id, nome, valor)
            
            response = "HTTP/1.1 200 OK\n\n" + content
        elif split_request[0] == 'DELETE':
            
            response = "HTTP/1.1 200 OK\n\n" + content
            #delete.deletaArquivo()
        else:
            print("Comando não pode ser interpretado por esse servidor!")
            response = ("ERRO! Servidor não reconhece esse comando!").encode()
            connectionSocket.send(response)
        connectionSocket.sendall(response.encode())

        connectionSocket.close()

    except:
        pass