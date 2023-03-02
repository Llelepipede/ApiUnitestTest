from pydantic import BaseModel
from typing import List

class CreateAndUpdateGame(BaseModel):
    Name: str
    StudioName: str

class Game(CreateAndUpdateGame):
    id: int

    class Config:
        orm_mode = True

class GameList(BaseModel):
    limit: int
    offset: int
    data: List[Game]