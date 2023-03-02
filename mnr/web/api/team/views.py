from typing import List

from fastapi import APIRouter
from fastapi.param_functions import Depends

from mnr.db.dao.team_dao import TeamDAO
from mnr.db.models.team_model import TeamModel
from mnr.web.api.team.schema import TeamModelDTO, TeamModelInputDTO

router = APIRouter()


@router.get("/", response_model=List[TeamModelDTO])
async def get_team_models(
    limit: int = 10,
    offset: int = 0,
    team_dao: TeamDAO = Depends(),
) -> List[TeamModel]:
    """
    Retrieve all team objects from the database.

    :param limit: limit of team objects, defaults to 10.
    :param offset: offset of team objects, defaults to 0.
    :param team_dao: DAO for team models.
    :return: list of team objects from database.
    """
    return await team_dao.get_all_teams(limit=limit, offset=offset)


@router.post("/")
async def create_team_model(
    new_team_object: TeamModelInputDTO,
    team_dao: TeamDAO = Depends(),
) -> None:
    """
    Creates team model in the database.

    :param new_team_object: new team model item.
    :param team_dao: DAO for team models.
    """
    await team_dao.create_team_model(**new_team_object.dict())
