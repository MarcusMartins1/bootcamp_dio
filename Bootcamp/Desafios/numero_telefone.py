import re

def validar_telefone(numero):
    # Definindo a expressão regular para validar o formato de telefone
    padrao = r'^\(\d{2}\) 9\d{4}-\d{4}$'
    
    # Usando a função fullmatch para verificar se o número de telefone corresponde ao padrão
    if re.fullmatch(padrao, numero):
        return "Número de telefone válido."
    else:
        return "Número de telefone inválido."

# Solicitando ao usuário que insira o número de telefone
numero_telefone = input("Digite o número de telefone no formato (XX) 9XXXX-XXXX: ")

# Validando o número de telefone
resultado = validar_telefone(numero_telefone)

# Exibindo o resultado da validação
print(resultado)
