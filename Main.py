import requests


def consultar():

    print('#########################')
    print('######## Via Cep ########')
    print('#########################')
    print()

    cep = input('Digite o CEP: ')

    if len(cep) != 8:
        print('Quantidade de dígitos inválidos!')
        exit()

    url = 'http://viacep.com.br/ws/' + cep + '/json/'

    return requests.get(url=url)


repetir = '1'

while repetir == '1':

    resposta = consultar()

    response_data = resposta.json()

    if 'erro' not in response_data:

        print('CEP - ', response_data['cep'])
        print('Logradouro - ', response_data['logradouro'])
        print('Complemento - ', response_data['complemento'])
        print('Bairro - ', response_data['bairro'])
        print('Localidade - ', response_data['localidade'])
        print('UF - ', response_data['uf'])
        print('IBGE - ', response_data['ibge'])
        print('GIA - ', response_data['gia'])
        print('DDD - ', response_data['ddd'])
        print('SIAFI - ', response_data['siafi'])

    elif resposta.status_code == 400 or 'erro' in response_data:
        print('Número do CEP inválido')

    else:
        print(resposta.text)

    print()
    print('Gostaria de fazer mais alguma consulta: \n 1 - Sim \n 2 - Não')
    print()
    repetir = input()
    print()
