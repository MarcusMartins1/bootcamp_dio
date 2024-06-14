def meu_decorador(funcao):
    def envelope():
        print("Before")
        funcao()
        print("After")
    
    return envelope      

def ola_mundo():
    print("Olá mundo!")
    
ola_mundo = meu_decorador(ola_mundo)    
ola_mundo()       