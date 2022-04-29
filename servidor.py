import socket
import json
import post
import put
import delete
#from post import alteraLinha

REQUESTS = {
    "GET": "/index.html", 
    "POST": "/post.html", 
    "PUT": "/put.html", 
    "DELETE": "/delete.html"
    }

PORT = ""
SERVERPORT = 8080

#cria o socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#atribuir o socket a uma porta especifica
serverSocket.bind((PORT, SERVERPORT))

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
            print("Entrou no metodo GET")
            if split_request[1] == '/' or split_request[1] == REQUESTS['GET']:
                print("Entrou no metodo GET /")
                fin = open("web" + REQUESTS['GET'])
                content = fin.read()
                fin.close()
                response = "HTTP/1.1 200 OK\n\n" + content
            elif split_request[1] == REQUESTS['POST'] or (split_request[1].find(REQUESTS['POST']) != -1 and split_request[1].find('?name=') != -1):
                print("Entrou no metodo GET /post.html")
                fin = open("web" + REQUESTS['POST'])
                content = fin.read()
                fin.close()
                response = "HTTP/1.1 200 OK\n\n" + content
            elif split_request[1] == REQUESTS['PUT']:
                print("Entrou no metodo GET /put.html")
                fin = open("web" + REQUESTS['PUT'])
                content = fin.read()
                fin.close()
                response = "HTTP/1.1 200 OK\n\n" + content
            elif split_request[1] == REQUESTS['DELETE'] or (split_request[1].find(REQUESTS['DELETE']) != -1 and split_request[1].find('?name=') != -1):
                print("Entrou no metodo GET /delete.html")
                fin = open("web" + REQUESTS['DELETE'])
                content = fin.read()
                fin.close()
                response = "HTTP/1.1 200 OK\n\n" + content
            else:
                print("Pagina nao mapeada")
                response = "HTTP/1.1 404 Pagina nao encontrada\n\n" + content

        elif split_request[0] == 'POST':
            print("Executando metodo POST...")
            body = request.split('\r\n\r\n')
            if( len(body) > 1 ):
                print("Body ACEITO!")
                try:
                    body = json.loads(body[1])
                    response = post.alteraLinha(body['name'], body['content'])
                except:
                    response = "HTTP/1.1 406 Nao foi aceito o tamanho do arquivo\n\n"
            else:
                print("Body NAO ACEITO!")
                response = "HTTP/1.1 404 Nao foi encontrato o arquivo\n\n" + content
            
        elif split_request[0] == 'PUT':
            print("Executando metodo PUT...")
            body = request.split('\r\n\r\n')
            if(len(body) > 1):
                print("Body ACEITO!")
                try:
                    body = json.loads(body[1])
                    response = put.createFile(body['name'], body['content'])
                except:
                    response = "HTTP/1.1 406 Nao foi aceito o tamanho do arquivo\n\n"
            else:
                print("Body NAO ACEITO!")
                response = "HTTP/1.1 404 Arquivo nao encontrado\n\n" + content
                
        elif split_request[0] == 'DELETE':
            print("Executando metodo DELETE...")
            body = request.split('\r\n\r\n')
            if(len(body) > 1):
                print("Body ACEITO!")
                try:
                    body = json.loads(body[1])
                    response = delete.deletaArquivo(body['name'])
                except:
                    response = "HTTP/1.1 500 Erro ao deletar arquivo\n\n"
            else:
                print("Body NAO ACEITO!")
                response = "HTTP/1.1 404 Nao foi encontrato o arquivo\n\n" + content
        else:
            print("Comando não pode ser interpretado por esse servidor!")
            response = ("ERRO! Servidor não reconhece esse comando!").encode()
            connectionSocket.send(response)
        connectionSocket.sendall(response.encode())

        connectionSocket.close()

    except:
        pass