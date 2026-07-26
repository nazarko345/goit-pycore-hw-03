import random

def get_numbers_ticket(min, max, quantity):
    lottery_numbers = set()
    
    if min < 1:
        print("Недостатня кількість білетів. Мінімальна кількість білетів має бути більше 1.")
        return []
    elif max > 1000:
        print("Завелика кількість білетів. Максимальне число має бути менше 49.")
        return []
    elif min >= max:
        print("Недостатня кількість білетів. Мінімальна кількість білетів має бути більше 1.")
        return []
    elif quantity > max - min + 1:
        print("Мінімальне число має бути менше максимального.")
        return []
    else:
        while len(lottery_numbers) < quantity:
            lottery_numbers.add(random.randint(min, max))
        return sorted(lottery_numbers)