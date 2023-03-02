from pydantic import BaseModel


class TeamModelDTO(BaseModel):
    """
    DTO for team models.

    It returned when accessing team models from the API.
    """

    id: int
    name: str
    is_full: bool

    class Config:
        orm_mode = True


class TeamModelInputDTO(BaseModel):
    """DTO for creating new team model."""

    name: str
