import requests
from acesso_cep import BuscaEndereco

cep = input("Insira o CEP: ")
objeto_cep = BuscaEndereco(cep)  #instancia  o objeto
print(objeto_cep)

# r = requests.get("https://viacep.com.br/ws/01001000/json/")
# print(r.text)

logradouro, bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(logradouro, bairro, cidade, uf)    #printa o endereço formatadinho ;)

