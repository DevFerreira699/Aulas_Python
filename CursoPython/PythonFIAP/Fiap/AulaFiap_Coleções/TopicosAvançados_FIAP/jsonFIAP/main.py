import json

dic = {
    "Nome":"Ferreira",
    "Idade":23
}
conteudo = json.dumps(dic, ensure_ascii=False, indent=4)
with open("arquivo.json", mode="w", encoding="UTF-8") as arquivo:
    arquivo.write(conteudo)