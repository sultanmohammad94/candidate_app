import pytest
from unittest.mock import patch
from fastapi import FastAPI
from repositories.user_repositories import UserInMemoryRepository, IUserRepository
from services.user_services import UserCreateService, UserReadService
from models.user import UserBaseModel
from utils.logger import ApplicationLogger

@pytest.mark.parametrize(
    "user_data,expected",
    [
        (
            UserBaseModel(first_name="John", last_name="Doe", email="john.doe@example.com", UUID="123456789"),
            UserBaseModel(first_name="John", last_name="Doe", email="john.doe@example.com", UUID="123456789"),
        ),
        (
            UserBaseModel(first_name="Jane", last_name="Smith", email="jane.smith@example.com", UUID="abcdef0123"),
            UserBaseModel(first_name="Jane", last_name="Smith", email="jane.smith@example.com", UUID="abcdef0123"),
        ),
    ]
)
def test_create_user(user_data, expected):
    user_repo = UserInMemoryRepository()
    user_service = UserCreateService(user_repo)

    # We should pass the full path to the method we want to mock
    with patch("services.user_services.UserCreateService.create_user") as mock_create_user:
        try:
            mock_create_user.return_value = expected

            result = user_service.create_user(user_data)
            assert result.UUID == expected.UUID
            assert result.first_name == expected.first_name
            assert result.last_name == expected.last_name
            assert result.email == expected.email
        except Exception as e:
            # Print the arguments passed to the mocked method
            ApplicationLogger().log_error(f"Mock user create args: \n{mock_create_user.call_args}")
            # Print the number of times the mocked method was called
            ApplicationLogger().log_error(f"Mock user create call count: \n{mock_create_user.call_count}")


@pytest.mark.parametrize(
    "user_uuid, expected",
    [
        ("123456789", UserBaseModel(first_name="John", last_name="Doe", email="john.doe@example.com", UUID="123456789")),
        ("abcdef0123", UserBaseModel(first_name="Jane", last_name="Smith", email="jane.smith@example.com", UUID="abcdef0123")),
    ]
)
def test_get_user(user_uuid, expected):
    user_repo = UserInMemoryRepository()
    user_service = UserReadService(user_repo)

    with patch("services.user_services.UserReadService.get_user") as mock_get_user:
        mock_get_user.return_value = expected

        result = user_service.get_user(user_uuid)

        assert result.UUID == expected.UUID
        assert result.first_name == expected.first_name
        assert result.last_name == expected.last_name
        assert result.email == expected.email