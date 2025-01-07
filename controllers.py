from models import Aluno, Professor, Disciplina, Turma
from database import carregar_dados, salvar_dados
from utils import validar_email, validar_data, input_validado, validar_matricula_nao_vazia

# CRUD ALUNO
def cadastrar_aluno():
    print("\n=== CADASTRAR ALUNO ===")
    nome = input("Nome do aluno: ")
    matricula = input_validado("Matrícula: ", validar_matricula_nao_vazia)
    data_nasc = input_validado("Data de nascimento (dd/mm/aaaa): ", validar_data)
    sexo = input("Sexo: ")
    endereco = input("Endereço: ")
    telefone = input("Telefone: ")
    email = input_validado("E-mail: ", validar_email)

    aluno = Aluno(nome, matricula, data_nasc, sexo, endereco, telefone, email)

    lista_alunos = carregar_dados("alunos.json")

    dict_aluno = vars(aluno)
    lista_alunos.append(dict_aluno)

    salvar_dados("alunos.json", lista_alunos)
    print("Aluno cadastrado com sucesso!\n")

def listar_alunos():
    print("\n=== LISTAR ALUNOS ===")
    lista_alunos = carregar_dados("alunos.json")
    if not lista_alunos:
        print("Nenhum aluno cadastrado.")
        return

    for a in lista_alunos:
        print(a)
    print()

def editar_aluno():
    print("\n=== EDITAR ALUNO ===")
    matricula_busca = input("Informe a matrícula do aluno que deseja editar: ")

    lista_alunos = carregar_dados("alunos.json")
    aluno_encontrado = None

    for al in lista_alunos:
        if al["matricula"] == matricula_busca:
            aluno_encontrado = al
            break

    if not aluno_encontrado:
        print("Aluno não encontrado.")
        return

    novo_nome = input(f"Novo nome (enter para manter '{aluno_encontrado['nome']}'): ")
    if novo_nome.strip():
        aluno_encontrado["nome"] = novo_nome

    nova_data = input(f"Nova data de nascimento (enter para manter '{aluno_encontrado['data_nascimento']}'): ")
    if nova_data.strip():
        aluno_encontrado["data_nascimento"] = nova_data

    novo_sexo = input(f"Novo sexo (enter para manter '{aluno_encontrado['sexo']}'): ")
    if novo_sexo.strip():
        aluno_encontrado["sexo"] = novo_sexo

    novo_endereco = input(f"Novo endereço (enter para manter '{aluno_encontrado['endereco']}'): ")
    if novo_endereco.strip():
        aluno_encontrado["endereco"] = novo_endereco

    novo_telefone = input(f"Novo telefone (enter para manter '{aluno_encontrado['telefone']}'): ")
    if novo_telefone.strip():
        aluno_encontrado["telefone"] = novo_telefone

    novo_email = input(f"Novo e-mail (enter para manter '{aluno_encontrado['email']}'): ")
    if novo_email.strip():
        aluno_encontrado["email"] = novo_email

    salvar_dados("alunos.json", lista_alunos)
    print("Aluno atualizado com sucesso!\n")

def excluir_aluno():
    print("\n=== EXCLUIR ALUNO ===")
    matricula_busca = input("Informe a matrícula do aluno que deseja excluir: ")

    lista_alunos = carregar_dados("alunos.json")
    lista_atualizada = [al for al in lista_alunos if al["matricula"] != matricula_busca]

    if len(lista_atualizada) == len(lista_alunos):
        print("Aluno não encontrado.")
        return

    salvar_dados("alunos.json", lista_atualizada)
    print("Aluno excluído com sucesso!\n")

# CRUD PROFESSOR
def cadastrar_professor():
    print("\n=== CADASTRAR PROFESSOR ===")
    nome = input("Nome do professor: ")
    matricula = input_validado("Matrícula: ", validar_matricula_nao_vazia)
    data_nasc = input_validado("Data de nascimento (dd/mm/aaaa): ", validar_data)
    sexo = input("Sexo: ")
    endereco = input("Endereço: ")
    telefone = input("Telefone: ")
    email = input_validado("E-mail: ", validar_email)
    disciplina = input("Disciplina principal (ex: 'A1234' ou nome): ")

    professor = Professor(nome, matricula, data_nasc, sexo, endereco, telefone, email, disciplina)

    lista_professores = carregar_dados("professores.json")

    dict_professor = vars(professor)
    lista_professores.append(dict_professor)

    salvar_dados("professores.json", lista_professores)
    print("Professor cadastrado com sucesso!\n")

