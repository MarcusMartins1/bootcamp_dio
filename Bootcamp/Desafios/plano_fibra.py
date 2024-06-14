def recomendar_plano(dados):
    if dados <= 10:
     print("Plano Essencial Fibra - 50Mbps")   
      
    elif 10 < dados < 20:
        print("Plano Prata Fibra - 100Mbps")
        
    elif dados > 20:
        print("Plano Premium Fibra - 300Mbps")
            

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input("Qual o consumo médio mensal de dados?: "))
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))