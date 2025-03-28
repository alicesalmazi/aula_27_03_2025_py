def validador(mensagem):
    while True:
        try:
            value = str(input(mensagem))
            if value == value:
                return value
        except ValueError:
            print("Digite um valor válido!")

def descobrirPalavra(number):
    keys = {
        'a': 6,
        'b': 1,
        'd': 7,
        'e': 4,
        'i': 3,
        'l': 2,
        'm': 9,
        'n': 8,
        'o': 0,
        't': 5
    }

    word = ""
    for digito in str(number):
        for key in keys:
            if keys[key] == int(digito):
                word += key


number = validador("Digite um número: ")
descobrirPalavra(number)