def listar_professores():
    print("\n=== LISTAR PROFESSORES ===")
    lista_professores = carregar_dados("professores.json")
    if not lista_professores:
        print("Nenhum professor cadastrado.")
        return

    for p in lista_professores:
        print(p)
    print()

def editar_professor():
    print("\n=== EDITAR PROFESSOR ===")
    matricula_busca = input("Informe a matrícula do professor que deseja editar: ")

    lista_professores = carregar_dados("professores.json")
    professor_encontrado = None

    for prof in lista_professores:
        if prof["matricula"] == matricula_busca:
            professor_encontrado = prof
            break

    if not professor_encontrado:
        print("Professor não encontrado.")
        return

    novo_nome = input(f"Novo nome (enter para manter '{professor_encontrado['nome']}'): ")
    if novo_nome.strip():
        professor_encontrado["nome"] = novo_nome

    nova_data = input(f"Nova data de nascimento (enter para manter '{professor_encontrado['data_nascimento']}'): ")
    if nova_data.strip():
        professor_encontrado["data_nascimento"] = nova_data

    novo_sexo = input(f"Novo sexo (enter para manter '{professor_encontrado['sexo']}'): ")
    if novo_sexo.strip():
        professor_encontrado["sexo"] = novo_sexo

    novo_endereco = input(f"Novo endereço (enter para manter '{professor_encontrado['endereco']}'): ")
    if novo_endereco.strip():
        professor_encontrado["endereco"] = novo_endereco

    novo_telefone = input(f"Novo telefone (enter para manter '{professor_encontrado['telefone']}'): ")
    if novo_telefone.strip():
        professor_encontrado["telefone"] = novo_telefone

    novo_email = input(f"Novo e-mail (enter para manter '{professor_encontrado['email']}'): ")
    if novo_email.strip():
        professor_encontrado["email"] = novo_email

    nova_disciplina = input(f"Nova disciplina (enter para manter '{professor_encontrado['disciplina']}'): ")
    if nova_disciplina.strip():
        professor_encontrado["disciplina"] = nova_disciplina

    salvar_dados("professores.json", lista_professores)
    print("Professor atualizado com sucesso!\n")

def excluir_professor():
    print("\n=== EXCLUIR PROFESSOR ===")
    matricula_busca = input("Informe a matrícula do professor que deseja excluir: ")

    lista_professores = carregar_dados("professores.json")
    lista_atualizada = [prof for prof in lista_professores if prof["matricula"] != matricula_busca]

    if len(lista_atualizada) == len(lista_professores):
        print("Professor não encontrado.")
        return

    salvar_dados("professores.json", lista_atualizada)
    print("Professor excluído com sucesso!\n")

# CRUD DISCIPLINA
def cadastrar_disciplina():
    print("\n=== CADASTRAR DISCIPLINA ===")
    nome = input("Nome da disciplina: ")
    codigo = input("Código da disciplina (ex: A1234): ")
    carga_horaria = input("Carga horária (ex: 60h): ")
    professor = input("Matrícula do professor responsável (ex: P0001) ou enter se não houver: ")

    disciplina = Disciplina(nome, codigo, carga_horaria, professor)

    lista_disciplinas = carregar_dados("disciplinas.json")

    dict_disciplina = vars(disciplina)
    lista_disciplinas.append(dict_disciplina)

    salvar_dados("disciplinas.json", lista_disciplinas)
    print("Disciplina cadastrada com sucesso!\n")

def listar_disciplinas():
    print("\n=== LISTAR DISCIPLINAS ===")
    lista_disciplinas = carregar_dados("disciplinas.json")
    if not lista_disciplinas:
        print("Nenhuma disciplina cadastrada.")
        return

    for d in lista_disciplinas:
        print(d)
    print()

def editar_disciplina():
    print("\n=== EDITAR DISCIPLINA ===")
    codigo_busca = input("Informe o código da disciplina que deseja editar: ")

    lista_disciplinas = carregar_dados("disciplinas.json")
    disciplina_encontrada = None

    for disc in lista_disciplinas:
        if disc["codigo"] == codigo_busca:
            disciplina_encontrada = disc
            break

    if not disciplina_encontrada:
        print("Disciplina não encontrada.")
        return

    novo_nome = input(f"Novo nome (enter para manter '{disciplina_encontrada['nome']}'): ")
    if novo_nome.strip():
        disciplina_encontrada["nome"] = novo_nome

    nova_carga = input(f"Nova carga horária (enter para manter '{disciplina_encontrada['carga_horaria']}'): ")
    if nova_carga.strip():
        disciplina_encontrada["carga_horaria"] = nova_carga

    novo_professor = input(f"Novo professor responsável (enter para manter '{disciplina_encontrada['professor']}'): ")
    if novo_professor.strip():
        disciplina_encontrada["professor"] = novo_professor

    salvar_dados("disciplinas.json", lista_disciplinas)
    print("Disciplina atualizada com sucesso!\n")

