import pytest
from functions import calculate_average, calculate_average_with_loop, User

def test_calculate_average():
    """Test basic user creation with constructor."""
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0
    assert calculate_average([1.5, 2.5, 3.5]) == 2.5
    assert calculate_average([42]) == 42.0

def test_calculate_average_with_loop():
    """Test the full_name property."""
    assert calculate_average_with_loop([1, 2, 3, 4, 5]) == 3.0
    assert calculate_average_with_loop([1.5, 2.5, 3.5]) == 2.5
    assert calculate_average_with_loop([42]) == 42.0

# User class tests
def test_user_creation():
    """Test basic user creation with constructor."""
    user = User("John", "Doe")
    assert user.first_name == "John"
    assert user.last_name == "Doe"

def test_user_full_name():
    """Test the full_name property."""
    user = User("John", "Doe")
    assert user.full_name == "John Doe"

def test_user_to_dict():
    """Test conversion to dictionary format."""
    user = User("John", "Doe")
    user_dict = user.to_dict()
    assert user_dict == {
        "first_name": "John",
        "last_name": "Doe"
    }

def test_create_user_factory():
    """Test the create_user factory method."""
    # Test with normal input
    user1 = User.create_user("John", "Doe")
    assert user1.first_name == "John"
    assert user1.last_name == "Doe"
    
    # Test with whitespace that should be stripped
    user2 = User.create_user("  Jane  ", "  Smith  ")
    assert user2.first_name == "Jane"
    assert user2.last_name == "Smith"

def test_user_attributes_are_strings():
    """Test that user attributes are stored as strings."""
    # Test with non-string input that can be converted to string
    user = User(123, 456)
    assert isinstance(user.first_name, str)
    assert isinstance(user.last_name, str)
    assert user.first_name == "123"
    assert user.last_name == "456" 