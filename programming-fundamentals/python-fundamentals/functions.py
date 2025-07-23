def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    return sum(numbers) / len(numbers)

def calculate_average_with_loop(numbers):
    """Calculate the average of a list of numbers using a loop."""
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
    return total / count


class User:
    def __init__(self, first_name: str, last_name: str):
     
        self.first_name = str(first_name)
        self.last_name = str(last_name)
    
    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    def to_dict(self) -> dict:
       
        return {
            "first_name": self.first_name,
            "last_name": self.last_name
        }
    
    @classmethod
    def create_user(cls, first_name: str, last_name: str) -> 'User':
        """
        Factory method to create a new user.
        
        Args:
            first_name (str): The user's first name
            last_name (str): The user's last name
            
        Returns:
            User: A new User instance
        """
        # Here we could add validation, formatting, or other preprocessing
        # before creating the user
        first_name = str(first_name).strip()
        last_name = str(last_name).strip()
        
        return cls(first_name, last_name)



