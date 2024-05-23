import pytest
from httpx import AsyncClient, ASGITransport
from api.main import app


@pytest.mark.asyncio
async def test_create_role():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/api/v1/role", json={"name": "testRole"})
        assert response.status_code == 200
        assert response.json() == {"name": "testRole"}


@pytest.mark.asyncio
async def test_create_duplicate_role():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # First create a role
        await ac.post("/api/v1/role", json={"name": "testRole"})
        # Try to create the same role again
        response = await ac.post("/api/v1/role", json={"name": "testRole"})
        await ac.delete("/api/v1/role/testRole")
        assert response.status_code == 400
        assert response.json() == {"detail": "Role name already exists"}


@pytest.mark.asyncio
async def test_update_role():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Create a role to update
        await ac.post("/api/v1/role", json={"name": "oldRoleName"})
        # Update the role's name
        response = await ac.put("/api/v1/role/oldRoleName", json={"new_name": "newRoleName"})  # noqa E501
        await ac.delete("/api/v1/role/oldRoleName")
        assert response.status_code == 200
        assert response.json() == {"name": "newRoleName"}


@pytest.mark.asyncio
async def test_update_nonexistent_role():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.put("/api/v1/role/nonexistentRole", json={"new_name": "newRoleName"})  # noqa E501
        await ac.delete("/api/v1/role/newRoleName")
        assert response.status_code == 404
        assert response.json() == {"detail": "Role not found"}


@pytest.mark.asyncio
async def test_delete_role():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Create a role to delete
        await ac.post("/api/v1/role", json={"name": "roleToDelete"})
        # Delete the role
        response = await ac.delete("/api/v1/role/roleToDelete")
        assert response.status_code == 200
        assert response.json() == {"delete_role": "roleToDelete"}


@pytest.mark.asyncio
async def test_delete_nonexistent_role():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.delete("/api/v1/role/nonexistentRole")
        assert response.status_code == 404
        assert response.json() == {"detail": "nonexistentRole NOT found"}
