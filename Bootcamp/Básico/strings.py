nome = "MArcuS"

print(nome.upper()) #Deixar tudo maiúsculo
print(nome.lower()) #Deixar tudo minúsculo
print(nome.title()) #Deixar inicial maiúsculo

texto = "   Olá mundo    "

print(texto.strip()+ ".") #Tirar todos espaços
print(texto.lstrip() + ".") #Tirar espaços da esquerda
print(texto.rstrip() + ".") #Tirar espaços da direita

n2 = "Marcus"
print(n2.center(8, "#")) #Centralizar
print(".".join(n2)) #Separar letras por algo