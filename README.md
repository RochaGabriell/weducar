# Weducar - School Management System

Sistema de gestão escolar desenvolvido com Django, projetado para ajudar escolas a gerenciar alunos, turmas, horários e processos acadêmicos e administrativos.

## Aplicações

### 1. **App: `students`** (Responsável pelos dados relacionados aos alunos)
- `Alunos` (Student)
- `Historico` (History)
- `HistoricoAreas` (HistoryArea)
- `SituacaoAluno` (StudentStatus)
- `TurmasAluno` (StudentClasses)

### 2. **App: `academics`** (Responsável pelas funcionalidades acadêmicas e conteúdo)
- `AnosEscolares` (SchoolYear)
- `AnosLetivos` (AcademicYear)
- `Avaliacoes` (Evaluation)
- `ComponentesCurriculares` (CurricularComponent)
- `ConteudoAula` (LessonContent)
- `Diarios` (Diary)
- `Notas` (Grade)
- `MatrizComponentes` (CurricularComponentMatrix)
- `MatrizCurricular` (CurricularMatrix)

### 3. **App: `attendance`** (Responsável pela presença e faltas dos alunos)
- `FaltasJustificadas` (JustifiedAbsence)
- `Frequencias` (Frequency)
- `SysPresenca` (SysPresence)

### 4. **App: `administration`** (Responsável pela administração escolar)
- `Escolas` (School)
- `Funcionarios` (Employee)
- `FuncionariosEscolas` (EmployeeSchool)
- `TipoContrato` (ContractType)
- `Cargos` (Position)
- `Salas` (Room)
- `GradesHorarios` (ScheduleGrid)
- `HorariosAulas` (ClassSchedule)
- `Escolaridade` (Schooling)

### 5. **App: `locations`** (Responsável pelos dados relacionados a localizações)
- `Cidades` (City)
- `Estados` (State)
- `Moradia` (Housing)
- `Instancias` (Instance)

### 6. **App: `management`** (Responsável pelo gerenciamento de turmas e horários)
- `Turmas` (Classe)
- `Turnos` (Shift)
- `Semana` (Week)

### 7. **App: `accounts`** (Responsável pelos dados relacionados às contas de usuário)
- `Usuarios` (User)

---

## Instalação

### Pré-requisitos:
- Python 3.9+
- Django 3.2+

### Passo a Passo:

1. Clone o repositório:
   ```bash
   git clone https://github.com/RochaGabriell/weducar.git
   cd weducar
   ```

2. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Realize as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```

5. Crie a tabela de escolaridade, status, cargos e tipos de contrato:
   ```bash
   python manage.py create_schooling
   python manage.py create_student_status
   python manage.py create_position 
   python manage.py create_contract_type
   ```

6. Crie um superusuário para acessar o painel administrativo:
   ```bash
   python manage.py createsuperuser
   ```

7. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```

### Acessos:
- **Admin:** http://127.0.0.1:8000/admin/
- **API (Swagger):** http://127.0.0.1:8000/
- **API (Redoc):** http://127.0.0.1:8000/api/v1/redoc/

---

## Documentação

A API do sistema está documentada utilizando o Swagger e o Redoc, acessíveis pelas URLs acima. Para mais detalhes sobre as rotas disponíveis e o uso da API, consulte os respectivos links.