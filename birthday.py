from random import randint
 
 
NUM_PEOPLE = 23
NUM_POSSIBLE_BIRTHDAYS = 365
NUM_TRIALS = 10000
 
 
def generate_random_birthday():
    birthday = randint(1, NUM_POSSIBLE_BIRTHDAYS)
    return birthday
 
 
def generate_k_birthdays(k):
    birthdays = [generate_random_birthday() for _ in range(k)]
    return birthdays
 
 
def aloc(birthdays):
    unique_birthdays = set(birthdays)
 
    num_birthdays = len(birthdays)
    num_unique_birthdays = len(unique_birthdays)
    has_coincidence = (num_birthdays != num_unique_birthdays)
 
    return has_coincidence
 
 
def estimate_p_aloc():
    num_aloc = 0
    for _ in range(NUM_TRIALS):
        birthdays = generate_k_birthdays(NUM_PEOPLE)
        has_coincidence = aloc(birthdays)
        if has_coincidence:
            num_aloc += 1
 
    p_aloc = num_aloc / NUM_TRIALS
    return p_aloc
 
 
p_aloc = estimate_p_aloc()
print(f"Estimated P(ALOC) after {NUM_TRIALS} trials: {p_aloc}")
