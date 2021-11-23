import random

max_random = 1000
mysterious_nb = random.randint(1, max_random)
print(mysterious_nb)

is_found = False
guess_counter = 0

while not is_found:
    guess = int(input("N=?"))
    guess_counter += 1

    if guess > mysterious_nb:
        print("Trop Grand")
    elif guess < mysterious_nb:
        print("Trop petit")
    else :
        is_found = True

print("Trouvé en :", guess_counter, " Coups")
