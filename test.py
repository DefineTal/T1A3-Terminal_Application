import random

cards = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Get a list of key-value pairs from the dictionary
key_value_pairs = list(cards.items())

# Randomly choose a key-value pair
random_key_value = random.choice(key_value_pairs)

# Extract the key and value from the chosen pair
random_key, random_value = random_key_value

print("Random Key:", random_key)
print("Random Value:", random_value)