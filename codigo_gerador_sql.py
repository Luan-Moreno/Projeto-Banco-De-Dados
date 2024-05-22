from faker import Faker # type: ignore
from random import randint, uniform, choice

qtd = 100

fake = Faker('pt-BR')
nomes_a = [fake.unique.name() for i in range(qtd)]
nomes_p = [fake.unique.name() for i in range(qtd)]

prefixo_ra = '220'

ras = [(prefixo_ra + str(ra)) for ra in range(qtd)]

prefixo_historico_a = 'HA'

ids_historico_a = [(prefixo_historico_a + str(ra)) for ra in range(qtd)]


prefixo_id = '230'

ids = [(prefixo_id + str(id)) for id in range(qtd)]

prefixo_historico_p = 'HP'

ids_historico_p = [(prefixo_historico_p + str(id)) for id in range(qtd)]



prefixo_tcc = 'TCC'

tcc_ids = [(prefixo_tcc + str(id)) for id in range(qtd)]



departamentos = ["Civil", "Eletrica", "Mecanica", "Quimica", "Robotica", "Producao", "Computacao", "Fisica", "Matematica", "Administracao",]


prefixo_curso = 'C0'

ids_curso = [(prefixo_curso + str(id)) for id in range(10)]

cursos = ["Engenharia Civil", "Engenharia Eletrica", "Engenharia Mecanica", "Engenharia Quimica", "Engenharia de Robos", "Engenharia de Producao", "Ciencia da Computacao", "Fisica", "Matematica", "Administracao"]


prefixo_disciplina = 'D0'

ids_disciplina = [(prefixo_disciplina + str(id)) for id in range(200)]

siglas = ['EC', 'EE', 'EM', 'EQ', 'ER', 'EP', 'CC', 'FS', 'MT', 'AD']
disciplinas = [(choice(siglas) + str(id)) for id in range(200)]


edificios = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

finall = 99
final_cursos = 9
final_disciplinas = 199

def cria_tabelas_sql(final_cursos=final_cursos, final_disciplinas = final_disciplinas):
    global finall
    aleatorio = randint(0, finall)
    aleatorio_cursos = randint(0, final_cursos)
    aleatorio_disciplinas = randint(0, final_disciplinas)

    dept_nome = departamentos[aleatorio_cursos]
    orcamento = round(uniform(10000, 100000), 2)
    edificio = edificios[aleatorio_cursos]

    print(f"insert into departamento(dept_nome, orcamento, edificio) values ('{dept_nome}', '{orcamento}', '{edificio}')")

    id = ids.pop(aleatorio)
    nome = nomes_p.pop(aleatorio)
    salario = round(uniform(5000, 20000), 2)
    eh_chefe = choice([True, False])

    print(f"insert into professor(id, nome, dept_nome, salario, eh_chefe) values ('{id}', '{nome}', '{dept_nome}', '{salario}', {eh_chefe})")

    aleatorio = randint(0, finall)
    tcc_id = tcc_ids.pop(aleatorio)
    print(f"insert into grupo_tcc(tcc_id, id) values ('{tcc_id}', '{id}')")

    aleatorio = randint(0, finall)
    ra = ras.pop(aleatorio)
    dept_nome = departamentos[aleatorio_cursos]
    nome = nomes_a.pop(aleatorio)   

    print(f"insert into aluno(ra, dept_nome, nome, tcc_id) values ('{ra}', '{dept_nome}', '{nome}', '{tcc_id}')")

    print(f"insert into orientado(p_id, a_ra) values ('{id}', '{ra}')")
    
    id_historico_a = ids_historico_a.pop(aleatorio)

    print(f"insert into historico_aluno(id_historico_a, ra) values ('{id_historico_a}', '{ra}')")
    
    id_historico_p = ids_historico_p.pop(aleatorio)

    print(f"insert into historico_professor(id_historico_p, id) values ('{id_historico_p}', '{id}')")
    
    id_curso = ids_curso[aleatorio_cursos]
    titulo = cursos[aleatorio_cursos]

    print(f"insert into curso(id_curso, dept_nome, titulo) values ('{id_curso}', '{dept_nome}', '{titulo}')")
    
    id_disciplina = ids_disciplina[aleatorio_disciplinas]
    nome = disciplinas[aleatorio_disciplinas]

    print(f"insert into disciplina(id_disciplina, nome, id_curso) values ('{id_disciplina}', '{nome}', '{id_curso}')")

    print(f"insert into matriz_curricular(id_curso, id_disciplina) values ('{id_curso}', '{id_disciplina}')")

    id_historico = id_historico_a
    semestre = choice([1, 2])
    ano = randint(1990, 2024)
    media = randint(0, 10)

    print(f"insert into estudou(id_historico, id_disciplina, semestre, ano, media) values ('{id_historico}', '{id_disciplina}', '{semestre}', '{ano}', '{media}')")

    id_historico = id_historico_p

    print(f"insert into lecionou(id_historico, id_disciplina, semestre, ano) values ('{id_historico}', '{id_disciplina}', '{semestre}', '{ano}')")
    finall -= 1

for x in range(1):
    cria_tabelas_sql()