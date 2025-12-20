def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def is_prime_factor(number, potential_factor):
    return is_prime(potential_factor) and number % potential_factor == 0


print(is_prime_factor(15, 3))  # Output: True
print(is_prime_factor(15, 4))
