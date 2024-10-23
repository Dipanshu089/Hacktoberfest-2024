def is_perfect_number(n):
    # A perfect number should be greater than 1
    if n <= 1:
        return False
    
    # Find all divisors and calculate the sum of proper divisors
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    
    # Check if sum of divisors equals the number itself 
    return divisors_sum == n

# Example usage:
num =int(input())
if is_perfect_number(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")