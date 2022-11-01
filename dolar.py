#  pip install requests

import requests

#  Link público com valor atual da cotação do dólar
url = 'https://economia.awesomeapi.com.br/all/USD-COP'

#  Busca de dados
response = requests.get(url)

#  Se a busca funcionou mostra o valor
if response.status_code == 200:
    dolar_value = response.json()['USD']['low']
    print(f'O valor do Dólar é {dolar_value} COP')
else:
    print('Erro ao buscar valor do Dolar')
