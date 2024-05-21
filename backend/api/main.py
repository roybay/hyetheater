from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from pony.orm import db_session, select
from api.orm import connect_db, Role


app = FastAPI()
connect_db()


class GetRoleName(BaseModel):
    roles: List[str]


@app.get("/api/v1/roles", response_model=GetRoleName)
@db_session
def get_list_role_names():
    roles = select(r.name for r in Role)[:]
    return {"roles": list(roles)}
