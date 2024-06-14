def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("Before")
        funcao(*args, **kwargs)
        print("After")
    
    return envelope      

@meu_decorador
def ola_mundo(nome):
    print(f"Olá {nome}!")    
    
    
ola_mundo("Marcus")    