from fastapi.testclient import TestClient
from ..models import User
from ..main import app
from ..dependencies import get_current_user
from datetime import datetime


client = TestClient(app)


async def override_get_current_user_active():
    return User(
        id=1,
        email='test@test.com',
        name='Test',
        auth0_id='auth0|1',
        created_at=datetime(2024, 1, 1),
        updated_at=datetime(2024, 1, 1)
    )


async def override_get_current_user_inactive():
    return User(
        id=1,
        email='test@test.com',
        name='Test',
        auth0_id='auth0|1',
        is_active=False,
        created_at=datetime(2024, 1, 1),
        updated_at=datetime(2024, 1, 1)
    )


def test_active_user_allow_access():
    """
    Test that an active user has access to the endpoint /me
    """
    app.dependency_overrides[get_current_user] = \
        override_get_current_user_active
    response = client.get('/users/me')
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "email": "test@test.com",
        "name": "Test",
        "auth0_id": "auth0|1",
        "is_active": True,
        "start_cycle_day": 1,
        "end_cycle_day": 31,
        "created_at": "2024-01-01T00:00:00",
        "updated_at": "2024-01-01T00:00:00"
    }
    app.dependency_overrides = {}


def test_inactive_user_deny_access():
    """
    Test that an inactive user can't access a protected resource
    """
    app.dependency_overrides[get_current_user] = \
        override_get_current_user_inactive
    response = client.get('/users/me')
    assert response.status_code == 401
    app.dependency_overrides = {}
