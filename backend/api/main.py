from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from pony.orm import db_session, select
from api.orm import connect_db, Role

tags_metadata = [
    {
        "name": "roles",
        "description": "Operations with ROLES. The **login** logic is also here.",
    },
]

app = FastAPI(
    title="HyeTheater API",
    description="""
    This is a custom description for my API.

    ## Features

    * **Feature 1**: Description of feature 1.
    * **Feature 2**: Description of feature 2.
    """,
    version="1.0.0",
    openapi_tags=tags_metadata,
    swagger_ui_parameters={"defaultModelsExpandDepth": -1}
    # Hide Schema
)
connect_db()


class GetRoleName(BaseModel):
    roles: List[str]


@app.get("/api/v1/roles", tags=["roles"], response_model=GetRoleName)
@db_session
def get_list_role_names():
    roles = select(r.name for r in Role)[:]
    return {"roles": list(roles)}

