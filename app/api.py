# api.py
from fastapi import APIRouter, Depends, HTTPException,FastAPI
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from routes.route import create_Game,get_Game_by_id,get_Games,delete_Game,update_Game
from database import get_db
from exceptions.exceptions import GameDBException
from templates.Game import Game,CreateAndUpdateGame,GameList

app = FastAPI()
router = APIRouter()

app.include_router(router)

@cbv(router)
class Games:
    session: Session = Depends(get_db)

    # GET list
    @router.get("/games", response_model=GameList)
    def list_games(self, limit: int = 100, offset: int = 0):

        games_list = get_Games(self.session, limit, offset)
        response = {"limit": limit, "offset": offset, "data": games_list}

        return response
    
    # POST
    @router.post("/game")
    def add_games(self, result: CreateAndUpdateGame):

        try:
            result = create_Game(self.session, result)
            return result
        except GameDBException as cie:
            raise HTTPException(**cie.__dict__)


# GET by id
@router.get("/game/{id}", response_model = Game)
def get_game(id: int, session: Session = Depends(get_db)):

    try:
        result = get_Game_by_id(session, id)
        return result
    except GameDBException as cie:
        raise HTTPException(**cie.__dict__)


# PUT by id
@router.put("/game/{id}", response_model = Game)
def update_game(id: int, new_info: CreateAndUpdateGame, session: Session = Depends(get_db)):

    try:
        result = update_Game(session, id, new_info)
        return result
    except GameDBException as cie:
        raise HTTPException(**cie.__dict__)


# DEL by id
@router.delete("/game/{id}")
def delete_game(id: int, session: Session = Depends(get_db)):

    try:
        return delete_Game(session, id)
    except GameDBException as cie:
        raise HTTPException(**cie.__dict__)


