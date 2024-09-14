import finnhub.client
import websocket
import argparse
import sys
import finnhub
import json

parser = argparse.ArgumentParser(description="Retorna informações sobre ativos e o mercado financeiro em tempo real\n"
                                              "Forma de uso: python3 main.py -a Ativo")
parser.add_argument('--trade',metavar='t',help='Retonar o valor da ultima transção do ativo selecionado'
                                                        'Usage: main.py --trade [symbol]')
parser.add_argument('--is_open',required=False,metavar='io',help='Retorna o status do mercado' 
                                                                    'Usage: main.py --is_open [Market]')
parser.add_argument('--quote',nargs='+',metavar='q',help='Retornar a ultima cotação de um determinado ativo' 
                                                'Usage: main.py --quote [symbols] ')
args = parser.parse_args()


def Quote(symbol):
    for i in symbol:
        data = finnhub_client.quote(i)
        print(f"#########Ultima cotação de {i}##############")
        print(f"Máxima: {data.get('h',0)}")
        print(f"Mínima: {data.get('l',0)}")
        print(f"Abertura: {data.get('o',0)}")
        print(f"Fechamento: {data.get('pc',0)}")


def marketSatus():
        data = finnhub_client.market_status(exchange=args.is_open)
        print(f"Bolsa: '{data.get('exchange',0)}'")
        print(f"Aberto: '{data.get('isOpne',0)}'")
        print(f"Feriado: '{data.get('holiday',0)}'")

def on_message(ws, message):
    try:
        # Converter a string em JSON(POR QUE POR ALGUM MOTIVO A API RETORNA UMA STRING)
        message_json = json.loads(message)
    except json.JSONDecodeError:
        print(f"Falha ao decodificar mensagem: {message}")
    print(f"Last price:'{message_json['data'][0]['p']}'")

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws,symbol):
    ws.send('{"type":"subscribe","symbol":"{symbol}"}')

if __name__ == "__main__":
    finnhub_client = finnhub.Client(api_key='criduihr01qqt33roaggcriduihr01qqt33roah0')
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=criduihr01qqt33roaggcriduihr01qqt33roah0",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    if args.is_open:
        marketSatus()
    if args.quote:
        Quote(args.quote)
    if args.trade:
        ws.on_open = on_open(args.trade)
        ws.run_forever()
    ws.on_close = on_close



