from controllers import (
    cadastrar_aluno, listar_alunos, editar_aluno, excluir_aluno,
    cadastrar_professor, listar_professores, editar_professor, excluir_professor,
    cadastrar_disciplina, listar_disciplinas, editar_disciplina, excluir_disciplina,
    cadastrar_turma, listar_turmas, editar_turma, excluir_turma,
    matricular_aluno_em_turma, alocar_professor_em_disciplina, filtrar_professores_por_disciplina,
    alocar_disciplina_em_turma, consultar_alunos_matriculados_em_turma,
    consultar_disciplinas_alocadas_em_turmas, consultar_professores_alocados_em_disciplinas
)

def menu_principal():
    while True:
        print("=== SISTEMA ESCOLAR ===")
        print("1 - Alunos")
        print("2 - Professores")
        print("3 - Disciplinas")
        print("4 - Turmas")
        print("5 - Matrículas e Alocações")
        print("6 - Consultas Avançadas")
        print("0 - Sair")

        opc = input("Escolha uma opção: ")

        if opc == "1":
            menu_alunos()
        elif opc == "2":
            menu_professores()
        elif opc == "3":
            menu_disciplinas()
        elif opc == "4":
            menu_turmas()
        elif opc == "5":
            menu_matriculas_alocacoes()
        elif opc == "6":
            menu_consultas()
        elif opc == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_alunos():
    while True:
        print("\n=== MENU ALUNOS ===")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Editar")
        print("4 - Excluir")
        print("0 - Voltar")

        opc = input("Escolha uma opção: ")

        if opc == "1":
            cadastrar_aluno()
        elif opc == "2":
            listar_alunos()
        elif opc == "3":
            editar_aluno()
        elif opc == "4":
            excluir_aluno()
        elif opc == "0":
            break
        else:
            print("Opção inválida.")

def menu_professores():
    while True:
        print("\n=== MENU PROFESSORES ===")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Editar")
        print("4 - Excluir")
        print("0 - Voltar")

        opc = input("Escolha uma opção: ")

        if opc == "1":
            cadastrar_professor()
        elif opc == "2":
            listar_professores()
        elif opc == "3":
            editar_professor()
        elif opc == "4":
            excluir_professor()
        elif opc == "0":
            break
        else:
            print("Opção inválida.")

def menu_disciplinas():
    while True:
        print("\n=== MENU DISCIPLINAS ===")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Editar")
        print("4 - Excluir")
        print("0 - Voltar")

        opc = input("Escolha uma opção: ")

        if opc == "1":
            cadastrar_disciplina()
        elif opc == "2":
            listar_disciplinas()
        elif opc == "3":
            editar_disciplina()
        elif opc == "4":
            excluir_disciplina()
        elif opc == "0":
            break
        else:
            print("Opção inválida.")

def menu_turmas():
    while True:
        print("\n=== MENU TURMAS ===")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Editar")
        print("4 - Excluir")
        print("0 - Voltar")

        opc = input("Escolha uma opção: ")

        if opc == "1":
            cadastrar_turma()
        elif opc == "2":
            listar_turmas()
        elif opc == "3":
            editar_turma()
        elif opc == "4":
            excluir_turma()
        elif opc == "0":
            break
        else:
            print("Opção inválida.")

def menu_matriculas_alocacoes():
    while True:
        print("\n=== MATRÍCULAS E ALOCAÇÕES ===")
        print("1 - Matricular Aluno em Turma")
        print("2 - Alocar Professor em Disciplina")
        print("3 - Alocar Disciplina em Turma")
        print("0 - Voltar")

        opc = input("Escolha uma opção: ")

        if opc == "1":
            matricular_aluno_em_turma()
        elif opc == "2":
            alocar_professor_em_disciplina()
        elif opc == "3":
            alocar_disciplina_em_turma()
        elif opc == "0":
            break
        else:
            print("Opção inválida.")

def menu_consultas():
    while True:
        print("\n=== CONSULTAS ===")
        print("1 - Filtrar Professores por Disciplina")
        print("2 - Consultar Alunos Matriculados em Turma")
        print("3 - Consultar Professores Alocados em Disciplinas")
        print("4 - Consultar Disciplinas Alocadas em Turmas")
        print("0 - Voltar")

        opc = input("Escolha uma opção: ")

        if opc == "1":
            filtrar_professores_por_disciplina()
        elif opc == "2":
            consultar_alunos_matriculados_em_turma()
        elif opc == "3":
            consultar_professores_alocados_em_disciplinas()
        elif opc == "4":
            consultar_disciplinas_alocadas_em_turmas()
        elif opc == "0":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu_principal()
