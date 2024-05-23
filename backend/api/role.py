from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel
from pony.orm import db_session, select
from api.orm import connect_db, Role


router = APIRouter()
connect_db()


class GetRoleName(BaseModel):
    roles: List[str]


class RoleName(BaseModel):
    name: str


class UpdateRoleName(BaseModel):
    new_name: str


class DeleteRoleName(BaseModel):
    delete_role: str



@router.get("/api/v1/roles", tags=["role"], response_model=GetRoleName)
@db_session
def get_role_names():
    roles = select(r.name for r in Role)[:]
    return {"roles": list(roles)}


@router.post("/api/v1/role", tags=["role"], response_model=RoleName)
@db_session
def create_role(role: RoleName):
    if Role.get(name=role.name):
        raise HTTPException(status_code=400, detail="Role name already exists")
    new_role = Role(name=role.name)
    return {"name": new_role.name}


@router.put("/api/v1/role/{role_name}", tags=["role"], response_model=RoleName)
@db_session
def update_role(role_name: str, role: UpdateRoleName):
    existing_role = Role.get(name=role_name)
    if not existing_role:
        raise HTTPException(status_code=404, detail="Role not found")
    if Role.get(name=role.new_name):
        raise HTTPException(status_code=400, detail="New role name already exists")  # noqa: E501
    existing_role.name = role.new_name
    return {"name": existing_role.name}


@router.delete("/api/v1/role/{role_name}", tags=["role"], response_model=DeleteRoleName)  # noqa: E501
@db_session
def delete_role(role_name: str):
    existing_role = Role.get(name=role_name)
    if not existing_role:
        raise HTTPException(status_code=404, detail=role_name+" NOT found")  # noqa: E501
    existing_role.delete()
    return {"delete_role": existing_role.name}
