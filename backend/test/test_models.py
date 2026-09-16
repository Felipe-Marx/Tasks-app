import pytest
from backend.models import TaskCreate

def test_task_create_valida():
    task = TaskCreate(titulo="Estudar FastAPI", descricao="Estudar Pydantic")
    assert task.titulo == "Estudar FastAPI"
    assert task.descricao == "Estudar Pydantic"

def test_task_create_sem_desc():
    task = TaskCreate(titulo="Estudar FastAPI")
    assert task.titulo == "Estudar FastAPI"
    assert task.descricao is None

def test_task_create_remove_espacos():
    task = TaskCreate(titulo="   Estudar FastAPI   ", descricao="  Aprender Pydantic  ")
    assert task.titulo == "Estudar FastAPI"
    assert task.descricao == "Aprender Pydantic"

def test_task_create_titulo_vazio():
    with pytest.raises(ValueError, match="O Titulo está vazio ou contém apenas espaços."):
        TaskCreate(titulo="    ", descricao="Aprender Pydantic")

def test_task_create_desc_vazia():
    with pytest.raises(ValueError, match="A descricao está vazia ou contém apenas espaços."):
        TaskCreate(titulo="Estudar FastAPI", descricao="       ")

