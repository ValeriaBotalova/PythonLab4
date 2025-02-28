import random

def generate_random(file, n):
    with open(file, "w") as f:
        for i in range(n):
            f.write(f"{random.randint(-100, 100)}\n") 

def opposite_counter(file):
    with open(file, 'r') as f:
        numbers = [int(line.strip()) for line in f]

    count = 0
    s = set()

    for number in numbers:
        if -number in s:
            count += 1
        s.add(number)
    
    return count

generate_random("file.txt", 15)
print(f"Всего пар {opposite_counter('file.txt')} противоположных чисел.")
