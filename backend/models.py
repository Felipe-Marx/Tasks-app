from pydantic import BaseModel, Field, field_validator

class Task(BaseModel):
    id: int
    titulo: str
    descricao: str | None = None
    concluida: bool

class TaskCreate(BaseModel):
    titulo: str = Field(min_length=1, max_length=100)
    descricao: str | None = None

    @field_validator("titulo")
    @classmethod
    def validar_titulo(cls, v:str):
        if not v.strip():
            raise ValueError("O Titulo está vazio ou contém apenas espaços.")
        return v.strip()

    @field_validator("descricao")
    @classmethod
    def validar_descricao(cls, v:str | None):
        if v is None:
            return None
        if not v.strip():
            raise ValueError("A descricao está vazia ou contém apenas espaços.")
        return v.strip()