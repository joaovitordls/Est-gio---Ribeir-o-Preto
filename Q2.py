while True:
    palavra = input("Escreva uma palavra: ")
    letra = (palavra.count("a") + palavra.count("A") + palavra.count("ã") + palavra.count("Ã") + palavra.count("á") + palavra.count("Á") + palavra.count("à") + palavra.count("À") + palavra.count("â") + palavra.count("Â"))
    if letra == 0:
        print(f"A palavra '{palavra}' não contém a letra A")
    elif letra > 0 and letra == 1:
        print(f"A palavra '{palavra}' contém {letra} letra A")
    elif letra > 0 and letra > 1:
        print(f"A palavra '{palavra}' contém {letra} letras A")
