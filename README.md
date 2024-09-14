
# Finsearch - Informações Financeiras em Tempo Real

Este programa permite que você obtenha informações financeiras em tempo real, como a última cotação de ativos, o status do mercado e o preço mais recente de uma transação. Ele utiliza a API do [Finnhub](https://finnhub.io/) para buscar dados financeiros e usa WebSocket para atualização contínua.

## Requisitos

- Python 3.x
- Bibliotecas necessárias:
  - `finnhub-python`
  - `websocket-client`
  - `argparse`

Você pode instalar as dependências executando o seguinte comando:

```bash
pip install finnhub-python websocket-client argparse
```

## Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/seu-usuario/Finsearch
.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd Finsearch

    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

Execute o programa passando argumentos para obter informações financeiras em tempo real.

### Obter o preço mais recente de uma transação

```bash
python3 main.py --trade [SYMBOL]
```

### Obter o status do mercado (aberto/fechado)

```bash
python3 main.py --is_open [EXCHANGE]
```

### Obter a última cotação de um ativo

```bash
python3 main.py --quote [SYMBOL1 SYMBOL2 ...]
```

## Exemplo de Execução

### Cotação de um ativo

```bash
python3 main.py --quote AAPL MSFT
```

Saída:

```
######### Ultima cotação de AAPL ##############
Máxima: 175.64
Mínima: 172.32
Abertura: 174.20
Fechamento: 173.56

######### Ultima cotação de MSFT ##############
Máxima: 305.65
Mínima: 299.45
Abertura: 302.15
Fechamento: 300.81
```

### Verificar se o mercado está aberto

```bash
python3 main.py --is_open NYSE
```

Saída:

```
Bolsa: 'NYSE'
Aberto: 'True'
Feriado: 'False'
```

### Exibir o preço mais recente de uma transação via WebSocket

```bash
python3 main.py --trade BINANCE:BTCUSDT
```

A resposta será atualizada em tempo real:

```
Last price: 43000.45
Last price: 43001.12
```

## Funcionalidades

- **Obtenção de Cotações**: Retorna as informações da última cotação de um ativo, incluindo preço de abertura, preço máximo, preço mínimo e preço de fechamento.
- **Status do Mercado**: Retorna se o mercado está aberto ou fechado.
- **Preço Atual via WebSocket**: Recebe o preço mais recente de uma transação em tempo real utilizando WebSocket.

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.

## Contribuição

Contribuições são bem-vindas! Se você tiver melhorias ou correções a serem feitas, por favor, abra uma issue ou envie um pull request.
