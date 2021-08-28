import requests

class BuscaEndereco:


    def __init__(self, cep):
        cep = str(cep)
        if self.cep_e_valido(cep):  #inicializa e valida
            self.cep = cep
        else:
            raise ValueError ("CEP inválido!!")
 
    def __str__(self):
        return self.format_cep()  #transforma em str

    def cep_e_valido(self, cep):
        if len(cep) == 8:
            return True         #valida
        else:
            return False

    def format_cep(self):
        return f"{self.cep[:5]}-{self.cep[5:]}"   #formata no estilo "99999-999"

    def acessa_via_cep(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        r = requests.get(url)
        dados = r.json()                                           #acessa a API
        return (
           dados["logradouro"],
           dados["bairro"],
           dados["localidade"],
           dados["uf"]
       )
