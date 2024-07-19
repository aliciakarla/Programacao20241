def ContaVogais(texto):
    Vogais = ['a', 'e', 'i', 'o', 'u']
    Contagem = {}
    
    for Vogal in Vogais:
        Contagem[Vogal] = texto.count(Vogal)     
    return Contagem
