def InverteDicionario(Dic):
    Inverso = {}
    for Chave, Valor in Dic.items():
        if Valor not in Inverso:
            Inverso[Valor] = []
        Inverso[Valor].append(Chave)
    return Inverso

Dic = { "a": 1, "b": 3, "c": 1, "d": 5 }
print(InverteDicionario(Dic))
