from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import String,Boolean

from mnr.db.base import Base


class TeamModel(Base):
    """God help us all."""

    __tablename__ = "team_model"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(length=200))  # noqa: WPS432
    is_full: Mapped[bool] = mapped_column(Boolean,default=False)  