def excluir_disciplina():
    print("\n=== EXCLUIR DISCIPLINA ===")
    codigo_busca = input("Informe o código da disciplina que deseja excluir: ")

    lista_disciplinas = carregar_dados("disciplinas.json")
    lista_atualizada = [disc for disc in lista_disciplinas if disc["codigo"] != codigo_busca]

    if len(lista_atualizada) == len(lista_disciplinas):
        print("Disciplina não encontrada.")
        return

    salvar_dados("disciplinas.json", lista_atualizada)
    print("Disciplina excluída com sucesso!\n")

# CRUD TURMA
def cadastrar_turma():
    print("\n=== CADASTRAR TURMA ===")
    nome = input("Nome da turma: ")
    codigo = input("Código da turma (ex: T101): ")
    disciplina = input("Código da disciplina (ex: A1234) para esta turma: ")
    professor = input("Matrícula do professor (ex: P0001) para esta turma: ")

    nova_turma = Turma(nome, codigo, disciplina, professor, alunos=[])

    lista_turmas = carregar_dados("turmas.json")

    dict_turma = {
        "nome": nova_turma.nome,
        "codigo": nova_turma.codigo,
        "disciplina": nova_turma.disciplina,
        "professor": nova_turma.professor,
        "alunos": nova_turma.alunos
    }

    lista_turmas.append(dict_turma)
    salvar_dados("turmas.json", lista_turmas)
    print("Turma cadastrada com sucesso!\n")

def listar_turmas():
    print("\n=== LISTAR TURMAS ===")
    lista_turmas = carregar_dados("turmas.json")
    if not lista_turmas:
        print("Nenhuma turma cadastrada.")
        return

    for t in lista_turmas:
        print(t)
    print()

def editar_turma():
    print("\n=== EDITAR TURMA ===")
    codigo_busca = input("Informe o código da turma que deseja editar: ")

    lista_turmas = carregar_dados("turmas.json")
    turma_encontrada = None

    for t in lista_turmas:
        if t["codigo"] == codigo_busca:
            turma_encontrada = t
            break

    if not turma_encontrada:
        print("Turma não encontrada.")
        return

    novo_nome = input(f"Novo nome (enter para manter '{turma_encontrada['nome']}'): ")
    if novo_nome.strip():
        turma_encontrada["nome"] = novo_nome

    nova_disciplina = input(f"Nova disciplina (enter para manter '{turma_encontrada['disciplina']}'): ")
    if nova_disciplina.strip():
        turma_encontrada["disciplina"] = nova_disciplina

    novo_professor = input(f"Novo professor (enter para manter '{turma_encontrada['professor']}'): ")
    if novo_professor.strip():
        turma_encontrada["professor"] = novo_professor

    salvar_dados("turmas.json", lista_turmas)
    print("Turma atualizada com sucesso!\n")

def excluir_turma():
    print("\n=== EXCLUIR TURMA ===")
    codigo_busca = input("Informe o código da turma que deseja excluir: ")

    lista_turmas = carregar_dados("turmas.json")
    lista_atualizada = [t for t in lista_turmas if t["codigo"] != codigo_busca]

    if len(lista_atualizada) == len(lista_turmas):
        print("Turma não encontrada.")
        return

    salvar_dados("turmas.json", lista_atualizada)
    print("Turma excluída com sucesso!\n")

# FUNCIONALIDADES EXTRAS

def matricular_aluno_em_turma():
    """
    Adiciona a matrícula de um aluno à lista de alunos de uma Turma.
    """
    print("\n=== MATRICULAR ALUNO EM TURMA ===")
    matricula = input("Digite a matrícula do aluno: ")
    codigo_turma = input("Digite o código da turma: ")

    lista_turmas = carregar_dados("turmas.json")
    turma_encontrada = None
    for t in lista_turmas:
        if t["codigo"] == codigo_turma:
            turma_encontrada = t
            break

    if not turma_encontrada:
        print("Turma não encontrada.")
        return

    if "alunos" not in turma_encontrada:
        turma_encontrada["alunos"] = []

    if matricula in turma_encontrada["alunos"]:
        print("Esse aluno já está matriculado nesta turma.")
        return

    turma_encontrada["alunos"].append(matricula)

    salvar_dados("turmas.json", lista_turmas)
    print("Matrícula efetuada com sucesso!\n")

