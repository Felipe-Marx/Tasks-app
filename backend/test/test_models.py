

from backend.models import TaskCreate

def test_task_create_valida():
    task = TaskCreate(titulo="Estudar FastAPI", descricao="Estudar Pydantic")
    assert task.titulo == "Estudar FastAPI"
    assert task.descricao == "Estudar Pydantic"

def test_task_create_sem_desc():
    task = TaskCreate(titulo="Estudar FastAPI")
    assert task.titulo == "Estudar FastAPI"
    assert task.descricao is None
