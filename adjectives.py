import random

adjectives = []

def load_adjectives(filename):
    global adjectives
    with open(filename, 'r') as f:
        adjectives = [line.strip() for line in f.readlines()]

def get_random_adjective():
    return random.choice(adjectives)

# Usage
filename = 'adjectives.txt'
load_adjectives(filename)