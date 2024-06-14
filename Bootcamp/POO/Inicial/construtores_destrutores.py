class Cachorro:
    def __init__(self,nome,cor,acordado=True):
        print("Inicializando a classe ...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def __del__(self):
        print("Removendo a instância de classe.")
        
    def falar(self):
        print("Auau")     
        
def criar_cachorro():
    c = Cachorro("Zeus", "Branco e Preto", False) 
    print(c.nome)   
        
        
#c = Cachorro("Chappie","Amarelo")   
#c.falar() 

criar_cachorro()
criar_cachorro()
criar_cachorro()
criar_cachorro()

        