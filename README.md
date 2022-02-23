# Local Chat Socket Application

Projeto desenvolvido para a disciplina de Redes de Computadores - 2021.1, no Instituto de Computação da Universidade de Alagoas (IC/UFAL). Este README busca descrever o trabalho de forma mais técnica e voltada para o desenvolvimento. Para mais detalhes e informações, acessar o arquivo ``relatorio.pdf``  na raiz do repositório.

#### Professor
- Leandro Melo de Sales

#### Alunos 
- Bruno Lemos de Lima
- José Ferreira Leite Neto

## Sumário

Clique nos links abaixo para acessar rapidamente a seção desejada:

- [Sobre](#sobre)
- [Principais Funcionalidades](#principais-funcionalidades)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Dependências](#dependências)
- [Como executar](#como-executar)

## Sobre
O projeto, desenvolvido utilizando a linguagem Python, permite que diversos usuários troquem mensagens em sua rede local, no formato de salas de chat intermediadas por um servidor. Os usuários definem usernames (nomes de usuário ou apelidos) e podem criar e entrar nos ambientes de bate-papo conforme desejarem.

## Principais Funcionalidades

- **Definição de username**
    Assim que o usuário se conecta, é solicitado que defina um nome de usuário (com no mínimo três carateres) para identificá-lo no servidor (indicando a origem das mensagens para os outros usuários).

- **Criar uma sala**
    Após definido o username, o usuário pode escolher entre criar uma sala ou entrar em uma já existente. Caso opte pela primeira opção, deverá fornecer um nome para a sala (com no mínimo três caracteres) e esta será criada e ficará disponível para outros usuários.

- **Entrar em uma sala**
    Já no caso de o usuário optar por entrar em uma sala já existente, ele deverá informar o nome da sala em que deseja entrar, de forma que o servidor faz a verificação e, se a sala existir, conecta o usuário que fez a solicitação e anuncia sua entrada.

- **Enviar e receber mensagens**
    Uma vez conectado a uma sala, o usuário pode enviar mensagens e receber as mensagens enviadas por outros usuários a partir de sua entrada, podendo se desconectar a qualquer momento pressionando ``CTRL + C``, além de rolar as mensagens pressionando ``Page Up`` e ``Page Down``.

## Estrutura do Projeto

O projeto está estruturado da seguinte forma:

```
Socket
│   LICENSE
│   README.md
│   requirements.txt
│   relatorio.pdf
└───src
│   └───client
│       │   chat.py
│       │   client.py
│       │   room.py
│   └───server
│       │   room.py
│       │   server.py
│   └───utils
│       │   utils.py
```

- Na raiz do projeto, podem ser encontrados: ``LICENSE`` (licença padrão MIT), ``README.md`` (este README), ``requirements.txt``, com as bibliotecas necessárias para executar o projeto e ``relatorio.pdf``, um arquivo PDF contendo um relatório sobre a execução do projeto.
- Na pasta ``client`` ficam os arquivos responsáveis pelo funcionamento da aplicação no lado cliente, incluindo ``chat.py``, que implementa a interface gráfica (no console) do chat com o usuário e suas funcionalidades, como o envio e recebimento de mensagens, ``client.py``, com o código de conexão, exibição do menu, definição de username e outros e ``room.py`` que traz as funções do cliente para criação de salas, entrada nas salas, conexão, entre outros.
- Já na pasta ``server``, de maneira análoga, se encontram os arquivos responsáveis pelo funcionamento da aplicação no lado servidor, incluindo ``room.py``, que implementa a lógica de funcionamento das salas no lado servidor (funções como criar a sala, conectar, enviar e receber mensagens, sair da sala) e ``server.py``, com o código de criação do servidor, gerenciamento de conexões e threads, conexão e desconexão de clientes, exibição de logs e outros.
- Por fim, temos a pasta ``utils``, que abriga apenas o arquivo ``utils.py``, onde estão funções úteis para os demais módulos da aplicação, como tratamento de argumentos na execução dos arquivos (IP e porta) e limpar o console independentemente do sistema operacional.

## Dependências

O projeto foi totalmente desenvolvido utilizando Python, então se faz necessário ter uma versão atualizada do mesmo instalada. Também foram utilizadas duas bibliotecas para facilitar a implementação de algumas funcionalidades (necessário realizar a instalação através do arquivo ``requirements.txt``), que estão listadas abaixo:

| Biblioteca | Informações | Uso no Projeto |
| ------ | ------ | ------ |
| console-menu | [Github](https://github.com/aegirhall/console-menu) | Utilizada para implementar o menu |
| prompt-toolkit | [Github](https://github.com/prompt-toolkit/python-prompt-toolkit) | Utilizada para implementar a interface de chat |

## Como executar

Para executar o projeto, além do Python instalado, é necessário abrir tanto a aplicação servidor quanto a cliente (podendo abrir quantos clientes desejar para testar a funcionalidade de chat). A execução se dá no terminal (console) e segue os passos descritos abaixo. Para todos os casos, os comandos são executados a partir da raiz do projeto.

### Primeira execução

Ao executar o projeto pela primeira vez, faz-se necessário instalar as dependências presentes no arquivo ``requirements.txt``. Para isso, basta executar o comando abaixo:

```
    $ pip install -r requirements.txt
```

Na sequência, execute os comandos da seção a seguir.

### Demais execuções

Será necessário utilizar um terminal para executar o código do servidor e quantos desejar para serem os clientes. É importante que o servidor seja executado primeiro, utilizando os comandos da seção [Servidor](#servidor)

#### Servidor

Para executar o servidor, abra o terminal na raiz do projeto e execute os comandos:

```
    $ cd src/server
    $ python server.py
```

O servidor será executado e ficará disponível para conexões. É possível passar parâmetros para indicar o IP e porta em que o servidor deve funcionar, bastando informar como no exemplo:

```bash
    $ python server.py 192.168.0.1 1000
```

Caso os parâmetros não sejam informados, o servidor será executado por padrão no IP 127.0.0.1, porta 443.

#### Clientes

Para executar um cliente, abra o terminal na raiz do projeto e execute os comandos:

```
    $ cd src/client
    $ python client.py
```

O cliente será executado e se conectará ao servidor (que deve estar em execução). É possível passar parâmetros para indicar o IP e porta em que o cliente deve se conectar, bastando informar como no exemplo:

```bash
    $ python client.py 192.168.0.1 1000
```

Caso os parâmetros não sejam informados, o cliente conectará por padrão no IP 127.0.0.1, porta 443. 

Ao executar o cliente, será exibido um menu e as demais instruções de excução serão fornecidas. Repetir os passos conforme a quantidade de clientes que deseja executar.
