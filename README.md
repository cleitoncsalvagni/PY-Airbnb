# Projeto de Sistema Distribuído com Flask

Este projeto é um sistema distribuído desenvolvido em Python utilizando o framework Flask. Ele consiste em replicar uma
pasta em várias instâncias, cada uma executando um servidor Flask em uma porta diferente. Cada instância do servidor
possui um arquivo de vizinhos, que contém informações sobre os servidores vizinhos com os quais ele se comunica.

## Estrutura de Pastas

O projeto possui a seguinte estrutura de pastas:

- **/server.py**: Este é o arquivo principal do servidor Flask. Ele contém as rotas e a lógica de busca no servidor. O
  arquivo `vizinhos.json` é carregado para obter as informações sobre os vizinhos do servidor atual.

- **/utils/serialize.py**: Este arquivo contém funções de serialização personalizadas para tornar os objetos
  serializáveis em JSON. Ele é utilizado para serializar as respostas JSON do servidor.

- **/models/busca_no_servidor.py**: Este arquivo contém a lógica de busca do servidor. Ele se conecta ao banco de dados
  MongoDB e realiza a busca por um ID fornecido. Caso o ID não seja encontrado localmente, o servidor consulta seus
  vizinhos para procurar o ID nos servidores vizinhos.

- **vizinhos.json**: Este arquivo contém as informações sobre o servidor atual e seus vizinhos. Ele é alterado de
  acordo com o grafo que o usuário deseja criar, especificando os IDs, portas, URI do MongoDB e nome do banco de dados
  de cada servidor e seus vizinhos.

## Roteamento e Funcionalidades

O servidor Flask possui as seguintes rotas e funcionalidades:

- **GET /buscar/**<br>
  Rota principal do servidor que retorna um erro quando o ID não é fornecido.

- **GET /buscar/<id>**<br>
  Rota que realiza a busca por um ID fornecido. O ID é passado como um parâmetro na URL. Se o ID for encontrado no
  servidor local, ele é retornado como resposta JSON. Caso contrário, o servidor consulta seus vizinhos para procurar o
  ID nos servidores vizinhos. O parâmetro `visited` pode ser fornecido opcionalmente para rastrear os servidores
  visitados durante a busca.

## Erros e Retornos

O servidor Flask retorna as seguintes respostas e erros:

- **200 OK**: Quando a busca é realizada com sucesso e o ID é encontrado no servidor local ou em um dos servidores
  vizinhos.

- **400 Bad Request**: Quando o ID não é fornecido na rota.

- **404 Not Found**: Quando o ID não é encontrado em nenhum dos servidores.

- **500 Internal Server Error**: Quando ocorre um erro interno no servidor durante a busca ou ao consultar um servidor
  vizinho.

## Alterações nos servidores

No arquivo `server.py` de cada pasta, você pode alterar a porta do servidor e o arquivo de vizinhos que ele vai buscar.

```pycon
# Importações

with open('vizinhos1.json') as json_file:
    server = json.load(json_file)
    
# Restante do código

if __name__ == "__main__":
    app.run(port=5001)

```

## Instalando dependências:

```sh
    python -m pip install flask
    python -m pip install pymongo
    python -m pip install requests
```

## Iniciando os Servidores

#### Ambiente Windows:

- Para iniciar os servidores, é possível utilizar o arquivo `start.bash`. Certifique-se de estar na pasta raiz onde
  todas
  as pastas replicadas estão localizadas, ele vai acessar todos as pastas `server/` e iniciar o server.py.
  **Observação**: Não pode ser
  executado em modo administrador, pois ele vai buscar os servidores no System32

No entanto, é importante mencionar que o arquivo `start.bash` pode não ser compatível com outros sistemas operacionais.
Nesse caso, será necessário iniciar cada servidor manualmente executando o arquivo `server.py` em cada pasta replicada.
Pode ser feito utilizando:

```sh
python server.py
```

## Testando a API

É importante ressaltar que o funcionamento correto do projeto depende da configuração adequada dos servidores e dos
arquivos de vizinhos. Certifique-se de que todas as informações necessárias, como portas, URI do MongoDB e nome do banco
de dados, estejam configuradas corretamente em cada servidor e arquivo de vizinhos.