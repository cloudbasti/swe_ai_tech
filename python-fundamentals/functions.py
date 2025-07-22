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



