# Crie uma Lista 'itens' para armazenar os equipamentos:
itens = []

# Solicita ao usuário que insira três equipamentos
while len(itens) < 3:
    # Solicita o item e armazena na variável "item"
    item = input("")
    
    # Adiciona o item à lista "itens"
    itens.append(item)

# Exibe a lista de itens
print("Lista de Equipamentos:")
for item in itens:
    print(f"- {item}")
