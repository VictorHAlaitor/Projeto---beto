class Aluno:
    def __init__(self, nome, matricula, data_nasc, sexo, endereco, telefone, email):
        self.nome = nome
        self.matricula = matricula
        self.data_nasc = data_nasc
        self.sexo = sexo
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

    def __repr__(self):
        return f"Aluno(matricula={self.matricula}, nome={self.nome})"
    
class Professor:
    def __init__(self, nome, matricula, data_nasc, sexo, endereco, telefone, email, disciplina=None):
        self.nome = nome
        self.matricula = matricula
        self.data_nasc = data_nasc
        self.sexo = sexo
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.disciplina = disciplina

    def __repr__(self):
        return f"Professor(matrícula={self.matricula}, nome={self.nome})"
    
class Disciplina:
    def __init__(self, nome, codigo, carga_horaria, professor=None):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria
        self.professor = professor

    def __repr__(self):
        return f"Disciplina(código={self.codigo}, nome={self.nome})"


class Turma:
    def __init__(self, nome, codigo, disciplina, professor, alunos=None):
        self.nome = nome
        self.codigo = codigo
        self.disciplina = disciplina
        self.professor = professor
        self.alunos = alunos if alunos else []

    def __repr__(self):
        return f"Turma(código={self.codigo}, nome={self.nome})"