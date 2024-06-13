class Veiculo:
    def __init__(self, cor, placa,numero_rodas) :
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
        
    
    def ligar_motor(self):
        print("Ligando motor")   
        
class Motocicleta(Veiculo):
    pass        

class Carro(Veiculo):
    pass 

class Caminhao(Veiculo):
    pass 

moto = Motocicleta("Preta", "ABC-1234",2)
moto.ligar_motor()

carro = Carro("Branco", "ABC-4321", 4)
carro.ligar_motor()

caminhao = Caminhao("Vermelho","ABC-1324", 8)
caminhao.ligar_motor()