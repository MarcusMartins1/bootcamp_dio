nome_real = ["Martins","Oliveira"]
nome_pessoa = input("Digite seu nome: ").strip()

partes_nome = nome_pessoa.split()

nome_encontrado = any(nome in nome_real for nome in partes_nome)

print(nome_encontrado)