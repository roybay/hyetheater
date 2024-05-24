import pytest
from httpx import AsyncClient, ASGITransport
from api.main import app


@pytest.mark.asyncio
async def test_create_user():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/api/v1/users", json={"email": "test@example.com", "password": "Test@1234"})  # noqa E501
        assert response.status_code == 200
        assert "access_token" in response.json()
        assert response.json()["token_type"] == "bearer"


@pytest.mark.asyncio
async def test_create_user_with_weak_password():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/api/v1/users", json={"email": "test2@example.com", "password": "weakpass"})  # noqa E501
        assert response.status_code == 400
        assert response.json()["detail"] == "Password must contain at least one uppercase letter"


@pytest.mark.asyncio
async def test_login_user():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Create a user first
        await ac.post("/api/v1/users", json={"email": "test@example.com", "password": "Test@1234"})  # noqa E501
        # Login with the created user
        response = await ac.post("/api/v1/token", json={"email": "test@example.com", "password": "Test@1234"})  # noqa E501
        assert response.status_code == 200
        assert "access_token" in response.json()
        assert response.json()["token_type"] == "bearer"


@pytest.mark.asyncio
async def test_read_users_me():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Create and login a user to get the token
        response = await ac.post("/api/v1/users", json={"email": "me@example.com", "password": "Test@1234"})  # noqa E501
        token = response.json()["access_token"]
        
        # Use the token to access the protected endpoint
        response = await ac.get("/api/v1/users/me", headers={"Authorization": f"Bearer {token}"})  # noqa E501
        assert response.status_code == 200
        assert response.json() == {"email": "me@example.com"}
