from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional
from database import Base

class TaskDB(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    titulo: Mapped[str] = mapped_column(nullable=False)
    descricao: Mapped[Optional[str]] = mapped_column(nullable=True)
    concluida: Mapped[bool] = mapped_column(nullable=False, default=False)


