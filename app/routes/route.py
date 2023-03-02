from typing import List
from sqlalchemy.orm import Session
from exceptions.exceptions import GameDBNotFound,GamesDBAlreadyExist
from models.Gamesql import GameDB
from templates.Game import CreateAndUpdateGame

# POST
def create_Game(session: Session, Game_db: CreateAndUpdateGame) -> GameDB:
    check_duplic = session.query(GameDB).filter(GameDB.Name == Game_db.Name, GameDB.StudioName == Game_db.StudioName).first()
    if check_duplic is not None:
        raise GamesDBAlreadyExist

    result = GameDB(**Game_db.dict())
    session.add(result)
    session.commit()
    session.refresh(result)
    return result

# GET by id
def get_Game_by_id(session: Session, _id: int) -> GameDB:
    result = session.query(GameDB).get(_id)

    if result is None:
        raise GameDBNotFound

    return result

# GET list
def get_Games(session: Session, limit: int, offset: int) -> List[GameDB]:
    return session.query(GameDB).offset(offset).limit(limit).all()

# PUT by id
def update_Game(session: Session, _id: int, info_update: CreateAndUpdateGame) -> GameDB:
    result = get_Game_by_id(session, _id)

    if result is None:
        raise GameDBNotFound

    result.firstname = info_update.firstname
    result.lastname = info_update.lastname
    result.house = info_update.house

    session.commit()
    session.refresh(result)

    return result

# DEL by id
def delete_wizard(session: Session, _id: int):
    result = get_Game_by_id(session, _id)

    if result is None:
        raise GameDBNotFound

    session.delete(result)
    session.commit()

    return