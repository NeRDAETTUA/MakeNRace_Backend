from typing import List, Optional

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from mnr.db.dependencies import get_db_session
from mnr.db.models.team_model import TeamModel


class TeamDAO:
    """Class for accessing team table."""

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def create_team_model(self, name: str) -> None:
        """
        Add single team to session.

        :param name: name of a team.
        """
        self.session.add(TeamModel(name=name))

    async def get_all_teams(self, limit: int, offset: int) -> List[TeamModel]:
        """
        Get all team models with limit/offset pagination.

        :param limit: limit of teams.
        :param offset: offset of teams.
        :return: stream of teams.
        """
        raw_teams = await self.session.execute(
            select(TeamModel).limit(limit).offset(offset),
        )

        return list(raw_teams.scalars().fetchall())

    async def filter(
        self,
        name: Optional[str] = None,
    ) -> List[TeamModel]:
        """
        Get specific team model.

        :param name: name of team instance.
        :return: team models.
        """
        query = select(TeamModel)
        if name:
            query = query.where(TeamModel.name == name)
        rows = await self.session.execute(query)
        return list(rows.scalars().fetchall())
