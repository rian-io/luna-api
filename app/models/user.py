from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "users"

    name: Mapped[str] = mapped_column(nullable=False)
