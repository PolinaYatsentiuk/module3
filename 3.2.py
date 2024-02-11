import random

def get_numbers_ticket(min, max, quantity):
    if max <= min or quantity > max or max-min+1<quantity:
        return []

    for num in [min, max, quantity]:
        if not (1 <= num <= 1000):
            return []
    unique_numbers = random.sample(range(min,max+1), quantity)
    return sorted(unique_numbers)

lottery_numbers = get_numbers_ticket(15, 100, 24)
print("Ваші лотерейні числа:", lottery_numbers)