def alocar_professor_em_disciplina():
    """
    Define um professor responsável por uma disciplina, atualizando a disciplina no JSON.
    """
    print("\n=== ALOCAR PROFESSOR EM DISCIPLINA ===")
    matricula_prof = input("Digite a matrícula do professor: ")
    codigo_disc = input("Digite o código da disciplina: ")

    lista_disciplinas = carregar_dados("disciplinas.json")
    disciplina_encontrada = None

    for d in lista_disciplinas:
        if d["codigo"] == codigo_disc:
            disciplina_encontrada = d
            break

    if not disciplina_encontrada:
        print("Disciplina não encontrada.")
        return

    disciplina_encontrada["professor"] = matricula_prof

    salvar_dados("disciplinas.json", lista_disciplinas)
    print("Professor alocado à disciplina com sucesso!\n")

def filtrar_professores_por_disciplina():
    """
    Pergunta a disciplina desejada e exibe somente os professores que têm 
    essa disciplina no campo 'disciplina'.
    """
    print("\n=== FILTRAR PROFESSORES POR DISCIPLINA ===")
    disciplina_busca = input("Digite o código/nome da disciplina: ")

    lista_professores = carregar_dados("professores.json")
    professores_filtrados = []

    for prof in lista_professores:
        if prof["disciplina"] == disciplina_busca:
            professores_filtrados.append(prof)

    if professores_filtrados:
        print("\nProfessores que lecionam a disciplina:", disciplina_busca)
        for p in professores_filtrados:
            print(f"- {p['nome']} (Matrícula: {p['matricula']})")
    else:
        print("Nenhum professor encontrado para essa disciplina.")
    print()

def alocar_disciplina_em_turma():
    """
    Pede um código de disciplina e um código de turma,
    e atualiza a turma definindo essa disciplina como a 'oficial' da turma.
    """
    print("\n=== ALOCAR DISCIPLINA EM TURMA ===")
    codigo_disc = input("Digite o código da disciplina (ex: A1234): ")
    codigo_turma = input("Digite o código da turma (ex: T101): ")

    lista_turmas = carregar_dados("turmas.json")

    turma_encontrada = None
    for t in lista_turmas:
        if t["codigo"] == codigo_turma:
            turma_encontrada = t
            break

    if not turma_encontrada:
        print("Turma não encontrada.")
        return

    turma_encontrada["disciplina"] = codigo_disc
    salvar_dados("turmas.json", lista_turmas)
    print(f"Disciplina '{codigo_disc}' alocada à turma '{codigo_turma}' com sucesso!\n")

def consultar_alunos_matriculados_em_turma():
    """
    Pede o código da turma e exibe somente os alunos (matrículas) dessa turma.
    """
    print("\n=== CONSULTA DE ALUNOS MATRICULADOS EM TURMA ===")
    codigo_turma = input("Digite o código da turma (ex: T101): ")

    lista_turmas = carregar_dados("turmas.json")
    turma_encontrada = None
    for turma in lista_turmas:
        if turma["codigo"] == codigo_turma:
            turma_encontrada = turma
            break

    if not turma_encontrada:
        print("Turma não encontrada.")
        return

    alunos_matriculados = turma_encontrada.get("alunos", [])
    if not alunos_matriculados:
        print("Nenhum aluno matriculado nesta turma.")
        return

    # Se quiser exibir só as matrículas:
    print(f"Alunos matriculados na turma '{codigo_turma}':")
    for matr in alunos_matriculados:
        print(f"- Matrícula: {matr}")
    print()

def consultar_professores_alocados_em_disciplinas():
    """
    Lista, para cada disciplina, qual professor está alocado.
    Se quiser filtrar só uma disciplina, peça o código e mostre apenas aquela.
    """
    print("\n=== CONSULTA DE PROFESSORES ALOCADOS EM DISCIPLINAS ===")
    lista_disciplinas = carregar_dados("disciplinas.json")
    if not lista_disciplinas:
        print("Nenhuma disciplina cadastrada.")
        return

    for disc in lista_disciplinas:
        cod = disc["codigo"]
        prof = disc["professor"]
        print(f"Disciplina {cod} => Professor {prof if prof else 'Nenhum'}")
    print()

def consultar_disciplinas_alocadas_em_turmas():
    """
    Lista cada turma e a disciplina associada a ela.
    """
    print("\n=== CONSULTA DE DISCIPLINAS ALOCADAS EM TURMAS ===")
    lista_turmas = carregar_dados("turmas.json")
    if not lista_turmas:
        print("Nenhuma turma cadastrada.")
        return

    for t in lista_turmas:
        print(f"Turma {t['codigo']} => Disciplina {t['disciplina']}")
    print()

