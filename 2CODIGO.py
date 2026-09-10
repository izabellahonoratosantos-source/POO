class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def aprovado(self):
        return self.nota >= 6


aluno = Aluno("iza", 6.0)

print("Nome: ", aluno.nome)
print("Nota: ", aluno.nota)
print("Aprovado: ", aluno.aprovado()
)
