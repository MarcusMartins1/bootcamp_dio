def principal():
    print("Executando a função principal")
    
    def funcao_interna():
        print("Executando função interna")
        
    def funcao_2():
        print("Executando a última função")
        
    funcao_interna()
    funcao_2()
    
principal()        
          
