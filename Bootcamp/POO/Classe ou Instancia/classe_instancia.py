class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


aluno_1 = Estudante("Marcus", 1)
aluno_2 = Estudante("Myllena", 2)
mostrar_valores(aluno_1, aluno_2)

Estudante.escola = "Python"
aluno_3 = Estudante("Kinhos", 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)