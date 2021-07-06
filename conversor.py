import requests

def converso():
    req = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL')
    json = req.json()
    print("Preços das moedas:\n")

    for k in json:
        print(json[k]["name"],"\n",json[k]["high"]) 

          
   