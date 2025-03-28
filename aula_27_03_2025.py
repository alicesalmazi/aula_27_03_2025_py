#Tacos: monte o seu!!
def entrada(mensagem):
    while True:
        try: 
            valor = str(input(mensagem))
            if valor == valor:
                return valor
        except ValueError:
            print("Digite um valor válido!")

def montarTaco(palavra):
    ingredientes = {
        'a':'beef', 
        'e':'beef', 
        'i':'beef', 
        'o':'beef', 
        'u':'beef', 
        'l':'lettuce', 
        't':'tomate', 
        'c':'cheese', 
        'g':'guacamole',
        's':'salsa'
    }

    taco = ['shell']
    for letra in palavra.lower():
        if letra in ingredientes:
            taco.append(ingredientes[letra])
        
    taco.append('shell')
    if taco == ['shell', 'shell']:
        print(f"Que taco seco Sr(a)! Taco: {taco}")
    else:
        print(f"Sr(a), seu taco: {taco}")

palavra = entrada("Monte seu taco: ")
montarTaco(palavra)