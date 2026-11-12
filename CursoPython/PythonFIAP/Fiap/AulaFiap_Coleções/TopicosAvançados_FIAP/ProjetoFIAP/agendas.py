#Tupla que contem os contatos suportados
contatos_suportados = ("telefone", "email", "endereço")

#Dicionario de exemplo
agenda = {
    "Pessoa 1":{
        "telefone":["11 1234-5678"],
        "email":["oi@gmail.com"],
        "endereço":["Rua 123"]
    },
    "Pessoa 2":{
        "telefone":["11 9876-9876"],
        "email":["ola@gmail.com"],
        "endereço":["Rua bbb"]
    }
}

def contato_para_texto(nome_contato:str, **formas_contatos):
    """Recebe um nome de contato com string e um dicionario
    com as formas de contato.
    Retorna uma string com os dados recebidos"""
    formato_texto = f"{nome_contato}"
    for meio_contato, contato in formas_contatos.items():
        formato_texto = f"{formato_texto}\n{meio_contato.upper()}"
        contador_formas = 1
        for valor in contato:
            formato_texto = f"{formato_texto}\n\t{contador_formas}"
            contador_formas = contador_formas + 1
            
    return formato_texto

#FUNÇÃO DE VISUALIZAÇÃO DA AGENDA COMPLETA
def agenda_para_texto(**agenda_completa):
    """Recebe um dicionario de dicionarios com a agenda qu3e será exibida
    e
    retorna uma string com este dicionario formatado"""
    formato_texto = ""
    for nome_contato, formas_contato in agenda_completa.items():
        formato_texto = f"{formato_texto} {contato_para_texto(nome_contato, **formas_contato)}\n"
        formato_texto = f"{formato_texto}-----------------\n"
    return formato_texto